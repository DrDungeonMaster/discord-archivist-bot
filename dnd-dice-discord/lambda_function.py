import math
import boto3
import json
import logging
import os
import subprocess
import requests

from random import randint
from base64 import b64decode
from subprocess import call
from datetime import datetime

from commons.common_functions import choose
from commons.common_functions import parse_event
from commons.common_functions import is_numeric
from commons.common_functions import arrange
from commons.common_functions import slack_send
from commons.common_functions import slack_reply
from commons.common_functions import textcode
from commons.common_functions import time_format
from commons.common_functions import get_event_timestamp

from dice_roller import parse_roll
from dice_roller import hide_fudging
#from dice_roll_tester import test_dice

from query_rolls import get_rolls,rollstats_text

from commons.slack_params import aws_access_key_id,aws_secret_access_key,region_name,gm_users,player_chars,foundry_to_discord

def clusters_to_storable(clusters,max_dice:int=20):
    storable_rolls = {}
    for i in clusters:
        die_size = i.split('d')[-1].split('r')[0].split('k')[0]
        rolls = clusters[i]['kept'] + clusters[i]['discarded']
        if die_size in ['4','6','8','10','12','20','100'] and len(rolls) <= max_dice:
            storable_rolls[str(die_size)]=rolls
    return storable_rolls

def rolls_to_db(user_id:str, die_rolls:list, dynamo_client, timestamp:str=None, die_size:int=20,user_name:str=None,roll_text:str=None,roll_note:str=None,character:str=None,source:str=None):
    if roll_text and ('#nolog' in roll_text.lower() or '#notrack' in roll_text.lower()):
        pass
    else:
        if not timestamp:
            timestamp = datetime.now().strftime(time_format)
        for i in range(0,len(die_rolls)):
            die_rolls[i] = str(int(die_rolls[i]))
        param_dict = {
                "user_id":{"S":user_id},
                "timestamp":{"S":timestamp + str(i)},
                "die_size":{"N":str(int(die_size))},
                "die_rolls":{"S":",".join(die_rolls)},
                }
        if user_name:
            param_dict["user_name"]={"S":user_name}
        if roll_text:
            text_parts = roll_text.split(":")
            if len(text_parts) > 1 and text_parts[0].replace(' ','') == text_parts[-1].replace(' ':
                roll_text = ":".join(text_parts[0:-1])
            param_dict["roll_text"]={"S":roll_text}
        if source:
            param_dict["source"]={"S":source}
        if character:
            param_dict["character"]:{"S":character}
        if roll_note == 'Nat20' and "20" in die_rolls and int(die_size) == 20:
            param_dict["roll_note"]={"S":roll_note}
        elif roll_note == 'Nat1' and "1" in die_rolls and int(die_size) == 20:
            param_dict["roll_note"]={"S":roll_note}
        else:
            pass
        dynamo_client.put_item(
            TableName='Greg-DnD-DiceRolls', 
            Item=param_dict
            )
        print(f'Roll log success: {param_dict}')

def log_vtt_roll(body:str, dynamo_client, timestamp=None, userID_conversion_dict:dict=None):
    body_dict = json.loads(body)
    userID = body_dict['userID']
    if userID_conversion_dict and userID in userID_conversion_dict:
        userID = userID_conversion_dict[userID]
    try:
        user_name = body_dict['user_name']
    except:
        user_name = None
    try:
        character = body_dict['character']
    except:
        character = None
    try:
        roll_text = body_dict['roll']['options']['flavor']
        if character:
            roll_text = character + ': ' + roll_text
    except:
        roll_text = None
    
    roll_count = 0
    for i in body_dict['roll']['terms']:
        roll_note = None
        if i['class'] == 'Die':
            die_rolls = []
            active_rolls = []
            for j in i['results']:
                die_rolls.append(j['result'])
                if j['active']:
                    active_rolls.append(j['result'])
            die_size = str(i['faces'])
            if die_size not in ['4','6','8','10','12','20','100']:
                break
            if die_size == '20' and len(active_rolls) == 1:
                if str(active_rolls[0]) == '20':
                    roll_note = 'Nat20'
                elif str(active_rolls[0]) == '1':
                    roll_note = 'Nat1'
            iter_time = timestamp + '.' + str(roll_count).zfill(3) 
            rolls_to_db(user_id=str(userID), die_rolls=die_rolls, dynamo_client=dynamo_client, timestamp=iter_time, die_size=die_size, user_name=user_name, roll_text=roll_text, roll_note=roll_note, character=character, source='Foundry')
            roll_count += 1

def diceroll_command_handler(text:str):
    text = " "+ text.strip()
    sub_text,clusters,dice_total,dice_range,fudged_rolls=parse_roll(text)
    if not fudged_rolls:
        store_rolls = clusters_to_storable(clusters)
    else:
        store_rolls = None
    if dice_total % 1 == 0:
        dice_total = int(dice_total)
    rolls_list = []
    for c in clusters:
        for r in range(0,len(clusters[c]['rolls'])):
            if c.endswith('d20') and len(clusters[c]['rolls']) <= 2:
                if str(clusters[c]['rolls'][r]) == '20':
                    clusters[c]['rolls'][r] = '<a:nat20:906636383806955611> '
                elif str(clusters[c]['rolls'][r]) == '1':
                    clusters[c]['rolls'][r] = '<a:critfail:906639652008656966>'
            if 'r' in clusters[c]['rolls'][r] and ':' not in clusters[c]['rolls'][r]:
                clusters[c]['rolls'][r] = '~~' + clusters[c]['rolls'][r].replace('r','~~ _') + '_'
            if 'd' in clusters[c]['rolls'][r]:
                clusters[c]['rolls'][r] = '~~' + clusters[c]['rolls'][r].replace('d','~~')
        cluster_string = f"{c.split(':')[1]}: {' '.join(clusters[c]['rolls'])}"
        rolls_list.append(cluster_string)
    rolls_text = '> ' + "\n> ".join(rolls_list) + '\n'
    if dice_range[0] == dice_range[1]:
        dice_range_text = ''
    else:
        dice_range_text = f'  [{dice_range[0]},{dice_range[1]}]'
    if is_numeric(sub_text):
        if len(rolls_list) == 0:
            rolls_text = ''
            label = 'Value'
        else:
            label = 'Total'
        out_text = f'{rolls_text}**{label}: {dice_total}** {dice_range_text}'
    else:
        if store_rolls:
            store_rolls['text']=sub_text
        out_text = f'{sub_text.replace(" -","-")}\n{rolls_text}> **Total: {dice_total}**{dice_range_text}'
    if store_rolls and 'text' not in store_rolls:
        store_rolls['text']=None
    if ':nat20:' in out_text:
        store_rolls['note']='Nat20'
    elif ':critfail:' in out_text:
        store_rolls['note']='Nat1'
    else:
        store_rolls['note']=None
    return out_text, fudged_rolls, store_rolls

def rollstats_command_handler(user_id:str=None, date_from:str=None, date_to:str=None, source:str=None):
    rolls_df,query_info = get_rolls(user_id,date_from,date_to,source)
    text_out = rollstats_text(rolls_df,query_info)
    return text_out

def lambda_handler(event, context):
    print(event)
    message_out = None
    short_message = "It appears you did not include any text with your command. Please give me something to work with."
    error_message = "I am very sorry, but something has gone wrong."
    try:
        timestamp = get_event_timestamp(event)
    except Exception as e:
        print(f'Timestamp retrieval failed: {str(e)}')
        timestamp = None
    if 'body' in event and '"command":"logFoundryRolls"' in event['body']:
        command = 'logFoundryRolls'
    else:
        command = event['command']
    if command == 'roll':
        response_url = event['response_url']
        user_id = event['member']['user']['id']
        text = event['options'][0]['value']
        user_name = event['member']['user']['username']
        try:
            message_out,is_fudged,store_rolls = diceroll_command_handler(text)
            if store_rolls and not is_fudged:
                try:
                    dynamo_client = boto3.client("dynamodb",aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key,region_name=region_name)
                    roll_count = 0
                    for die in ['4','6','8','10','12','20','100']:
                        if die in store_rolls:
                            iter_time = timestamp + '.' + str(roll_count).zfill(3) 
                            rolls_to_db(user_id,die_rolls=store_rolls[die],die_size=die,dynamo_client=dynamo_client,user_name=user_name,timestamp=iter_time,roll_text=store_rolls['text'],roll_note=store_rolls['note'],source="Discord")
                            roll_count += 1
                except Exception as e:
                    print(f'Logging rolls failed: [{str(e)}]')
            if is_fudged:
                if user_id in gm_users and channel_id in gm_users[user_id]:
                    command_text = f'||{command} {hide_fudging(text)}||'
                    message_out = command_text + '\n' + message_out
                else:
                    command_text = f'||/{command} {text}||'
                    message_out = command_text + '\n' + message_out + '\n\n:exclamation: **THIS ROLL WAS FUDGED WITHOUT AUTHORIZATION** :exclamation:'
            else:
                command_text = f'||/{command} {text}||'
                message_out = command_text + '\n' + message_out
        except Exception as e:
            print(str(e))
            message_out = error_message
    elif command == 'rollstats':
        response_url = event['response_url']
        user_id = None
        date_from = None
        date_to = None
        source = None
        try:
            options = event['options']
            if options:
                for i in options:
                    if i['name'] == 'user':
                        user_id = i['value']
                    elif i['name'] == 'from':
                        date_from = i['value']
                    elif i['name'] == 'to':
                        date_to = i['value']
                    elif i['name'] == 'source':
                        source = i['value']
            message_out = "\n".join(rollstats_command_handler(user_id, date_from, date_to, source))
        except Exception as e:
            message_out = f'Retrieving logged rolls failed: [{str(e)}]'
    elif command == 'logFoundryRolls':
        dynamo_client = boto3.client("dynamodb",aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key,region_name=region_name)
        log_vtt_roll(body=event['body'], dynamo_client=dynamo_client, timestamp=timestamp, userID_conversion_dict=foundry_to_discord)
    else:
        message_out = "I am not yet prepared to handle that command yet. Please be patient."
    if message_out:
        response_json = {"content": message_out,"tts":False,"embeds": [],"allowed_mentions": { "parse": [] }}
        print(response_json)
        print(response_url)
        r = requests.patch(url=response_url,json=response_json)
        print(r.text)
    to_return = {'status':200}
    return to_return

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
from commons.common_functions import textcode
from commons.common_functions import time_format
from commons.common_functions import get_event_timestamp

#from commons.discord_params import aws_access_key_id,aws_secret_access_key,region_name,gm_users,player_chars,foundry_to_discord

from age_converter import convert_age_text, race_age_info

def convert_ages(options:list=None, command:str="age"):
    from_race = None
    to_race = None
    age = None
    try:
        for i in options:
            if 'name' in i and 'value' in i:
                if i['name'] == 'years':
                    age = int(i['value'])
                elif i['name'] == 'from':
                    from_race = i['value']
                elif i['name'] == 'to':
                    to_race = i['value']
        if from_race and not to_race and not age:
            age_text = race_age_info(from_race)
        elif not from_race and not to_race:
            age_text = "I'm terribly sorry, but you did not provide enough information to complete your request. You must at least specify one race."
        else:
            age_text = convert_age_text(from_race=from_race,to_race=to_race,age=age)
    except:
        age_text = "I'm terribly sorry, but it seems that you specified something incorrectly. Please be careful when choosing your options."
    return age_text

def lambda_handler(event, context):
    print(event)
    options = event['options']
    command = event['command']
    response_url = event['response_url']
    if command == 'age':
        message_out = convert_ages(options, command)
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

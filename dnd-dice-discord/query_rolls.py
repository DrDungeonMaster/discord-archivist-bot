from commons.slack_params import aws_access_key_id,aws_secret_access_key,region_name,gm_users,player_chars
from commons.common_functions import time_format

from math import floor,ceil
from copy import deepcopy

import boto3
from boto3.dynamodb.conditions import Key
import time,datetime
from calendar import monthrange

try:
    import numpy
except:
    from pandas.numpy import numpy
try:
    import pytz
except:
    from pandas.pytz import pytz
try:
    import pandas as pd
except:
    from pandas import pandas as pd

timestamp_levels = {
    1: 'year',
    2: 'month',
    3: 'day',
    4: 'hour',
    5: 'minute'
    }

rolls_dict_template = {
    4:[],
    6:[],
    8:[],
    10:[],
    12:[],
    20:[],
    100:[],
    'Nat1':0,
    'Nat20':0
    }

roll_quintiles = {
    4:[1.85,2.125,2.5,2.875,3.125],
    6:[2.25,2.75,3.5,4.25,4.75],
    8:[3,3.75,4.5,5.25,6],
    10:[3.75,4.75,5.5,6.25,7.25],
    12:[4.5,5.5,6.5,7.5,8.5],
    20:[8.5,9.25,10.5,11.25,13.0],
    100:[30,40,51,60,70],
    }

deviation_indicators = {
    'low':':small_red_triangle_down:',
    'v_low':':three_red_arrows:',
    'high':':small_green_triangle_up:',
    'v_high':':three_green_arrows:',
    'low_good':':small_green_triangle_down:',
    'v_low_good':':three_green_arrows_down:',
    'high_bad':':small_red_triangle:',
    'v_high_bad':':three_red_arrows_up:',
    }

def correct_timestamp(timestamp:str):
    split_timestamp = timestamp.replace(' ','-').split('-')
    if len(split_timestamp) == 1:
        split_timestamp = split_timestamp + ['1','1']
    if int(split_timestamp[0]) <= 13:
        split_timestamp = [str(datetime.datetime.now().year)] + split_timestamp
    if len(split_timestamp) == 3:
        timestamp = "-".join(split_timestamp) + ' 0:0:0'
    elif len(split_timestamp) > 4 or len(split_timestamp) < 3:
        pass #this is an error
    else:
        timestamp = "-".join(split_timestamp[0:3]) + ' ' + split_timestamp[3]
    return timestamp

def time_to_range(timestamp:str):
    split_timestamp = timestamp.replace(' ','-').replace(':','-').split('-')
    if int(split_timestamp[0]) <= 13:
        split_timestamp = [str(datetime.datetime.now().year)] + split_timestamp
    if len(split_timestamp) < 6 and len(split_timestamp) > 0:
        level = timestamp_levels[len(split_timestamp)]
        if level == 'year':
            year = [split_timestamp[0]] * 2
            month = [1,12]
            day = [1,monthrange(int(year[1]),int(month[1]))[1]]
            hour = [0,23]
            minute = [0,59]
            second = [0,59]
        elif level == 'month':
            year = [split_timestamp[0]] * 2
            month = [split_timestamp[1]] * 2
            day = [1,monthrange(int(year[1]),int(month[1]))[1]]
            hour = [0,23]
            minute = [0,59]
            second = [0,59]
        elif level == 'day':
            year = [split_timestamp[0]] * 2
            month = [split_timestamp[1]] * 2
            day = [split_timestamp[2]] * 2
            hour = [0,23]
            minute = [0,59]
            second = [0,59]
        elif level == 'hour':
            year = [split_timestamp[0]] * 2
            month = [split_timestamp[1]] * 2
            day = [split_timestamp[2]] * 2
            hour = [split_timestamp[3]] * 2
            minute = [0,59]
            second = [0,59]
        elif level == 'minute':
            year = [split_timestamp[0]] * 2
            month = [split_timestamp[1]] * 2
            day = [split_timestamp[2]] * 2
            hour = [split_timestamp[3]] * 2
            minute = [split_timestamp[4]] * 2
            second = [0,59]
        time_start = f'{year[0]}-{month[0]}-{day[0]} {hour[0]}:{minute[0]}:{second[0]}'
        time_end = f'{year[1]}-{month[1]}-{day[1]} {hour[1]}:{minute[1]}:{second[1]}'
    return [time_start, time_end]

def time_to_epoch(timestamp:str):
    epoch_time = int(time.mktime(time.strptime(timestamp.split('.')[0], time_format)))
    return epoch_time

def get_rolls(user_id:str=None,date_from=None,date_to=None,source=None):
    dynamodb = boto3.resource('dynamodb',aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key,region_name=region_name)    
    table = dynamodb.Table('Greg-DnD-DiceRolls')
    query_info={}
    if user_id:
        if user_id.lower() in player_chars:
            user_id_text = user_id.lower()
            user_id = player_chars[user_id_text]
            user_id_text = user_id_text.title()
            print(f'Getting rolls for {user_id_text} (ID:{user_id}) ...')
        else:
            print(f'Getting rolls for user ID {user_id} ...')
            user_id_text = user_id
        rolls_df = pd.DataFrame(data=table.query(KeyConditionExpression=Key('user_id').eq(user_id))['Items'])
        query_info['user_id']=user_id_text
    else:
        rolls_df = pd.DataFrame(data=table.scan()['Items'])
        query_info['user_id']=None
    print(rolls_df)
    rolls_df['epoch']=rolls_df['timestamp'].apply(time_to_epoch)
    if date_from or date_to:
        if type(date) is not list:
            date = time_to_range(date)
        elif len(date) == 1:
            date = time_to_range(date[0])
        print(f'Filtering to rolls from {date[0]} to {date[1]}...')
        query_info['date_range']=date
        epoch_date_start = time_to_epoch(correct_timestamp(date[0]))
        epoch_date_end = time_to_epoch(correct_timestamp(date[1]))
        epoch_date = [epoch_date_start,epoch_date_end]
        rolls_df = rolls_df.loc[(rolls_df['epoch'] <= max(epoch_date)) & (rolls_df['epoch'] >= min(epoch_date))]
    else:
        query_info['date_range']=None
    query_info['clusters'] = len(rolls_df['die_rolls'])
    return rolls_df,query_info

def roll_stats(rolls_df):
    rolls_dict = deepcopy(rolls_dict_template)
    for die in [4,6,8,10,12,100]:
        sub_df = rolls_df.loc[(rolls_df['die_size'] == die)]
        for rolls in sub_df['die_rolls']:
            for roll in rolls.split(','):
                rolls_dict[die].append(int(roll))
    die = 20
    sub_df = rolls_df.loc[(rolls_df['die_size'] == die)]
    for rolls in sub_df['die_rolls']:
        for roll in rolls.split(','):
            rolls_dict[die].append(int(roll))
    if 'roll_note' in rolls_df:
        nat20_df = rolls_df.loc[(rolls_df['roll_note'] == 'Nat20')]
        d20_expected = len(rolls_dict[20])/20
        rolls_dict['Nat20'] = len(nat20_df['die_rolls'])
        nat1_df = rolls_df.loc[(rolls_df['roll_note'] == 'Nat1')]
        rolls_dict['Nat1'] = len(nat1_df['die_rolls'])
    if 'roll_text' in rolls_df:
        sub_df = rolls_df.loc[(rolls_df.roll_text.notna())].sort_values(by=['epoch'],ascending=False)
        num_annotated = len(sub_df['roll_text'])
        if 'roll_note' in sub_df:
            most_recent_20s = list(sub_df.loc[sub_df['roll_note']=='Nat20']['roll_text'])
            if len(most_recent_20s) > 0:
                most_recent_20 = most_recent_20s[0]
            else:
                most_recent_20=None
            most_recent_1s = list(sub_df.loc[sub_df['roll_note']=='Nat1']['roll_text'])
            if len(most_recent_1s) > 0:
                most_recent_1 = most_recent_1s[0]
            else:
                most_recent_1=None
        else:
            most_recent_20,most_recent_1 = None,None
        rolls_dict['text']={'num_annotated':num_annotated,'most_recent_20':most_recent_20,'most_recent_1':most_recent_1}
    else:
        rolls_dict['text']={'num_annotated':0,'most_recent_20':None,'most_recent_1':None}
    return rolls_dict

def test_deviation_mean(die_size:int,observed_mean:int,high_bad:bool=False):
    minus_2,minus_1,expected_mean,plus_1,plus_2 = roll_quintiles[die_size]
    
    print(f'Expected: {expected_mean} | Observed: {observed_mean}')
    
    deviation = None
    if observed_mean < minus_1:
        if observed_mean < minus_2:
            deviation = 'v_low'
        else:
            deviation = 'low'
        if high_bad:
            deviation = deviation + '_good'
    elif observed_mean > plus_1:
        if observed_mean > plus_2:
            deviation = 'v_high'
        else:
            deviation = 'high'
        if high_bad:
            deviation = deviation + '_bad'
    return deviation

def test_deviation_count(die_size:int,num_outcome:int,total_rolls:int,high_bad:bool=False):
    outcomes_expected = (total_rolls/die_size)
    
    print(f'Expected: {round(outcomes_expected)} | Observed: {num_outcome}')
    
    minus_1 = round(outcomes_expected - max(1,(outcomes_expected*(0.15))))
    minus_2 = round(outcomes_expected - max(2,(outcomes_expected*(0.3))))
    plus_1 = round(outcomes_expected + max(1,(outcomes_expected*(0.15))))
    plus_2 = round(outcomes_expected + max(2,(outcomes_expected*(0.3))))
    
    outcomes_expected = round(outcomes_expected)
    
    print(f'Expected: {round(outcomes_expected)} | Observed: {num_outcome}')
    print([minus_2,minus_1,outcomes_expected,plus_1,plus_2])
    
    deviation = None
    if num_outcome <= minus_1:
        if num_outcome < minus_2:
            deviation = 'v_low'
        else:
            deviation = 'low'
        if high_bad:
            deviation = deviation + '_good'
    elif num_outcome >= plus_1:
        if num_outcome > plus_2:
            deviation = 'v_high'
        else:
            deviation = 'high'
        if high_bad:
            deviation = deviation + '_bad'
    return deviation

def rollstats_text(roll_df,query_info):
    rolls_dict = roll_stats(roll_df)
    print(query_info)
    if query_info['date_range'] and query_info['user_id']:
        header_text = f"Showing statistics for {query_info['user_id']}'s dice rolls from _{query_info['date_range'][0]}_ to _{query_info['date_range'][1]}_ ..."
    elif query_info['date_range']:
        header_text = f"Showing statistics for dice rolls from _{query_info['date_range'][0]}_ to _{query_info['date_range'][1]}_ ..."
    elif query_info['user_id']:
        header_text = f"Showing statistics for {query_info['user_id']}'s dice rolls ..."
    else:
        header_text = "Showing dice roll statistics ..."
    text_out=['','\t\t# Rolls\tAverage']
    total_dice=0
    for i in [4,6,8,10,12,20,100]:
        rolls_list = rolls_dict[i]
        total_dice += len(rolls_list)
        die_string = f'd{i}'
        die_string = "".join(['  ']*(4-len(die_string))) + die_string
        if len(rolls_list) > 0:
            rolls_mean = sum(rolls_list)/len(rolls_list)
            line_text = f'\t{die_string}:\t{len(rolls_dict[i])}\t{rolls_mean:.1f}'
            rolls_deviation = test_deviation_mean(i,rolls_mean)
            if rolls_deviation:
                line_text = line_text + ' ' + deviation_indicators[rolls_deviation]
        else:
            line_text = f'\t{die_string}:\t0\tNA'
        text_out.append(line_text)
    text_out.append('')
    text_out.append('\t\t# Rolls')
    if len(rolls_dict[20]) > 0:
        d20_expected=round(len(rolls_dict[20])/20)
    else:
        d20_expected='NA'
    nat_20s = rolls_dict['Nat20']
    line_text = f'\t<a:nat20:906636383806955611>: {nat_20s}'
    if d20_expected != 'NA':
        rolls_deviation = test_deviation_count(20,nat_20s,len(rolls_dict[20]))
        if rolls_deviation:
            line_text = line_text + ' ' + deviation_indicators[rolls_deviation]
        text_out.append(line_text)
    nat_1s = rolls_dict['Nat1']
    line_text = f'\t<a:critfail:906639652008656966>: {nat_1s}'
    if d20_expected != 'NA':
        rolls_deviation = test_deviation_count(20,nat_1s,len(rolls_dict[20]),True)
        if rolls_deviation:
            line_text = line_text + ' ' + deviation_indicators[rolls_deviation]
        text_out.append(line_text)
    if 'text' in rolls_dict:
        annotated_rolls = rolls_dict['text']['num_annotated']
        annotated_rolls_text = f"\nAnnotated Rolls: {annotated_rolls} ({annotated_rolls/query_info['clusters']*100:.1f}%)\n"
        text_out.append(annotated_rolls_text)
        if rolls_dict['text']['most_recent_20']:
            recent_20_text = f"Most recent annotated :nat-20::\n\t*\\\"{rolls_dict['text']['most_recent_20']}\\\"*\n".replace('" ','"')
            text_out.append(recent_20_text)
        if rolls_dict['text']['most_recent_1']:
            recent_1_text = f"Most recent annotated :crit-fail::\n\t*\\\"{rolls_dict['text']['most_recent_1']}\\\"*\n".replace('" ','"')
            text_out.append(recent_1_text)
    counts_text = f"{total_dice} dice rolled in {query_info['clusters']} sets."
    text_out = [header_text,counts_text] + text_out
    print("\n".join(text_out))
    return text_out
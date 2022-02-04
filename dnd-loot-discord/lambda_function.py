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

from loot_generator import generate_loot_text as loot_generator
from loot_generator import generate_single

def generate_loot(options:list, command:str="loot"):
    value = None
    hoard_size = 'stash'
    loot_type = None
    cursed = None
    
    if options:
        for i in options:
            if i['name'] == 'value':
                value = int(i['value'])
            elif i['name'] == 'size':
                hoard_size = i['value']
            elif i['name'] == 'type':
                loot_type = i['value']
            elif i['name'] == 'cursed':
                cursed = i['value']
                
    if hoard_size == 'hoard':
        if not value:
            value = 15000
        is_hoard = True
    elif hoard_size == 'item':
        if not value:
            value = 3500
        is_hoard = False
    else:
        if not value:
            value = 6500
        is_hoard = False
    
    if hoard_size == 'item':
        loot_text, total_value = generate_single(amount=value,item_type=loot_type)
    else:
        loot_text, total_value = loot_generator(value, loot_type=loot_type, is_hoard=is_hoard)

    if not loot_type:
        pass
    elif loot_type == 'art' and hoard_size != 'item':
        loot_type = 'art items'
    elif loot_type == 'weapon':
        loot_type = 'weaponry'
    elif loot_type != 'currency' and loot_type != 'armor' and loot_type != 'ammo' and hoard_size != 'item':
        loot_type = loot_type + 's'
    if loot_type:
        item_type_text = f" of {loot_type}"
    else:
        item_type_text = ''
    loot_text = f'Generated a loot {hoard_size}{item_type_text} worth {total_value} GP:\n{loot_text}'
    return loot_text

def lambda_handler(event, context):
    print(event)
    options = event['options']
    command = event['command']
    response_url = event['response_url']
    if command == 'loot':
        message_out = generate_loot(options, command)
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

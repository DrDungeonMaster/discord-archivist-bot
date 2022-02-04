from math import floor,ceil
import re

from loot_generator import retrieve_item_info
from commons.common_functions import is_numeric

def value_per_day(skill_modifier: int=0):
    gp_per_day = ceil((2 ** skill_modifier)*10)/10
    return gp_per_day


def is_modifier_check(mod_str:str):
    is_modifier = True
    legal_characters = ['+','-','*','x',',']
    for i in range(0,10):
        legal_characters.append(str(i))
    for i in mod_str:
        if i not in legal_characters:
            is_modifier = False
    return is_modifier

def teamwork_value_per_day(skill_modifiers: list):
    num_workers = 0
    gp_per_day = 0
    for i in skill_modifiers:
        if type(i) is str and ('x' in i or '*' in i):
            worker_split = re.split('[\*x]',i)
            worker_output = value_per_day(int(worker_split[0])) * int(worker_split[1])
            gp_per_day += worker_output
            num_workers += int(worker_split[1])
        else:
            worker_output = value_per_day(int(i))
            gp_per_day += worker_output
            num_workers += 1
    return gp_per_day, num_workers

def time_to_text(input_time_days:float):
    time_parts = []
    time_years = floor(input_time_days/365)
    if time_years > 0:
        years_str = f'{time_years} year'
        if time_years > 1:
            years_str = years_str + 's'
        time_parts.append(years_str)
        input_time_days = input_time_days - time_years*365
    time_days = floor(input_time_days)
    if time_days > 0:
        days_str = f'{time_days} day'
        if time_days > 1:
            days_str = days_str + 's'
        time_parts.append(days_str)
        input_time_days = input_time_days - time_days
    if time_years == 0 and time_days < 10:
        time_hours = input_time_days * 8
        if time_hours > 7.984:
            time_hours = 0
            time_days += 1
            days_str = f'{time_days} day'
            if time_days > 1:
                days_str = days_str + 's'
                time_parts[-1] = days_str
            elif time_days == 1:
                time_parts.append('1 day')
        elif floor(time_hours) > 0:
            time_hours = floor(time_hours)
            hours_str = f'{time_hours} hour'
            if time_hours > 1:
                hours_str = hours_str + 's'
            time_parts.append(hours_str)
            input_time_days = input_time_days - (time_hours/8)
    if time_days == 0 and time_hours < 8:
        time_minutes = input_time_days * 8 * 60
        if ceil(time_minutes) == 60:
            time_minutes = 0
            time_hours += 1
            if time_hours == 2:
                time_parts[-1] = time_parts[-1] + 's'
            elif time_hours == 1:
                time_parts.append('1 hour')
        elif time_minutes > 0:
            time_minutes = ceil(time_minutes)
            minutes_str = f'{time_minutes} minute'
            if time_minutes > 1:
                minutes_str = minutes_str + 's'
            time_parts.append(minutes_str)
            input_time_days = 0
    out_text = " and ".join(time_parts)
    return out_text


def produce_item(value_str:str=None, skill_str:str=None):
    out_text = None
    describe_text = None
    is_unique = False
    craft_value = None
    if value_str:
        if is_numeric(value_str):
            # An amount of money was given
            craft_value = float(value_str)
            item_text = 'an item of this value'
            describe_text = None
        else:
            # An item was given. Do a search.
            is_item = True
            item_info, good_match = retrieve_item_info(value_str)
            if good_match:
                item_name = item_info[0]
                craft_value = item_info[3]
                item_text = 'this item'
                if '~' in item_name:
                    is_unique = True
                    item_name = item_name.replace('~','')
                describe_text = f'{item_info[2].lower()} {item_info[1].lower()}, valued at {craft_value:,} GP.'
                first_letter_item = item_name.replace('~','').replace('_','').replace("\'","")[0].lower()
                first_letter_describe = describe_text[0].lower()
                if is_unique:
                    first_article = ''
                elif first_letter_item in ['a','e','i','o','u']:
                    first_article = 'An '
                else:
                    first_article = 'A '
                if first_letter_describe in ['a','e','i','o','u']:
                    second_article = 'an'
                else:
                    second_article = 'a'
                describe_text = f'{first_article}{item_name} is {second_article} {describe_text}'
            else:
                out_text = f"There was no item that was a good match for your search term: \'{value_str}\'\nThe closest matches were:\n\t" + "\n\t".join(item_info)
    if is_unique:
        out_text = f'It is considered to be a unique item, which cannot be replicated by normal means.'
    elif not out_text:
        if skill_str:
            gp_per_day, num_workers = teamwork_value_per_day(str(skill_str).split(','))
            if gp_per_day >= 10:
                gp_per_day = int(ceil(gp_per_day))
            if craft_value:
                days_to_produce = craft_value / gp_per_day
                if num_workers > 1:
                    worker_text = f'With these {num_workers} workers'
                else:
                    worker_text = f'With this worker'
                worker_text = f'{worker_text} ({skill_str})'
                time_text = f'{item_text} would require {time_to_text(days_to_produce)} to produce'
                cost_text = f'at a materials cost of {ceil(craft_value/2):,} GP.'
                out_text = ", ".join([worker_text, time_text, cost_text])
            else:
                if num_workers > 1:
                    worker_text = f'these {num_workers} workers'
                else:
                    worker_text = 'this worker'
                worker_text = f'With {worker_text} ({skill_str}) working 8-hour days'
                value_text = f'it is possible to produce up to {gp_per_day:,} GP of item value per day.'
                out_text = ", ".join([worker_text, value_text])
        else:
            gp_per_day, num_workers = teamwork_value_per_day('0'.split(','))
            days_to_produce = craft_value / gp_per_day
            worker_text = f'Using one unskilled laborer'
            time_text = f'{item_text} would require {time_to_text(days_to_produce)} to produce'
            cost_text = f'at a materials cost of {ceil(craft_value/2):,} GP.'
            out_text = ", ".join([worker_text,time_text,cost_text])
    if describe_text:
        out_text = describe_text + '\n\n' + out_text
    return out_text

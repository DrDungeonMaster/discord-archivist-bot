from itertools import cycle
from random import random
from random import betavariate as rand_beta
from random import uniform as rand_unif
from random import shuffle as shuffle
from copy import deepcopy as copy
from difflib import get_close_matches as fuzzmatch
from math import floor, ceil
from statistics import median
import re

from commons.common_functions import choose
from loot_database import curses_data, coin_value, gems_data, gem_types, items_replace, items_data, emojis


### loot-holder dictionaries ###

master_coins_dict = {}
for coin in coin_value.keys():
    master_coins_dict[coin]=0
master_coins_dict['Other']=[]
    
master_gems_dict = {}
for gem in gems_data.keys():
    master_gems_dict[gem]=[]

master_items_dict = {}
for item in items_data.keys():
    master_items_dict[item]=[]

reverse_categories={'items':{},'gems':{}}
for i in [0,1]:
    for c in gems_data:
        cat_label = gems_data[c][i]
        if cat_label not in reverse_categories['gems']:
            reverse_categories['gems'][cat_label]=[c]
        else:
            reverse_categories['gems'][cat_label].append(c)
    for c in items_data:
        cat_label = items_data[c][i]
        if cat_label not in reverse_categories['items']:
            reverse_categories['items'][cat_label]=[c]
        else:
            reverse_categories['items'][cat_label].append(c)

### functions ###

def choose_curses(amount:float):
    if amount < 500:
        curse_level = 'non_cursed'
    elif amount < 2500:
        curse_level = 'curses_0'
    elif amount < 15000:
        curse_level = 'curses_1'
    elif amount < 50000:
        curse_level = 'curses_2'
    elif amount < 150000:
        curse_level = 'curses_3'
    else:
        curse_level = 'curses_4'
    return curse_level

def is_cursed(item_name:str, item_value:float, curses_dict:dict=curses_data['curses_4'], prob_cursed:float=0.01, bonus_value:int=0):
    if random() <= prob_cursed:
        cursed_item = True
    else:
        cursed_item = False
    if cursed_item is True:
        curse=choose(list(curses_dict.keys()))[0]
        curse_value_modifier=curses_dict[curse]
        item_value = int(item_value * curse_value_modifier + bonus_value)
        item_name = item_name + f' *Curse of {curse}'
    return item_name, item_value

def choose_jewels_composition(amount:float):
    if amount < 25:
        composition = ''
    elif amount < 500:
        composition = 'FBA'
    elif amount < 5000:
        composition = 'GKCFB'
    elif amount < 50000:
        composition = 'MQHDPLG'
    elif amount < 500000:
        composition = 'NRIEMQHP'
    elif amount < 5000000:
        composition = 'TSJRIEM'
    else:
        composition = 'STOJNRIE'
    return composition

def generate_coinage(amount:int,coin_type:str='Gold',coin_value:dict=coin_value,error_margin:float=0.10):
    value_coins = amount * (1 - rand_beta(2,4.5)) * (1+error_margin*1.5)
    count_coins = int(value_coins/coin_value[coin_type])
    return count_coins

def choose_coins_composition(amount:float):
    if amount < 2:
        composition = 'SC'
    elif amount < 10:
        composition = 'GSSC'
    elif amount < 100:
        composition = 'GPSJSC'
    elif amount < 1000:
        composition = 'GPJGS'
    elif amount < 10000:
        composition = 'PJGGS'
    else:
        composition = 'JPG'
    return composition

def assorted_coinage(amount:float,composition:str=None,error_margin:float=0.10,original_amount:int=None,coins_dict:dict=master_coins_dict,big_coin_rate:float=(1/10000)):
    print('Generating coins:')
    coins_dict = copy(coins_dict)
    if big_coin_rate > 0:
        big_coin_tries = min(50,ceil(big_coin_rate * amount))
        for i in range(0, big_coin_tries):
            if ceil(rand_unif(0,20)) == 20:
                big_coin_value = round(rand_unif(0,amount))
                coins_dict['Other'].append(generate_coin_single(big_coin_value,is_single=False))
                amount -= big_coin_value
    if original_amount is None:
        original_amount = amount
    if composition is None:
        composition = choose_coins_composition(original_amount)
    for i in list(composition):
        if i.upper() == 'P' and amount > (error_margin*original_amount):
            count_coins = generate_coinage(amount,'Platinum',error_margin=error_margin)
            coins_dict['Platinum'] += count_coins
            amount -= (count_coins * coin_value['Platinum'])
        elif i.upper() == 'G' and amount > (error_margin*original_amount):
            count_coins = generate_coinage(amount,'Gold',error_margin=error_margin)
            coins_dict['Gold'] += count_coins
            amount -= (count_coins * coin_value['Gold'])
        elif i.upper() == 'E' and amount > (error_margin*original_amount*coin_value['Electrum']):
            count_coins = generate_coinage(amount,'Electrum',error_margin=error_margin)
            coins_dict['Electrum'] += count_coins
            amount -= (count_coins * coin_value['Electrum'])
        elif i.upper() == 'S' and amount > (error_margin*original_amount*coin_value['Silver']):
            count_coins = generate_coinage(amount,'Silver',error_margin=error_margin)
            coins_dict['Silver'] += count_coins
            amount -= (count_coins * coin_value['Silver'])
        elif i.upper() == 'C' and amount > (error_margin*original_amount*coin_value['Copper']):
            count_coins = generate_coinage(amount,'Copper',error_margin=error_margin)
            coins_dict['Copper'] += count_coins
            amount -= (count_coins * coin_value['Copper'])
        else:
            pass
    if amount > (error_margin*original_amount):
        coins_dict = assorted_coinage(amount*(1+error_margin/2),composition,error_margin,original_amount,coins_dict)
    print(coins_dict)
    return coins_dict

def generate_gemstones(amount:int,composition:str=None,gems_data:dict=gems_data,error_margin:float=0.10,prob_cursed:float=0.01, curses_dict:dict=None):
    print('Generating gemstones:')
    if composition is None:
        composition = choose_jewels_composition(amount)
    if curses_dict is None:
        curse_level = choose_curses(amount)
        curses_dict = curses_data[curse_level]
    gems_dict = copy(master_gems_dict)
    gems_total_value = 0
    if len(composition) == 0:
        pass
    else:
        for i in cycle(list(composition)):
            if gems_total_value > (amount * (1-error_margin)):
                break
            gem_info = gems_data[i]
            gem_size = gem_info[0]
            gem_type = gem_info[1]
            gem_description = choose(gem_types[gem_type],1)[0]
            gem_value = gem_info[2]
            if prob_cursed > 0 and len(curses_dict) >= 1:
                gem_description,gem_value=is_cursed(gem_description,gem_value,curses_dict,prob_cursed,250)
            if gems_total_value + gem_value <= amount*(1+error_margin):
                #probability_factor = (3*gem_value)/(amount-gems_total_value)
                #if probability_factor <= 0:
                #    add_gem = True
                #else:
                #    add_gem = round(rand_beta(2.5,probability_factor))
                #if bool(add_gem) is True:
                gems_total_value += gem_value
                gem_description = f'{gem_description} : {gem_value} GP'
                gems_dict[i].append(gem_description)
    print(gems_dict)
    return gems_dict

def total_coins_value(coins_dict:dict,coin_value:dict=coin_value):
    total_value = 0
    for i in coins_dict:
        total_value += coins_dict[i] * coin_value[i]
    return total_value

def parse_gems_dict(gems_dict:dict,gems_data:dict=gems_data):
    total_gems_value = 0
    total_gems_count = 0
    output_dict = {}
    for i in gems_dict:
        num_gems = len(gems_dict[i])
        gems_value = num_gems * gems_data[i][2]
        rarity_class = gems_data[i][1]
        size_class = gems_data[i][0]
        total_gems_value += gems_value
        total_gems_count += num_gems
        if num_gems > 0:
            if size_class not in output_dict:
                output_dict[size_class]={}
            if rarity_class not in output_dict[size_class]:
                output_dict[size_class][rarity_class]=[]
            output_dict[size_class][rarity_class].extend(gems_dict[i])
    text_report = []
    for i in output_dict:
        size_count = 0
        size_lines = []
        for j in output_dict[i]:
            rarity_count = len(output_dict[i][j])
            size_count += rarity_count
            size_lines.append(f'{rarity_count} {j} ({",".join(output_dict[i][j])})')
        size_lines.reverse()
        size_line = f'{size_count} {i}: ' + ", ".join(size_lines)
        text_report.append(size_line)
    start_text = f'You found {total_gems_count} gemstones:'
    value_text = f'Total value: {total_gems_value}'
    text_report = [start_text] + text_report + [value_text]
    return text_report

def test_gemstones(input_number:int):
    gemstones_found=generate_gemstones(input_number)
    text_report=parse_gems_dict(gemstones_found)
    print("\n".join(text_report))
    return None

def choose_items_composition(amount:float, item_type:str=None, is_hoard:bool=False, items_data:dict=items_data):
    include_items = []
    for i in items_data:
        if item_type:
            if item_type == 'food':
                item_type = 'delicacy'
            if items_data[i][0].lower().startswith(item_type.lower()[0:3]):
                include_items.append(i)
        else:
            include_items.append(i)
    composition = []
    shuffle(include_items)
    for i in include_items:
        item_values = list(items_data[i][2].values())
        cat_med = median(item_values)
        cat_min = min(item_values)
        cat_max = max(item_values)
        if items_data[i][0].lower().startswith('amm'):
            cat_med = cat_med * 6
            cat_min = cat_min * 3
            cat_max = cat_max * 12
        if (is_hoard and amount/3 >= cat_med) or (amount > cat_min*1.1 and amount < cat_max * 5):
            composition.append(i)
    if not item_type and not is_hoard:
        bonus_composition = []
        for i in composition:
            if not items_data[i][0].startswith('Del') and not items_data[i][0].startswith('Art'):
                bonus_composition.append(i)
        composition.extend(bonus_composition)
    shuffle(composition)
    return composition

def string_to_type(string:str,convert_dict:dict=reverse_categories['items']):
    composition = ""
    if string is None:
        for i in convert_dict:
            composition = composition + "".join(convert_dict[i])
    else:
        start_str = string.replace("-"," ").split(" ")[0][0:4].lower()
        for i in convert_dict:
            if i.lower().startswith(start_str):
                composition = "".join(convert_dict[i])
                break
            else:
                pass
    return composition

def convert_type(item_type:str,subtype:str=None):
    if item_type.lower().startswith('gem') or item_type.lower().startswith('jewel'):
        convert_dict = reverse_categories['gems']
        composition = string_to_type(subtype,convert_dict)
    else:
        convert_dict = reverse_categories['items']
        composition = string_to_type(subtype,convert_dict)
    return composition

def generate_items(amount:int, loot_type:str=None, composition:str=None, items_data:dict=items_data,error_margin:float=0.10,prob_cursed:float=0.02, curses_dict:dict=None, loop_max:int=20):
    print('Generating items:')
    loop_counter = 0
    if composition is None:
        composition = choose_items_composition(amount, loot_type)
    if curses_dict is None:
        curse_level = choose_curses(amount)
        curses_dict = curses_data[curse_level]
    items_dict = copy(master_items_dict)
    items_total_value = 0
    unique_items = []
    if len(composition) == 0:
        exit('No items composition generated...?!')
    else:
        print(f'Allocated {items_total_value} of {amount}...')
        while items_total_value < amount*(1-error_margin):
            if loop_counter >= loop_max:
                composition = choose_items_composition(amount-items_total_value, loot_type)
                if len(composition) == 0:
                    break
            for i in composition:
                item_info = items_data[i]
                if min(item_info[2].values()) <= (amount-items_total_value):
                    item_type = item_info[0]
                    item_rarity = item_info[1]
                    item_name_raw = choose(adjust_item_freq(item_info[2]))[0]
                    item_name = update_item_name(item_name_raw)
                    if '~' in item_name:
                        unique = True
                        if item_name in unique_items:
                            duplicate = True
                            print(f'Removed duplicate item: {item_name}')
                        else:
                            duplicate = False
                            unique_items.append(item_name)
                    else:
                        duplicate = False
                        unique = False
                    if not duplicate:
                        item_value = item_info[2][item_name_raw]
                        if prob_cursed > 0 and len(curses_dict) >= 1 and not unique:
                            item_name,item_value=is_cursed(item_name,item_value,curses_dict,prob_cursed,500)
                        if '<' in item_name and '>' in item_name:
                            item_name, item_value = item_multiplier(item_name, item_value)
                        if items_total_value + item_value <= amount*(1+error_margin):
                            add_item = True
                            #if amount - items_total_value == 0:
                            #    items_total_value += 0.01
                            #probability_factor = (2*item_value)/(amount-items_total_value)
                            #if probability_factor <= 0:
                            #    add_item = True
                            #else:
                            #    add_item = round(rand_beta(2.5,probability_factor))
                            #if bool(add_item) is True:
                            item_name = update_item_name(item_name,item_value)
                            items_total_value += item_value
                            print(f'Added {item_name} : {item_value} GP')
                            items_dict[i].append(item_name.replace('~',''))
                        else:
                            print(f'Rejected {item_name} : {item_value} GP')
                        print(f'{amount-items_total_value} remaining.')
            loop_counter += 1
    return items_dict
    
def make_verbose_items(items_dict:dict,items_data:dict=items_data):
    verbose_items_dict={}
    for i in items_dict.keys():
        if len(items_dict[i]) > 0:
            verbose_items_dict[f'{items_data[i][0]}, {items_data[i][1]}'] = items_dict[i]
            
    return verbose_items_dict

def update_item_name(item_name:str,append_value:int=None,items_replace:dict=items_replace):
    if '{' in item_name and '}' in item_name:
        for i in items_replace:
            replacement = choose(items_replace[i])[0]
            item_name = item_name.replace('{' + i + '}',replacement)
    else:
        pass
    item_name = item_name.title().replace("'S ","'s ").replace('Of','of').replace(' The',' the').replace(' Di ','di')
    if '|' in item_name:
        item_name = item_name.split('|')[0]
    if append_value is not None:
        item_name = f'{item_name} : {int(append_value)} GP'
    return item_name

def item_multiplier(item_name:str,item_value:int=1):
    text_regex = '(?<=\<)[^\\d]*(?=\>)'
    num_regex = '(?<=\<)[0-9].*[0-9](?=\>)'
    num_matches = re.findall(num_regex,item_name)
    item_count = 1
    if len(num_matches) > 0:
        for i in num_matches:
            if '-' in i:
                [min, max] = i.split('-')
                count = floor(rand_unif(int(min),int(max)+1))
                item_name = item_name.replace(f'<{i}>',f'{count} ')
                item_count += count-1
        print(item_count)
        if item_count > 1:
            item_name = item_name.replace('<','').replace('>','')
        else:
            text_matches = re.findall(text_regex,item_name)
            print(text_matches)
            for i in text_matches:
                item_name = item_name.replace(f'<{i}>','')
    item_value = ceil(item_value * item_count)
    return item_name, item_value

def all_possible_versions(item_name:str, items_replace:dict=items_replace, remaining_loops: int=3, retain_template:bool=False):
    if '{' in item_name and '}' in item_name:
        possible_items = []
        if retain_template:
            possible_items.append(item_name.replace('{','').replace('}',''))
        for i in items_replace:
            replace_count = item_name.count('{')
            for replacement in items_replace[i]:
                new_item = item_name.replace('{' + i + '}',replacement)
                if new_item.count('{') < replace_count:
                    possible_items.append(new_item)
        possible_items = list(set(possible_items))
        if remaining_loops > 0:
            more_items = []
            for i in range(0,len(possible_items)):
                if '{' in possible_items[i] and '}' in possible_items[i]:
                    more_items.extend(all_possible_versions(possible_items[i], items_replace=items_replace, remaining_loops=remaining_loops-1,retain_template=retain_template))
                    possible_items[i] = ''
            possible_items.extend(more_items)
        else:
            for i in range(0,len(possible_items)):
                possible_items[i]=possible_items[i]
    else:
        possible_items = [item_name]
    possible_items = list(set(possible_items))
    return possible_items

def all_items_info(items_dict:dict=items_data):
    all_items_dict={}
    for i in items_dict:
        for j in items_data[i][2]:
            for k in all_possible_versions(j):
                k = k.title().replace("'S ","'s ").replace('Of','of').replace(' The',' the').replace(' Di ',' di ').replace('*','')
                all_items_dict[k] = [items_data[i][0],items_data[i][1],items_data[i][2][j]]
    return all_items_dict
    
def retrieve_item_info(item_search_string:str, items_info_dict:dict=all_items_info(),match_confidence:float=0.8):
    item_match = fuzzmatch(item_search_string.title(),list(items_info_dict.keys()),1,match_confidence)
    if len(item_match) > 0:
        good_match = True
        item_match = [item_match[0]] + items_info_dict[item_match[0]]
    else:
        good_match = False
        item_match = fuzzmatch(item_search_string.title(),list(items_info_dict.keys()),5,0)
    return item_match, good_match
    
def item_search_text(item_search_string:str,give_value:bool=False):
    item_match, good_match = retrieve_item_info(item_search_string)
    if good_match:
        item_name = item_match[0]
        item_type = item_match[1]
        item_rarity = item_match[2]
        item_value = item_match[3]
        unique_item = '~' in item_name
        if unique_item:
            item_name = item_name.replace('~','')
        out_text = f"'{item_name.replace('~','')} is an item of type '{item_type}' with a rarity of '{item_rarity}.'"
        if unique_item:
            out_text = out_text + ' It is considered to be unique item.'
        if give_value:
            out_text = out_text + f' Its estimated value is {item_value} GP.'
    else:
        out_text = f"There was no high-certainty match for your query: '{item_search_string}'. The next-closest matches are:\n"
        out_text = out_text + "\n".join(item_match).replace('~','')
    return out_text

def generate_loot(amount:int,loot_type:str=None,composition:str=None, is_hoard:bool=False):
    if loot_type is None:
        loot_results={'coins':None,'gemstones':None,'items':None}
    else:
        loot_type = loot_type.lower()
        if loot_type.startswith('jewels') or loot_type.startswith('gem'):
            loot_results={'gemstones':None}
        elif loot_type.startswith('coin') or loot_type == 'money' or loot_type == 'gold' or loot_type == 'currency':
            loot_results={'coins':None}
        else:
            loot_results={'items':None}
    print(loot_results)
    loot_totals=copy(loot_results)
    loot_types=list(loot_results.keys())
    loot_type_values={}
    if 'items' in loot_types and not is_hoard:
        loot_types.append('items')
    elif is_hoard:
        loot_types = loot_types * 2
    shuffle(loot_types)
    allocated_value = 0
    includes_items = False
    for loot_index in range(0,len(loot_types)):
        loot = loot_types[loot_index]
        if loot == "items":
            includes_items = True
        remaining_value = amount - allocated_value
        if loot_index == len(loot_types)-1:
            loot_type_value = remaining_value
        else:
            if is_hoard:
                multiplier = min(loot_index+1 / (len(loot_types)/2),1)
            else:
                multiplier = 1
            loot_type_value = round(rand_unif(0,remaining_value*multiplier))
            if loot_type_value < amount/10:
                loot_type_value=0
            elif remaining_value - loot_type_value < amount/10:
                loot_type_value = remaining_value
        if loot in loot_totals and loot_totals[loot] is not None:
            loot_totals[loot] += loot_type_value
        else:
            loot_totals[loot] = loot_type_value
        allocated_value = allocated_value + loot_type_value
    for loot in loot_totals:
        loot_type_value = loot_totals[loot]
        if loot == 'coins':
            loot_results[loot]=assorted_coinage(loot_type_value)
        elif loot == 'gemstones':
            gems_composition = choose_jewels_composition(loot_type_value)
            loot_results[loot]=make_verbose_items(generate_gemstones(loot_type_value,composition=gems_composition),gems_data)
        elif loot == 'items':
            if not composition:
                items_composition = choose_items_composition(amount,loot_type)
            else:
                items_composition = composition
            loot_results[loot]=make_verbose_items(generate_items(loot_type_value,loot_type=loot_type,composition=items_composition),items_data)
        else:
            loot_results[loot]=loot_type_value
    return loot_results, allocated_value
        
def generate_loot_text(amount:int,loot_type:str=None, is_hoard:bool=False):
    composition = choose_items_composition(amount, item_type=loot_type, is_hoard=is_hoard)
    print(composition)
    loot_results,loot_value = generate_loot(amount,loot_type,composition, is_hoard=is_hoard)
    output_text = []
    for loot in sorted(list(loot_results.keys())):
        if type(loot_results[loot]) is int or type(loot_results[loot]) is str:
            pass
        else:
            temp_text=[]
            if loot_type and loot_type.lower() in emojis:
                emoji = emojis[loot_type.lower()]
            elif loot.lower() in emojis:
                emoji = emojis[loot.lower()]
            elif loot.lower()[0:-1] in emojis:
                emoji = emojis[loot.lower()[0:-1]]
            else:
                emoji = "  "
            temp_text.append(f"\n {emoji} **{loot.title()}**:")
            category_total=0
            if loot_results[loot]:
                print(loot_results[loot])
                if loot == 'coins':
                    sort_order = ['Other','Platinum','Gold','Electrum','Silver','Copper']
                else:
                    sort_order = list(loot_results[loot].keys())
                for category in sort_order:
                    if type(loot_results[loot][category]) is int:
                        if loot_results[loot][category] > 0:
                            category_total += 1
                            text_line = f'\t\t{loot_results[loot][category]} {category} pieces'
                            temp_text.append(text_line)
                    else:
                        itemcount = len(loot_results[loot][category])
                        if itemcount > 0:
                            category_total += 1
                            if loot == 'gemstones':
                                category_label = f'\t\t{itemcount} {category}'
                                if itemcount > 1:
                                    category_label = category_label.replace(',','s,')
                                temp_text.append(category_label)
                                for indiv_item in loot_results[loot][category]:
                                    temp_text.append(f'\t\t\t{indiv_item}')
                            else:
                                for indiv_item in loot_results[loot][category]:
                                    temp_text.append(f'\t\t{indiv_item}')
        if category_total > 0:
            if loot == 'items':
                temp_text = sorted(temp_text,key=item_value, reverse=True)
            output_text.extend(temp_text)
            temp_text=[]
    output_text_paragraph = "\n".join(output_text)

    return output_text_paragraph,loot_value


def generate_item_single(amount:int,composition:str=None,item_type:str=None, items_data:dict=items_data,error_margin:float=0.30,prob_cursed:float=0.1, curses_dict:dict=None):
    if composition is None:
        composition = choose_items_composition(amount,item_type)
    if curses_dict is None:
        curse_level = choose_curses(amount)
        curses_dict = curses_data[curse_level]
    item_value = 0
    attempt_count = 0
    upper_value_limit = amount * (1 + error_margin)
    lower_value_limit = amount * (1 - error_margin)
    if len(composition) == 0:
        pass
    else:
        for i in cycle(list(composition)):
            if item_value >= lower_value_limit and item_value <= upper_value_limit:
                break
            if attempt_count >= 100:
                upper_value_limit = upper_value_limit * (1 + (error_margin/2))
                lower_value_limit = lower_value_limit * (1 - (error_margin/3))
                attempt_count = 0
            item_info = items_data[i]
            item_type = item_info[0]
            item_rarity = item_info[1]
            possible_items = list(item_info[2].keys())
            item_name = choose(possible_items)[0]
            if '~' in item_name:
                unique = True
            else:
                unique = False
            item_value = item_info[2][item_name]
            if prob_cursed > 0 and len(curses_dict) >= 1 and not unique:
                item_name,item_value=is_cursed(item_name,item_value,curses_dict,prob_cursed,500)
            item_name = update_item_name(item_name)
            attempt_count += 1
            if item_type.lower() == "wondrous item":
                item_type_key = 'wonder'
            elif item_type.lower() == 'delicacy':
                item_type_key = 'food'
            elif item_type.lower().startswith('art'):
                item_type_key = 'art'
            elif item_type.lower().startswith('gem'):
                item_type_key = 'gemstone'
            else:
                item_type_key = item_type.lower()
        try:
            if item_type_key.lower() in emojis:
                emoji = emojis[item_type_key]
            else:
                emoji = emojis['items']
        except:
            emoji = ' '
        item_description = f'{emoji} {item_name} ({item_rarity} {item_type})'
    return item_description,item_value

def generate_gemstone_single(amount:int,composition:str=None,gems_data:dict=gems_data,error_margin:float=0.25,prob_cursed:float=0.05, curses_dict:dict=None):
    if composition is None:
        composition = choose_jewels_composition(amount)
    if curses_dict is None:
        curse_level = choose_curses(amount)
        curses_dict = curses_data[curse_level]
    gems_dict = copy(master_gems_dict)
    gem_value = 0
    attempt_count = 0
    upper_value_limit = amount * (1 + error_margin)
    lower_value_limit = amount * (1 - error_margin)
    if len(composition) == 0:
        pass
    else:
        for i in cycle(list(composition)):
            if gem_value >= lower_value_limit and gem_value <= upper_value_limit:
                break
            if attempt_count >= 100:
                upper_value_limit = upper_value_limit * (1 + (error_margin/2))
                lower_value_limit = lower_value_limit * (1 - (error_margin/3))
                attempt_count = 0
            gem_info = gems_data[i]
            gem_size = gem_info[0]
            gem_type = gem_info[1]
            gem_description = choose(gem_types[gem_type],1)[0]
            gem_value = gem_info[2]
            print(gem_value)
            print(f'[{lower_value_limit},{upper_value_limit}]')
            if prob_cursed > 0 and len(curses_dict) >= 1:
                gem_description,gem_value=is_cursed(gem_description,gem_value,curses_dict,prob_cursed,250)
            attempt_count += 1
    gem_description = f'{emojis["gemstone"]} {gem_description} ({gem_size}, {gem_type})'
    return gem_description,gem_value

def generate_single(amount:int,item_type:str):
    if item_type and (item_type.lower().startswith('gem') or item_type.lower().startswith('jewel')):
        composition = choose_jewels_composition(amount)
        item_result,item_value = generate_gemstone_single(amount,composition,gems_data)
    elif item_type and (item_type.lower().startswith('coin') or item_type.lower().startswith('currency')):
        item_result = generate_coin_single(amount)
        item_value = amount
    else:
        composition = choose_items_composition(amount,item_type)
        item_result,item_value = generate_item_single(amount,composition,item_type,items_data)
    return item_result,item_value

def generate_coin_single(amount:int, is_single:bool=True):
    if amount > 5000:
        material = ["platinum", "platinum", "gold"]
    elif amount > 2000:
        material = ["platinum", "gold"]
    elif amount > 500:
        material = ["platinum","gold","gold"]
    elif amount > 100:
        material = ["platinum", "gold", "gold", "gold", "silver", "electrum"]
    elif amount > 20:
        material = ["platinum", "gold", "gold", "silver", "silver", "copper", "electrum"]
    else:
        material = ["gold", "silver", "silver", "silver", "copper", "copper", "electrum"]
    material_choice = choose(material)[0]
    multiplied_size = amount/coin_value[material_choice.title()]
    weight_oz = ceil((multiplied_size % 50) * (16/50))
    weight_lb = floor(multiplied_size / 50)
    if weight_oz == 16:
        weight_oz = 0
        weight_lb += 1
    weight_list = []
    if weight_lb > 0:
        weight_list.append(f'{weight_lb} lb')
    if weight_oz > 0:
        weight_list.append(f'{weight_oz} oz')
    weight_text = " ".join(weight_list)
    if weight_lb > 10000:
        size = "mind-bogglingly gargantuan"
    elif weight_lb > 1000:
        size = "absolutely enormous"
    elif weight_lb > 100:
        size = "comically oversized"
    elif weight_lb > 10:
        size = "huge"
    elif weight_lb > 1:
        size = "large"
    else:
        size = "strange"
    if is_single:
        coin_text = f"A single {size} {material_choice} coin, weighing {weight_text} and worth exactly {amount} GP."
    else:
        coin_text = f"{size} {material_choice} Coin ({weight_text}) : {amount} GP"
    return coin_text

def item_value(item:str):
    try:
        gp_value = int(item.split(':')[1].replace(' GP',''))
    except:
        gp_value = 10 ** 10
    return gp_value

def adjust_item_freq(loot_value_dict:dict):
    items_list = list(loot_value_dict.keys())
    added_items_list = []
    for i in items_list:
        if '|' in i:
            try:
                item_multiplier = i.split('|')[1]
                added_items_list.extend([i]*(int(item_multiplier)-1))
            except:
                pass
    items_list.extend(added_items_list)
    return items_list
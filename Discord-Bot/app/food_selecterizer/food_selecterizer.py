from random import choice, shuffle
from copy import deepcopy
from app.commons.common_functions import simplify
from app.food_selecterizer.food_options import food_options as food_options_dict

# Set tags you never want to see as 0
custom_tag_limits={
    'Avocado':3,
    'Rice':2,
    'Takeout':2
    }

def filter_food_choices(require:str=None, exclude:str=None, food_options:dict=food_options_dict):
    if require:
        require = require.split(',')
        for i in range(0,len(require)):
            require[i] = simplify(require[i])
        num_requirements = len(require)
    else:
        num_requirements = 0
    if exclude:
        exclude = exclude.split(',')
        for i in range(0,len(exclude)):
            exclude[i] = simplify(exclude[i])
    food_options_simpletags = deepcopy(food_options)
    food_options_filtered = {}
    for i in food_options_simpletags:
        for j in range(0,len(food_options_simpletags[i])):
            food_options_simpletags[i][j] = simplify(food_options[i][j])
        filter_list = [0]
        if require:
            for j in require:
                if j in food_options_simpletags[i]:
                    filter_list.append(1)
        if exclude:
            for j in exclude:
                if j in food_options_simpletags[i]:
                    filter_list.append(-1)
        if sum(filter_list) == num_requirements:
            food_options_filtered[i]=food_options[i]
    return food_options_filtered

def choose_food_options(days_to_generate:int=None,default_tag_limit:int=1,custom_tag_limits:dict=custom_tag_limits,loop_limit:int=15,required_tags:str=None,excluded_tags:str=None,food_options:dict=food_options_dict):
    food_note_list = []
    if required_tags or excluded_tags:
        food_options = filter_food_choices(required_tags, excluded_tags, food_options_dict)
        if required_tags:
            food_note_list.append(" tagged " + required_tags.replace(",",", ").title() )
        if excluded_tags:
            food_note_list.append(" not tagged " + excluded_tags.replace(",",", ").title())
    food_note = " and".join(food_note_list)
    if not days_to_generate:
        days_to_generate = min(len(food_options),7)
    if days_to_generate == len(food_options):
        dishes_selected = list(food_options.keys())
    else:
        loop_counter = 0
        dishes_selected=[]
        all_tags = []
        while len(dishes_selected) < days_to_generate:
            if loop_counter >= loop_limit:
                #print(f'It was impossible to select sufficiently diverse options with a limit of {default_tag_limit}. Increasing by one.')
                default_tag_limit += 1
                for i in custom_tag_limits:
                    if custom_tag_limits[i] > 0:
                        custom_tag_limits[i] += 1
                loop_counter = 0
            food = choice(list(food_options.keys()))
            if food in dishes_selected and days_to_generate < len(food_options):
                #print(f'Rejected Food:{food} Reason:Duplicate Entry')
                pass
            else:
                tags = food_options[food]
                include_food = True
                for i in tags:
                    tag_occurrences = all_tags.count(i)
                    tag_limit = default_tag_limit
                    if i in custom_tag_limits:
                        tag_limit = custom_tag_limits[i]
                    if tag_occurrences >= tag_limit:
                        include_food = False
                        #print(f'Rejected Food:{food} Reason:{i}')
                    else:
                        #print(f'Food:{food} Tag:{i}')
                        pass
                if include_food:
                    dishes_selected.append(food)
                    all_tags.extend(tags)
                else:
                    loop_counter += 1
    #shuffle(dishes_selected)
    return dishes_selected, food_note

def list_dishes(dishes_selected:list, food_note:str='', food_options:dict=food_options_dict):
    if len(dishes_selected) == 0:
        meals_text = 'There were no possible food options that satisfied your requirements.'
    elif len(dishes_selected) == 1:
        meals_text = f'Here is a carefully-selected meal{food_note}:'
        for i in dishes_selected:
            meals_text = f'{meals_text}\n> {i} ||({", ".join(food_options[i])})||'
    else:
        meals_text = f'Here are {len(dishes_selected)} carefully-selected meals{food_note}:'
        for i in dishes_selected:
            meals_text = f'{meals_text}\n> {i} ||({", ".join(food_options[i])})||'
    return meals_text

if __name__ == "__main__":
    import sys
    try:
        meals = sys.argv[1]
    except:
        meals = 7
    meals_text = list_dishes(choose_food_options(meals))
    print(meals_text)
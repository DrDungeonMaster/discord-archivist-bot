import boto3
import json

from app.commons.common_functions import choose

error_json = {"type": 4,"data": {"content": f"That command is under construction. Please be patient.","tts":False,"embeds": [],"allowed_mentions": { "parse": [] }}}
thinking_json = {"type": 5,"data": {"content": f"<Asynchronous function executing>","tts":False,"embeds": [],"allowed_mentions": { "parse": [] }}}

def command_handler(event:dict):
    print(event)
    time_epoch = event['requestContext']['timeEpoch']
    body = json.loads(event['body'])
    data = body['data']
    if 'member' in body:
        member = body['member']
        user = member['user']
    else:
        user = body['user']
        member = {"user":user}
    print(user)
    username = user['username']
    discriminator = user['discriminator']
    application_id = body['application_id']
    interaction_id = data['id']
    interaction_token = body['token']
    command = data['name']
    try:
        options = data['options']
    except:
        options = None
    
    response_url = f"https://discord.com/api/v8/webhooks/{application_id}/{interaction_token}/messages/@original"
    
    print(f'Command: {command}')
    if command == 'roll' or command == 'rollstats':
        to_return = diceroll_lambda(member, options, response_url, command, time_epoch)
        print('Success')
    elif command == "names":
        to_return = names_generator(options,command)
        print('Success')
    elif command == "books":
        to_return = books_generator(options,command)
        print('Success')
    elif command == 'meals':
        to_return = suggest_meals(options,command)
        print('Success')
    elif command == 'age':
        to_return = ageconvert_lambda(options, response_url, command)
        print('Success')
    elif command == 'loot':
        to_return = lootgenerate_lambda(options, response_url, command)
    else:
        to_return = error_json
        print('Not yet ready')
    return to_return

### Calls the various functions ###

def names_generator(options:list, command:str="names"):
    from app.name_generator.names_handler import get_names
    race = "human"
    gender = "both"
    count = 10
    for i in options:
        if 'name' in i and 'value' in i:
            if i['name'] == 'race':
                race = i['value']
            elif i['name'] == 'gender':
                gender = i['value']
            elif i['name'] == 'count':
                count = int(i['value'])
    names_list = get_names(race=race, sex=gender, count=count)
    names_text = f'Generated {count} {race.title()} name'
    if count > 1:
        names_text = names_text + 's'
    names_text = names_text + ':\n> ' + "\n> ".join(names_list)
    to_return = {"type": 4,"data": {"content": names_text,"tts":False,"embeds": [],"allowed_mentions": { "parse": [] }}}
    return to_return

def books_generator(options:list, command:str="books"):
    from app.name_generator.book_names import get_book_names
    from app.name_generator.book_names import book_formats_list
    topic = "all"
    count = 10
    use_emojis = True
    if options:
        for i in options:
            if 'name' in i and 'value' in i:
                if i['name'] == 'topic':
                    topic = i['value']
                elif i['name'] == 'count':
                    count = min(int(i['value']),50)
                elif i['name'] == 'emojis':
                    use_emojis = i['value']
        if topic == 'random' or (topic == 'all' and count == 1):
            topic = choose(book_formats_list)[0]
    books_list = get_book_names(topic=topic, count=count, use_emojis=use_emojis)
    if count > 1:
        s = 's'
    else:
        s = ''
    if topic == 'all':
        subject_text = 'a variety of subjects'
    else:
        subject_text = f'on the topic of _{topic.title()}_'
    books_text = f'Generated {count} book{s} on {subject_text}'
    if use_emojis:
        books_text = ':books: ' + books_text
    books_text = books_text + ':\n> ' + "\n> ".join(books_list)
    to_return = {"type": 4,"data": {"content": books_text,"tts":False,"embeds": [],"allowed_mentions": { "parse": [] }}}
    return to_return

def suggest_meals(options:list=None, command:str="food"):
    from app.food_selecterizer.food_selecterizer import choose_food_options,list_dishes
    meals = None
    require = None
    exclude = None
    if options:
        for i in options:
            if i['name'] == 'count':
                meals = int(i['value'])
            elif i['name'] == 'require':
                require = i['value']
            elif i['name'] == 'exclude':
                exclude = i['value']
    dishes_selected, food_note = choose_food_options(meals, required_tags=require, excluded_tags=exclude)
    meals_text = list_dishes(dishes_selected, food_note)
    to_return = {"type": 4,"data": {"content": meals_text,"tts":False,"embeds": [],"allowed_mentions": { "parse": [] }}}
    return to_return

def diceroll_lambda(member:dict, options:list, response_url:str, command:str="roll", time_epoch:int=None):
    to_return = thinking_json
    
    payload_dict={'member':member, 'options':options, 'response_url':response_url,'command':command, 'timeEpoch':time_epoch}
    print(payload_dict)
    
    lambda_client = boto3.client('lambda')
    lambda_payload = json.dumps(payload_dict)
    lambda_client.invoke(FunctionName='dnd-dice-discord', 
                        InvocationType='Event',
                        Payload=lambda_payload)
    return to_return

def ageconvert_lambda(options:list, response_url:str, command:str="roll"):
    to_return = thinking_json
    
    payload_dict={'options':options, 'response_url':response_url,'command':command}
    print(payload_dict)
    
    lambda_client = boto3.client('lambda')
    lambda_payload = json.dumps(payload_dict)
    lambda_client.invoke(FunctionName='dnd-age-discord', 
                        InvocationType='Event',
                        Payload=lambda_payload)
    return to_return

def lootgenerate_lambda(options:list, response_url:str, command:str="loot"):
    to_return = thinking_json
    
    payload_dict={'options':options, 'response_url':response_url,'command':command}
    print(payload_dict)
    
    lambda_client = boto3.client('lambda')
    lambda_payload = json.dumps(payload_dict)
    lambda_client.invoke(FunctionName='dnd-loot-discord', 
                        InvocationType='Event',
                        Payload=lambda_payload)
    return to_return
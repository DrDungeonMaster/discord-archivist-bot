from app.commons.common_functions import choose
from app.name_generator.import_names import names
from app.name_generator.hybrid_names import hybrid_options
for i in hybrid_options:
    names[i]=hybrid_options[i]

def get_names(race:str='human',sex:str='both',count:int=10):
    names_list = []
    if race == 'goblin':
        from app.name_generator.goblin_names import get_goblin_names
        sex = None
        names_list = get_goblin_names(count)
    elif race == 'tabaxi':
        from app.name_generator.tabaxi_names import get_tabaxi_names
        sex = None
        names_list = get_tabaxi_names(count)
    elif race in hybrid_options:
        from app.name_generator.hybrid_names import get_hybrid_names
        [race_1,race_2] = hybrid_options[race]['parent_races']
        [r1_given_rate,r1_surname_rate] = hybrid_options[race]['mix']
        names_list = get_hybrid_names(count=count,race_1=race_1,race_2=race_2,r1_given_rate=r1_given_rate,r1_surname_rate=r1_surname_rate)
    elif race == 'gnome':
        from app.name_generator.gnome_names import get_gnome_names
        names_list = get_gnome_names(count,sex)
    elif race == 'kobold':
        from app.name_generator.kobold_names import get_kobold_names
        names_list = get_kobold_names(count)
    elif race in names:
        from app.name_generator.general_names import get_general_names
        names_list = get_general_names(race,sex,count)
    else:
        names_list = []
    if race == 'orc':
        for i in range(0,len(names_list)):
            names_list[i] = names_list[i].upper()
    return names_list
    
def get_books(topic:str="all", count:str=10):
    books_list = get_book_names(topic, count)
    return books_list

def names_command_handler(text:str):
    split_text = text.split(' ')
    if len(split_text) == 0 or len(split_text) > 3:
        to_return = {'statusCode':200, 'body':error_message}
    elif len(split_text) == 1:
        if split_text[0] in names:
            race = split_text[0]
            count = 10
            sex = 'both'
        elif is_numeric(split_text[0]):
            race = 'human'
            count = int(split_text[0])
            sex = 'both'
        elif split_text[0] in names['human']:
            race = 'human'
            count = 10
            sex = split_text[0]
        else:
            error=True
    elif len(split_text) == 2:
        if split_text[0] in names:
            race = split_text[0]
            if is_numeric(split_text[1]):
                count = int(split_text[1])
                sex = 'both'
            else:
                count = 10
                sex = split_text[1]
        else:
            race = 'human'
            sex = split_text[0]
            count = int(split_text[1])
    else:
        race = split_text[0]
        sex = split_text[1]
        count = int(split_text[2])
        
    generated_names = get_names(race,sex,count)
    if count > 1:
        s = 's'
    else:
        s = ''
    if sex != 'both':
        race_gender = f'{sex} {race}'
    else:
        race_gender = f'{race}'
    explanation = f'Generated {count} {race_gender} name{s}:'
    
    return generated_names,explanation

def shop_names_handler(text:str):
    from .shop_names import get_shop_names
    from .shop_names import categories_dict as shop_categories
    number = 10
    keywords = text.replace(","," ").split(" ")
    keywords_valid = []
    for i in keywords:
        if is_numeric(i):
            number = int(i)
        elif type(i) is str and i in shop_categories:
            keywords_valid.append(i)
        else:
            pass
    generated_names = get_shop_names(" ".join(keywords_valid),number)
    explanation = f'Generated {number} shop names with the keywords {str(keywords_valid)}:'
    
    return generated_names,explanation

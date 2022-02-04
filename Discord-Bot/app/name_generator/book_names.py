from app.commons.common_functions import choose, choose_separate
from random import randint,shuffle

from app.name_generator.names_handler import get_names
from app.name_generator.import_names import names

races = list(names.keys()) + ['kobold']
race_plurals = {'elf':'elves','half-elf':'half_elves','dwarf':'dwarves','tabaxi':'tabaxi'}
book_emojis = [':blue_book:',':green_book:',':orange_book:',':closed_book:']*3 + [':book:']

book_formats_list = ['people']*9 + ['skills']*12 + ['spellbooks']

book_formats = {}

#'place':[],
#'event':[],
#'nature':[],
#'concept':[]

book_formats['people']=["The {adjective} {life_word} of {name}{ending}", "{name}: {ending}", "{name}{ending}'s {adjective} {life_word}",
                       "The {adjective} {life_word} of {name} and {name_2}", "{name}, {name_2}, and {name_3}", "{name} and the {race_2}", "{name} and the {profession}",
                       "{name}{ending} and {name_2}{ending_2}", "{name} the {adjective} {race}", "{name} the {adjective} {profession}"]

book_formats['skills']=['Becoming a {profession} {reason}', '{gerund} {reason}', "{name}'s Guide to {gerund}",
                       "{name} and {name_2}'s Guide to {gerund}", "The Art of {gerund}", "{life_word} as a {profession}",
                      "A {life_word} of {gerund}", "The {life_word} of a {profession}"]

book_formats['spellbooks']=["{wizard_title}'s {adjective} {spellbook_type}","The {adjective} {spellbook_type} of {wizard_title}",
                            "A {adjective} {spellbook_type}", "{wizard_title}'s {spellbook_type}", "A {wizard_type}'s {spellbook_type}"]

adjectives = names['tabaxi']['adjectives']
gerunds = names['tabaxi']['gerunds']
wizard_types = ['mage','wizard','evoker','enchanter','illusionist','necromancer','abjurer','summoner','conjurer','transmuter','diviner','druid','warlock','witch','occultist','thaumaturge','spellweaver']
professions = ['fighter','barbarian','bard','wizard','warlock','sorcerer','rogue','druid','ranger','paladin','cobbler','adventurer','alchemist','apothecary','pharmacist','midwife','potionmaker','fisher','hunter','butcher','lover','consort','murderer','assassin','thief','farmer','drunkard','sailor','soldier','witch','doctor','surgeon','undertaker','gravedigger','jeweler','treasurehunter','blacksmith','smith','merchant','artist','sculptor','painter','potter','floutist','minstrel','drummer','singer','actor','thespian','mastermind','scholar','teacher','scientist','naturalist','surgeon','doctor','healer','veterinarian','stylist','model','hero','dragonslayer','cleric','priest','fortuneteller','seer','clown','strongman','performer','counterfeiter','highwayman','pirate','mercenary','hermit','traveller','beastmaster','werewolf','wererat','werebear','vampire','undead']*2 + wizard_types
life_words = ['Life','Life','Time','Story','Legend','Tale','Life','Misadventures','Foibles','Stories','Teachings','Times','Journeys','Adventures','Journey','Adventures','Tale','Tales','Friendships','Romances','Battles','Mishaps']
person_endings = ['']*5 + [', {race}', ' the {race}', ' the {race}',' the {profession}', ', a {profession}',', {profession}', ', a {race} and a {profession}',', {race} and {profession}', ', {race} {profession}']
groups = ['Group','Team','Colleagues','Comrades','Coworkers','Rivals','Enemies','Family','Parents','Party','Race','People','Kinsmen','the Townsfolk','Everyone','The Gods','Spouse','King','City','Town','Homies']
reasons = ['to Piss Off Your {group}', "to Delight Your {group}", "to Strike it Rich", "For Fun and Profit", "to Be a Legend", "to Win the hearts of your {group}", "For the hell of it", "Because I said so"]
spellbook_types=['Spellbook']*3 + ['Grimoire','Book of Spells','Spells']*2 + ['Arcanium', 'Book of Shadows','Guide to Magic', 'Notes', 'Guide to the Craft','Homework Assignments']

def shorten_name(name:str):
    if name.count(',') > 1:
        name = name.split(',')[0]
    name_parts = name.split(' ')
    short_name = None
    for i in name_parts:
        if i.startswith("'") and i.endswith("'"):
            short_name = i #.replace("'","")
    if not short_name:
        if round(randint(0,3)) > 1:
            short_name = name_parts[-1]
        else:
            short_name = name_parts[0]
    else:
        if round(randint(0,3) > 1) and name_parts[-1] != short_name:
            short_name = f'{short_name} {name_parts[-1]}'
    if short_name.endswith(','):
        short_name = short_name[0:-1]
    if '.' in short_name:
        short_name = 'the {short_name}'
    if len(short_name) == 0:
        short_name = shorten_name(name)
    if short_name.startswith('_') and not short_name.endswith('_'):
        short_name = short_name + '_'
    elif short_name.endswith('_') and not short_name.startswith('_'):
        short_name = '_' + short_name
    return short_name

def a_to_an(string:str):
    string_parts = string.split(' ')
    for i in range(0,len(string_parts)-1):
        if string_parts[i].lower() == 'a':
            next_part = string_parts[i+1].lower()
            rnum = round(randint(0,5))
            if next_part.endswith('s') and not next_part.endswith("'s") and next_part.title() not in adjectives:
                if rnum > 2:
                    string_parts[i+1] = string_parts[i+1][0:-1]
                else:
                    string_parts[i] = ''
            if next_part[0].lower() in ['a','e','i','o','u'] and len(string_parts[i]) > 0:
                string_parts[i] = string_parts[i].replace('a','an').replace('A','An')
    return " ".join(string_parts)

def get_book_names(topic:str=None,count:int=1,book_formats:dict=book_formats, use_emojis:bool=True):
    
    book_titles=[]
    
    if topic and topic.lower() == 'random':
        topic = choose(book_formats_list)[0]
    
    for i in range(0,max(1,count)):
        [adjective, gerund, life_word, race, name, race_2, name_2, race_3, name_3, profession, profession_2, ending, ending_2, group, reason, wizard_title, wizard_type, spellbook_type] = [None]*18
        if not topic or topic.lower() == 'all':
            book_format = choose(book_formats_list)[0]
        else:
            book_format = topic
        if book_format == 'spellbooks':
            book_emoji = ':bookmark:'
        else:
            book_emoji = choose(book_emojis)[0]
        book_title = choose(book_formats[book_format])[0]
        if '{adjective}' in book_title:
            adjective = choose(adjectives)[0]
        if '{gerund}' in book_title:
            gerund = choose(gerunds)[0]
        if '{life_word}' in book_title:
            life_word = choose(life_words)[0]
        if '{race}' in book_title or '{name}' in book_title or '{wizard_title}' in book_title:
            if '{race_3}' in book_title or '{name_3}' in book_title:
                [race,race_2,race_3] = choose(races,3)
                name = get_names(race=race, count=1)[0]
                name_2 = shorten_name(get_names(race=race_2, count=1)[0])
                name_3 = get_names(race=race_3, count=1)[0]
                rnum = round(randint(0,10))
                if rnum < 2:
                    name = shorten_name(name)
                elif rnum > 8:
                    name_3 = shorten_name(name_3)
                else:
                    name = shorten_name(name)
                    name_3 = shorten_name(name_3)
                
                if race == 'tabaxi':
                    name = f'_{name}_'
                if race_3 == 'tabaxi':
                    name_3 = f'_{name_3}_'
                if race_2 == 'tabaxi':
                    name_2 = f'_{name_2}_'
            elif '{race_2}' in book_title or '{name_2}' in book_title:
                [race,race_2] = choose(races,2)
                name = get_names(race=race, count=1)[0]
                name_2 = get_names(race=race_2, count=1)[0]
                rnum = round(randint(0,10))
                if rnum < 2:
                    name = shorten_name(name)
                elif rnum > 10:
                    name_2 = shorten_name(name_2)
                elif rnum == 5:
                    pass
                else:
                    name = shorten_name(name)
                    name_2 = shorten_name(name_2)
                if race == 'tabaxi':
                    name = f'_{name}_'
                if race_2 == 'tabaxi':
                    name_2 = f'_{name_2}_'
            else:
                race = choose(races)[0]
                name = get_names(race=race, count=1)[0]
                if round(randint(0,10)) > 8:
                    name = shorten_name(name)
                if race == 'tabaxi':
                    name = f'_{name}_'
            if '{wizard_title}' in book_title:
                wizard_type = choose(wizard_types)[0]
                rnum = randint(0,10)
                if rnum < 2:
                    wizard_title = name
                elif rnum < 4:
                    wizard_title = f'{name} the {wizard_type}'
                elif rnum < 6:
                    wizard_title = f'{wizard_type} {name}'
                elif rnum < 7:
                    wizard_title = f'{wizard_type} {shorten_name(name)}'
                else:
                    wizard_title = f'{shorten_name(name)} the {wizard_type}'
        if '{spellbook_type}' in book_title:
            spellbook_type = choose(spellbook_types)[0]
        if '{wizard_type}' in book_title:
            wizard_type = choose(wizard_types)[0]
        if '{ending}' in book_title:
            ending = choose(person_endings)[0]
        if '{ending_2}' in book_title:
            ending_2 = choose(person_endings)[0].replace('}','_2}')
        while '{' in book_title:
            if '{profession_2}' in book_title:
                [profession, profession_2] = choose_separate(professions,professions)
            elif '{profession}' in book_title:
                profession = choose(professions)[0]
            if '{group}' in book_title:
                group = choose(groups)[0]
            if '{reason}' in book_title:
                reason = choose(reasons)[0]
            book_title = book_title.format(adjective=adjective, name=name, race=race, life_word=life_word, profession=profession, profession_2=profession_2, ending=ending, ending_2=ending_2, race_2=race_2, race_3=race_3, name_2=name_2, name_3=name_3, reason=reason, group=group, gerund=gerund, spellbook_type=spellbook_type, wizard_type=wizard_type, wizard_title=wizard_title)
        book_title = book_title.strip().replace(": ,",":").title().replace("'S ","'s ").replace('  ',' ').replace('Your The ','The ').replace('To For ','To ').replace('Your Everyone','Everyone').replace(' For Be ',' To Be ')
        if book_title.endswith(':'):
            book_title = book_title[0:-1]
        book_title = a_to_an(book_title)
        if book_title.endswith(f'and the {race_2}'.title()):
            if race == race_2 or round(randint(0,10)) < 4:
                if race_2 in race_plurals:
                    race_plural = race_plurals[race_2]
                else:
                    race_plural = race + 's'
                book_title = book_title.replace(race_2.title(),race_plural.title())
        if race == 'orc':
            if name_2:
                book_title = book_title.replace(name.title(), name.upper())
                if race_2 == 'orc':
                    book_title = book_title.replace(name_2.title(), name_2.upper())
                if race_3 == 'orc':
                    book_title = book_title.replace(name_3.title(), name_3.upper())
            else:
                book_title = book_title.upper()
        if count <= 25 and use_emojis:
            book_title = f'{book_emoji} {book_title}'
        book_titles.append(book_title)
    
    shuffle(book_titles)
    return book_titles
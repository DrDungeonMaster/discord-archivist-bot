from app.commons.common_functions import choose, choose_separate
from random import randint,shuffle

from app.name_generator.names_handler import get_names
from app.name_generator.import_names import names

nameable_races = (list(names.keys()) + ['kobold'])*10
meta_races = ['vampire','werewolf','wererat','werebear','undead','genasi','aasimar','immortal','tiefling']
races = nameable_races + meta_races + ['halfling','dragonborn']*10 + ['goliath','aasimar','firbolg','ogre','giant','sprite','lizardfolk','lizardman','minotaur','centaur']*3 + ['dragon','fiend','archfey','celestial','djinn','cloaker']
race_plurals = {'elf':'elves','half-elf':'half-elves','dwarf':'dwarves','tabaxi':'tabaxi','genasi':'genasi','lizardfolk':'lizardfolk','lizardman':'lizardmen','aasimar':'aasimar','djinn':'djinni','dragonborn':'dragonborn'}
book_emojis = {'people':':closed_book:','nature':':green_book:','places':':blue_book:','skills':':orange_book:','cookbooks':'<:brown_book:939672284677955656>','spellbooks':':bookmark:'}

book_formats_list = ['people']*7 + ['skills']*4 + ['places']*3 + ['nature']*5 + ['cookbooks']*3 + ['spellbooks']

book_formats = {}

#'place':[],
#'event':[],
#'nature':[],
#'concept':[]

book_formats['people']=["The {adjective} {life_word} of {name}{ending}"]*3 + ["{name}: {ending}", "{name}{ending}'s {adjective} {life_word}",
                       "The {adjective} {life_word} of {name} and {name_2}", "{name}, {name_2}, and {name_3}", "The {adjective} {life_word} of {name}, {name_2}, and {name_3}", "{name} and the {race_2}", "{name} and the {profession}",
                       "{name}{ending} and {name_2}{ending_2}", "{name} the {adjective} {race}", "{name} the {adjective} {profession}",
                       "{name} and the {noun}", "{name}{ending} and the {adjective} {noun}", "The {adjective} {life_word} of {name} and the {noun}", 
                       "{name}{ending} from {place}"]

book_formats['skills']=['Becoming a {profession} {reason}', '{gerund} {reason}']*2 + ["{name}'s Guide to {gerund}",
                       "{name} and {name_2}'s Guide to {gerund}", "The Art of {gerund}", "{life_word} as a {profession}",
                      "A {life_word} of {gerund}", "The {life_word} of a {profession}"]
                      
book_formats['nature']=['{nature_adjective} {nature} of {region}']*3 + ['A {adjective} book of {adjective} {nature}', "{name}'s {adjective} Guide to {nature_adjective} {nature}", "{name} and {name_2}'s {adjective} Guide to {nature_adjective} {nature}"]
book_formats['places']=['A {noun} in {place}', '{gerund} in {place}', "{name}'s {adjective} Guide to {place}", "{name} and {name_2}'s {adjective} Guide to {place}", '{city}: The {adjective} City']

book_formats['spellbooks']=["{wizard_title}'s {adjective} {spellbook_type}","The {adjective} {spellbook_type} of {wizard_title}",
                            "A {adjective} {spellbook_type}", "{wizard_title}'s {spellbook_type}", "A {wizard_type}'s {spellbook_type}"]

book_formats['cookbooks']=["{name}{ending}'s {adjective} Book of {food_noun}",'The {food_adjective} {food_noun} of {place}','{food_noun} for {group}','The {adjective} Guide to {food_adjective} {race} Cuisine', "{name}{ending}'s Cookbook of {nature}", "{food_adjective} {food_noun} {reason}"]

nature_adjectives = ['wild','native','invasive','rare','common','edible','poisonous','medicinal','extinct','ancient','mythical','endemic','exotic','cultivated','delicious','parasitic','symbiotic','venomous','toxic','legendary','hallucinogenic','colorful','beautiful','ugly','aquatic','marine','freshwater','land','carnivorous','predatory','sentient','magical','cursed','dangerous','friendly','collectible','nocturnal']
adjectives = names['tabaxi']['adjectives'] + nature_adjectives
nature_adjectives = nature_adjectives + ['']*10
gerunds = names['tabaxi']['gerunds']
regions = ['Kara-Tur','Faerun','The Sword Coast','Amn','the Hartlands','Zakhara','Matzica','The Underdark','Toril','Tethyr','Calimshan','Chult','Anauroch']*10 + ['the Moonwood','The Endless Wastes','Icewind Dale','the Moonshae Isles','the Nelanther Isles','the Marshes of Tun','The Wealdath','the Cloud Peaks', 'the Calim Desert', 'the Shilmista', 'the Moonsea', 'the Sea of Fallen Stars','the Shining Sea','the Great Sea','the Stonelands']*3 + ['the Feywilds','the Lower Planes','the Higher Planes','the Elemental Planes','the Shadowfell','the Astral Plane']
cities = ['Neverwinter',"Baldur's Gate",'Athkatla','Velen','Waterdeep','Murann','Iraebor','Luskan','Brightmoon']
places = cities*10 + regions
nature_things = ['Birds','Mammals','Rodents','Squirrels','Predators','Herbivores','Canines','Felines','Mustelids','Ungulates','Bats','Primates','Fish','Plants','Flowers','Trees','Herbs','Mosses','Ferns','Crabs','Shrimp','Shellfish','Bivalves','Tubers','Lichens','Molds','Grasses','Shrubs','Fruits','Berries','Beasts','Cryptids','Mushrooms','Fungi','Cats','Dogs','Bears','Lizards','Reptiles','Bugs','Insects','Spiders','Sharks','Invertebrates','Vertebrates','Tetrapods','Snakes','Herps','Slugs','Snails','Gastropods','Sentients','Cephalopods','Turtles','Amphibians','Frogs','Salamanders','Newts','Scorpions','Mites','Bees','Flies','Butterflies','Dragonflies','Parasites','Moths','Ants','Beetles','Aberratons','Slimes','Oozes','Plantoids','Faeries','Undead','Fiends','Monsters','Celestials','Elementals']
wizard_types = ['mage','wizard','evoker','enchanter','illusionist','necromancer','abjurer','summoner','conjurer','transmuter','diviner','druid','warlock','witch','occultist','thaumaturge','spellweaver']
professions = ['fighter','barbarian','bard','wizard','warlock','sorcerer','rogue','druid','ranger','paladin','cobbler','adventurer','alchemist','apothecary','pharmacist','brewer','winemaker','bartender','innkeeper','landlord','midwife','potionmaker','fisher','hunter','butcher','lover','consort','murderer','assassin','thief','farmer','drunkard','sailor','soldier','witch','doctor','surgeon','undertaker','gravedigger','jeweler','gambler','cardshark','giggolo','bankrobber','treasurehunter','blacksmith','smith','merchant','artist','sculptor','painter','potter','floutist','minstrel','drummer','singer','actor','thespian','mastermind','scholar','teacher','scientist','naturalist','surgeon','doctor','healer','veterinarian','stylist','model','hero','dragonslayer','cleric','priest','fortuneteller','seer','clown','strongman','performer','counterfeiter','highwayman','pirate','mercenary','hermit','traveller','beastmaster','noble','gentleman-thief','man','women','mother','father','child']*2 + wizard_types + meta_races
life_words = ['Life','Life','Time','Story','Legend','Tale','Life','Misadventures','Foibles','Stories','Teachings','Times','Journeys','Adventures','Journey','Adventures','Tale','Tales','Friendships','Romances','Battles','Mishaps']
person_endings = ['']*5 + [', {race}', ' the {race}', ' the {race}',' the {profession}', ', a {profession}',', {profession}', ', a {race} and a {profession}',', {race} and {profession}', ', {race} {profession}']
groups = ['the Group','your Team','your Colleagues','your Comrades','your Coworkers','your Rivals','your Enemies','your Family','Your Son','Your Daughter','Your Child','Your Children','Your Kids','Babies','your Parents','your Mother','your Father','Grannies','Mommies','Daddies','your Sibling','the Ancestors','your ancestors','the ancients','the Party','your Race','your People','your Kinsmen','the Townsfolk','Everyone','The Gods','your Spouse','your King','your Queen','the City','the Town','the village', 'the homies', 'your Homies', 'the Fae', 'the Undead', 'Fiends', 'Spirits', 'the spirits', 'Ghosts', 'Vampires', 'Fair Maidens', 'Eligible Bachelors', 'Old People', 'Young People', 'the Nobility', 'the Poor', 'the Proletariat', 'the Bourgeoisie', 'Rich People', 'pirates', 'bandits', 'criminals', 'authority figures', 'famous people', 'magic-users', 'the cops', 'your boss', 'your pets', 'the woodland creatures', 'animals', 'wildlife', 'livestock']
reasons = ['to Piss Off {group}', "to Anger {group}", "to get kidnapped by {group}", "to become feared by {group}", "to seduce {group}", "to Delight {group}", "to Strike it Rich", "For Fun and Profit", "to Be a Legend", "to Win the hearts of {group}", "For the hell of it", "Because I said so", "For no reason whatsoever", "For mysterious reasons"]
spellbook_types=['Spellbook']*5 + ['Grimoire','Book of Spells','Spells', 'Tome', 'Compendium']*2 + ['Arcanium', 'Book of Shadows','Guide to Magic', 'Notes', 'Guide to the Craft','Homework Assignments']
food_nouns = ['recipes']*5 + ['concoctions','dishes','desserts','entrees','appetizers','meals','cuisine','breakfasts','second-breakfasts','lunches','food','soups','salads','cocktails','wines','beers','snacks','cheeses','delicacies','candymaking','cakes','bread','sushi','midnight snacks','afternoon tea','cookies','baking','grilling','barbecue','charcuterie','treats']
food_adjectives = ['']*10 + ['Delicious','Mouth-Watering','Quick','Easy','Impressive','Exotic','Spicy','Savory','Sweet','Tart','Bitter','Filling','Light','Festive','Traditional','Beginner','Advanced','Banquet-Sized','Family-Sized','Snack-Sized','Subsistence','Foraged','From-Scratch','Scrumptious','Satiating','Secret']
nouns = names['tabaxi']['nouns']*2 + professions + nature_things + spellbook_types + food_nouns

def assign_name(race:str):
    if race in nameable_races:
        name = get_names(race,count=1)[0]
    elif race in meta_races:
        birth_race = choose(nameable_races)[0]
        name = get_names(birth_race,count=1)[0]
        if birth_race == 'tabaxi':
            name = '_' + name + '_'
    else:
        race = choose(nameable_races)[0]
        name = get_names(race,count=1)[0]
    if race == 'tabaxi':
        name = '_' + name + '_'
    return name,race

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
        elif string_parts[i] in meta_races and string_parts[i+1] == string_parts[i]:
            string_parts[i+1] = ''
    return " ".join(string_parts)

def get_book_names(topic:str=None,count:int=1,book_formats:dict=book_formats, use_emojis:bool=True):
    
    book_titles=[]
    
    if topic and topic.lower() == 'random':
        topic = choose(book_formats_list)[0]
    
    for i in range(0,max(1,count)):
        [noun, adjective, nature_adjective, food_noun, food_adjective, gerund, life_word, race, name, race_2, name_2, race_3, name_3, profession, profession_2, ending, ending_2, group, reason, wizard_title, wizard_type, spellbook_type, city, region, place, nature] = [None]*26
        if not topic or topic.lower() == 'all':
            book_format = choose(book_formats_list)[0]
        else:
            book_format = topic
        try:
            if randint(0,21) >= 20:
                book_emoji = ':book:'
            else:
                book_emoji = book_emojis[book_format]
        except:
            book_emoji = ':closed_book:'
        book_title = choose(book_formats[book_format])[0]
        if '{noun}' in book_title:
            noun = choose(nouns)[0]
        if '{adjective}' in book_title:
            adjective = choose(adjectives)[0]
        if '{nature_adjective}' in book_title:
            nature_adjective = choose(nature_adjectives)[0]
        if '{gerund}' in book_title:
            gerund = choose(gerunds)[0]
        if '{life_word}' in book_title:
            life_word = choose(life_words)[0]
        if '{race}' in book_title or '{name}' in book_title or '{wizard_title}' in book_title:
            if '{race_3}' in book_title or '{name_3}' in book_title:
                [race,race_2,race_3] = choose(races,3)
                name,race = assign_name(race=race)
                name_2,race_2 = assign_name(race=race_2)
                name_2 = shorten_name(name_2)
                name_3,race_3 = assign_name(race=race_3)
                rnum = round(randint(0,10))
                if rnum < 2:
                    name = shorten_name(name)
                elif rnum > 8:
                    name_3 = shorten_name(name_3)
                else:
                    name = shorten_name(name)
                    name_3 = shorten_name(name_3)

            elif '{race_2}' in book_title or '{name_2}' in book_title:
                [race,race_2] = choose(races,2)
                name,race = assign_name(race=race)
                name_2,race_2 = assign_name(race=race_2)
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
            else:
                race = choose(races)[0]
                name,race = assign_name(race=race)
                if round(randint(0,10)) > 8:
                    name = shorten_name(name)
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
        if '{food_noun}' in book_title:
            food_noun = choose(food_nouns)[0]
        if '{food_adjective}' in book_title:
            food_adjective = choose(food_adjectives)[0]
        if '{city}' in book_title:
            city = choose(cities)[0]
        if '{region}' in book_title:
            region = choose(regions)[0]
        if '{place}' in book_title:
            place = choose(places)[0]
        if '{nature}' in book_title:
            nature = choose(nature_things)[0]
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
            book_title = book_title.format(adjective=adjective, name=name, race=race, life_word=life_word, profession=profession, profession_2=profession_2, 
                ending=ending, ending_2=ending_2, race_2=race_2, race_3=race_3, name_2=name_2, name_3=name_3, reason=reason, group=group, gerund=gerund, 
                spellbook_type=spellbook_type, wizard_type=wizard_type, wizard_title=wizard_title, region=region, city=city, place=place, 
                noun=noun, nature=nature, nature_adjective=nature_adjective, food_noun=food_noun, food_adjective=food_adjective)
        book_title = book_title.strip().replace(": ,",":").title().replace("'S ","'s ").replace('  ',' ').replace('Your The ','The ').replace('To For ','To ').replace('Your Everyone','Everyone').replace(' For Be ',' To Be ')
        if book_title.endswith(':'):
            book_title = book_title[0:-1]
        book_title = a_to_an(book_title)
        if book_title.endswith(f'and the {race_2}'.title()):
            if race == race_2 or round(randint(0,10)) < 4:
                if race_2.lower() in race_plurals:
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
            elif book_format == 'spellbook' or randint(0,5) >= 4:
                book_title = book_title.upper()
        elif randint(0,50) == 50:
            book_title = book_title.upper()
        if count <= 25 and use_emojis:
            book_title = f'{book_emoji} {book_title}'
        book_titles.append(book_title)
    
    shuffle(book_titles)
    return book_titles
### curses ###

curses_data={
'curses_0':{'Clinging':0.85,'Aging':0.65, 'Hirsuitism':0.95, 'Baldness':0.9, 'Elusiveness':0.8, 'Stench':0.9, 'Swarming Insects':0.85, 'Loudness':0.9},
'curses_1':{'Weight':0.7, 'Polymorphing':0.8, 'Birds':0.8, 'Expansion':0.7, 'Dwarfism':0.9, 'Gigantism':0.9,},
'curses_2':{'Mania':0.6, 'Depression':0.6, 'Awkwardness':0.6, 'Weakness':0.6, 'Sickliness':0.6, 'Clumsiness':0.6, 'Obliviousness': 0.6, 'Ignorance':0.6,' the Vampire':0.5},
'curses_3':{'the Murderous Hand':0.5, 'Water-Breathing':0.4},
'curses_4':{'Disintegration':0,'Transmogrification':0.4,'Petrification':0.3},
'non_cursed':{}
}

curses_data['curses_1'].update(curses_data['curses_0'])
curses_data['curses_2'].update(curses_data['curses_1'])
curses_data['curses_3'].update(curses_data['curses_2'])
curses_data['curses_4'].update(curses_data['curses_3'])

### emojis ###
emojis = {
    'items':':crossed_swords:',
    'weapon':':dagger:',
    'currency':':coin:',
    'coin':':coin:',
    'art':':art:',
    'wonder':':crystal_ball:',
    'food':':cheese:',
    'armor':':shield:',
    'gemstone':':gem:',
    'scroll':':scroll:',
    'potion':':alembic:',
    'ammunition':':bow_and_arrow:',
    'ammo':':bow_and_arrow:'
    }

### currency ###
coin_value={
'Gold':1,
'Platinum':10,
'Silver':0.1,
'Copper':0.01,
'Electrum':0.5}

### gemstones ###

gems_data={
'A': ['Small Gem', 'Semi-Precious', 25],
'B': ['Medium Gem', 'Semi-Precious', 100],
'C': ['Large Gem', 'Semi-Precious', 675],
'D': ['Huge Gem', 'Semi-Precious', 6500],
'E': ['Massive Gem', 'Semi-Precious', 75000],
'F': ['Small Gem', 'Precious', 500],
'G': ['Medium Gem', 'Precious', 2000],
'H': ['Large Gem', 'Precious', 13500],
'I': ['Huge Gem', 'Precious', 125000],
'J': ['Massive Gem', 'Precious', 1500000],
'K': ['Small Gem', 'Exotic', 1500],
'L': ['Medium Gem', 'Exotic', 6000],
'M': ['Large Gem', 'Exotic', 45000],
'N': ['Huge Gem', 'Exotic', 385000],
'O': ['Massive Gem', 'Exotic', 4500000],
'P': ['Small Gem', 'Magical', 6500],
'Q': ['Medium Gem', 'Magical', 25000],
'R': ['Large Gem', 'Magical', 175000],
'S': ['Huge Gem', 'Magical', 1650000],
'T': ['Massive Gem', 'Magical', 20000000]}

gem_types={
'Semi-Precious':['Topaz','Aquamarine','Quartz','Amethyst','Opal','Fluorite','Rose Quartz','Jasper','Pearl','Amber','Agate','Chalcedony','Citrine','Beryl','Tiger-Eye','Hematite','Lapis Lazuli','Rhodonite','Snowflake Obsidian','Flame Obsidian','Tiger Obsidian','Zebra Marble'],
'Precious':['Ruby','Emerald','Sapphire','Diamond','Garnet','Blue Diamond','Yellow Diamond','Pink Diamond','Clear Sapphire','Pink Sapphire','Star Sapphire'],
'Exotic':['Mithril Sapphire','Orichalcon','Selunite','Vantacite','Dragonite','Luminous Diamond','Adamancite','Hyperpink','Limbocite','Celestite','Starfall Gem','Abyssal Shard','Inferno Pearl'],
'Magical':['Ragestone','Grimstone','Bloodstone','Gods\' Tear','Feystone','Wildstone','Chaos Stone','Law Stone','Balance Stone','Sonicstone','Thoughtstone','Voltstone','Soulstone','Moonstone','Sunstone','Dreamstone','Noostone','Shadowstone','Firestone','Earthstone','Waterstone','Windstone','Green Dragonstone','Red Dragonstone','Blue Dragonstone','White Dragonstone','Black Dragonstone','Brass Dragonstone','Bronze Dragonstone','Gold Dragonstone','Silver Dragonstone','Copper Dragonstone','Platinum Dragonstone','Polychromatic Dragonstone','Fairy Dragonstone']
}


### items ###

items_data={
'A': ['Art Piece','Typical',{'{metal_0} {jewelry}':5,'{metal_1} {jewelry}':35,'{instrument}':35, 'Novelty {carving} Toy':5,'Wood {carving} Carving':5,'Bone {carving} Carving':15,'Stone {carving} Carving':25,'{metal_0} {carving} Statuette':35,'{art} Painting':10,'{art} Sketch':10,'Vial of Cheap {fragrance}':10,'Wooden {boardgame} Set':5, 'Clay {boardgame} Set':10, 'Bone {boardgame} Set':25,'Deck of {cardgame} Cards':1,'Wooden Dice':1, 'Bone Dice':2, 'Wooden Polyhedral Dice Set':5, 'Bone Polyhedral Dice Set':15, '{metal_0} Dice':10,'{metal_0} Polyhedral Dice Set':5, '{metal_0} {boardgame} Set':35}], 
'B': ['Art Piece','Fine',{'{metal_2} {jewelry}':350,'Finely-Crafted {instrument}':500,'{wood_0} {carving} Carving':150,'{stone_0} {carving} Carving':350,'{metal_1} {carving} Statuette':500,'Tasteful {art} Canvas':250,'Beautiful {art} Painting':150,'{art} Pen & Ink':75,'Dropper of Fine {fragrance}':100, 'Deck of {metal_1}-Inlaid {cardgame} Cards':200, 'Deck of Illustrated {cardgame} Cards':300, '{stone_0} {boardgame} Set':200, '{wood_0} {boardgame} Set':100, '{stone_0} Dice':35, '{wood_0} Dice':25, '{stone_0} Polyhedral Dice Set':185, '{wood_0} Polyhedral Dice Set':250, '{stone_0} {boardgame} Set':200, '{wood_0} {boardgame} Set':100, '{stone_0} Dice':35, '{wood_0} Dice':25, '{stone_0} Polyhedral Dice Set':185, '{wood_0} Polyhedral Dice Set':250,'{metal_1} Dice':100,'{metal_1} Polyhedral Dice Set':300, '{metal_1} {boardgame} Set':600}], 
'C': ['Art Piece','Exemplary',{'{metal_2} {carving} Statuette':2500,'{metal_3} {jewelry}':1200,'Masterwork {instrument}':2000,'Impressive {art} Canvas':1000,'Memorable {art} Painting':750, 'Atomizer of Elegant {fragrance}':650,'Deck of {metal_2}-Inlaid {cardgame} Cards':750, 'Deck of Masterfully-Illustrated {cardgame} Cards':1750, '{stone_1} {boardgame} Set':1000, '{gem_0} {boardgame} Set':2500, '{wood_1} {boardgame} Set':750, '{stone_1} Dice':350, '{wood_1} Dice':250, '{gem_0} Dice':500, '{stone_1} Polyhedral Dice Set':1850, '{wood_1} Polyhedral Dice Set':1250, '{gem_0} Polyhedral Dice Set':2000, '{gem_0} {boardgame} Set':3500, '{metal_2} Dice':200,'{metal_2} Polyhedral Dice Set':1000, '{metal_2} {boardgame} Set':2000}], 
'D': ['Art Piece','Famed',{'{metal_3} {carving} Statuette':25000, "~_Psst Hey, Wanna Buy Some Cubes?_":65000,'~_Dragon Hoard 1:{imdh_1}_':15000,'~_Dragon Hoard 2:{imdh_2}_':10000,'~_Dragon Hoard 3:{imdh_3}':6500,'~_Dragon Hoard 4:{imdh_4}_':10000,'Deck of {metal_3}-Inlaid {cardgame} Cards':10000,'{gem_1} {boardgame} Set':50000,'{gem_1} Dice':5000,'{gem_1} Polyhedral Dice Set':25000, '{metal_3} Dice':2000,'{metal_3} Polyhedral Dice Set':10000, '{metal_3} {boardgame} Set':20000}], 
'E': ['Art Piece','Renowned',{"~_The Silken Sword_":100000,"~_The Oracle_":150000,"~_The Emissary_":100000,"Obliskura's _Untitled_":185000,"~_Twinkling Stars_":95000,"~_Fat Nuts_":690000,'{gem_2} {boardgame} Set':250000,'{gem_2} Dice':50000, '{gem_2} Polyhedral Dice Set':350000}],
'a': ['Delicacy','Typical',{'Pouch of Loose {tea_0}':5,'<1-3>Brick<s> of Pressed {tea_0}':20,'Cask of Mediocre {alcohol_0}':20,'<1-6>Bottle<s> of {alcohol_0}':0.2,'<1-6>Bottle<s> of Fine {alcohol_0}':2,'<1-12>Bottle<s> of Cheap {alcohol_1}':5, 'Wedge of {cheese_0}':1, 'Block of {cheese_0}':2, 'Wheel of {cheese_0}': 10, 'Wedge of {cheese_1}':20,'Block of {cheese_1}':20}],
'b': ['Delicacy','Fine', {'Cask of Fine {alcohol_0}':100,'<1-3>Bottle<s> of Good {alcohol_1}':35,'Box of Fine {tea_0}':100,'<1-6>Pouch<es> of Fine {tea_1}':35, 'Wheel of {cheese_1}':100, 'Serving of {cheese_2}':30, '<1-3>Wedge<s> of {cheese_2}':100, '<1-2>Block<s> of {cheese_2}':200}],
'c': ['Delicacy','Exemplary',{'Cask of Exquisite {alcohol_0}':500,'Cask of {alcohol_1}':1000,'Chest of Fine {tea_1}':350, 'Wheel of {cheese_2}':1000, 'Serving of {cheese_3}':650}],
'd': ['Delicacy', 'Famed', {'Wedge of {cheese_3}':1500, 'Block of {cheese_3}':3000, 'Butteload of Exquisite {alcohol_0}':2000, 'Butteload of {alcohol_1}':4000}],
'e': ['Delicacy', 'Renowned', {'Wheel of {cheese_3}':10000, 'Serving of {cheese_4}':35000}],
'F': ['Weapon','Mundane',{'Shortsword':5,'Scimitar':25,'Longsword':100,'{weapon}':50}], 
'G': ['Weapon','Common',{'Moon-Touched {weapon}':450,'Untarnishing {weapon}':250,'Fearsome {weapon}':1000, 'Gentle {weapon}':650}], 
'H': ['Weapon','Uncommon',{'Berzerker Axe *':1200, '+1 {slash}':1500,'+1 {blunt}':1500,'+1 {pierce}':1500, '+1 {thrown}':1500,'+1 {ranged}':1500,'+1 {weapon}':1500,'{element_1} {weapon}':2500,'Hewing Axe':2000, 'Lightbringer\'s Mace':2000, 'Seeker Dart':200, 'Shatterspike':2500, 'Skyblinder Staff':2500,'Staff of the Adder':2500,'Staff of the Python':2500,'Storm Boomerang':1500,'{slash} of Vengeance *':750,'Trident of Fish Command':1500,'{weapon} of Warning':1500, '{thrown} of Returning':2500}],
'I': ['Weapon','Rare',{'Bonecounter':6500,'Armor of Vulnerability *':4500,'Acheron {slash}':16000,'+2 {weapon}':6500,'{element_2} {weapon}':10000,'{monster}-Slaying {weapon}':15000,'Javelin of Lightning':12000,'Dagger of Venom':12000}], 
'J': ['Weapon','Very Rare',{"Bloodaxe":75000,"Blood Spear":35000,"{sword} of the Medusa *":25000,'Arcane Cannon':200000,'+3 {weapon}':35000,'{element_3} {weapon}':50000,'Flametongue {slash}':85000, 'Greater {monster}-Slaying {weapon}':100000}], 
'K': ['Weapon','Legendary',{'~_Bookmark_':350000,"Vorpal {slash}":1000000,"~_Excalibur_":2500000,"~_Dáinslef_":1350000,"~_Joyeuse_":1690000,"~_Gungnir_":2000000,"~_Mjolnir_":2000000,"~_Gae Bolg_":1500000,"~_Ankusha_":1250000,'{weapon} Ayudhapurusha':500000,"~_Halayudha_":1000000,"~_Pasha_":650000,"~_Imhullu_":2000000,}], 
'f':['Ammunition','Mundane',{'<Quiver of ><1-12>{bow_ammunition}<s>|6':0.1,'<Box of ><1-8>{gun_ammunition}s|3':0.5,'<Case of ><1-4>{explosive}<s>':50}],
'g':['Ammunition','Common',{'<Quiver of ><1-12>+1 {bow_ammunition}<s>|6':65,'<Box of ><1-8>+1 {gun_ammunition}<s>|3':70,'<Quiver of ><1-12>{element_1} {bow_ammunition}<s>|4':100,'<Box of ><1-8>{element_1} {gun_ammunition}<s>|2':120,'<Case of ><1-4>{element_1} {explosive}<s>':200}],
'h':['Ammunition','Uncommon',{'<Quiver of ><1-12>+2 {bow_ammunition}<s>|6':350, '<Box of ><1-8>+2 {gun_ammunition}<s>|3':375,'<Quiver of ><1-12>{element_2} {bow_ammunition}<s>|4':450,'<Box of ><1-8>{element_2} {gun_ammunition}<s>|2':600,'<Case of ><1-4>{element_2} {explosive}<s>':1000}],
'i':['Ammunition','Rare',{'<Quiver of ><1-12>+3 {bow_ammunition}<s>|6':800, '<Box of ><1-8>+3 {gun_ammunition}<s>|3':900,'<Quiver of ><1-12>{element_3} {bow_ammunition}<s>|4':1250,'<Box of ><1-8>{element_3} {gun_ammunition}<s>|2':1500,'<Case of ><1-4>{element_3} {explosive}<s>':5000}],
'j':['Ammunition','Very Rare',{'<Quiver of ><1-12>Greater {monster}-Slaying {bow_ammunition}<s>|6':10000,'<Box of ><1-8>Greater {monster}-Slaying {gun_ammunition}<s>|3':10000}],
'k':['Ammunition','Legendary',{"<Quiver of ><1-12> Solar's Arrow<s> of Obliteration":1000000}],
'L': ['Armor','Mundane',{'Platemail':1500,'Studded Leather':45,'{light_armor}':20,'{medium_armor}':100,'{heavy_armor}':500}], 
'M': ['Armor','Common',{'{shield} of Expression':350,'Cast-Off {medium_armor}':1000,'Cast-Off {heavy_armor}':1500,'Gleaming {medium_armor}':1000,'Gleaming {heavy_armor}':1500,'Smoldering {armor}':1500}], 
'N': ['Armor','Uncommon',{'Sentinel {shield}':1500,'Mithral {metal_armor}':1500,'Mariner\'s {armor}':2500,'Adamantine {metal_armor}':1500,'+1 {armor}':2000,'+1 {shield}':1500,'Anti-{element_1} {shield}':2500}], 
'O': ['Armor','Rare',{'Mind-Carapace {heavy_armor}':10000,'+1 Adamantine {metal_armor}':8500, '+2 {armor}':10000,'+2 {shield}':6500,'{element_2}-Absorbing {shield}':10000,'{armor} of {damage} Resistance':10000}], 
'P': ['Armor','Very Rare',{'Animated Aegis':60000,'+2 Adamantine {mediun_armor}':35000,'+2 Adamantine {heavy_armor}':35000,'+3 {armor}':50000,'+3 {shield}':35000, 'Anti-{element_3} {shield}':50000, '{color} Dragon Scale-Mail':75000}], 
'Q': ['Armor','Legendary',{"~_Babr-e Bayan_":1500000,"~Wayland's Invincible Mail":1500000,"~Orvar-Oddr's Silken Mailcoat": 1000000, "~Armor of Achilles":2000000,"Green {armor}":500000,"Spiritual {armor} Kavacha":650000,"Sigurd's Golden Chaincoat":1000000}], 
'R': ['Wondrous Item','Common',{"Chest of Preserving":1500,"Cleansing Stone":1000,'Band of Loyalty':200,'Staff of Adornment':150,'Staff of Birdcalls':250,'Staff of Flowers':250,'Wand of Conducting':250,'Wand of Pyrotechnics':450,'Wand of Frowns':250,'Wand of Smiles':250,'Driftglobe':1000,"{instrument} of Illusions":650,"{instrument} of Scribing":500,"Imbued Wood Focus: {wood_1}":500,"Boots of False Tracks":350,"Breathing Bubble":500,"Candle of the Deep":200,"Charlatan\'s Die":200,"Cloak of Billowing":250,"Cloak of Many Fashions":350,"Clockwork Amulet":850,"Clothes of Mending":100,"Coin of Delving":50,"Dark Shard Amulet":850,"Dread Helm":650,"Ear Horn of Hearing":100,"Enduring Spellbook":650,"Ersatz Eye":500,"Everbright Lantern":750,"Featherfall Token":200,"Hat of Vermin":650,"Hat of Wizardry":850,"Heward\'s Handy Spice Pouch":750,"Horn of Silent Alarm":450,"Keycharm":500,"Lock of Trickery":350,"Mystery Key":100,"Orb of Direction":150,"Orb of Gonging":200,"Orb of Shielding: {stone_1}":850,"Orb of Time":150,"Pipe of Remembrance":650,"Pipe of Smoke Monsters":450,"Pole of Angling":100,"Pole of Collapsing":200,"Clockwork Rod & Reel":750,"Prosthetic Limb":1250,"Rope of Mending":150,"Scribe\'s Pen":450,"Sekolahian Shark Statuette":300,"Shiftweave":350,"Spellshard":400,'{jewelry} of _{spell_1}_':1350}], 
'S': ['Wondrous Item','Uncommon',{'Brooch of Shielding':4000,'Brooch of Living Essence':2000,'Bracers of Archery':5000,'Boots of the Winterlands':3500,'Boots of Elvenkind':3500,'Bell Branch':2500,'Balance of Harmony':2500,'Bag of Tricks':3500,'Bag of Bounty':2000,'Keepsake of the Drunkard':1250,'Amulet of Proof Against Detection & Location':2500,'Broom of Flying':4500, "Cartographer\'s Map Case":2000,'Pot of Awakening':4500, 'Bag of Holding':5000,'Gauntlets of Ogre Power':5000, 'Immovable Rod':3500, 'Cape of the Mountebank':5000,'{jewelry} of _{spell_0}_':3500,'{jewelry} of _{spell_2}_':3500,'{jewelry} of _{spell_3}_':6000,'{instrument} of _{spell_2}_':4500,'{instrument} of _{spell_3}_':7000}],
'T': ['Wondrous Item','Rare',{'Bridle of Capturing':9000,'Bracers of Defense':6000,'Bracer of Flying Daggers':8500,'Boots of Striding and Springing':10000,'Boots of Speed':12000,'Boots of Levetation':8500,'Hat of Disguise':8500,'Beads of Force':5000,'Battering Tower Shield':10000,'Banner of the Krig Rune':20000,'Balloon Pack':6500,'Bag of Beans':10000,'Astral Shard':6000,'Arcane Grimoire':6000,'Heward\'s Handy Haversack':6500,'All-Purpose Tool':6000,'Symbol of the Devout':6000,'Amulet of Health':30000,'Alchemical Compendium':13500,'Carpet of Flying':12500,'Dancing {weapon}':15000,'Boots of Speed':27500, 'Censer of Commanding Air Elementals':35000, 'Brazier of Commanding Fire Elementals':35000, 'Font of Commanding Water Elementals':35000, 'Stone of Commanding Earth Elementals':35000,'Boots of Levitation':8500,'Belt of Hill Giant Strength':15000,'Chime of Opening':10000,'Belt of Dwarvenkind':12500,'Cloak of the Manta-Ray':8500,'Robe of Eyes':17500,'{jewelry} of _{spell_4}_':15000,'{jewelry} of _{spell_5}_':25000,'{instrument} of _{spell_4}_':20000,'{instrument} of _{spell_5}_':30000}], 
'U': ['Wondrous Item','Very Rare',{'Bracelet of Rock Magic *':10000,'Bloodwell Vial':13500,"Blast Scepter":35000,'Atlas of Endless Horizons':13500,'Astromancy Archive':13500,'Amulet of the Planes':200000,'Amulet of the Black Skull *':45000,'Abracadabrus':50000,'Cloak of Displacement':65000, 'Belt of Fire Giant Strength':150000,'Belt of Stone Giant Strength':75000, 'Belt of Ice Giant Strength':75000,'{jewelry} of _{spell_6}_':50000,'_{jewelry}_ of _{spell_7}_':150000,'{instrument} of _{spell_6}_':65000,'{instrument} of _{spell_7}_':200000, 'Portable Hole':45000}], 
'V': ['Wondrous Item','Legendary',{'Dragon Mask':850000,'Belashyrra\'s Beholder Crown *':1200000,'Apparatus of Kwalish':800000,'Canvass of Unchanging Self':1500000,'Belt of Cloud Giant Strength':750000, 'Belt of Storm Giant Strength':1500000,'Cubic Gate':1500000,'{jewelry} of _{spell_8}_':450000,'{instrument} of _{spell_8}_':500000,'{jewelry} of _{spell_9}_':1250000,'{instrument} of _{spell_9}_':1500000}], 
'W': ['Scroll','Cantrip',{'Scroll of _{spell_0}_ (<1-5>Use<s>)':35}], 
'X': ['Scroll','Low-Level',{'Scroll of _{spell_1}_':100,'Scroll of _{spell_2}_':250}], 
'Y': ['Scroll','Mid-Level',{'Scroll of _{spell_3}_':500,'Scroll of _{spell_4}_':1500,'Scroll of _{spell_5}_':2500}], 
'Z': ['Scroll','High-Level',{'Scroll of _{spell_6}_':5000,'Scroll of _{spell_7}_':15000}],
'1': ['Scroll','Legendary',{'Scroll of _{spell_8}_':45000,'Scroll of _{spell_9}_':125000,'Scroll of Wish':500000}],
'2': ['Potion','Common',{'Vial of Quess\'rinth':75,'Potion of Watchful Rest':150,'Potion of Ogre Strength':250,'Potion of Climbing':150,'<Box of ><1-6>Basic Healing Potion<s>':50,'Crate of <6-24>Basic Healing Potions':50,'<Case of ><1-4>Basic Antidote<s>':100,'<Pouch of ><1-20>Bead<s> of Refreshment':2,'<Pouch of ><1-20>Bead<s> of Nourishment':2,"Moodmark Paint":135}],
'3': ['Potion','Uncommon',{'<Box of ><1-6>Greater Healing Potion<s>':250,'Potion of Water Breathing':350,'Potion of {damage} Resistance':500,'Potion of Shrinking':450,'Potion of Growth':450,'Potion of Hill Giant Strength':650,'Potion of Fire-Breathing':650,'Potion of Comprehension':500,'Potion of Animal Friendship':250,'Oil of Slipperiness':850,'Bottled Breath':350,"Philter of Love":500,"Perfume of Bewitching":300}],
'4': ['Potion','Rare',{"Thessaltoxin Antidote":3500,"Depth-Diving Capsule":1250,'Potion of Poison':500,'Potion of Frost Giant Strength':2000,'Potion of Stone Giant Strength':2000,'Potion of {color} Dragon\'s Breath':1750,'Lycanthropy Antidote':13500,'Mummy-Rot Antidote':3500,}],
'5': ['Potion','Very Rare',{'Potion of Fire Giant Strength':6500,'Potion of Cloud Giant Strength':10000,'Panacea':15000,'Mead of Poetry':35000,'Flask of Soma':35000,'Ampule of Ambrosia':35000}],
'6': ['Potion','Legendary',{'Potion of Storm Giant Strength':35000,'Elixir of Life':1000000,'Water of Youth':200000,'Anti-Magic Moly Tonic':25000,'Fruit of Knowledge':150000,'Fruit of Awareness':150000,'Fruit of Beauty & Wit':150000,'Fruit of Power':150000, 'Fruit of Resilience':150000,'Fruit of Finesse':150000,'Amrita':2500000}]
}

items_replace = {
'gem_0':gem_types['Semi-Precious'],
'gem_1':gem_types['Precious'],
'gem_2':gem_types['Exotic'],
'gem_3':gem_types['Magical'],
'stone_0':['marble','granite','limestone','sandstone','glass'],
'stone_1':["Fernian basalt","Irian quartz","Kythrian skarn","Lamannian flint","Mabaran obsidian","Xorian marble","Risian shale","Shavaran chert"],
'metal_0':['copper','steel','pewter','tin','brass','bronze','lead','iron'],
'metal_1':['silver','silver','silver','electrum','electrum','niello'],
'metal_2':['gold','gold','gold','rose-gold','white-gold'],
'metal_3':['platinum','platinum','platinum','iridium','mithril','adamantium','titanium'],
'wood_0':["ash","rosewood","oak","birch","cherrywood","cedar","pine","beechwood"],
'wood_1':["Fernian ash","Irian rosewood","Kythrian manchineel","Lamannian oak","Mabaran ebony","Risian pine","Shavarran birch", "Quori beech", "Xorian wenge"],
'color':['white','black','blue','red','green','black','copper','silver','gold','bronze','brass'],
'monster':['man','dragon','giant','fiend','angel','fairy'],
'slash':['handaxe','battleaxe','longsword','shortsword','saber','scimitar','greatsword','greataxe'],
'blunt':['club','mace','maul'],
'pierce':['rapier','spear','dagger','pike','lance','trident'],
'thrown':['handaxe','dagger','boomerang','javelin','spear'],
'sword':['shortsword','longsword','greatsword','saber','cutlass','scimitar','rapier'],
'axe':['handaxe','battleaxe','greataxe'],
'ranged':['shortbow','shortbow','shortbow','longbow','longbow','hand crossbow','light crossbow','light crossbow','heavy crossbow','pistol','rifle','sling','slingshot','blunderbus'],
'exotic_weapon':['swordstaff','nunchaku','swordcane','whip','kusarigama','gunsword','chain-staff', 'whip-sword', 'net', 'bolas', 'garrote'],
'bow_ammunition':['arrow','arrow','arrow','crossbow bolt','wrist crossbow bolt'],
'gun_ammunition':['bullet'],
'explosive':['bomb','bomb','grenade','explosive harpoon','blunderbus charge','blunderbus charge','blunderbus charge'],
'light_armor':['padded armor','leather armor','studded leather armor'],
'medium_armor':['chain shirt', 'hide armor', 'scale mail', 'breastplate', 'half-plate armor'],
'heavy_armor':['ringmail armor', 'chainmail armor', 'splint armor', 'platemail'],
'shield':['shield','kite shield','buckler','targe'],
'carving':['strange','sheep','horse','dog','cat','nude','bust','dragon','unicorn','face','phallic','angel','devil'],
'jewelry':['ring', 'necklace','bracelet','choker','broach','bangle','pin','hairpin','earring','earrings','beltbuckle','anklet','circlet','cufflinks'],
'instrument':['drum','flute','lute','lyre','horn','guitar','violin','viola','shamisen','panpipes','castinets','triangle','tuning fork','didgeridoo','ocarina'],
'art':['sunrise','sunset','landscape','battle','city','abstract','clouds', 'seascape'],
'cardgame':['Playing']*5 + ['Tarot']*3 + ['_Three-Dragon Ante_', 'Talis']*2 + ['_Elemental Empires_', '_Old Wizard_','_Koi-Koi_','Ganjifa','_Water Margin_','_Six Tigers_'],
'boardgame':['_Staans_ Tile']*3 + ['Chess', '_Tafl_', '_Game of Generals_','_Hounds and Jackals_','_Weiki_','Checkers','_Bao_','_Sternhalma_','_Dominos_ Tile','_Spheres_','_Little Wars_','_Sparrows_ Tile'],
'alcohol_0':['cider','mead','wine','spirits','liquer','beer','ale','stout'],
'alcohol_1':['whiskey','gin','brandy','rum','sake','absynthe','creme di violette','creme di menthe','dark rum','white rum','golden rum','vodka','whisky','port','vermouth'],
'tea_0':['black tea','green tea','red tea','chai','herbal tea'],
'tea_1':['Earl Grey','Lady Grey','Oolong','Rooibos','jasmine tea','peppermint tea','Grumplgod','rose tea','honey-green tea','Assam tea','white tea','Matcha','Chamomile tea','ginger-root tea','Lapsang Souchong','honey lemon tea','ginseng green tea','Waterdeep breakfast tea','Neverwinter breakfast tea','Elderberry tea','licorice-root tea','yerba mate'],
'cheese_0':['hard cheese', 'firm cheese', 'soft cheese', 'crumbly cheese', 'creamy cheese'],
'cheese_1':['Cheddar','Parmesan','Mozzarella','Gouda','Brie','Rothe Manchego','Bleu Cheese','Camembert','Emmentaler','Gruyère','Feta','Provolone','Edam','Gorgonzola','Roquefort','Mascarpone','Halloumi'],
'cheese_2':['Black-Truffle Moliterno','Leipäjuusto','Chhurpi','Caravane','Sverneblin Deep Rothé Ossau-Iraty', 'Dwarven Deep Rothé Idiazábal','Airag','Wild Elf Forest-Cheese','Caciocavallo'],
'cheese_3':['Centaur Caciocavallo','Minotaur Cheese','Yakfolk Chhurpi','Gryphon Cheese','Giantess Cheese','Feywilds Honey-Cheese'],
'cheese_4':['Unicorn Pule Cheese','Kirin Halloumi Cheese','Yeti Cheese'],
'fragrance':['perfume','cologne','fragrance','musk'],
'element_1':['Heat','Spark','Chill','Sonic','Corrosive','Toxic','Bright','Withering','Psionic'],
'element_2':['Flame','Lightning','Frostbite','Shockwave','Acid','Poison','Radiant','Necrotic','Mindstrike'],
'element_3':['Blaze','Boltstrike','Deepfreeze','Shattering','Venom','Scintillating','Rotting','Fluroantimonic','Braindeath'],
'physical_damage':['piercing','slashing','bludgeoning'],
'magic_damage':['fire','cold','lightning','thunder','poison','acid','radiant','necrotic','force','psychic'],
'spell_0':["Acid Splash","Blade Ward","Booming Blade","Chill Touch","Control Flames","Create Bonfire","Dancing Lights","Druidcraft","Eldritch Blast","Encode Thoughts","Fire Bolt","Friends","Frostbite","Green-Flame Blade","Guidance","Gust","Infestation","Light","Lightning Lure","Mage Hand","Magic Stone","Mending","Message","Mind Sliver","Minor Illusion","Mold Earth","Poison Spray","Prestidigitation","Primal Savagery","Produce Flame","Ray of Frost","Resistance","Sacred Flame","Sapping Sting","Shape Water","Shillelagh","Shocking Grasp","Spare the Dying","Sword Burst","Thaumaturgy","Thorn Whip","Thunderclap","Toll the Dead","True Strike","Vicious Mockery","Word of Radiance"],
'spell_1':["Absorb Elements","Acid Stream","Alarm","Burning Hands","Catapult","Cause Fear","Charm Person","Chromatic Orb","Color Spray","Comprehend Languages","Detect Magic","Disguise Self","Distort Value","Earth Tremor","Expeditious Retreat","False Life","Feather Fall","Find Familiar","Floating Disk","Fog Cloud","Grease","Hideous Laughter","Ice Knife","Identify","Illusory Script","Jump","Longstrider","Mage Armor","Magic Missile","Protection from Evil and Good","Ray of Sickness","Shield","Silent Image","Sleep","Snare","Tasha\'s Hideous Laughter","Tenser\'s Floating Disk","Thunderwave","Unseen Servant","Witch Bolt"],
'spell_2':["Acid Arrow","Aganazzar\'s Scorcher","Aid","Alter Self","Animal Messenger","Arcane Lock","Arcanist\'s Magic Aura","Augury","Barkskin","Beast Sense","Blindness/Deafness","Blur","Branding Smite","Calm Emotions","Cloud of Daggers","Continual Flame","Cordon of Arrows","Crown of Madness","Darkness","Darkvision","Detect Thoughts","Dragon\'s Breath","Dust Devil","Earthbind","Enhance Ability","Enlarge/Reduce","Enthrall","Find Steed","Find Traps","Flame Blade","Flaming Sphere","Flock of Familiars","Fortune\'s Favor","Gentle Repose","Gift of Gab","Gust of Wind","Healing Spirit","Heat Metal","Hold Person","Immovable Object","Invisibility","Jim\'s Glowing Coin","Knock","Lesser Restoration","Levitate","Locate Animals or Plants","Locate Object","Magic Mouth","Magic Weapon","Maximilian\'s Earthen Grasp","Melf\'s Acid Arrow","Mind Spike","Mind Thrust","Mirror Image","Misty Step","Moonbeam","Nystul\'s Magic Aura","Pass without Trace","Phantasmal Force","Prayer of Healing","Protection from Poison","Pyrotechnics","Ray of Enfeeblement","Rope Trick","Scorching Ray","See Invisibility","Shadow Blade","Shatter","Silence","Skywrite","Snilloc\'s Snowball Swarm","Spider Climb","Spike Growth","Spiritual Weapon","Suggestion","Summon Bestial Spirit","Warding Bond","Warding Wind","Web","Wristpocket","Zone of Truth"],
'spell_3':["Animate Dead","Aura of Vitality","Beacon of Hope","Bestow Curse","Blinding Smite","Blink","Call Lightning","Catnap","Clairvoyance","Conjure Animals","Conjure Barrage","Counterspell","Create Food and Water","Crusader\'s Mantle","Daylight","Dispel Magic","Elemental Weapon","Enemies Abound","Erupting Earth","Fast Friends","Fear","Feign Death","Fireball","Flame Arrows","Flame Stride","Fly","Galder\'s Tower","Gaseous Form","Glyph of Warding","Haste","Hunger of Hadar","Hypnotic Pattern","Incite Greed","Leomund\'s Tiny Hut","Life Transference","Lightning Arrow","Lightning Bolt","Magic Circle","Major Image","Mass Healing Word","Meld into Stone","Melf\'s Minute Meteors","Motivational Speech","Nondetection","Phantom Steed","Plant Growth","Protection from Energy","Pulse Wave","Remove Curse","Revivify","Sending","Sleet Storm","Slow","Speak with Dead","Speak with Plants","Spirit Guardians","Spirit Shroud","Stinking Cloud","Summon Fey Spirit","Summon Lesser Demons","Summon Shadow Spirit","Summon Undead Spirit","Thunder Step","Tidal Wave","Tiny Hut","Tiny Servant","Tongues","Vampiric Touch","Wall of Sand","Wall of Water","Water Breathing","Water Walk","Wind Wall"],
'spell_4':["Arcane Eye","Aura of Life","Aura of Purity","Banishment","Black Tentacles","Blight","Charm Monster","Compulsion","Confusion","Conjure Minor Elementals","Conjure Woodland Beings","Control Water","Death Ward","Dimension Door","Divination","Dominate Beast","Elemental Bane","Evard\'s Black Tentacles","Fabricate","Faithful Hound","Find Greater Steed","Fire Shield","Freedom of Movement","Galder\'s Speedy Courier","Giant Insect","Grasping Vine","Gravity Sinkhole","Greater Invisibility","Guardian of Faith","Guardian of Nature","Hallucinatory Terrain","Ice Storm","Intellect Fortress","Leomund\'s Secret Chest","Locate Creature","Mordenkainen\'s Faithful Hound","Mordenkainen\'s Private Sanctum","Otiluke\'s Resilient Sphere","Phantasmal Killer","Polymorph","Private Sanctum","Resilient Sphere","Secret Chest","Shadow of Moil","Sickening Radiance","Staggering Smite","Stone Shape","Stoneskin","Storm Sphere","Summon Aberrant Spirit","Summon Elemental Spirit","Summon Greater Demon","Vitriolic Sphere","Wall of Fire","Watery Sphere"],
'spell_5':["Animate Objects","Antilife Shell","Arcane Hand","Awaken","Banishing Smite","Bigby\'s Hand","Circle of Power","Cloudkill","Commune","Commune with Nature","Cone of Cold","Conjure Elemental","Conjure Volley","Contact Other Plane","Contagion","Control Winds","Creation","Danse Macabre","Dawn","Destructive Wave","Dispel Evil and Good","Dominate Person","Dream","Enervation","Far Step","Flame Strike","Geas","Greater Restoration","Hallow","Hold Monster","Holy Weapon","Immolation","Infernal Calling","Insect Plague","Legend Lore","Maelstrom","Mass Cure Wounds","Mislead","Modify Memory","Negative Energy Flood","Passwall","Planar Binding","Raise Dead","Rary\'s Telepathic Bond","Reincarnate","Scrying","Seeming","Skill Empowerment","Steel Wind Strike","Summon Celestial Spirit","Swift Quiver","Synaptic Static","Telekinesis","Telepathic Bond","Teleportation Circle","Temporal Shunt","Transmute Rock","Tree Stride","Wall of Force","Wall of Light","Wall of Stone","Wrath of Nature"],
'spell_6':["Arcane Gate","Blade Barrier","Bones of the Earth","Chain Lightning","Circle of Death","Conjure Fey","Contingency","Create Homunculus","Create Undead","Disintegrate","Drawmij\'s Instant Summons","Druid\'s Grove","Eyebite","Find the Path","Flesh to Stone","Forbiddance","Freezing Sphere","Globe of Invulnerability","Gravity Fissure","Guards and Wards","Harm","Heal","Heroes\' Feast","Instant Summons","Investiture of Flame","Investiture of Ice","Investiture of Stone","Investiture of Wind","Magic Jar","Mass Suggestion","Mental Prison","Move Earth","Otherworldly Form","Otiluke\'s Freezing Sphere","Otto\'s Irresistible Dance","Planar Ally","Primordial Ward","Programmed Illusion","Scatter","Soul Cage","Summon Fiendish Spirit","Sunbeam","Tenser\'s Transformation","Transport via Plants","True Seeing","Wall of Ice","Wall of Thorns","Wind Walk","Word of Recall"],
'spell_7':["Conjure Celestial","Crown of Stars","Delayed Blast Fireball","Divine Word","Etherealness","Finger of Death","Fire Storm","Forcecage","Magnificent Mansion","Mirage Arcane","Mordenkainen\'s Magnificent Mansion","Mordenkainen\'s Sword","Plane Shift","Power Word Pain","Prismatic Spray","Project Image","Regenerate","Resurrection","Reverse Gravity","Sequester","Simulacrum","Symbol","Teleport","Temple of the Gods","Tether Essence","Whirlwind"],
'spell_8':["Control Weather","Antimagic Field","Abi-Dalzim\'s Horrid Wilting","Dominate Monster","Incendiary Cloud","Maddening Darkness","Reality Break","Animal Shapes","Earthquake","Holy Aura","Dark Star","Illusory Dragon","Antipathy/Sympathy","Tsunami","Mighty Fortress","Maze","Feeblemind","Power Word Stun","Telepathy","Mind Blank","Sunburst","Clone","Glibness","Demiplane"],
'spell_9':["Mass Polymorph","True Polymorph","Storm of Vengeance","Invulnerability","Shapechange","Ravenous Void","Gate","Astral Projection","True Resurrection","Weird","Imprisonment","Power Word Heal","Prismatic Wall","Time Ravage","Power Word Kill","Foresight","Psychic Scream","Meteor Swarm","Time Stop","Mass Heal"],
'imdh_1':['1 - Cheese', '2 - Knives', '3 - Stuffed Animals', '4 - Lolita Garments', '5 - Bones','6 - Pastries','7 - Sea Creatures', '8 - Cosmetics','9 - Illustrated Tales', '10 - Dice'],
'imdh_2':['1 - Teacups & Saucers','2 - Bunnies','3 - Snakes & Lizards','4 - Music Boxes','5 - Undergarments','6 - Balls of Yarn','7 - Owls','8 - Stars','9 - Blankets','10 - Beads'],
'imdh_3':['1 - Plants & Terrariums','2 - Junk Food','3 - Cockatiels','4 - Cats','5 - Kittens','6 - Crested Geckos','7 - Books',"8 - Artist\'s Supplies",'9 - Festive Cheer','10 - Breakfast'],
'imdh_4':['1 - Trees','2 - Technology','3 - Footwear','4 - Squirrels','5 - Nightmares','6 - Herbs & Spices','7 - Dragon Items','8 - Garden Gnomes','9 - Corvids','10 - Spoons']}


items_replace['damage'] = items_replace['physical_damage'] + items_replace['magic_damage']
items_replace['weapon'] = (items_replace['slash'] + items_replace['blunt'] + items_replace['pierce'] + items_replace['ranged'] + items_replace['thrown'])*2 + items_replace['exotic_weapon']
items_replace['armor'] = items_replace['light_armor'] + items_replace['medium_armor'] + items_replace['heavy_armor']
items_replace['metal_armor'] = ['chain shirt', 'scale mail', 'breastplate', 'half-plate armor','ringmail armor', 'chainmail armor', 'splint armor', 'platemail']
items_replace['art'].extend(items_replace['carving'])
items_replace['game'] = items_replace['boardgame'] + items_replace['cardgame'] 
food_options = {
    "Taco Salad":['Mexican','Salad','Beef','Spicy','Avocado'],
    "Crispy Chicken Salad":['Salad','Chicken','Avocado'],
    "Paneer Golden Curry":['Indian','Asian','Curry','Rice','Dairy','Specialty Ingredient'],
    "Ratatouille":['French','Squash','Vegetables','Tomato','Couscous'],
    "Olive Chicken Tagine":['Chicken','Moroccan','African','Couscous','Tagine','Long Prep'],
    "_Jet's_ Detroit-Style Pizza":['Pizza','Italian','Dairy','Carbs','Takeout','Detroit'],
    "_Helen's Asian Kitchen_":['Asian','Rice','Tofu','Takeout'],
    "_ADDIS_ Ethiopian":['Ethiopian','African','Takeout','Vegetables','Carbs'],
    "_AFRA GRILL_":['African','Rice','Takeout'],
    "Muffaletta":['New Orleans','Sandwich','Carbs','Lunchmeat','Big Food'],
    "Cuban Sandwiches":['Sandwich','Lunchmeat'],
    "Hotdogs":['Sandwich','American','Lunchmeat','Grill'],
    "Hamburgers":['American','Beef','Sandwich','Grill'],
    "Spicy Beef & Plantains":['Beef','Spicy','Avocado','Rice','Plantains','Fruit','Difficult Timing'],
    "Poke Bowl":['Hawaiian','Asian','Sushi','Rice','Fish','Spicy','Difficult Timing'],
    "Chicken Something Dumplings":['Soup','Carbs','Chicken','D&D Cookbook'],
    "Fried Catfish":['Fish','Fried','Carbs','American'],
    "Mango Chicken Curry":['Asian','Curry','Mango','Fruit','Sweet','Rice'],
    "Falafel Gyros":['Mediterranean','Falafel','Sandwich'],
    "Quesadillas":['Mexican','Dairy','Carbs'],
    "Soup & Grilled Cheese":['Dairy','Soup','Tomato','Sandwich'],
    "Chicken Parmesan":['Italian','Chicken','Tomato'],
    "Hunter's Stew":['Slavic','Soup','Wine','Sausage','Cabbage'],
    "Kielbasa and Cabbage":['Slavic','Sausage','Cabbage','Mustard'],
    "Pierogis":['Slavic','Potato','Carbs'],
    "Herring Pumpkin Casserole":['Casserole','Fish','Squash','Carbs','Long Prep','Dairy','Big Food'],
    "Spaghetti Squash Alfredo Bowl":['Squash','Chicken','Alfredo','Dairy'],
    "Chicken & Waffles":['Chicken','Sweet','Breakfast','Carbs'],
    "_Lavash Cafe_":['Mediterranean','Lebanese','Takeout','Rice'],
    "_Fusian_ Sushi":['Asian','Sushi','Fish','Rice','Takeout'],
    "Salmon & Veggie Skewers":['Grill','Fish','Vegetables'],
    "Chicken & Sausage Gumbo":['New Orleans','Rice','Soup','Spicy','Cajun','Chicken','Sausage'],
    "_Tensuke Express_ Ramen":['Japanese','Asian','Noodle','Soup','Takeout'],
    "_Sushi-Ten_":['Japanese','Asian','Sushi','Rice','Fish','Takeout'],
    "Reuben Sandwiches":['Sandwich','Lunchmeat'],
    "Calzones":['Pizza','Carbs','Tomato','Dairy','Long Prep','Big Food'],
    "Acorn Squash Quinoa Bowl":['Squash','Rice','Vegetables'],
    "Potato Soup Bread Bowl":['Potato','Carbs','Soup','Big Food'],
    "_Ben's Vegan Frisbees_ Pizza":['Italian','Pizza','Takeout','Difficult Timing'],
    "Wonton Soup":['Asian','Soup','Egg'],
    "Vedbread":['Carbs','Mushroom','D&D Cookbook'],
    "Curly Kale Pasta Salad":['Italian','Salad','Noodle','Beans'],
    "White Beans & Rice":['American','Beans','Rice','Sausage'],
    "Lemon Fish Tagine":['African','Moroccan','Fish','Tagine','Long Prep'],
    "_Mt. Everest_ Nepalese":['Indian','Nepalese','Curry','Rice','Expensive','Takeout','Long Prep'],
    "Fish Tacos":['Fish','Sandwich','Mexican'],
    "Mushroom Risotto":['Rice','Mushrooms','Risotto','Long Prep'],
    "_Olive & Thyme_ Falafel Gyros":['Takeout','Mediterranean','Greek','Sandwich','Falafel'],
    "Okonomiyaki":['Japanese','Carbs','Beef','Specialty Ingredient','Cabbage'],
    "Shepherd's Pie":['English','Pie','Beef','Potato','Big Food'],
    "Tavern Hand-Pies":['Human','Pie','Sandwich','Beef','Potato','D&D Cookbook','Savory'],
    "Sword Coast Seafood Bouillabaisse":['French','Seafood','Shellfish','Human','D&D Cookbook','Soup','Tomato'],
    "Pan-Fried Knucklehead Trout":['Fried','Seafood','Fish','D&D Cookbook','Human'],
    "Amphail Braised Beef":['Beef','Meat','Human','D&D Cookbook'],
    "Hommet Golden-Brown Roasted Turkey with Sausage Stuffing and Drippings":['Human','Meat','Turkey','Sausage','D&D Cookbook','Long Prep','Big Food'],
    "Kara-Tur Noodles":['Asian','Human','Noodles','D&D Cookbook'],
    "Smoked Salmon Bagel Sandwich":['Sandwich','Seafood','Fish','Jewish'],
    "Matzo Ball Soup":['Soup','Jewish','Salty'],
    "Red Lentil & Lime Soup":['Lentils','Soup','Rice','Thai','Vegan']
    }

for i in food_options:
    food_options[i].sort()
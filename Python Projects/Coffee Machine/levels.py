from data import MENU, MACHINE_RESOURCES_NEEDED

# !INGREDIENT LEVELS NEEDED
# WATER VALUES
espresso_water_level = MENU['espresso']['ingredients']['water']
latte_water_level = MENU['latte']['ingredients']['water']
cappuccino_water_level = MENU['cappuccino']['ingredients']['water']

# COFFEE VALUES
espresso_coffee_level = MENU['espresso']['ingredients']['coffee']
latte_coffee_level = MENU['latte']['ingredients']['coffee']
cappuccino_coffee_level = MENU['cappuccino']['ingredients']['coffee']

# MILK VALUES
espresso_milk_level = MENU['espresso']['ingredients']['milk']
latte_milk_level = MENU['latte']['ingredients']['milk']
cappuccino_milk_level = MENU['cappuccino']['ingredients']['milk']

# !CURRENT MACHINE LEVELS
# WATER LEVELS
machine_water_level = MACHINE_RESOURCES_NEEDED['water']

# COFFEE LEVELS
machine_coffee_level = MACHINE_RESOURCES_NEEDED['coffee']

# MILK LEVELS
machine_milk_level = MACHINE_RESOURCES_NEEDED['milk']

# !VALUES IF DRINKS MADE
# WATER LEVELS
new_espresso_water_levels = MACHINE_RESOURCES_NEEDED['water'] - MENU['espresso']['ingredients']['water']
new_latte_water_levels = MACHINE_RESOURCES_NEEDED['water'] - MENU['latte']['ingredients']['water']
new_cappuccino_water_levels = MACHINE_RESOURCES_NEEDED['water'] - MENU['cappuccino']['ingredients']['water']

# COFFEE LEVELS
new_espresso_coffee_levels = MACHINE_RESOURCES_NEEDED['coffee'] - MENU['espresso']['ingredients']['coffee']
new_latte_coffee_levels = MACHINE_RESOURCES_NEEDED['coffee'] - MENU['latte']['ingredients']['coffee']
new_cappuccino_coffee_levels = MACHINE_RESOURCES_NEEDED['coffee'] - MENU['cappuccino']['ingredients']['coffee']

# MILK LEVELS
new_espresso_milk_levels = MACHINE_RESOURCES_NEEDED['milk'] - MENU['espresso']['ingredients']['milk']
new_latte_milk_levels = MACHINE_RESOURCES_NEEDED['milk'] - MENU['latte']['ingredients']['milk']
new_cappuccino_milk_levels = MACHINE_RESOURCES_NEEDED['milk'] - MENU['cappuccino']['ingredients']['milk']

# !COIN VALUES
penny = 0.01
nickle = 0.05
dime = 0.10
quarter = 0.25
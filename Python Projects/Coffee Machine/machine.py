import random
import math
from levels import espresso_water_level, latte_water_level, cappuccino_water_level, espresso_coffee_level, latte_coffee_level, cappuccino_coffee_level, espresso_milk_level, latte_milk_level, cappuccino_milk_level, machine_water_level, machine_coffee_level, machine_milk_level, penny, nickle, dime, quarter, new_latte_water_levels, new_espresso_water_levels, new_cappuccino_coffee_levels, new_cappuccino_milk_levels, new_cappuccino_water_levels, new_espresso_coffee_levels, new_espresso_milk_levels, new_latte_coffee_levels, new_latte_milk_levels

# We will make our drinks here
def drink_maker():
    while True:
        
        print(f'\n\tCurrent Milk Levels: {machine_milk_level}') 
        print(f'\tCurrent Water Levels: {machine_water_level}') 
        print(f'\tCurrent Coffee Levels: {machine_coffee_level}\n')
        
        drink_choice = int(input(f'\nPlease choose a drink {name}: \n\n\t1. Espresso \n\t2. Latte \n\t3. Cappuccino\n \n\nPlease choose here: '))
        if drink_choice == 1:
            print('\nYou have chosen espresso!')
            new_espresso_coffee_levels
            new_espresso_milk_levels
            new_espresso_water_levels
            
        elif drink_choice == 2:
            print('\nYou have chosen latte!')
        elif drink_choice == 3:
            print('\nYou have chosen cappuccino!')

# We will check ingredient levels here   


# We will check how much money the user has put in
def money_check():
    current_money = 0
    
    money_deposit = int(input(f'\nSo {name}, You can choose to either: \n\n\t1. Deposit Money \n\t2. Check Money \n\nPlease choose here: '))
    print (current_money)
    
    
    
# We will dispense drinks and check money here
def machine():
    choice = int(input(f'\nOkay {name}, what would you like to do: \n\n\t1. Check a Machine Report \n\t2. Make a Drink \n\t3. Show current Money\n \n\nPlease choose here: '))
    
    if choice == 1:
        ...
    elif choice == 2:
        drink_maker()
    elif choice == 3:
        money_check()
    else:
        exit    

name = input('Hello user, please enter your name: ')
machine()
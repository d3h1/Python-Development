from art import logo, vs
from game_data import data
import random

print(logo)

def game():
    
    playerPoints = 0

    while True:
        
        print('Compare A: ')
        print( randomObject1['name'] + ', a ' + randomObject1['description'] + ', from ' + randomObject1['country'])

        print(vs)

        print('Compare B: ')
        print( randomObject2['name'] + ', a ' + randomObject2['description'] + ', from ' + randomObject2['country'])

        print(f'You currently have {playerPoints} points!')
        userAns = input('Choose A or B: ')
        
        
        if userAns == 'a': 
            if randomObject1['follower_count'] < randomObject2['follower_count']:
                print(f'You lost with {playerPoints} points')
                return False
                
            elif randomObject1['follower_count'] > randomObject2['follower_count']:
                playerPoints += 1
                print(f'You were correct!')
                
        if userAns == 'b': 
            if randomObject2['follower_count'] < randomObject1['follower_count']:
                print(f'You lost with {playerPoints} points')
                return False
                
            elif randomObject2['follower_count'] > randomObject1['follower_count']:
                playerPoints += 1
                print(f'You were correct!')


# !GLOBAL VARIABLES

randomObject1 = random.choice(data)
choiceA = randomObject1['name'] + ', a ' + randomObject1['description'] + ', from ' + randomObject1['country']

randomObject2 = random.choice(data)
choiceB = randomObject2['name'] + ', a ' + randomObject2['description'] + ', from ' + randomObject2['country']


if randomObject1 == randomObject2:
    randomObject2 = random.choice(data)

game()
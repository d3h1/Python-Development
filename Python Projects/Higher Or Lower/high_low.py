from art import logo, vs
from game_data import data
import random

print(logo)

def game():
    
    randomObject1 = random.choice(data)
    choiceA = randomObject1['name'] + ', a ' + randomObject1['description'] + ', from ' + randomObject1['country']

    randomObject2 = random.choice(data)
    choiceB = randomObject2['name'] + ', a ' + randomObject2['description'] + ', from ' + randomObject2['country']
    
    if randomObject1 == randomObject2:
        randomObject2 = random.choice(data)
    
    playerPoints = 0

    while True:
        
        print('Compare A: ')
        print( randomObject1['name'] + ', a ' + randomObject1['description'] + ', from ' + randomObject1['country'])

        print(vs)

        print('Compare B: ')
        print( randomObject2['name'] + ', a ' + randomObject2['description'] + ', from ' + randomObject2['country'])

        print(f'\nYou currently have {playerPoints} points!\n')
        userAns = input('Choose A or B: \n')
        
        
        if userAns == 'a': 
            if randomObject1['follower_count'] < randomObject2['follower_count']:
                print(f'You lost with {playerPoints} points')
                return False
                
            elif randomObject1['follower_count'] > randomObject2['follower_count']:
                playerPoints += 1
                print(f'You were correct!')
                randomObject2 = random.choice(data)
            
                
        if userAns == 'b': 
            if randomObject2['follower_count'] < randomObject1['follower_count']:
                print(f'You lost with {playerPoints} points')
                return False
                
            elif randomObject2['follower_count'] > randomObject1['follower_count']:
                playerPoints += 1
                print(f'You were correct!')
                randomObject1 = random.choice(data)


game()
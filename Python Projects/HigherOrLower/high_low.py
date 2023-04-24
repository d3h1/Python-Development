from art import logo, vs
from game_data import data
import random

print(logo)

def game():
    
    while True:
        
        print('Compare A: ')
        print( randomObject1['name'] + ', a ' + randomObject1['description'] + ', from ' + randomObject1['country'])

        print(vs)

        print('Compare B: ')
        print( randomObject2['name'] + ', a ' + randomObject2['description'] + ', from ' + randomObject2['country'])

        userAns = input('Choose A or B: ')
        
        if userAns == 'a': 
            if randomObject1['follower_count'] < randomObject2['follower_count']:
                False
            elif randomObject1['follower_count'] > randomObject2['follower_count']:
                playerPoints.append(1)
                print(f'You were correct! You have {playerPoints[0]} points now!')
                
        if userAns == 'b': 
            if randomObject2['follower_count'] < randomObject1['follower_count']:
                False
            elif randomObject2['follower_count'] > randomObject1['follower_count']:
                playerPoints.append(1)
                print(f'You were correct! You have {playerPoints[0]} points now!')


# !GLOBAL VARIABLES
playerPoints = []

randomObject1 = random.choice(data)
choiceA = randomObject1['name'] + ', a ' + randomObject1['description'] + ', from ' + randomObject1['country']

randomObject2 = random.choice(data)
choiceB = randomObject2['name'] + ', a ' + randomObject2['description'] + ', from ' + randomObject2['country']

# # TESTING
# if randomObject1['follower_count'] == randomObject2['follower_count']:
#     print (True)
#     print(randomObject1['follower_count'],randomObject2['follower_count'])
# else:
#     print(False)
#     print(randomObject1['follower_count'],randomObject2['follower_count'])

# userAns = input('Choose A or B: ')
# if userAns == 'a': 
#     if randomObject1['follower_count'] < randomObject2['follower_count']:
#         False
#     elif randomObject1['follower_count'] > randomObject2['follower_count']:
#         playerPoints.append(1)
#         print(f'You were correct! You have {playerPoints[0]} points now!')
# if userAns == 'b': 
#     if randomObject2['follower_count'] < randomObject1['follower_count']:
#         False
#     elif randomObject2['follower_count'] > randomObject1['follower_count']:
#         playerPoints.append(1)
#         print(f'You were correct! You have {playerPoints[0]} points now!')

# print (choiceA + '\n' + choiceB)




# game()
from art import logo, vs
from game_data import data
import random

print(logo)

# def game():
    
#     while True:
        
#         print('Compare A: ')
#         print( randomObject['name'] + ', a ' + randomObject['description'] + ', from ' + randomObject['country'])

#         print(vs)

#         print('Compare B: ')
#         print( randomObject['name'] + ', a ' + randomObject['description'] + ', from ' + randomObject['country'])

#         input(' Does A or B have more followers in instagram?')


# !GLOBAL VARIABLES
score = {} # score : count
playerPoints = [0]
randomObject1 = random.choice(data)
randomObject2 = random.choice(data)



choiceA = randomObject1['name'] + ', a ' + randomObject1['description'] + ', from ' + randomObject1['country']

choiceB = randomObject2['name'] + ', a ' + randomObject2['description'] + ', from ' + randomObject2['country']

if randomObject1['follower_count'] != randomObject2['follower_count']:
    print ('This is true')

print (choiceA + '\n' + choiceB)




# game()
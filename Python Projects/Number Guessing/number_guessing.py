from logo import logo
import random

def number_guessing_easy(numOfTries = 10):
    print(f'Easy Difficulty: {numOfTries} Tries')
    while numOfTries > 0:
        # print (randomGuess) # *TESTING
        userEasyGuess = int(input(f'\nYou have {numOfTries} tries left. Make a guess: '))
        # !Giving user hints to guess the answer
        if userEasyGuess > randomGuess:
            print('Your answer is too high! Keep trying. . .')
            numOfTries -= 1 
        elif userEasyGuess < randomGuess:
            print('Your answer is too low! Keep trying. . .')
            numOfTries -= 1
        elif userEasyGuess == randomGuess:
            print(goodAns)
            break
        else:
            print('Enter a valid answer next try. . . ')
            numOfTries -= 1
    # !Outputting correct or wrong        
    if numOfTries == 0:
        print(badAns)
        return
    
        
def number_guessing_hard(numOfTries = 5):
    print(f'Hard Difficulty: {numOfTries} Tries')
    while numOfTries > 0:
        # print (randomGuess) # *TESTING
        userHardGuess = int(input(f'You have {numOfTries} tries left. Make a guess: '))
        # !Giving user hints to guess the answer
        if userHardGuess > randomGuess:
            print('Your answer is too high! Keep trying. . .')
            numOfTries -= 1
            badAns
        elif userHardGuess < randomGuess:
            print('Your answer is too low! Keep trying. . .')
            numOfTries -= 1
            badAns
        elif userHardGuess == randomGuess:
            print(goodAns)
            break
        else:
            print('Enter a valid answer next try. . . ')
            numOfTries -= 1
    # !Outputting correct or wrong        
    if numOfTries == 0:
        print(badAns)
        return
    
# !Define main function
def main():
    print(logo)
    userName = input('\n\nEnter your name here: ')
    print(f'Welcome {userName}. \n\tI am thinking of a number between 1 and 100. . .')
    difficultyChosen = input('\t\tChoose a difficulty by simply typing : "easy" or "hard".\n')
    # !Choose your level of play
    if difficultyChosen == 'easy':
        number_guessing_easy()
    elif difficultyChosen == 'hard':
        number_guessing_hard()
    else:
        print('Please type either "easy" or "hard". . .')
        return

# !Global Scope
numberList = list(range(1, 101))
randomGuess = random.choice(numberList)
goodAns = '\n\t\t\tThat\'s the answer! Congratulations!'
badAns = '\n\t\t\tYou have run out of tries! Please come back and try again.'

main()
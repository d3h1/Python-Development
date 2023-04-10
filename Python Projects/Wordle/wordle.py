word = 'snake'


for n in range(1, 7):
    guess = input(f"\nGuess {n}: ").lower()
    if guess == word:
        print('Correct!')
        break
    
    print('Wrong!')

if guess != word:
    print ('You failed!')
else:
    print('You did it!')
    




    

word = 'snake'


for n in range(1, 7):
    guess = input(f"\nGuess {n}: ").lower()
    if guess == word:
        print('Correct!')
        break
    
    print('Wrong!')
    
    #  We will now display wrong and correct letters between a users guess and the word from the word list
    
    # We are using set comprehension to collect correct letters
    correctLetters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }
    # We will use boolean logic to find a count for misplaced and wrong letters
    misplacedLetters = set(guess) & set(word) - correctLetters
    wrongLetters = set(guess) - set(word)
    
    # This will print out each form of letter based on your guess and the word
    print('Correct Letters:', ', '.join(sorted(correctLetters)))
    print('Misplaced Letters:', ', '.join(sorted(misplacedLetters)))
    print('Wrong Letters:', ', '.join(sorted(wrongLetters)))

if guess != word:
    print ('You failed!')
else:
    print('You did it!')
    




    

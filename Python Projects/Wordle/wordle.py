import pathlib
import random

# We are using pathlib to get the src path of the word.txt
wordlist = pathlib.Path('./words.txt')

words = [
    # lowercase the word so user can enter whatever case they want and it will always be lowercase
    word.lower()
    # ['adder', 'crane', 'etc...']
    for word in wordlist.read_text(encoding="utf-8").strip().split("\n")
]

randomWord = random.choice(words)

# !TESTING ONLY -- comment when done
print(randomWord)


for n in range(1, 7):
    guess = input(f"\nGuess {n}: ").lower()
    if guess == randomWord:
        print('Correct!')
        break
    
    print('Wrong!')
    
    #  We will now display wrong and correct letters between a users guess and the word from the word list
    
    # We are using set comprehension to collect correct letters
    correctLetters = {
        letter for letter, correct in zip(guess, randomWord) if letter == correct
    }
    # We will use boolean logic to find a count for misplaced and wrong letters
    misplacedLetters = set(guess) & set(randomWord) - correctLetters
    wrongLetters = set(guess) - set(randomWord)
    
    # This will print out each form of letter based on your guess and the randomWord
    print('Correct Letters:', ', '.join(sorted(correctLetters)))
    print('Misplaced Letters:', ', '.join(sorted(misplacedLetters)))
    print('Wrong Letters:', ', '.join(sorted(wrongLetters)))

if guess != randomWord:
    print (f'You failed! The word was {randomWord}')
else:
    print('You did it!')
    




    

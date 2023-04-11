import pathlib
import random

from rich.console import Console
from string import ascii_letters
from rich.theme import Theme

console = Console(width=40, theme=Theme({'Warning': 'red on yellow'}))
console.rule(":leafy_green: A Game Called: Wordle :leafy_green:")

def main():
    # This is how we get our main word
    randomWord = get_random_word()
    
    # !FOR TESTING -- COMMENT OUT WHEN DONE
    print(randomWord)    
    
    # Processing the main loop
    for n in range(1, 7):
        guess = input(f"\nGuess {n}: ").lower()
        
        show_guess(guess, randomWord)
        if guess == randomWord:
            game_win()
            break
        
    else:
        game_over(randomWord)

def get_random_word():
    # We are using pathlib to get the src path of the word.txt
    wordlist = pathlib.Path('./words.txt')
    
    words = [
        # lowercase the word so user can enter whatever case they want and it will always be lowercase
        word.lower()
        # ['adder', 'crane', 'etc...']
        for word in wordlist.read_text(encoding="utf-8").split("\n")
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]
    return random.choice(words)

def show_guess(guess, randomWord):
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

def refresh_page(headline):
    console.clear()
    console.rule(f'[bold blue]: leafy_green: {headline} :leafy_green:[/]\n')

def game_win():
    print("\nYou have won the game! Please play again!\n")

def game_over(randomWord):
    print(f'\n\nYou guessed wrong!\nThe word was "{randomWord}"!')    

if __name__ == "__main__":
    main()  

    

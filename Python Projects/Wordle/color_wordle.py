import pathlib
import random
import contextlib

from rich.console import Console
from string import ascii_letters, ascii_uppercase
from rich.theme import Theme

console = Console(width=40, theme=Theme({'Warning': 'red on yellow'}))

numOfLetters = 5
numOfGuesses = 6
words_path = pathlib.Path(__file__).parent / "words.txt"

def main():
    # This is how we get our main word
    randomWord = get_random_word(words_path.read_text(encoding='utf-8').split('\n'))
    guesses = ['_' * numOfLetters] * numOfGuesses
    
    # # !FOR TESTING -- COMMENT OUT WHEN DONE
    # print(randomWord)    
    
    # Processing the main loop
    with contextlib.suppress(KeyboardInterrupt):
        for i in range(numOfGuesses):
            refresh_page(headline=f'Guess {i + 1}')
            show_guesses(guesses, randomWord)
            
            guesses[i] = guess_word(previous_guesses = guesses[:i])
            if guesses[i] == randomWord:
                break
        
    # POST
    game_over(guesses, randomWord, guessed_correctly = guesses[i] == randomWord)

def get_random_word(word_list):
    # We are using pathlib to get the src path of the word.txt
    # *Using the walrus operator allows you the user to fix their problem versus seeing a traceback error -- actionable feedback
    if words := [
        # uppercase the word so user can enter whatever case they want and it will always be uppercase
        word.upper()
        # ['adder', 'crane', 'etc...']
        for word in word_list
        if len(word) == numOfLetters and all(letter in ascii_letters for letter in word)
    ]:
        return random.choice(words)
    else:
        console.print(f'No words of length {numOfLetters} in the word list!', style='red')
        raise SystemExit()

def show_guesses(guesses, randomWord):
    letter_status = {letter: letter for letter in ascii_uppercase}
    for guess in guesses:
        styled_guess = []
        # WE are populating an empty list with our guesses as they are entered by the user
        for letter, correct in zip(guess, randomWord):
            if letter == correct:
                style = 'bold white on green'
            elif letter in randomWord:
                style = 'bold white on yellow'
            elif letter in ascii_letters:
                style = 'white on #666666'
            else:
                style = 'dim'
            styled_guess.append(f'[{style}]{letter}[/]')
            if letter != '_':
                letter_status[letter] = f'[{style}]{letter}[/]'
        console.print("".join(styled_guess), justify='center')
    console.print('\n' + ''.join(letter_status.values()), justify='center')
        
def guess_word(previous_guesses):
    guess = console.input('\nGuess word: ').upper()
    
    # Using recursive calls to make an elegant approach to create a loop in this case
    if guess in previous_guesses:
        console.print(f'You have already guessed {guess}.', style='red')
        return guess_word(previous_guesses)
    
    # We have to check the length of the users inputted word to make sure it matches the secret word length of 5
    if len(guess) != numOfLetters:
        console.print('Your guess must be 5 letter!', style='red')
        return guess_word(previous_guesses)
    
    # We are gonna guide the user to only the english alphabet 
    # *Again we use the walrus operator inside the any function to collect an example of a char thats invalid
    if any((invalid := letter) not in ascii_letters for letter in guess):
        console.print(f'Invalid Letter: "{invalid}". Please use English Letters', style='warning')
        return guess_word(previous_guesses)
    
    return guess

def refresh_page(headline):
    console.clear()
    console.rule(f'[bold blue]: leafy_green: {headline} :leafy_green:[/]\n')


def game_over(guesses, randomWord, guessed_correctly):
    refresh_page(headline='Game OVER!')
    show_guesses(guesses, randomWord)    
    
    if guessed_correctly:
        console.print(f"\n[bold white on green]Correct, the word is {randomWord}[/]")
    else:
        console.print(f"\n[bold white on red]Sorry, the word was {randomWord}[/]")

if __name__ == "__main__":
    main()  
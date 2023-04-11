import pathlib
import random

from rich.console import Console
from string import ascii_letters
from rich.theme import Theme

console = Console(width=40, theme=Theme({'Warning': 'red on yellow'}))
# console.rule(":leafy_green: A Game Called: Wordle :leafy_green:")

def main():
    # This is how we get our main word
    words_path = pathlib.Path(__file__).parent / "words.txt"
    randomWord = get_random_word(words_path.read_text(encoding='utf-8').split('\n'))
    guesses = ['_' * 5] * 6
    
    # # !FOR TESTING -- COMMENT OUT WHEN DONE
    # print(randomWord)    
    
    # Processing the main loop
    for i in range(6):
        refresh_page(headline=f'Guess {i + 1}')
        show_guesses(guesses, randomWord)
        
        guesses[i] = input('\nGuess Word: ').lower()
        if guesses[i] == randomWord:
            # game_win()
            break
        
    # POST
    game_over(guesses, randomWord, guessed_correctly = guesses[i] == randomWord)

def get_random_word(word_list):
    # We are using pathlib to get the src path of the word.txt
    words = [
        # lowercase the word so user can enter whatever case they want and it will always be lowercase
        word.lower()
        # ['adder', 'crane', 'etc...']
        for word in word_list
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]
    return random.choice(words)

def show_guesses(guesses, randomWord):
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
        console.print("".join(styled_guess), justify='center')

def refresh_page(headline):
    console.clear()
    console.rule(f'[bold blue]: leafy_green: {headline} :leafy_green:[/]\n')

# def game_win():
#     print("\nYou have won the game! Please play again!\n")

def game_over(guesses, randomWord, guessed_correctly):
    refresh_page(headline='Game OVER!')
    show_guesses(guesses, randomWord)    
    
    if guessed_correctly:
        console.print(f"\n[bold white on green]Correct, the word is {randomWord}[/]")
    else:
        console.print(f"\n[bold white on red]Sorry, the word was {randomWord}[/]")

if __name__ == "__main__":
    main()  
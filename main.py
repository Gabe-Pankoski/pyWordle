from rich.console import Console
import random

FILE_PATH = "valid-wordle-words.txt"

def main():
    guess_word = ""
    word_guessed = False
    max_guesses = 6
    guesses = max_guesses
    console = Console()
    word_list = []
    guess_letters = []

    with open(FILE_PATH, 'r') as file:
        for line in file:
            word_list.append(line.strip())

    random_int = random.randint(0, len(word_list)-1)
    guess_word = word_list[random_int]

    console.print("[bold yellow]W[/bold yellow]o[bold green]r[/bold green]d[bold yellow]l[/bold yellow]e")

    while guesses > 0:
        guess = console.input(f"({guesses}/{max_guesses}) - [bold white]Guess the five-letter word: ")
        guess = guess.strip()
        if guess.lower() == "quit":
            break
        if len(guess) != 5:
            console.print(f"[bold red]Guess must be five-letter word.")
            continue
        if guess.lower() not in word_list:
            console.print(f"[bold red]{guess} is not a valid word.")
            continue
        temp_word = guess_word
        output = ""
        for index, char in enumerate(guess):
            if char == temp_word[index]:
                output += f"[bold green]{char}[/bold green]"
            elif char in temp_word:
                output += f"[bold yellow]{char}[/bold yellow]"
                temp_word = temp_word.replace(char, "_", 1)
            else:
                output += f"{char}"
        console.print(output)
        if guess.lower() == guess_word:
            console.print(f"[bold green]You guessed the word!")
            word_guessed = True
            break
        guesses -= 1

    if word_guessed == False:
        console.print(f"[bold red]Sorry, the word was {guess_word}")

if __name__ == "__main__":
    main()

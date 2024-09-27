import random  # noqa
import os

hangman = {
    0: ("       ", "       ", "       "),
    1: ("     o ", "       ", "       "),
    2: ("     o ", "     | ", "       "),
    3: ("     o ", "    /| ", "       "),
    4: ("     o ", "    /|\\", "       "),
    5: ("     o ", "    /|\\", "    /  "),
    6: ("     o ", "    /|\\", "    / \\"),
    7: ("     o/", "    /|\\", "    / \\"),
}


def clear_screen():
    os.system("clear")


"""
enter your choice : list of words   we can select type like fruits or pc brand or something
-list of these


"""

planets = ["neptune", "earth", "mars", "mercury"]
countries = ["canada", "australia", "japan"]
car_brands = [
    "tesla",
    "bmw",
    "toyota",
    "mercedesbenz",
    "audi",
    "ford",
    "chevrolet",
    "honda",
    "hyundai",
    "kia",
    "nissan",
    "porsche",
    "ferrari",
    "lamborghini",
]
cryptocurrencies = ["bitcoin", "ethereum", "dogecoin", "litecoin", "ripple"]


def display_man(wrong_guesses):
    print("************")
    for line in hangman[wrong_guesses]:
        print(line)
    print("************")


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def program_handler(get_choice):
    answer = get_choice
    attempt = 0
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        if wrong_guesses == 6:
            print("\n!!!Last Guess\n")
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("\nEnter a letter: ").lower()
        print("\nAttempt -- {}".format(attempt))
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)
        attempt += 1
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
        if "_" not in hint:
            clear_screen()
            display_man(wrong_guesses)
            display_answer(answer)
            print('Guessed in "{}" attempts '.format(attempt))
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False


def main():
    menu_option = 0
    while menu_option != 5:
        try:
            print("\nWelcome to Hangman Game")
            menu_option = int(
                input(
                    "Which subject you like the most?\n 1) Planets\n 2) Countries\n 3) Car_brands\n 4) Cryptocurrencies\n 5) Exit \nChoice: "
                )
            )
            if menu_option == 1:
                clear_screen()
                print("Guess the name of the Planet")
                program_handler(random.choice(planets))
            elif menu_option == 2:
                clear_screen()
                print("Guess the name of the Country")
                program_handler(random.choice(countries))
            elif menu_option == 3:
                clear_screen()
                print("Guess the name of the Car_brand")
                program_handler(random.choice(car_brands))
            elif menu_option == 4:
                clear_screen()
                print("Guess the name of the Cryptocurrency")
                program_handler(random.choice(cryptocurrencies))
            elif menu_option == 5:
                clear_screen()
                print("Thank for playing! ")
            if menu_option > 5 or menu_option < 1:
                raise ValueError

        except ValueError:
            clear_screen()
            print("!!!Enter valid choice please :) ")


if __name__ == "__main__":
    main()

import random
import os


def clear_screen():
    os.system("clear")


def guess_game():
    print(
        "Welcome to the Guessing Game \nWe have a random number and you have to guess it!\nNew number will be generated each time you make a wrong guess.\nLet's start the game!"
    )
    while True:
        try:
            target_number = random.randint(2, 10)
            user_guess = int(input("Guess the target between 2 to 10: "))
            if user_guess < 2 or user_guess > 10:
                clear_screen()
                print("Hey Buddy, you entered {}.".format(user_guess))
                print("Guess the number between 2 to 10!")
                continue
            if isinstance(user_guess, int):
                if user_guess == target_number:
                    clear_screen()
                    print('Amazing! You guessed the target" {}"'.format(user_guess))
                    break
                else:
                    clear_screen()
                    print("Nope! Try again! \nThe target was {}".format(target_number))
        except ValueError:
            clear_screen()
            print("Huh, that was not a number :( \nEnter an integer!")
            print('The target was "{}".'.format(target_number))


def steady_random():
    print(
        "Welcome to the Steady Guessing Game \nWe have a random number and you have to guess it!\nLet's start the game!"
    )
    constant_number = random.randint(2, 20)
    while True:
        try:
            user_guess = int(input("Guess the target between 2 to 20: "))
            if user_guess < 2 or user_guess > 20:
                clear_screen()
                print("Hey Buddy, you entered {}.".format(user_guess))
                print("Guess the number between 2 to 20!")
                continue
            if isinstance(user_guess, int):
                print("You entered: ", user_guess)
                if user_guess == constant_number:
                    clear_screen()
                    print('Amazing! You guessed the target "{}".'.format(user_guess))
                    break
                elif user_guess < constant_number:
                    clear_screen()
                    print("Ah, your input was low!\nIncrease the value.")
                else:
                    clear_screen()
                    print("Oh, too high! \nDecrease your values.")
        except ValueError:
            clear_screen()
            print("Huh, that was not a number :( \nEnter an integer!")


menu_option = 0
while menu_option != 3:
    print("\nWelcome to the main menu")
    try:
        menu_option = int(
            input(
                "Which game do you want to play? \n1) Steady Random number Guessing \n2) Always Random\n3) Exit\nChoice: "
            )
        )
        clear_screen()
        if isinstance(menu_option, int):
            if menu_option == 1:
                steady_random()
            elif menu_option == 2:
                guess_game()
            elif menu_option == 3:
                print("Thank you for playing! Goodbye!")
    except ValueError:
        clear_screen()
        print("Not a valid choice!")

import random
import os


def clear_screen():
    os.system("clear")


def guess_game():
    print(
        "Welcome to the Guessing Game \nWe have a random number and you have to guess it !\nNew number will be generated each time you guess Wrong\nLet's start the game "
    )
    while True:
        try:
            num = random.randint(2, 10)
            a = int(input("Guess the Target between 2 to 10 : "))
            if a < 2 or a > 10:
                clear_screen()
                print("Hey Buddy You entered {} ".format(a))
                print("Guess the number between 2 to 10!")
                continue
            clear_screen()
            if isinstance(a, int):
                if a == num:
                    print("Amazing You guessed the target")
                    break
                else:
                    print("Nope Try again! \nThe target was {}".format(num))
        except ValueError:
            clear_screen()
            print("HUh that was not a number :( \n Enter an integer!")

            print('The target was "{}"'.format(num))


def steady_random():
    print(
        "Welcome to the Guessing Game \nWe have a random number and you have to guess it !\nLet's start the game "
    )
    c = random.randint(2, 20)
    while True:
        try:
            print(c)
            a = int(input("Guess the Target between 2 to 20 : "))
            if a < 2 or a > 20:
                clear_screen()
                print("Hey Buddy You entered {} ".format(a))
                print("Guess the number between 2 to 20!")
                continue
            if isinstance(a, int):
                print("You entered : ", a)
                if a == c:
                    print("Amazing You guessed the target")
                    break

                elif a < c:
                    print("Ah Your input was Low!\nIncrease the value")
                else:
                    print("Oh Too High! \nDecrease your values")

        except ValueError:
            clear_screen()
            print("HUh that was not a number :( \n Enter an integer!")


try:
    b = int(
        input(
            "Which game do you want to play? \n 1)Steady guessing game \n 2)Always random\n "
        )
    )
    if isinstance(b, int):
        clear_screen()
        if b == 1:
            steady_random()
            clear_screen()
        elif b == 2:
            guess_game()
            clear_screen()
except ValueError:
    print("Not a valid choice!")

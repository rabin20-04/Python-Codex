import random
import os


def clear_screen():
    os.system("clear")


def guess_game():
    while True:
        try:
            num = random.randint(2, 10)
            a = int(input("Guess the Target: "))
            clear_screen()
            if isinstance(a, int):
                if a == num:
                    print("Amazing You guessed the target")
                    break
                else:
                    print("Nope Try again! \nThe target was {}".format(num))
        except ValueError:
            print("HUh that was not a number :( \n Enter a integer!")

            print('You Entered {} \nThe target was "{}"'.format(a, num))


guess_game()

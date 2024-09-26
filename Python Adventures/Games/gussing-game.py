import random
import os


def clear_screen():
    os.system("clear")


def guess_game():
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


guess_game()

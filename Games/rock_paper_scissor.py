import random
import os


def clear_screen():
    os.system("clear")


choices_list = ["rock", "scissor", "paper"]
clear_screen()


def main():
    user_input = 0
    while user_input != "4":
        random_value = random.choice(choices_list)
        # print(random_value)
        # clear_screen()
        user_input = input(
            "\n**************************\nWelcome to Rock Paper Scissor Game  \nEnter Choices: \n 1) Rock\n 2) Paper\n 3) Scissor \n 4) Exit \n Enter your choice: "
        )
        clear_screen()
        print("Your choice : ", user_input)
        ro = "rock"
        si = "Scissor"
        pa = "Paper"
        user_result = None

        if (
            user_input == "1"
            or user_input.lower() == "r"
            or user_input.lower() == ro.lower()
        ):
            user_result = "rock"
            # or
            # if user_input.lower() -in ["1", "r", "rock"]:

        elif (
            user_input == "2"
            or user_input.lower() == "p"
            or user_input.lower() == pa.lower()
        ):
            user_result = "paper"

        elif (
            user_input == "3"
            or user_input.lower() == "s"
            or user_input.lower() == si.lower()
        ):
            user_result = "scissor"

        if user_result in ["rock", "paper", "scissor"]:
            give_user_result(user_result, random_value)
        else:
            print(
                f'------------ !!! Invalid input "{user_input}" ------------ \nPlease enter the given Choices \n'
            )


def give_user_result(user_result, random_value):
    if (
        (user_result == "rock" and random_value.lower() == "paper")
        or (user_result == "paper" and random_value.lower() == "scissor")
        or (user_result == "scissor" and random_value.lower() == "rock")
    ):
        # clear_screen()
        print(
            f'----------- You "{user_result.capitalize()}" and Computer "{random_value.capitalize()}"-----------  \nComputer wins!\n You losed the match '
        )
    elif (
        (user_result == "rock" and random_value.lower() == "scissor")
        or (user_result == "paper" and random_value.lower() == "rock")
        or (user_result == "scissor" and random_value.lower() == "paper")
    ):
        # clear_screen()
        print(
            f'----------- You "{user_result.capitalize()}" and Computer "{random_value.capitalize()}"-----------  \nCongrats You Won the match!'
        )
    else:
        # clear_screen()
        print(
            f'----------- You and Computer both "{random_value.capitalize()}" ----------- \nIt\'s a tie!'
        )


main()

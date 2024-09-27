import os


def clear_screen():
    os.system("clear")


"""
enter your choice : list of words   we can select type like fruits or pc brand or something
-list of these


"""

Planets = ["Neptune", "Earth", "Mars", "Mercury"]
Countries = ["Canada", "Australia", "Japan"]
car_brands = [
    "Tesla",
    "BMW",
    "Toyota",
    "Mercedes-Benz",
    "Audi",
    "Ford",
    "Chevrolet",
    "Honda",
    "Hyundai",
    "Kia",
    "Nissan",
    "Porsche",
    "Ferrari",
    "Lamborghini",
]
cryptocurrencies = ["Bitcoin", "Ethereum", "Dogecoin", "Litecoin", "Ripple"]


menu_option = 0
while menu_option != 5:
    try:
        print("Welcome to Hangman Game")
        menu_option = int(
            input(
                "Which subject you like the most?\n 1) Planets\n 2) Countries\n 3) Car_brands\n 4) Cryptocurrencies\n 5) Exit \nChoice: "
            )
        )
        if menu_option == 1:
            pass
        if menu_option == 2:
            pass
        if menu_option == 3:
            pass
        if menu_option == 4:
            pass
        if menu_option == 5:
            clear_screen()
            print("Thank for playing! ")

    except ValueError:
        clear_screen()
        print("Enter valid choice please :) ")

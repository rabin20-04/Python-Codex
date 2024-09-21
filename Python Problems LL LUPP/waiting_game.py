import time


import random


def waiting_game():
    target_time = random.randint(2, 6)
    print("Your target time is  ", target_time)

    input("--- Press Enter to Begin! ---")
    start_count = time.perf_counter()   # current time noted

    input(f"Press Enter after  {target_time}Seconds")
    check_value = time.perf_counter() - start_count     # new time after hitting enter
    print(f"Elapsed time :{check_value:.2f} seconds")

    if abs(check_value - target_time) < 0.1:
        print("OH! Perfect Timing Congrats!")
    elif check_value < target_time:
        print("Too fast!")
    else:
        print("Too slow!")


waiting_game()

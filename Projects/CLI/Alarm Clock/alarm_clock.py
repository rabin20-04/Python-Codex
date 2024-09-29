import time
import datetime

import pygame  # noqa
import os


def clear_screen():
    os.system("clear")


clear_screen()


def alarm_clock(user_input):
    print(f"Alarm set for {user_input}")
    sound_file = "alarm_sound.mp3"  # replace with your audio file path if direct method doesn't work

    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)

        if current_time == user_input:
            print("WAKE UP! 😴")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False


if __name__ == "__main__":
    user_input = input("Enter the time in format  HH:MM:SS = ")
    alarm_clock(user_input)

import time
import os


def start_battle():
    print("Battle Started!")
    time.sleep(2.5)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
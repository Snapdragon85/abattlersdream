import time
import os
import random


def wait(n):
    time.sleep(n)


def name():
    name_pool = ["Jared", "Nico", "Jay", "Chris", "Roy", "Scott", "Theodore",
                "Emma", "Alexia", "Naomi", "Molly", "Julie", "Hazel", "Sebastian",
                "Nathan", "Aarav", "Joe", "Munem", "Jivin", "Vince", "Ayrown"]
    selected = random.choice(name_pool)
    print("Battler", selected, "would like to fight!")

def whatdonext():
    print("What will you do?")
    print("1) FIGHT, 2) SHOP, 3) QUIT")
    choice = input(":")
    if choice == 1:
        print("Dealt 2 damage!")


def battle():
    print("Battle Started!")
    wait(2.5)
    name()
    wait(2.5)
    whatdonext()



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
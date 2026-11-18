import time
import os
import random

PlayerMaxHealth = 10
PlayerHealth = 10
PlayerDamage = 2

EnemyMaxHealth = 10
EnemyHealth = 10
EnemyDamage = 1
selected = "none"

def wait(n):
    time.sleep(n)


def name():
    global selected
    name_pool = ["Jared", "Nico", "Jay", "Chris", "Roy", "Scott", "Theodore",
                "Emma", "Alexia", "Naomi", "Molly", "Julie", "Hazel", "Sebastian",
                "Nathan", "Aarav", "Joseph", "Munem", "Jivin", "Vince", "Ayrown"]
    selected = random.choice(name_pool)
    print("Battler", selected, "would like to fight!")

def whatdonext():
    print("What will you do?")
    print("1) FIGHT, 2) SHOP, 3) QUIT")
    choice = input(":")
    if choice == "1":
        global EnemyHealth
        global PlayerDamage
        global EnemyMaxHealth
        global selected

        EnemyHealth -= PlayerDamage
        print("Dealt", PlayerDamage, "Damage!")
        wait(1.5)
        print(EnemyHealth)
        if EnemyHealth <= 0:
            print("Battler", selected, "Defeated!")
            wait(1.5)
            clear()
            name()
            EnemyHealth = EnemyMaxHealth
        whatdonext()
        


def battle():
    print("Battle Started!")
    wait(2.5)
    name()
    wait(2.5)
    whatdonext()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
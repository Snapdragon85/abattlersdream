import time
import os
import random

PlayerMaxHealth = 10
PlayerHealth = 10
PlayerDamage = 2
PlayerGold = 0

ShopUpgradePrice = 10
ShopHealPrice = 5

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
                "Nathan", "Aarav", "Joseph", "Munem", "Jivin", "Vince", "Ayrown",
                "John", "Dan", "Dilan", "Joshua", "Zakir", "Vicky", "Wallace"]
    selected = random.choice(name_pool)
    print("Battler", selected, "would like to fight!")
    wait(2.5)

def shop():
    print("Welcome to the SHOP!")
    print("1) UPGRADE, 2) HEAL, 3) EXIT")
    shopChoice = input(":")
    if shopChoice == "1":
        if PlayerGold == 0:
            print("Not enough GOLD")
            whatdonext()

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
        if EnemyHealth <= 0:
            print("Battler", selected, "Defeated!")
            wait(1.5)
            clear()
            name()
            EnemyHealth = EnemyMaxHealth
        whatdonext()
    if choice == "2":
        shop()
    if choice == "3":
        print("Okay then bye bye now")
        wait(2)
    if choice == "":
        wait(5)
        print("what")
        wait(2)
    if choice == "Sjelter":
        clear()
        print("Sjelter?")
        wait(3)


def battle():
    print("Battle Started!")
    wait(2.5)
    name()
    whatdonext()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
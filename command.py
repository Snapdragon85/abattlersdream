import time
import os
import random

PlayerMaxHealth = 10
PlayerHealth = 10
PlayerDamage = 2
PlayerGold = 0
AddedGold = 0

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
                "John", "Dan", "Dilan", "Joshua", "Zakir", "Vicky", "Wallace", "Phil"]
    selected = random.choice(name_pool)
    print("Battler", selected, "would like to fight!")
    wait(2.5)

def shop():
    global PlayerGold
    global ShopUpgradePrice
    global ShopHealPrice
    global PlayerDamage

    print("Welcome to the SHOP! Gold:", PlayerGold, "G")
    print("1) UPGRADE, 2) HEAL, 3) EXIT")
    shopChoice = input(":")
    if shopChoice == "1":
        print("COST:", ShopUpgradePrice, "G")
        spend = input("PROCEED?(y/n)")
        if spend == "n":
            shop()
        if spend == "y":
            if PlayerGold == 0:
                print("No GOLD")
                whatdonext()
            if PlayerGold < ShopUpgradePrice:
                print("Not Enoguh Gold!")
            if PlayerGold >= ShopUpgradePrice:
                print("A deals a deal!")
                PlayerGold -= ShopUpgradePrice
                wait(1)
                PlayerDamage += 2
                ShopUpgradePrice += 5
                print("Damage increased to ", PlayerDamage)
                wait(1.5)
                whatdonext()
        
    if shopChoice == "2":
        global PlayerMaxHealth
        global PlayerHealth
        if PlayerGold == 0:
            print("No GOLD")
            whatdonext()
        if PlayerGold < ShopHealPrice:
            print("Not Enoguh Gold!")
        if PlayerGold >= ShopHealPrice:
            print("A deals a deal!")
            PlayerGold -= ShopHealPrice
            PlayerHealth = PlayerMaxHealth
            wait(1)
            whatdonext()        

def whatdonext():
    global EnemyHealth
    global PlayerDamage
    global EnemyMaxHealth
    global PlayerHealth
    global selected
    global AddedGold
    global ShopUpgradePrice
    global PlayerGold
    
    print("What will you do?")
    print("Enemy HP:", EnemyHealth, ". Your  HP:", PlayerHealth)
    print("1) FIGHT, 2) SHOP, 3) QUIT")
    choice = input(":")
    if choice == "1":

        EnemyHealth -= PlayerDamage
        print("Dealt", PlayerDamage, "Damage!")
        wait(1.5)
        if EnemyHealth <= 0:
            print("Battler", selected, "Defeated!")
            wait(1.5)
            AddedGold = ShopUpgradePrice * 0.7
            PlayerGold += AddedGold
            print("Recieved", AddedGold, "G")
            wait(1.5)
            clear()
            name()
            EnemyHealth = EnemyMaxHealth
            whatdonext()
        else:
            print("Battler", selected, "Dealt", EnemyDamage, "HP!")
            wait(1.5)
            PlayerHealth -= EnemyDamage
            if PlayerHealth <= 0:
                clear()
                print("GAME OVER")
                wait(5)
                print("u suck")
                return 0
            whatdonext()
    if choice == "2":
        shop()
    if choice == "3":
        print("Okay cya")
        wait(2)
    if choice == "":
        wait(5)
        print("what")
        wait(2)
    if choice == "Sjelter":
        clear()
        print("Sjelter?")
        wait(3)
    if choice == "sjelter":
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
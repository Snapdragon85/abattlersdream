import command

def shop():
    
    global PlayerGold
    global PlayerMaxHealth
    global ShopUpgradePrice
    global ShopHealPrice
    global PlayerDamage
    global EnemyDamage
    global EnemyMaxHealth

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
                command.whatdonext()
            if PlayerGold < ShopUpgradePrice:
                print("Not Enoguh Gold!")
            if PlayerGold >= ShopUpgradePrice:
                print("A deals a deal!")
                PlayerGold -= ShopUpgradePrice
                command.wait(1)
                PlayerDamage += 2
                PlayerMaxHealth + 5
                EnemyMaxHealth += 5
                EnemyDamage += 2
                ShopUpgradePrice += 5
                print("Damage increased to ", PlayerDamage)
                print("Health Increased to ", PlayerMaxHealth)
                command.wait(1.5)
                command.whatdonext()
        
    if shopChoice == "2":
        global PlayerMaxHealth
        global PlayerHealth
        if PlayerGold == 0:
            print("No GOLD")
            command.whatdonext()
        if PlayerGold < ShopHealPrice:
            print("Not Enoguh Gold!")
        if PlayerGold >= ShopHealPrice:
            print("A deals a deal!")
            PlayerGold -= ShopHealPrice
            PlayerHealth = PlayerMaxHealth
            command.wait(1)
            command.whatdonext()
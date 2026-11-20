import command

def shop():
    
    global PlayerGold
    global PlayerMaxHealth
    global ShopUpgradePrice
    global ShopHealPrice
    global PlayerDamage
    global EnemyDamage
    global EnemyMaxHealth
    global PlayerHealth

    print("Welcome to the SHOP! Gold:", command.PlayerGold, "G")
    print("1) UPGRADE, 2) HEAL, 3) EXIT")
    shopChoice = input(":")
    if shopChoice == "1":
        print("COST:", command.ShopUpgradePrice, "G")
        spend = input("PROCEED?(y/n)")
        if spend == "n":
            shop()
        if spend == "y":
            if command.PlayerGold == 0:
                print("No GOLD")
                command.wait(2)
                command.whatdonext()
            if command.PlayerGold < command.ShopUpgradePrice:
                print("Not Enough Gold!")
            if command.PlayerGold >= command.ShopUpgradePrice:
                print("A deals a deal!")
                command.PlayerGold -= command.ShopUpgradePrice
                command.wait(1)
                command.PlayerDamage += 2
                command.PlayerMaxHealth + 5
                command.EnemyMaxHealth += 5
                command.EnemyDamage += 2
                command.ShopUpgradePrice += 5
                print("Damage increased to ", command.PlayerDamage)
                print("Health Increased to ", command.PlayerMaxHealth)
                command.wait(1.5)
                command.whatdonext()
        
    if shopChoice == "2":
        if command.PlayerGold == 0:
            print("No GOLD")
            command.wait(2)
            command.whatdonext()
        if command.PlayerGold < command.ShopHealPrice:
            print("Not Enoguh Gold!")
        if command.PlayerGold >= command.ShopHealPrice:
            print("A deals a deal!")
            command.PlayerGold -= command.ShopHealPrice
            command.PlayerHealth = command.PlayerMaxHealth
            command.wait(1)
            command.whatdonext()
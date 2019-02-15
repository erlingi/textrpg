from bin import objekter


wep1 = objekter.Weapon("Sword of Kings", 14, 5)
wep2 = objekter.Weapon("Hammer of Doom", 18, 8)
player1 = objekter.Player("Erling", 100, wep1, 20)
monster1 = objekter.Monster("Gorgo", 23, 100)


player1.addInventory("bag")
player1.addInventory("test")
#print(player1.name, player1.health, player1.weapon.name, player1.wallet)
#player1.playerAttack()

#print(player1.inventory)

monster1.addLoot(wep1)
monster1.addLoot(wep2)
monster1.getLoot()

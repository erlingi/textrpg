from bin import objekter
from bin import funksjoner


wep1 = objekter.Weapon("Sword of Kings", 14, 5)
wep2 = objekter.Weapon("Hammer of Doom", 55, 8)
wep3 = objekter.Weapon("Doomshield Hammer", 32, 8)

cons1 = objekter.Consumable("Potion of Health", 50)
cons2 = objekter.Consumable("Potion of Amplified Damage!", 14)

player1 = objekter.Player("Erling", 100, wep3, 20)
monster1 = objekter.Monster("Gorgo", 80, 100)

player1.addInventory(wep1)
player1.addInventory(wep3)
player1.addInventory(cons1)

monster1.addLoot(cons1)
monster1.addLoot(cons2)
#player1.getInventory()




#funksjoner.battleMonster(player1, monster1)

#player1.getInventory()

#print(player1.hearts)
#player1.minusHeart()
funksjoner.battleMonster(player1, monster1)
print(player1.life)


#player1.addInventory("bag")
#player1.addInventory("test")
#print(player1.name, player1.health, player1.weapon.name, player1.wallet)
#player1.playerAttack()

#print(player1.inventory)

#monster1.addLoot(wep1)
#monster1.addLoot(wep2)
#monster1.getLoot()

#funksjoner.attackMonster(player1, monster1)
#funksjoner.monsterAttack(monster1, player1)



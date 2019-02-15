#objekter

import random


# player class
class Player:
	def __init__(self, name, health, weapon, wallet):
		self.name = name
		self.health = health
		self.weapon = weapon
		self.wallet = wallet
		self.inventory = []

	def addInventory(self, leggTil):
		self.leggTil = leggTil
		self.inventory.append(leggTil)

	def getInventory(self):
		return self.inventory

	def setHealth(self, newHealth):
		self.newHealth = newHealth
		self.health = newHealth

	def playerAttack(self):
		critChance = 0
		for x in range(10):
			critChance += random.randint(1,8)
		
		if critChance >= 50:
			playerDmg = ((self.weapon.dmg + random.randint(1,self.weapon.dmg)) * 2)
			print(playerDmg)
			
		else:
			print(self.weapon.dmg + random.randint(1,self.weapon.dmg))


# weapon class
class Weapon:
	def __init__(self, name, dmg, cost):
		self.name = name
		self.dmg = dmg
		self.cost = cost

# consumable class
class Consumable:
	def __init__(self, name):
		self.name = name
		self.attribute = 50



# monster class
class Monster:
	def __init__(self, name, dmg, health):
		self.name = name
		self.dmg = dmg
		self.health = health
		self.loot = []

	def addLoot(self, lootAdd):
		self.lootAdd = lootAdd
		self.loot.append(lootAdd)

	def getLoot(self):
		for x in range(len(self.loot)):
			print(self.loot[x].name)




wep1 = Weapon("Sword of Kings", 14, 5)
wep2 = Weapon("Hammer of Doom", 18, 8)
player1 = Player("Erling", 100, wep1, 20)
monster1 = Monster("Gorgo", 23, 100)


player1.addInventory("bag")
player1.addInventory("test")
#print(player1.name, player1.health, player1.weapon.name, player1.wallet)
#player1.playerAttack()

#print(player1.inventory)

monster1.addLoot(wep1)
monster1.addLoot(wep2)
monster1.getLoot()

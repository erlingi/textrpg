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
		self.alive = True

	def addInventory(self, leggTil):
		self.leggTil = leggTil
		self.inventory.append(leggTil)

	def getInventory(self):
		print("Equipped weapon: {}".format(self.weapon.name))
		for x in self.inventory:
			if x.type == 1:
				print(x.name, x.dmg, x.cost)
			elif x.type == 2:
				print(x.name, x.attribute)

	def setHealth(self, newHealth):
		self.newHealth = newHealth
		self.health = newHealth

	def playerAttack(self):
		critChance = 0
		for x in range(10):
			critChance += random.randint(1,8)
		
		if critChance >= 50:
			playerDmg = ((self.weapon.dmg + random.randint(1,self.weapon.dmg)) * 2)
			return playerDmg
			
		else:
			return (self.weapon.dmg + random.randint(1,self.weapon.dmg))


# weapon class
class Weapon:
	def __init__(self, name, dmg, cost):
		self.name = name
		self.dmg = dmg
		self.cost = cost
		self.type = 1

# consumable class
class Consumable:
	def __init__(self, name, attribute):
		self.name = name
		self.attribute = 50
		self.type = 2



# monster class
class Monster:
	def __init__(self, name, dmg, health):
		self.name = name
		self.dmg = dmg
		self.health = health
		self.loot = []
		self.alive = True

	def addLoot(self, lootAdd):
		self.lootAdd = lootAdd
		self.loot.append(lootAdd)

	def getLoot(self):
		for x in range(len(self.loot)):
			print(self.loot[x].name)

	def monsterAttack(self):
		return self.dmg + 2	



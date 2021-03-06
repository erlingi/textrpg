#objekter

import random
import mapmodel


# player class
class Player:

	def __init__(self, name, health, weapon, wallet):
		self.name = name
		self.health = health
		self.weapon = weapon
		self.wallet = wallet
		self.inventory = []
		self.alive = True
		self.life = 5
		self.location = 1

	def status(self):
		return ("NAME: {}\nHEALTH: {} \nLIVES REMAINING: {} \nWEAPON: {} \nLOCATION: {}".format(self.name, self.health, self.life, self.weapon.name, mapmodel.rooms[self.location]["name"]))

	def addInventory(self, leggTil):
		self.leggTil = leggTil
		self.inventory.append(leggTil)

	def getInventory(self):
		print("----------------------------")
		print("Equipped weapon: {}".format(self.weapon.name))
		for x in self.inventory:
			if x.hvilken == 1:
				print(x.name, x.dmg, x.cost)
			elif x.hvilken == 2 or x.hvilken == 3:
				print(x.name, x.attribute)
		print("----------------------------")
		
	def setHealth(self, newHealth):
		self.newHealth = newHealth
		self.health = newHealth

	def currentRoom(self):

		if self.location == 1:
			print("---------------------------------")
			print("You are in room \"{}\" number {}".format(mapmodel.rooms[self.location]["name"], self.location))
			print("\nYou can go to room number 2 \"{}\" in the east or 3 \"{}\" southbound".format(mapmodel.rooms[2]["name"], mapmodel.rooms[3]["name"]))
			print("---------------------------------")		
		elif self.location == 2:	
			print("---------------------------------")			
			print("You are in room \"{}\" number {}".format(mapmodel.rooms[self.location]["name"], self.location))
			print("\nYou can go to room number 1 \"{}\" heading east or 4 \"{}\" southbound".format(mapmodel.rooms[1]["name"], mapmodel.rooms[4]["name"]))
			print("---------------------------------")
		elif self.location == 3:
			print("---------------------------------")			
			print("You are in room \"{}\" number {}".format(mapmodel.rooms[self.location]["name"], self.location))
			print("\nYou can go to room number 1 \"{}\" north.".format(mapmodel.rooms[1]["name"]))
			print("---------------------------------")			
		elif self.location == 4:
			print("---------------------------------")
			print("You are in room \"{}\" number {}".format(mapmodel.rooms[self.location]["name"], self.location))
			print("\nYou can go to room number 2 \"{}\" north".format(mapmodel.rooms[2]["name"]))			
			print("---------------------------------")
		else:
			print("Unknown location")
	

	def playerAttack(self):
		critChance = 0
		for x in range(10):
			critChance += random.randint(1,8)
		
		if critChance >= 50:
			playerDmg = ((self.weapon.dmg + random.randint(1,self.weapon.dmg)) * 2)
			return playerDmg
			
		else:
			return (self.weapon.dmg + random.randint(1,self.weapon.dmg))

	def minusLife(self):
		self.life -= 1
		if self.life == 0:
			print("You have no remaining lifes. You start over.")
			exit()
		else:
			print("You have {} lifes remaining.".format(self.life))


# weapon class
class Weapon:
	def __init__(self, name, dmg, cost, wepid):
		self.name = name
		self.dmg = dmg
		self.cost = cost
		self.hvilken = 1
		self.wepid = wepid

# consumable class
class Consumable:
	def __init__(self, name, attribute, hvilken):
		self.name = name
		self.attribute = attribute
		self.hvilken = hvilken



# monster class
class Monster:
	def __init__(self, name, dmg, health):
		self.name = name
		self.dmg = dmg
		self.health = health
		self.loot = []
		self.alive = True
		self.looted = False

	def addLoot(self, lootAdd):
		self.lootAdd = lootAdd
		self.loot.append(lootAdd)

	def getLoot(self):
		for x in self.loot:
			if x.hvilken == 1:
				print(x.name, x.dmg, x.cost)
			elif x.hvilken == 2 or 3:
				print(x.name, x.attribute)

	def monsterAttack(self):
		return self.dmg + 2	



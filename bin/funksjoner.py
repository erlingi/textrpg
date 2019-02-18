# funksjoner

from bin import objekter
from bin import mapmodel
import time

# game controller
def runtime(spillerObjekt):
	
	choice = raw_input("CHOICE: ")
	
	if choice == "status":

		print("------------------------------")
		print(spillerObjekt.status())
		print("------------------------------")
	
	elif choice == "move":

		moveLocation(spillerObjekt)

	elif choice == "location":

		spillerObjekt.currentRoom()

	elif choice == "powerpotion":

		consumePowerEnchantmentPot(spillerObjekt)

	elif choice == "inventory":
		
		spillerObjekt.getInventory()

	elif choice == "healthpotion":

		consumeHealthPot(spillerObjekt)

	elif choice == "switchwep":

		switchWeapon(spillerObjekt)

	elif choice == "help":
	
		gameHelp()

	elif choice == "exit":

		exit()
	
	else:
	
		print("Unknown choice")

def gameHelp():
	print("----------------------------------------------------------------------------------------------")
	print("Commands: status, inventory, switchwep healthpotion, powerpotion, move, location, help, exit")
	print("----------------------------------------------------------------------------------------------")


# the battle function, inputs spillerObject and encountered monsterObject
def battleMonster(spillerObjekt, monsterObjekt):


	# while the monster and the player is alive, execute the fight
	print("{} have encountered {}!! What would you like to do?".format(spillerObjekt.name, monsterObjekt.name))
	while monsterObjekt.alive and spillerObjekt.alive:
			
		choice = input("\n1: Fight the monster, 2: Flee combat (you will take a hit for running) ")
	
		if choice == 1:
			time.sleep(1)
			print("--------------------------------------")
			print("You swing your weapon at him!")
			attackMonster(spillerObjekt, monsterObjekt)
			time.sleep(1)
	
			if monsterObjekt.alive:
				time.sleep(1)
				monsterAttack(monsterObjekt, spillerObjekt)
				print("--------------------------------------")
				print("What would you like to do?")

		elif choice == 2:
	
			print("You're fleeing from {}! In the process he hits you one time with his weapon before you escape.".format(monsterObjekt.name))
			monsterAttack(monsterObjekt, spillerObjekt)
	
			break
	
	#if boolean monsterObject.alive is FALSE, the player killed him and following code will execute
	if not monsterObjekt.alive:
		print("\n-->You have killed the monster!<--")
		
		if not monsterObjekt.looted:

			print("--------------------------------------")
			print("He dropped the following loot:")
			monsterObjekt.getLoot()			
			print("\nWould you like to loot his items?")
			print("--------------------------------------")
			choice = input("1 for looting and 2 for leaving them: ")
			
			if choice == 1:
				
				lootDead(spillerObjekt, monsterObjekt)
				print("--------------------------------------")
				print("You looted its items.")
				print("--------------------------------------")
				monsterObjekt.looted = True
			
			elif choice == 2:
				
				print("--------------------------------------")
				print("You left the items on its dead corpse.")
				print("--------------------------------------")
		
		else:
			print("You already looted this corpse")
	
	# if player is not alive, the monster killed him and minusLife() is called upon
	elif not spillerObjekt.alive:
	
		if spillerObjekt.life > 0:
			print("The monster killed you....You lost a life")
			spillerObjekt.minusLife()
			spillerObjekt.health = 100
			spillerObjekt.alive = True
			monsterObjekt.health = 100
	
		else:
			spillerObjekt.minusLife()


def encounterMonster(spillerObjekt):
	
	# checks if current room contains a monster in the mapmodel	
	if mapmodel.rooms[spillerObjekt.location]["monster"]:
		return True

def whichMonster(room):

	# if player is in the toilet, summon appropriate monster
	if (room == 2) or (room == 2):
		return mapmodel.rooms[room]["montype"]

def consumeHealthPot(spillerObjekt):
	
	# unless the players inventory returned a type2 consumable (health potion), the boolean will remain false.
	foundHealthPotion = False
	for x in spillerObjekt.inventory:
		if x.hvilken == 2:
			spillerObjekt.health += x.attribute
			spillerObjekt.inventory.remove(x)
			print("You consumed a health potion. New health: {}".format(spillerObjekt.health))
			foundHealthPotion = True
			break

	# if iterating through the players inventory did not discover a health potion, foundHealthPotion will remain False
	if foundHealthPotion == False:
		print("You have no health potions")

def consumePowerEnchantmentPot(spillerObjekt):
	
	# unless the players inventory returned a type3 consumable (power potion), the boolean will remain false.
	foundPowerPotion = False
	for x in spillerObjekt.inventory:
		if x.hvilken == 3:
			print("You enchanted you weapon with extra damage. New damage: {}+{}".format(spillerObjekt.weapon.dmg, x.attribute))
			spillerObjekt.weapon.dmg += x.attribute
			spillerObjekt.inventory.remove(x)
			foundPowerPotion = True
			break

	# if iterating through the players inventory did not discover a power potion, foundPowerPotion will remain False
	if foundPowerPotion == False:
		print("You have no power potions")

def switchWeapon(spillerObjekt):

	switched = False
	print("---------------------------")
	for x in spillerObjekt.inventory:
		if hasattr(x, 'wepid'):
			print("ID: {} | WEAPON: {}".format(x.wepid, x.name))
		else:
			pass
	print("---------------------------")
	choice = input("Which weapon would you like to equip? (Input ID): ")
	for x in spillerObjekt.inventory:
		if hasattr(x, 'wepid'):
			if x.wepid == choice:
				spillerObjekt.inventory.append(spillerObjekt.weapon)
				spillerObjekt.weapon = x
				spillerObjekt.inventory.remove(x)
				switched = True
				print("\nYou equipped {}\n".format(x.name))

	if not switched:
		print("You do not have that weapon or miss-spelled it. Retype switchwep command and try again")
	

def moveLocation(spillerObjekt):

	lokasjon = spillerObjekt.location
	spillerObjekt.currentRoom()
	choice = input("Movement: ")
	
	# location: Home, 2 choices from movement: Toilet and Bedroom
	if lokasjon == 1:
		# toilet
		if choice == 2:
			spillerObjekt.location = choice
			# if room contains a monster (encounterMonster==TRUE), engage battle with it and-
			# figure out which monster object appropriate for the room with whichMonster() function
			if encounterMonster(spillerObjekt):
				battleMonster(spillerObjekt, whichMonster(choice))
			else:
				spillerObjekt.currentRoom()
		# bedroom
		elif choice == 3:
			spillerObjekt.location = choice
			if encounterMonster(spillerObjekt):
				battleMonster(spillerObjekt, whichMonster(choice))
			else:
				spillerObjekt.currentRoom()
		else:
			print("Wrong movement")

	# location: Toilet, 2 choices of movement: Home and Garden
	if lokasjon == 2:
		# home
		if choice == 1:
			spillerObjekt.location = choice
			if encounterMonster(spillerObjekt):
				battleMonster(spillerObjekt, whichMonster(choice))
			else:
				spillerObjekt.currentRoom()
		# garden
		elif choice == 4:
			spillerObjekt.location = choice
			if encounterMonster(spillerObjekt):
				battleMonster(spillerObjekt, whichMonster(choice))
			else:
				spillerObjekt.currentRoom()
		else:
			print("Wrong movement")

	# location: bedroom, 1 choice of movement: Home
	if lokasjon == 3:
		# home
		if choice == 1:
			spillerObjekt.location = choice
			if encounterMonster(spillerObjekt):
				battleMonster(spillerObjekt, whichMonster(choice))
			else:
				spillerObjekt.currentRoom()
		else:
			print("Wrong movement")

	# location: garden, 1 choice of movement: Toilet
	if lokasjon == 4:
		# toilet
		if choice == 2:
			spillerObjekt.location = choice
			if encounterMonster(spillerObjekt):
				battleMonster(spillerObjekt, whichMonster(choice))
			else:
				spillerObjekt.currentRoom()
		else:
			print("Wrong movement")



def attackMonster(spillerObjekt, monsterObjekt):
	damage = spillerObjekt.playerAttack()
	monsterObjekt.health -= damage

	#if the player is still alive, he will attack
	if spillerObjekt.alive:
		#if the monster in combat with the player is still alive, he will attack it
		if monsterObjekt.alive:
			if monsterObjekt.health >= 1:
				print("\n{} hit {} for {} damage! (monster hp: {})".format(spillerObjekt.name, monsterObjekt.name, damage, monsterObjekt.health))
			elif damage >= monsterObjekt.health:
				print("\n{} hit {} for {} damage! KILLING BLOW! (monster hp: {})".format(spillerObjekt.name, monsterObjekt.name, damage, monsterObjekt.health))
				monsterObjekt.alive = False
		else:
			print("{} is dead!".format(monsterObjekt.name))
	else:
		print("{} is dead and can't attack.".format(spillerObjekt.name))

# this function attacks the player it's currently in battle with based on object values
def monsterAttack(monsterObjekt, spillerObjekt):
	damage = monsterObjekt.monsterAttack()
	spillerObjekt.health -= damage

	# if the monster is still alive, it will attack
	if monsterObjekt.alive:
		# if the player in combat with the monster is still alive, it will attack him
		if spillerObjekt.alive:
			if spillerObjekt.health >= 1:
				print("\n{} hit {} for {} damage! (player hp: {})".format(monsterObjekt.name, spillerObjekt.name, damage, spillerObjekt.health))
			elif damage >= spillerObjekt.health:
				print("\n{} hit {} for {} damage! KILLING BLOW! (player hp: {})".format(monsterObjekt.name, spillerObjekt.name, damage, spillerObjekt.health))
				spillerObjekt.alive = False	
		else:
			print("{} is dead!".format(spillerObjekt.name))
	else:
		print("{} is dead and can't attack.".format(monsterObjekt.name))


# this function collects the objects from the monsters loot list, and appends them to the players inventory list.
def lootDead(spillerObjekt, monsterObjekt):
	loot = monsterObjekt.loot
	playerinventory = spillerObjekt.inventory
	for x in loot:
		playerinventory.append(x)
		#removes the loot from dead monsters inventory
		loot.remove(x)
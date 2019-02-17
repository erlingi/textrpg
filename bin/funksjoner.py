# funksjoner

from bin import objekter
import time


# the battle function, inputs spillerObject and encountered monsterObject
def battleMonster(spillerObjekt, monsterObjekt):
	print("{} have encountered {}!! What would you like to do?".format(spillerObjekt.name, monsterObjekt.name))	
	
	# while the monster and the player is alive, execute the fight
	while monsterObjekt.alive and spillerObjekt.alive:
		choice = input("\nPress 1 for fighting the monster, 2 for fleeing: ")
		if choice == 1:
			time.sleep(1)
			print("\nYou've decided to fight the monster! You swing your weapon at him.")
			attackMonster(spillerObjekt, monsterObjekt)
			time.sleep(1)
			if monsterObjekt.alive:
				time.sleep(1)
				monsterAttack(monsterObjekt, spillerObjekt)

		elif choice == 2:
			print("You're fleeing from {}! In the process he hits you one time with his weapon before you escape.".format(monsterObjekt.name))
			monsterAttack(monsterObjekt, spillerObjekt)
	
	#if boolean monsterObject.alive is FALSE, the player killed him and following code will execute
	if not monsterObjekt.alive:
		print("\nYou have killed the monster! He dropped the following loot: ")
		monsterObjekt.getLoot()
		print("\nWould you like to loot his items?")
		choice = input("1 for looting and 2 for leaving them: ")
		if choice == 1:
			lootDead(spillerObjekt, monsterObjekt)
			print("You looted its items.")
		elif choice == 2:
			print("You left his items on his dead corpse.")
	elif not spillerObjekt.alive:
		if spillerObjekt.life > 0:
			print("The monster killed you....You lost a life")
			spillerObjekt.minusLife()
		else:
			spillerObjekt.minusLife()



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





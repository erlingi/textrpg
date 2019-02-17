# funksjoner

from bin import objekter

def attackMonster(spillerObjekt, monsterObjekt):
	damage = spillerObjekt.playerAttack()
	monsterObjekt.health -= damage

	if spillerObjekt.alive:
		if monsterObjekt.alive:
			if monsterObjekt.health >= 1:
				print("{} hit {} for {} damage! (monster hp: {})".format(spillerObjekt.name, monsterObjekt.name, damage, monsterObjekt.health))
			elif damage >= monsterObjekt.health:
				print("{} hit {} for {} damage! KILLING BLOW! (monster hp: {})".format(spillerObjekt.name, monsterObjekt.name, damage, monsterObjekt.health))
				monsterObjekt.alive = False
		else:
			print("{} is dead!".format(monsterObjekt.name))
	else:
		print("{} is dead and can't attack.".format(spillerObjekt.name))

def monsterAttack(monsterObjekt, spillerObjekt):
	damage = monsterObjekt.monsterAttack()
	spillerObjekt.health -= damage

	if monsterObjekt.alive:
		if spillerObjekt.alive:
			if spillerObjekt.health >= 1:
				print("{} hit {} for {} damage! (player hp: {})".format(monsterObjekt.name, spillerObjekt.name, damage, spillerObjekt.health))
			elif damage >= spillerObjekt.health:
				print("{} hit {} for {} damage! KILLING BLOW! (player hp: {})".format(monsterObjekt.name, spillerObjekt.name, damage, spillerObjekt.health))
				spillerObjekt.alive = False	
		else:
			print("{} is dead!".format(spillerObjekt.name))
	else:
		print("{} is dead and can't attack.".format(monsterObjekt.name))


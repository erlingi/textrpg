import objekter


wep1 = objekter.Weapon("Sword of Kings", 14, 5)
wep2 = objekter.Weapon("Hammer of Doom", 49, 8)
wep3 = objekter.Weapon("Doomshield Hammer", 32, 8)

cons1 = objekter.Consumable("Potion of Health", 50, 2)
cons2 = objekter.Consumable("Potion of Amplified Damage!", 14, 3)
cons3 = objekter.Consumable("Potion of Health", 50, 2)

player1 = objekter.Player("Erling", 100, wep2, 20)
toiletMonster = objekter.Monster("Gorgo", 80, 100)

player1.addInventory(wep1)
player1.addInventory(wep3)
player1.addInventory(cons1)
player1.addInventory(cons2)

toiletMonster.addLoot(cons1)
toiletMonster.addLoot(cons2)
toiletMonster.addLoot(cons3)

rooms = { 
			1: {	"name"		: "Home",
					"east"		: 2,
					"south"		: 3, 
					"monster"	: False}, 

			2: {	"name"		: "Toilet",
					"west"		: 1,
					"south"		: 4,
					"monster"	: True,
					"montype"	: toiletMonster},

			3: {	"name"		: "Bedroom",
					"north"		: 1,
					"monster"	: False},

			4: {	"name"		: "Garden",
					"north"		: 2,
					"monster"	: False}
			}

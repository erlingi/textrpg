import objekter


# these are the weapons available in the game
wep1 = objekter.Weapon("Sword of Light", 14, 5, 1)
wep2 = objekter.Weapon("Hammer of Doom", 49, 8, 2)
wep3 = objekter.Weapon("Doomshield Hammer", 32, 8, 3)

# these are the consumables available in the game
cons1 = objekter.Consumable("Potion of Health", 50, 2)
cons2 = objekter.Consumable("Potion of Amplified Damage!", 14, 3)
cons3 = objekter.Consumable("Potion of Amplified Health!", 50, 2)

# creates placeholder player object
player1 = objekter.Player("name", 100, wep2, 20)
player1.addInventory(wep1)
player1.addInventory(wep3)
player1.addInventory(cons1)
player1.addInventory(cons2)

# character creation
def makeplayer(name):
	player1.name = name
		

# currently the only monster in the game, he resides in the bathroom at waypoint 2
toiletMonster = objekter.Monster("Gorgo", 80, 100)

# adds loot to the monsters inventory
toiletMonster.addLoot(cons1)
toiletMonster.addLoot(cons2)
toiletMonster.addLoot(cons3)


# room map
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

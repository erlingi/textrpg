from bin import mapmodel
from bin import funksjoner


print("******************************************")
print("          \n\nWELCOME TO TEXTRPG\n\n")	
print("******************************************")
funksjoner.gameHelp()


x = raw_input("Character name: ")
mapmodel.makeplayer(x)

while True:
	funksjoner.runtime(mapmodel.player1)




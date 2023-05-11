#George Mi, CS30, April 30th


#Imports for all the different files used
import Map
import Combat
import Tiles

#This function detects if you are on the end tile with the keys, thus winning the game

#Introduction to situation
print(f"{Map.Tile_Descriptions[Map.layout[Map.row][Map.col]]['Description']}\n")
#This will loop the code until they win the game or quit
while Map.Loop == True:
   Tiles.Closet.Get_Key()
   Tiles.Supply_Room.Get_Medkit()
   Combat.combat()
   Map.Move()
   Tiles.End.Win()
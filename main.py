#George Mi, CS30, April 30th


#Imports for all the different files used
import Map
import Tiles

#Introduction to situation
print(f"{Map.Tile_Descriptions[Map.layout[Map.row][Map.col]]['Description']}\n")
#This will loop the code until they win the game or quit
while Map.Loop == True:
   Tiles.Closet.Get_Key()
   Tiles.Supply_Room.Get_Medkit()
   Tiles.Enemy_Tile.Combat1()
   Map.Move()
   print(Map.row)
   print(Map.col)
   Tiles.End_Tile.Win()
import Map
import Inventory
import Enemies
#Class for the Closet tile that contains a function for picking up keys
class Closet():
    def Get_Key():
        if Map.row == 2 and Map.col == 2:
          try:
              choice4 = input("Yes/No\nChoice: ")
              if choice4 == "Yes":
                  Inventory.inventory[1].append("Keys")
                  print("\nYou picked up the keys\n")
                  Inventory.Keys = True
                  Map.Move()
              elif choice4 == "No":
                  print("\nYou did not pick up the keys\n")
                  Map.Move()
          except ValueError:
                  print("That wasn't a valid answer")
                  Closet.Get_Key()
#Class for the Supply room that contains a function for picking up a Medkit
class Supply_Room(Closet):
    def Get_Medkit():
        if Map.row == 0 and Map.col == 1:
            try:
                choice3 = input("Yes/No\nChoice: ")
                if choice3 == "Yes":
                    Inventory.inventory[0].append("Medkit")
                    print("\nYou picked up the Medkit\n")
                    Map.Move()
                elif choice3 == "No":
                    print("\nYou didn't pick up the Medkit\n")
                    Map.Move()
                else:
                    print("\nI didn't understand that")
                    Supply_Room.Get_Medkit()
            except ValueError:
                    print("That wasn't a valid answer")
                    Supply_Room.Get_Medkit()
'''Class for the end tile, contains a funtion that detects if you have the keys
to finish the game'''
class End_Tile():
    def Win():
        if Map.row == 0 and Map.col == 3 and Inventory.Keys == True:
          Map.Loop = False
        elif Map.row == 0 and Map.col == 3 and Inventory.Keys == False:
          print("You find an empty escape pod but there's no key for the ignition")
          Map.Move()
#Class for all enemy tiles that initiats combat when the player is on them
class Enemy_Tile():
    def Combat1():
        if Map.row == 0 and Map.col == 0 or Map.row == 1 and Map.col == 2 
        or Map.row == 2 and Map.col == 3 or Map.row == 3 and Map.col == 2:
            Enemies.Enemy.combat(Enemies.Enemy1)
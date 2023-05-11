import Map
import Inventory
class Closet():
    def Get_Key():
        if Map.row == 2 and Map.col == 2:
          try:
              choice4 = input("Choice: ")
              if choice4 == "Yes":
                  Inventory.inventory.append("Keys")
                  print("\nYou picked up the keys\n")
                  Inventory.Keys = True
                  Map.Move()
              elif choice4 == "No":
                  print("\nYou did not pick up the keys\n")
                  Map.Move()
          except ValueError:
                  print("That wasn't a valid answer")
                  Closet.Get_Key()

class Supply_Room(Closet):
    def Get_Medkit():
        if Map.row == 0 and Map.col == 1:
            try:
                choice3 = input("Choice: ")
                if choice3 == "Yes":
                    Inventory.inventory.append("Medkit")
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
class End():
    def Win():
        if Map.row == 0 and Map.col == 3 and Inventory.Keys == True:
          Map.Loop = False
        elif Map.row == 0 and Map.col == 3 and Inventory.Keys == False:
          print("You find an empty escape pod but there's no key for the ignition")
          Map.Move()
import Map
#Empty list for inventory
inventory = []
#Variable that detects if you have the keys or not
Keys = False
#Nested dictionaries for all of the items in the different rooms
items = {
    "Safe Room" : {
        "Item" : "None" },
    "Starting Room" : {
        "Item" : "None" },
    "Enemy Room" : {
        "Item" : "None" },
    "Supply Room" : {
        "Item" : "Medkit" },
    "Janitor Closet" : {
        "Item" : "Keys" }
    } 
#This function detects if you are in a room with an item and gives the choice to pick it up
def Get_Item():
    global Keys
    if Map.row == 0 and Map.col == 1:
        try:
            choice3 = input("Choice: ")
            if choice3 == "Yes":
                inventory.append("Medkit")
                print("\nYou picked up the Medkit\n")
                Map.Move()
            elif choice3 == "No":
                print("\nYou didn't pick up the Medkit\n")
                Map.Move()
            else:
                print("\nI didn't understand that")
                Get_Item()
        except ValueError:
                print("That wasn't a valid answer")
                Get_Item()
    elif Map.row == 2 and Map.col == 2:
        try:
            choice4 = input("Choice: ")
            if choice4 == "Yes":
                inventory.append("Keys")
                print("\nYou picked up the keys\n")
                Keys = True
                Map.Move()
            elif choice4 == "No":
                print("\nYou did not pick up the keys\n")
                Map.Move()
        except ValueError:
                print("That wasn't a valid answer")
                Get_Item()
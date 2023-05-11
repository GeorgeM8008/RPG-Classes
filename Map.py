import Inventory
import Combat
row = 3
col = 0
Loop = True
#Lists containing layout of the different rooms in the map
layout = [['Enemy Room', 'Supply Room', 'Safe Room', 'Escape Pod'],
          ['Safe Room',  'Safe Room',  'Enemy Room', 'Safe Room'],
          ['Safe Room',  'Safe Room',  'Janitor Closet',  'Enemy Room'],
          ['Starting Room', 'Safe Room', 'Enemy Room', 'Safe Room'],]
#Nested dictionaries describing the rooms and their effects
Tile_Descriptions = {
    "Safe Room" : {
        "Description" : "You enter an empty room",
        "Effect" : "You ponder your next actions" },
    "Starting Room" : {
        "Description" : "You find yourself on an enemy ship and must escape"},
    "Enemy Room" : {
        "Description" : "You enter room and find an alien enemy inside",
        "Effect" : "You prepare yourself for combat" },
    "Escape Pod" : {
        "Description" : "You find a lone escape pod at the end of the ship",
        "Effect" : "You jam the keys you found in the ignition and blast off into space.\n\nYou win!" },
    "Supply Room" : {
        "Description" : "You find a small storage room with a Medkit hanging on the wall",
        "Effect" : "Do you choose to pick it up?" },
    "Janitor Closet" : {
        "Description" : "You find a small janitor's closet with a pair of keys dangling off a key hook",
        "Effect" : "Do you choose to pick it up?",
    }
}
#This function moves the player around based on their input
#This function also detects if a player is trying to go out of bounds and prevents them
def Move():
    global row, col, Loop, inventory, file
    print("Options for action:\nQuit, Move, Inventory, Map\n")    
    choice = input("Action: ")
    if choice == "Quit":
        print("Quitting Game")
        Loop = False
    elif choice == "Move":
        print("Options for movement:\nN, S, E, W\n")
        choice2 = input("Action: ")
        if choice2 == "N":
            if row > 0:
                row -= 1
                print(f"\n{Tile_Descriptions[layout[row][col]]['Description']}")
                print(f"{Tile_Descriptions[layout[row][col]]['Effect']}\n")
            elif row == 0:
                print("\nYou have hit a wall.\n")
        elif choice2 == "S":
            if row < 3:
                row += 1
                print(f"\n{Tile_Descriptions[layout[row][col]]['Description']}")
                print(f"{Tile_Descriptions[layout[row][col]]['Effect']}\n")
            elif row == 3:
                print("\nYou have hit a wall.\n")
        elif choice2 == "W":
            if col > 0:
                col -= 1
                print(f"\n{Tile_Descriptions[layout[row][col]]['Description']}")
                print(f"{Tile_Descriptions[layout[row][col]]['Effect']}\n")
            elif col == 0:
                print("\nYou have hit a wall.\n")
        elif choice2 == "E":
            if col < 3:
                col += 1
                print(f"\n{Tile_Descriptions[layout[row][col]]['Description']}")
                print(f"{Tile_Descriptions[layout[row][col]]['Effect']}\n")
            elif col == 3:
                 print("\nYou have hit a wall.\n")
        elif choice2 == "Quit":
            print("Quitting Game")
            Loop = False
        else:
            print("I didn't understand that\n")

    elif choice == "Inventory":
        if len(Inventory.inventory) == 0:
            print("\nYour inventory is empty\n")
        else:
            for item in Inventory.inventory:
                print(f"\n-{item}\n")
            choiceI = input("Would you like to use anything?")
            if choiceI == "Medkit":
                print("You used the medkit on yourself")
                Combat.combat_stats['Player']['Health'] = 20
                Inventory.inventory.remove("Medkit")
            elif choiceI == "Keys":
                print("You have nothing to use those on")
            elif choiceI == "No":
                print("You didn't use anything")
                Move()
            else:
                print("I didn't understand that")
    elif choice == "Map":
        with open('map.txt') as file:
            contents = file.read()
        print(contents)
    else:
      print("\nI didn't understand that\n")

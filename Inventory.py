
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

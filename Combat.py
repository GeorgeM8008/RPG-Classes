import Map
import Enemies
from Player_Stats import Player
Terrance = Enemies.Enemy('Terrance', 2, 5)
Frank = Enemies.Enemy('Frank', 1, 9)
Steve = Enemies.Enemy('Steve', 6, 5)
Big_Fred = Enemies.Enemy('Big_Fred', 0.05, 100)
def combat():
    if Map.row == 0 and Map.col == 0:
        while Player.health and Terrance.health > 0:
            print("Current health: " + str(Player.health))
            print("Combat Options: Attack\n")
            choicec = input("Action: ") 
            try:
                if choicec == "Attack":
                    print("\nYou deal 4 damage")
                    Terrance.health -= Player.attack
                    if Terrance.health < 1:
                        print("You defeated the enemy\n")
                        break
                else:
                    print("I didn't understand that")
                    combat()
                print("The alien swings and deals 2 damage to you\n")
                Player.health -= Terrance.attack
                if Player.health < 1:
                    print("You have died\nYou lose")
                    break
                    Map.Loop = False
            except ValueError:
                print("That was not a valid answer")
                combat()
    elif Map.row == 1 and Map.col == 2:
        while Player.health > 0 and Frank.health > 0:
            print("Current health: " + str(Player.health))
            print("Combat Options: Attack\n")
            choicec = input("Action: ")
            try:
                if choicec == "Attack":
                        print("\nYou deal 4 damage")
                        Frank.health -= Player.attack
                        if Frank.health < 1:
                            print("You defeated the enemy\n")
                            break
                else:
                    print("I didn't understand that")
                    combat()
                print("The alien swings and deals 1 damage to you\n")
                Player.health -= Frank.attack
                if Player.health < 1:
                    print("You have died\nYou lose")
                    break
                    Map.Loop = False
            except ValueError:
                print("That was not a valid answer")
                combat()  
    elif Map.row == 2 and Map.col == 3:
        while Player.health > 0 and Steve.health > 0:
            print("Current health: " + str(Player.health))
            print("Combat Options: Attack\n")
            choicec = input("Action: ")
            try:
                if choicec == "Attack":
                        print("\nYou deal 4 damage")
                        Steve.health -= Player.attack
                        if Steve.health < 1:
                            print("You defeated the enemy\n")
                            break
                else:
                    print("I didn't understand that")
                    combat()
                print("The alien swings and deals 6 damage to you\n")
                Player.health -= Steve.attack
                if Player.health < 1:
                    print("You have died\nYou lose")
                    break
                    Map.Loop = False
            except ValueError:
                print("That was not a valid answer")
                combat()
    elif Map.row == 3 and Map.col == 2:
        while Player.health > 0 and Big_Fred.health > 0:
            print("Current health: " + str(Player.health))
            print("Combat Options: Attack\n")
            choicec = input("Action: ")
            try:
                if choicec == "Attack":
                        print("\nYou deal 4 damage")
                        Big_Fred.health -= Player.attack
                        if Big_Fred.health < 1:
                            print("You defeated the enemy\n")
                            break
                else:
                    print("I didn't understand that")
                    combat()
                print("The alien swings and deals 0.05 damage to you\n")
                print("It's clear this alien doesn't wish to hurt you yet you continue your attack")
                Player.health -= Big_Fred.attack
                if Player.health == 0:
                    print("You have died\nYou lose")
                    break
                    Map.Loop = False
            except ValueError:
                print("That wasn't a valid answer")
                combat()
import Map
from Player_Stats import Player
class Enemy:
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health
    def combat(self, x, y):
        if Map.row == x and Map.col == y:
            while Player.health > 0 and self.health > 0:
                print("Current health: " + str(Player.health)) 
                print("Combat Options: Attack\n")
                choicec = input("Action: ") 
                try:
                    if choicec == "Attack":
                        print("\nYou deal 3 damage")
                        self.health -= Player.attack
                        if self.health == 0:
                            print("You defeated the enemy\n")
                            break
                    else:
                        print("I didn't understand that")
                        Enemy.combat()
                    print(f"The alien swings and deals str({self.attack}) damage to you\n")
                    Player.health -= self.attack
                    if Player.health == 0:
                        print("You have died\nYou lose")
                        break
                        Map.Loop = False
                except ValueError:
                    print("That was not a valid answer")
                    Enemy.combat()
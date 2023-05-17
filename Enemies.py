import Map
import Player_Stats
class Enemy:
    def __init__(self, attack, health):
        self.attack = 5
        self.health = 5
    def combat(self):
          while Player_Stats.Player1.health > 0 and self.health > 0:
              print("Current health: " + str(Player_Stats.Player1.health)) 
              print("Combat Options: Attack\n")
              choicec = input("Action: ") 
              try:
                  if choicec == "Attack":
                      print("\nYou deal 4 damage")
                      self.health -= Player_Stats.Player1.attack
                      if self.health < 0:
                          print("You defeated the enemy\n")
                          Map.Move()
                  else:
                      print("I didn't understand that")
                      Enemy.combat(self)
                  print("The alien swings and deals " + str(self.attack) + " damage to you\n")
                  Player_Stats.Player1.health -= self.attack
                  if Player_Stats.Player1.health < 0:
                      print("You have died\nYou lose")
                      break
                      Map.Loop = False
              except ValueError:
                  print("That was not a valid answer")
                  Enemy.combat(self)
Enemy1 = Enemy(5, 5)
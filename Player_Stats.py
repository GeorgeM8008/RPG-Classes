#Class containing the attack and health stats of the player character
class Player:
    def __init__(self, attack, health):
        self.attack = attack
        self.health = health
Player1 = Player(4, 20)
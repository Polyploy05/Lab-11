'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/15/26
Group: 15
Description: Creates the troll class that is used in the expert factory
'''





import entity
import random

class Troll(entity.Entity):
    #Creates the troll entity
    def __init__(self):
        super().__init__("Troll", random.randint(10, 14))

    #Creates the attack that does damage to the hero
    def melee_attack(self, enemy):
        damage = random.randint(8, 12)
        enemy.take_damage(damage)
        return f"{self.name} whacks {enemy.name} for {damage} damage!"

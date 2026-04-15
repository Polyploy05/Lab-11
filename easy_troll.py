'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/15/26
Group: 15
Description: Creates the Troll, easy version, that is to be called when the player is in the beginner factory
'''


import entity
import random

class EasyTroll(entity.Entity):
    #Creates the easy troll entity
    def __init__(self):
        super().__init__("Easy Troll", random.randint(6, 9))

    def melee_attack(self, enemy):
        #Creates the attack that does damage to the hero.
        damage = random.randint(5, 9)
        enemy.take_damage(damage)
        return f"{self.name} whacks {enemy.name} for {damage} damage!"

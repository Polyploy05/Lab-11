'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/15/26
Group: 15
Description: Creates the easy version of the ogre that will be implemented into the beginner factory
'''

import entity
import random

class EasyOgre(entity.Entity):
    def __init__(self):
        super().__init__("Easy Ogre", random.randint(7, 8))

    def melee_attack(self, enemy):
        damage = random.randint(5, 8)
        enemy.take_damage(damage)
        return f"{self.name} bashes {enemy.name} for {damage} damage!"

'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/15/26
Group: 15
Description:
'''




import entity
import random

class Ogre(entity.Entity):
    def __init__(self):
        self.name = "Ogre"
        self.hp = random.randint(8, 12)

    def melee_attack(self, enemy):
        damage = random.randint(6, 10)
        enemy.take_damage(damage)
        return f"{self.name} bashes {enemy.name} for {damage} damage!"

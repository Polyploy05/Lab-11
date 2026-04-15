'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/15/26
Group: 15
Description: Creates the easy version of the goblin that is imported into the beginner factory.
'''



import entity
import random

class EasyGoblin(entity.Entity):
    def __init__(self):
        super().__init__("Easy Goblin", random.randint(5, 7))

    def melee_attack(self, enemy):
        damage = random.randint(4, 6)
        enemy.take_damage(damage)
        return f"{self.name} bites {enemy.name} for {damage} damage!"

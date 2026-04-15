'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/15/26
Group: 15
Description:
'''


import entity
import random

class EasyTroll(entity.Entity):
    def __init__(self):
        super().__init__("Easy Troll", random.randint(6, 9))

    def melee_attack(self, enemy):
        damage = random.randint(5, 9)
        enemy.take_damage(damage)
        return f"{self.name} whacks {enemy.name} for {damage} damage!"

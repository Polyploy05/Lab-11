'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/15/26
Group: 15
Description:
'''

import entity
import random

class Hero(entity.Entity):
    def __init__(self, name, health):
        super().__init__(name, health)

    def melee_attack(self, target):
        damage = random.randint(1, 6) + random.randint(1, 6)
        target.take_damage(damage)
        return f"{self.name} attacks {target.name} for {damage} damage!"
        
    def ranged_attack(self, target):
        damage = random.randint(1, 12)
        target.take_damage(damage)
        return f"{self.name} shoots {target.name} for {damage} damage!"

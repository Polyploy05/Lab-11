'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/15/26
Group: 15
Description: Constructor for the hero class. Inherits Entity and implements the melee 
attack method. Also has a ranged attack method that is unique to the hero class.
'''


import entity
import random

class Hero(entity.Entity):
    def __init__(self, name):
        super().__init__(name, 25)

    def melee_attack(self, target):
        #Roll 2d6 for damage. Total damage is done to the enemy and the result is printed
        damage = random.randint(1, 6) + random.randint(1, 6)
        target.take_damage(damage)
        return f"{self.name} attacks {target.name} for {damage} damage!"
        
    def ranged_attack(self, target):
        #Roll 1d12 for damage. Total damage is done to the enemy and the result is printed
        damage = random.randint(1, 12)
        target.take_damage(damage)
        return f"{self.name} shoots {target.name} for {damage} damage!"




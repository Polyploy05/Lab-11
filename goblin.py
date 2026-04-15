'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/15/26
Group: 15
Description: Creates the goblin class that is used in the expert factory.
'''



import entity
import random

class Goblin(entity.Entity):
    #Creates the goblin entity with a random set of hp ranging from 6-10
    def __init__(self):
        super().__init__("Goblin", random.randint(6, 10))
        
    #Creates the attack that does damage to the hero
    def melee_attack(self, enemy):
        damage = random.randint(5, 8)
        enemy.take_damage(damage)
        return f"{self.name} chomps down on {enemy.name} for {damage} damage!"

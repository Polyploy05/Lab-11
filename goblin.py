



import entity
import random

class Goblin(entity.Entity):
    def __init__(self):
        super().__init__("Goblin", random.randint(6, 10))

    def melee_attack(self, enemy):
        damage = random.randint(5, 8)
        enemy.take_damage(damage)
        return f"{self.name} chomps down on {enemy.name} for {damage} damage!"
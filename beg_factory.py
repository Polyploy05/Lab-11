

import random
from enemy_factory import EnemyFactory
from easy_goblin import EasyGoblin
from easy_ogre import EasyOgre
from easy_troll import EasyTroll



class BeginnerFactory(enemy_factory.EnemyFactory):
    def create_random_enemy(self):
        enemies = [EasyGoblin, EasyOgre, EasyTroll]
        chosen_enemy = random.choice(enemies)
        return chosen_enemy
        

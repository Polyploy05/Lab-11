'''

'''

import random
import enemy_factory
import easy_ogre
import easy_goblin
import easy_troll

class BeginnerFactory(enemy_factory.EnemyFactory):
    def create_random_enemy(self):
        enemy_type = random.choice(['easy_ogre', 'easy_goblin', 'easy_troll'])
        if enemy_type == 'easy_ogre':
            return easy_ogre.EasyOgre()
        elif enemy_type == 'easy_goblin':
            return easy_goblin.EasyGoblin()
        elif enemy_type == 'easy_troll':
            return easy_troll.EasyTroll()
        

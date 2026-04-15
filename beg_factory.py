'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/15/26
Group: 15
Description: Creates the beginner factory and imports the goblins, trolls and ogres with their easy version. 
'''

import random
import enemy_factory
import easy_ogre
import easy_goblin
import easy_troll

class BeginnerFactory(enemy_factory.EnemyFactory):
    # Creates the Beginner factory class
    def create_random_enemy(self):
        # Creates the choices for when each enemy can be selected
        enemy_type = random.choice(['easy_ogre', 'easy_goblin', 'easy_troll'])
        if enemy_type == 'easy_ogre':
            return easy_ogre.EasyOgre()
        elif enemy_type == 'easy_goblin':
            return easy_goblin.EasyGoblin()
        elif enemy_type == 'easy_troll':
            return easy_troll.EasyTroll()
        

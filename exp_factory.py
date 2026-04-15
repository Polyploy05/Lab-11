'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/15/26
Group: 15
Description: Creates the expert version of the factory that holds the expert versions of the monsters and returns them at random
'''


import random
import enemy_factory
import ogre
import goblin
import troll

class ExpertFactory(enemy_factory.EnemyFactory):
    def create_random_enemy(self):
        enemy_type = random.choice(['ogre', 'goblin', 'troll'])
        if enemy_type == 'ogre':
            return ogre.Ogre()
        elif enemy_type == 'goblin':
            return goblin.Goblin()
        elif enemy_type == 'troll':
            return troll.Troll()
        

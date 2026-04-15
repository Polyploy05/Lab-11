'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/15/26
Group: 15
Description: Creates the expert version of the factory that holds the expert versions of the monsters and returns them at random
'''



import random
from enemy_factory import EnemyFactory
from goblin import Goblin
from ogre import Ogre
from troll import Troll

class ExpertFactory:
  #Creates the difficult enemies 
  def create_monster(self):
    # Randomly generate and returns a difficult enemy
    enemies = [Goblin, Ogre, Troll]
    chosen_enemy = random.choice(enemies)
    return chosen_enemy()

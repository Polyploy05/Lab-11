



import random

class ExpertFactory:
  #Creates the difficult enemies 
  def create_monster(self):
    # Randomly generate and returns a difficult enemy
    enemies = [Goblin, Ogre, Troll]
    chosen_enemy = random.choice(enemies)
    return chosen_enemy()

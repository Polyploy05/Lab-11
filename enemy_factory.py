'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/15/26
Group: 15
Description: Creates the enemy factory that holds all the enemy factories and creates and returns a random enemy
'''


import abc
class EnemyFactory(abc.ABC):
    #Abstract base class for all the enemy factories 

    @abc.abstractmethod
    def create_random_enemy(self, name, hp):
        #Creates and returns a random enemy
        pass

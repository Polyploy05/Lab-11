'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/15/26
Group: 15
Description:
'''


import abc
class EnemyFactory(abc.ABC):

    @abc.abstractmethod
    def create_random_enemy(self, name, hp):
        pass

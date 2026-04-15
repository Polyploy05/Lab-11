'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/15/26
Group: 15
Description:
'''


import abc

class Entity(abc.ABC):
    def __init__(self, name, hp):
        self._name = name
        self._hp = 25

    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    
    def take_damage(self, damage):
        self._hp -= damage
        if self._hp < 0:
            self._hp = 0  

    def __str__(self):
        return f"{self._name} (HP: {self._hp})"
    
    @abc.abstractmethod
    def melee_attack(self, target):
        pass



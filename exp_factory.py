



import random

class ExpertFactory:
  
  def create_monster(self):
    monster_type = random.choice(["Goblin", "Ogre", "Troll"])

  if monster_type == "Goblin":
    hp = random.randint(6,10)
    dmg = random.randint(5,8)
    return Goblin(hp,dmg)

  elif monster_type == "Ogre":
    hp = random.randint(8,12)
    dmg = random.randint(6,10)
    return Ogre(hp,dmg)

  else:
    hp = random.randint(10,14)
    dmg = random.randint(8,12)
    return Troll(hp,dmg)


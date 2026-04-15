


def main():
    print("Monster Trials")

    #Get user input
    name = input("What is your name?").strip()
    print(f"\nYou will face a series of 3 monsters, {name}.")
    print("Defeat all to win.\n")

    print("Difficult.")
    print("1. Beginner")
    print("2. Expert")
    choice = input().strip()

    #Choose factory
    if choice == "1":
        factory = beg_factory()
    else:
        factory = enemy_factory()

    #Create Hero
    hero = Hero(name)

    #Generate the monsters
    monsters = []
    for _ in range (3):
        monsters.append(factory.create_monsters())

    #Loop the game
    while hero.hp > 0 and len(monsters) > 0: 

        #Display the enemies
        print("\nChoose an enemy to attack:")
        for i in range(len(monsters)):
            print(f"{i+1}.{monsters[i].name} HP: {monsters[i].hp}")

        enemy_choice = int(input("Enter choice:").strip()) - 1
        monster = monsters[enemy_choice]

        #Choose your attack
        print(f"\n{hero.name} HP: {hero.hp}")
        print("1. Sword attack")
        print("2. Arrow attack")
        attack_choice= input("Enter choice: ").strip()

        #Hero Attacks
        if attack_choice == "1":
            result = hero.sword_attack(monster)
        else:
            result = hero.arrow_attack(monster)

        print(result)

        #Is monster dead?
        if monster.hp <= 0:
            print("You have slain the {monster.name}")
            monsters.pop(enemy_choice)
        else:
            #Monster attacks back
            result = monster.attack(hero)
            print(result)
    #End condition
    if hero.hp <= 0:
        print("\nYou have been defeated.")
    else:
        print("\nYou have defeated all the monsters!")
            

if __name__ == "__main__":
    main()

'''
Name: Daniel Puerto & Jacob Miranda
Date: 4/15/26
Group: 15
Description:
'''



import hero
import beg_factory
import exp_factory
import check_input


def main():
    print("Monster Trials")

    #Get user input
    name = input("What is your name? ").strip()
    print(f"\nYou will face a series of 3 monsters, {name}.")
    print("Defeat all to win.\n")

    print("Difficult.")
    print("1. Beginner")
    print("2. Expert")
    choice = check_input.get_int_range("Enter choice: ", 1, 2)

    #Choose factory
    if choice == 1:
        factory = beg_factory.BeginnerFactory()
    else:
        factory = exp_factory.ExpertFactory()

    #Create Hero
    player = hero.Hero(name)

    #Generate the monsters
    monsters = []
    for _ in range (3):
        monsters.append(factory.create_random_enemy())

    #Loop the game
    while player.hp > 0 and len(monsters) > 0: 

        #Display the enemies
        print("\nChoose an enemy to attack:")
        for i in range(len(monsters)):
            print(f"{i+1}.{monsters[i].name} HP: {monsters[i].hp}")

        enemy_choice = check_input.get_int_range("Enter choice: ", 1, len(monsters)) - 1
        monster = monsters[enemy_choice]

        #Choose your attack
        print(f"\n{player.name} HP: {player.hp}")
        print("1. Sword attack")
        print("2. Arrow attack")
        attack_choice = check_input.get_int_range("Enter choice: ", 1, 2)

        #Hero Attacks
        if attack_choice == 1:
            result = player.melee_attack(monster)
        else:
            result = player.ranged_attack(monster)

        print(result)

        #Is monster dead?
        if monster.hp <= 0:
            print(f"You have slain the {monster.name}")
            monsters.pop(enemy_choice)
        else:
            #Monster attacks back
            result = monster.melee_attack(player)
            print(result)

    #End condition
    if player.hp <= 0:
        print("\nYou have been defeated.")
    else:
        print("\nYou have defeated all the monsters!")
            

if __name__ == "__main__":
    main()

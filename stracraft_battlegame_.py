import random

def creating_units(player_dictionary, player_army):
    global player_minerals
    player_units = input("Select the Units that you want to create by typing 1 or 2 ")
    if player_units == "1":
        cr_units = list(player_dictionary)
        cr_cost = list(player_dictionary.values())
        print("You have created one", cr_units[0])
        player_army.append(cr_units[0])
        player_minerals -= cr_cost[0]
        print("Your army:", player_army)
        input()
        if cr_cost[0] > player_minerals:
            print("Not enough minerals!")
            input()
        return (player_minerals)
        
    elif player_units == "2":
        cr_units = list(player_dictionary)
        cr_cost = list(player_dictionary.values())
        print("You have created one", cr_units[1])
        player_army.append(cr_units[1])
        player_minerals -= cr_cost[1]
        print("Your army:", player_army)
        input()
        return (player_minerals)

    else:
        print("Wrong selection, try again")
        input()


def battle():
    
    global player_army
    global computer_army
    global player_minerals
    while len(player_army) or len(computer_army) !=0:
        if len(player_army) == 0:
            print("\nYou have been defeated!")
            player_minerals += 100
            input()
            break
        elif len(computer_army) == 0:
            print("\nThe enemy has been defeated!. Victory!")
            player_minerals += 50
            print("Now you have", player_minerals, "minerals!")
            input()
            return player_minerals
            continue 
        else:
            print("\nYour army:",player_army)
            print("Enemy's army",computer_army)
            attacking_unit = int(input("\nChoose your attack, select the index  of your unit you want to attack: "))
            if attacking_unit > len(player_army):
                print("Unit number not in your army, try again")
                
            else:
                attacking_unit = player_army[attacking_unit-1]
                print("You have selected:", attacking_unit)
            
            print("Enemy's army", computer_army)
            attacked_unit = int(input("\nSelect the index number of the enemy's unit you want to be attacked: "))
            if attacked_unit > len(computer_army):
                print("Unit number not in enemy's army, try again")
                
            else:
                attacked_unit = computer_army[attacked_unit-1]
                print("You have selected to attack:", attacked_unit)
                if attacking_unit == "Dragoon" and attacked_unit == "Hydra":
                    print("\nYour Dragoon wins!")
                    computer_army.remove(attacked_unit)
                    input()
                    
                elif attacking_unit == "Zealot" and attacked_unit == "Zerling":
                    print("\nYour Zealot wins!")
                    computer_army.remove(attacked_unit)
                    input()
                    
                elif attacking_unit == "Vulture" and attacked_unit == "Zealot":
                    print("\nYour Vulture wins!")
                    computer_army.remove(attacked_unit)
                    input()
                    
                elif attacking_unit == "Marine" and attacked_unit == "Dragoon":
                    print("\nYour Marine wins!")
                    computer_army.remove(attacked_unit)
                    input()
                    
                elif attacking_unit == "Zerling" and attacked_unit == "Dragoon":
                    print("\nYour Zerling wins!")
                    computer_army.remove(attacked_unit)
                    input()
                    
                elif attacking_unit == "Zerling" and attacked_unit == "Vulture":
                    print("\nYour Zerling wins!")
                    computer_army.remove(attacked_unit)
                    input()
                   
                elif attacking_unit == "Hydra" and attacked_unit == "Marine":
                    print("\nYour Hydra wins!")
                    computer_army.remove(attacked_unit)
                    input()
                        
                else:
                    print("\nYour", attacking_unit, "loses!")   
                    player_army.remove(attacking_unit) 
                    input()
            
                
            print("\nIs the enemy turn")
            if "Hydra" in computer_army and "Zealot" in player_army:
                player_army.remove("Zealot")
                print("The Hydra kills your Zealot")
                input()
                continue
            elif "Zerling" in computer_army and "Dragoon" in player_army:
                player_army.remove("Dragoon")
                print("The Zerling kills your Dragoon")
                input()
                continue
            elif "Zealot" in computer_army and "Marine" in player_army:
                player_army.remove("Marine")
                print("The Zealot kills your Marine")
                input()
                continue
            elif "Marine" in computer_army and "Zerling" in player_army:
                player_army.remove("Zerling")
                print("The Marine kills your Zerling")
                input()
            elif "Dragoon" in computer_army and "Vulture" in player_army:
                player_army.remove("Vulture")
                print("The Dragoon kills your Vulture")
                input()
                continue
            elif "Vulture" in computer_army and "Hydra" in player_army:
                player_army.remove("Hydra")
                print("The Vulture kills your Hydra")
                input()
                continue
            else:
                print("The computer cannot attack!")
                input()
                continue
            

protoss_dic = {"Zealot": 25, "Dragoon": 50}
terran_dic = {"Marine": 25, "Vulture": 50}
zerg_dic = {"Zerling": 25, "Hydra": 50}
player_army = []
computer_choice = [protoss_dic, terran_dic, zerg_dic]
computer_army = []
player_minerals = 100   


while True: 
    

    print("\n- Welcome to StarCraft Battle Game - ")

    player_team = input("""Please choose your team:
    1) Protoss
    2) Zerg
    3) Terran
    """)
    while True: 
        if player_team == "1" or player_team.lower() == "protoss":
            while player_minerals > 0:
                computer_army = random.choices(list(computer_choice[2]), k=3)
                print("\nYou selected Protoss. You currently have", player_minerals, "minerals.")
                print("\nYou can create the following units:", protoss_dic)
                creating_units(protoss_dic, player_army)
                print(computer_army)
                
        elif player_team == "2" or player_team.lower() == "zerg":
            while player_minerals > 0:
                computer_army = random.choices(list(computer_choice[1]), k=3)
                print("\nYou selected Zergs. You currently have", player_minerals, "minerals.")
                print("\nYou can create the following units:", zerg_dic)
                creating_units(zerg_dic, player_army)
                print(computer_army)
        elif player_team == "3" or player_team.lower() == "terran":
            while player_minerals > 0:
                computer_army = random.choices(list(computer_choice[0]), k=3)
                print("\nYou selected Terran. You currently have", player_minerals, "minerals.")
                print("\nYou can create the following units:", terran_dic)
                creating_units(terran_dic, player_army)
                print(computer_army)
        print("\nYou have ran out of minerals. It's time for the battle, are you ready?")
        battle_choice = input("Y/N")
        if battle_choice.lower() == "n":
            quit()
        else:
            player_life = len(player_army)
            computer_life = len(computer_army)
            battle()
            
                


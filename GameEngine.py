import random
import time

the_world = [
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"], 
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"], 
        ["--", "--", "--", "--", "--", "--", "--", "--"], 
        ["--", "--", "--", "--", "--", "--", "--", "--"] 
    ]

# muuta jokkoe listat sanakirjaksi missä avain on nimi? ja siitä sitten jaotellaan ja ylläpidetään
r_id_character_list = [] # red team
g_id_character_list = [] # green team
all_character_list = []
r_id_win = False
g_id_win = False
turn_counter = 1




#printtaa theWorld:n rivit erikseen
def printing_the_world(): 
    loopCounter = 0
    for row in the_world:
        for cell in row:
            if loopCounter < 8:
                print(cell, end=" ")
                loopCounter += 1
                if loopCounter == 8:
                    print("\n")
                    loopCounter = 0

 # Tekee muuttujan verran esteitä theWorld:iin   
def making_obstacles(amount):
    if amount < 10 and amount > 1:
        howManyObstacle = amount
    i = 0
    while i < howManyObstacle:
        while True:
            random_row = random.randint(2, 5)
            random_cell = random.randint(1, 6)
            if the_world[random_row][random_cell] == "--":
                the_world[random_row][random_cell] = "XX"
                break
        i += 1

def start_menu():
    print()
    print("** Welcome to the world of gladiators **")
    print()
    print()
    print()
    print("* Start *")
    print("* Help *")
    print("* Quit *")
    print()
    player_input = input(" Choose what to do: ")
    return player_input

class bowman:
    character_movement = 1
    def __init__(self, name, id):
        self.name = name
        self.id = id # käytetään deploy kohdassa, R ja G
        self.position = ""
        self.character_hp = random.randint(6, 10)
        self.character_mp = random.randint(0, 0)
        if self.id == "RB":
            r_id_character_list.append(self.id)
        elif self.id == "GB":
            g_id_character_list.append(self.id)
        #all_character_list.append(f"{self.name}_{self.id}") ei toimi tolla muuttujalla .name + .id
        if id[0] == "R":
            while True:
                row = random.randint(0, 1)
                cell = random.randint(1, 6)
                if the_world[row][cell] == "--":
                    the_world[row][cell] = id
                    self.position = (row, cell)
                    break        
        if id[0] == "G":
            while True:
                row = random.randint(6, 7)
                cell = random.randint(1, 6)
                if the_world[row][cell] == "--":
                    the_world[row][cell] = id
                    self.position = (row, cell)
                    break        
    def melee_attack(self):
        #katso joku ruutu ja tee siihen dmg
        self.character_melee_dmg = random.randint(1, 1)
        print("hello my name is " + self.name)
    def ranged_attack(self):
        #katso joku ruutu ja tee siihen dmg
        self.character_range_dmg = random.randint(1, 5)
        print("hello my name is " + self.name)


class swordman:
    character_movement = 1
    # kutsu tätä XX = swordman(xx, .., xx)
    def __init__(self, name, id ):
        self.name = name
        self.id = id # käytetään deploy kohdassa, R ja G
        self.position = ""
        self.character_hp = random.randint(8, 15)
        self.character_mp = random.randint(0, 0)
        if self.id == "RS":
            r_id_character_list.append(self.id)
        elif self.id == "GS":
            g_id_character_list.append(self.id)  
        #all_character_list.append(f"{self.name}_{self.id}") ei toimi tolla muuttujalla .name + .id
        if id[0] == "R":
            while True:
                row = random.randint(0, 1)
                cell = random.randint(1, 6)
                if the_world[row][cell] == "--":
                    the_world[row][cell] = id
                    self.position = (row, cell)
                    break        
        if id[0] == "G":
            while True:
                row = random.randint(6, 7)
                cell = random.randint(1, 6)
                if the_world[row][cell] == "--":
                    the_world[row][cell] = id
                    self.position = (row, cell)
                    break  
    def melee_attack(self):
        #katso joku ruutu ja tee siihen dmg
        self.character_melee_dmg = random.randint(2, 5)
        print("hello my name is " + self.name)

def enemy_melee_attack(enemy_hahmo, player_hahmo_id):
    print(f"{enemy_hahmo.name} is preparing for an attack ")
    player_character_to_get_hit = ""
    position_in_list = 0
    osuma_listalta = 0
    hit_chance_list = [1, 2, 3, 4, 5]
    hit_chance = random.choice(hit_chance_list)

    for character in kaikki_hahmot:
        if player_hahmo_id in character.id:
            player_character_to_get_hit = kaikki_hahmot[position_in_list]
            osuma_listalta = position_in_list
            print(f"tulee osumaan: {player_character_to_get_hit.id}")
            break
        position_in_list += 1
    if enemy_hahmo.id == "RS":
        if hit_chance == 1:
            print(f"So close, but {player_character_to_get_hit.id} dodges gracefully")
        if hit_chance != 1:
            print(f"pelaajan hahmon hp ennen: {kaikki_hahmot[osuma_listalta].character_hp}")
            kaikki_hahmot[osuma_listalta].character_hp -= random.randint(2, 5)
            print(f"pelaajan hahmon hp jälkeen: {kaikki_hahmot[osuma_listalta].character_hp}")
    if enemy_hahmo.id == "RB":
        if hit_chance == 1:
            print(f"So close, but {player_character_to_get_hit.id} dodges gracefully")
        if hit_chance != 1:
            print(f"pelaajan hahmon hp ennen: {kaikki_hahmot[osuma_listalta].character_hp}")
            kaikki_hahmot[osuma_listalta].character_hp -= random.randint(1, 1)
            print(f"pelaajan hahmon hp jälkeen: {kaikki_hahmot[osuma_listalta].character_hp}")
    #JEE TOIMII, vähentää pelaajan hp :D ja 20% dodge chance tällähetkellä

def player_melee_attack(player_hahmo_og, enemy_hahmo_id):
    print(f"{player_hahmo_og.id} is preparing for an attack ")
    enemy_character_to_get_hit = ""
    position_in_list = 0
    osuma_listalta = 0
    hit_chance_list = [1, 2, 3, 4, 5]
    hit_chance = random.choice(hit_chance_list)

    for character in kaikki_hahmot:
        if enemy_hahmo_id in character.id:
            enemy_character_to_get_hit = kaikki_hahmot[position_in_list]
            osuma_listalta = position_in_list
            break
        position_in_list += 1
    # swordman tekee 2-5dmg ja bowman 1-1dmg
    if player_hahmo_og.id == "GS":
        if hit_chance == 1:
            print(f"So close, but {enemy_character_to_get_hit.id} dodges by fubbling to the ground face first")
        if hit_chance != 1:
            print(f"tietokoneen hahmon hp ennen: {kaikki_hahmot[osuma_listalta].character_hp}")
            kaikki_hahmot[osuma_listalta].character_hp -= random.randint(2, 5)
            print(f"tietokoneen hahmon hp jälkeen: {kaikki_hahmot[osuma_listalta].character_hp}")
    if player_hahmo_og.id == "GB":
        if hit_chance == 1:
            print(f"So close, but {enemy_character_to_get_hit.id} dodges by fumbling to the ground face first")
        if hit_chance != 1:
            print(f"tietokoneen hahmon hp ennen: {kaikki_hahmot[osuma_listalta].character_hp}")
            kaikki_hahmot[osuma_listalta].character_hp -= random.randint(1, 1)
            print(f"tietokoneen hahmon hp jälkeen: {kaikki_hahmot[osuma_listalta].character_hp}")

def player_ranged_attack(player_hahmo_og):
    enemy_character_to_get_hit = ""
    position_in_list = 0
    osuma_listalta = 0
    hit_chance_list = [1, 2, 3, 4, 5]
    hit_chance = random.choice(hit_chance_list)
    
    while True:
        enemy_to_take_damage_input = input("Choose an enemy to shoot an arrow: ")
        if enemy_to_take_damage_input.upper() == "RS":
            for character in kaikki_hahmot:
                if enemy_to_take_damage_input in character.id:
                    enemy_character_to_get_hit = kaikki_hahmot[position_in_list]
                    osuma_listalta = position_in_list
                    break
                position_in_list += 1  
            if hit_chance == 1 or hit_chance == 2:
                print(f"The arrow flies, but {kaikki_hahmot[osuma_listalta].id} uses afterimage")
            else:
                print(f"tietokoneen hahmon hp ennen: {kaikki_hahmot[osuma_listalta].character_hp}")
                kaikki_hahmot[osuma_listalta].character_hp -= random.randint(1, 5)
                print(f"tietokoneen hahmon hp jälkeen: {kaikki_hahmot[osuma_listalta].character_hp}")
            break
        if enemy_to_take_damage_input.upper() == "RB":
            for character in kaikki_hahmot:
                if enemy_to_take_damage_input in character.id:
                    enemy_character_to_get_hit = kaikki_hahmot[position_in_list]
                    osuma_listalta = position_in_list
                    break
                position_in_list += 1  
            if hit_chance == 1 or hit_chance == 2:
                print(f"The arrow flies, but {kaikki_hahmot[osuma_listalta].id} uses afterimage")
            else:
                print(f"tietokoneen hahmon hp ennen: {kaikki_hahmot[osuma_listalta].character_hp}")
                kaikki_hahmot[osuma_listalta].character_hp -= random.randint(1, 5)
                print(f"tietokoneen hahmon hp jälkeen: {kaikki_hahmot[osuma_listalta].character_hp}")
            break
        else:
            print("Beep Try again!")



def create_characters():
    swordman_RS = swordman("swordman", "RS")
    swordman_GS = swordman("swordman", "GS")
    bowman_RB = bowman("bowman", "RB")
    bowman_GB = bowman("bowman", "GB")

# funktio mikä sijoittaa ukkelit kartalle riippuen kumpi joukkoe. Tällä hetkellä deploy on classissa jo mukana
def deploy_character():
    # R joukkoe ylös, G joukkoe alas
    for x in r_id_character_list:
        if x[0] == "R":
            while True:
                row = random.randint(0, 1)
                cell = random.randint(1, 6)
                if the_world[row][cell] == "--":
                    the_world[row][cell] = x
                    #if x == "RS":
                     #   f"swordman_{x}".position = the_world[row][cell]
                    #if x == "RB":
                    #    f"bowman_{x}".position = the_world[row][cell]
                    break
        if x[0] == "G":
            while True:
                row = random.randint(6, 7)
                cell = random.randint(1, 6)
                if the_world[row][cell] == "--":
                    the_world[row][cell] = x
                    if x == "GS":
                        f"swordman_{x}".position = the_world[row][cell]
                    else:
                        f"bowman_{x}".position = the_world[row][cell]
                    break        
    for x in g_id_character_list:
        if x[0] == "R":
            while True:
                row = random.randint(0, 1)
                cell = random.randint(1, 6)
                if the_world[row][cell] == "--":
                    the_world[row][cell] = x
                    if x == "RB":
                        f"swordman_{x}".position = the_world[row][cell]
                    else:
                        f"bowman_{x}".position = the_world[row][cell]
                    break
        if x[0] == "G":
            while True:
                row = random.randint(6, 7)
                cell = random.randint(1, 6)
                if the_world[row][cell] == "--":
                    the_world[row][cell] = x
                    #if x == "GB":
                    #    f"swordman_{x}".position = the_world[row][cell]
                    #else:
                    #    f"bowman_{x}".position = the_world[row][cell]
                    break
    
def vicinity_check(hahmo):
    character_close = False
    current_position_row = hahmo.position[0]
    current_position_column = hahmo.position[1]
    if current_position_row != 0:
        check_beginning_row = current_position_row - 1
    else:
        check_beginning_row = current_position_row
    if current_position_column != 0:
        check_beginning_column = current_position_column - 1
    else:
        check_beginning_column = current_position_column

    if (check_beginning_row + 2) > 7:
        limiter_row = 7
    else:
        limiter_row = check_beginning_row + 2
    if (check_beginning_column + 2) > 7:
        limiter_column = 7
    else:
        limiter_column = check_beginning_column + 2       

    while check_beginning_row <= limiter_row and character_close == False:
        while check_beginning_column <= limiter_column:
            if the_world[check_beginning_row][check_beginning_column] == "RS":
                character_close = True
                return character_close
            if the_world[check_beginning_row][check_beginning_column] == "RB":
                character_close = True
                return character_close
            check_beginning_column += 1   
        check_beginning_row += 1
        check_beginning_column = limiter_column - 2 
    return character_close

def movement(hahmo):
    current_position_row = hahmo.position[0]
    current_position_column = hahmo.position[1]

    # nuolet joka suuntaan näppäimillä: Q W E D C X Z A
    # pitää vielä chekata ettei mene kentän yli tai ali tai ei ole XX
    is_enemy_adjacent = vicinity_check(hahmo)
    while True:
        player_movement_input = input("Choose where to move: ")
        if player_movement_input.upper() == "B":
            if hahmo.id == "GB":
                if is_enemy_adjacent == False:
                    player_ranged_attack(hahmo)
                    break 
                else:
                    print("There is a enemy besides you, so hit him!")
                    continue
            else:
                print("You don't have a bow!")
                continue
        if player_movement_input.upper() == "Q":
            if the_world[current_position_row-1][current_position_column-1] == "RS":
                enemy_character_to_take_damage = "RS"
                player_melee_attack(hahmo, enemy_character_to_take_damage)
                break
            if the_world[current_position_row-1][current_position_column-1] == "RB":
                enemy_character_to_take_damage = "RB"
                player_melee_attack(hahmo, enemy_character_to_take_damage)
                break
            if the_world[current_position_row-1][current_position_column-1] == "--":
                #do it eli saa liikkua
                the_world[current_position_row-1][current_position_column-1] = hahmo.id
                hahmo.position = (current_position_row-1, current_position_column-1)
                the_world[current_position_row][current_position_column] = "--"
                break
            if the_world[current_position_row-1][current_position_column-1] == "XX":
                print(f"Illegal move, please try again")
            if the_world[current_position_row-1][current_position_column-1] == "GS" or the_world[current_position_row-1][current_position_column-1] == "GB":
                print("You hug your teammate and continue")

                

        if player_movement_input.upper() == "W":
            if the_world[current_position_row-1][current_position_column] == "RS":
                enemy_character_to_take_damage = "RS"
                player_melee_attack(hahmo, enemy_character_to_take_damage)
                break
            if the_world[current_position_row-1][current_position_column] == "RB":
                enemy_character_to_take_damage = "RB"
                player_melee_attack(hahmo, enemy_character_to_take_damage)
                break
            if the_world[current_position_row-1][current_position_column] == "--":
                the_world[current_position_row-1][current_position_column] = hahmo.id
                hahmo.position = (current_position_row-1, current_position_column)
                the_world[current_position_row][current_position_column] = "--"
                break
            if the_world[current_position_row-1][current_position_column] == "XX":
                print(f"Illegal move, please try again")
            if the_world[current_position_row-1][current_position_column] == "GS" or the_world[current_position_row-1][current_position_column] == "GB":
                print("You hug your teammate and continue")

        if player_movement_input.upper() == "E":
            if the_world[current_position_row-1][current_position_column+1] == "RS":
                enemy_character_to_take_damage = "RS"
                player_melee_attack(hahmo, enemy_character_to_take_damage)
                break
            if the_world[current_position_row-1][current_position_column+1] == "RB":
                enemy_character_to_take_damage = "RB"
                player_melee_attack(hahmo, enemy_character_to_take_damage)
                break
            if the_world[current_position_row-1][current_position_column+1] == "--":
                the_world[current_position_row-1][current_position_column+1] = hahmo.id
                hahmo.position = (current_position_row-1, current_position_column+1)
                the_world[current_position_row][current_position_column] = "--"
                break
            if the_world[current_position_row-1][current_position_column+1] == "XX":
                print(f"Illegal move, please try again")
            if the_world[current_position_row-1][current_position_column+1] == "GS" or the_world[current_position_row-1][current_position_column+1] == "GB":
                print("You hug your teammate and continue")

        if player_movement_input.upper() == "D":
            if the_world[current_position_row][current_position_column+1] == "RS":
                enemy_character_to_take_damage = "RS"
                player_melee_attack(hahmo, enemy_character_to_take_damage)
                break
            if the_world[current_position_row][current_position_column+1] == "RB":
                enemy_character_to_take_damage = "RB"
                player_melee_attack(hahmo, enemy_character_to_take_damage)
                break
            if the_world[current_position_row][current_position_column+1] == "--":
                the_world[current_position_row][current_position_column+1] = hahmo.id
                hahmo.position = (current_position_row, current_position_column+1)
                the_world[current_position_row][current_position_column] = "--"
                break
            if the_world[current_position_row][current_position_column+1] == "XX":
                print(f"Illegal move, please try again")
            if the_world[current_position_row][current_position_column+1] == "GS" or the_world[current_position_row][current_position_column+1] == "GB":
                print("You hug your teammate and continue")
      
        if player_movement_input.upper() == "C":
            if the_world[current_position_row+1][current_position_column+1] == "RS":
                enemy_character_to_take_damage = "RS"
                player_melee_attack(hahmo, enemy_character_to_take_damage)
                break
            if the_world[current_position_row+1][current_position_column+1] == "RB":
                enemy_character_to_take_damage = "RB"
                player_melee_attack(hahmo, enemy_character_to_take_damage)
                break
            if the_world[current_position_row+1][current_position_column+1] == "--":
                the_world[current_position_row+1][current_position_column+1] = hahmo.id
                hahmo.position = (current_position_row+1, current_position_column+1)
                the_world[current_position_row][current_position_column] = "--"
                break
            if the_world[current_position_row+1][current_position_column+1] == "XX":
                print(f"Illegal move, please try again")
            if the_world[current_position_row+1][current_position_column+1] == "GS" or the_world[current_position_row+1][current_position_column+1] == "GB":
                print("You hug your teammate and continue")

        if player_movement_input.upper() == "X":
            if the_world[current_position_row+1][current_position_column] == "RS":
                enemy_character_to_take_damage = "RS"
                player_melee_attack(hahmo, enemy_character_to_take_damage)
                break
            if the_world[current_position_row+1][current_position_column] == "RB":
                enemy_character_to_take_damage = "RB"
                player_melee_attack(hahmo, enemy_character_to_take_damage)
                break
            if the_world[current_position_row+1][current_position_column] == "--":
                the_world[current_position_row+1][current_position_column] = hahmo.id
                hahmo.position = (current_position_row+1, current_position_column)
                the_world[current_position_row][current_position_column] = "--"
                break
            if the_world[current_position_row+1][current_position_column] == "XX":
                print(f"Illegal move, please try again")
            if the_world[current_position_row+1][current_position_column] == "GS" or the_world[current_position_row+1][current_position_column] == "GB":
                print("You hug your teammate and continue")

        if player_movement_input.upper() == "Z":
            if the_world[current_position_row+1][current_position_column-1] == "RS":
                enemy_character_to_take_damage = "RS"
                player_melee_attack(hahmo, enemy_character_to_take_damage)
                break
            if the_world[current_position_row+1][current_position_column-1] == "RB":
                enemy_character_to_take_damage = "RB"
                player_melee_attack(hahmo, enemy_character_to_take_damage)
                break
            if the_world[current_position_row+1][current_position_column-1] == "--":
                the_world[current_position_row+1][current_position_column-1] = hahmo.id
                hahmo.position = (current_position_row+1, current_position_column-1)
                the_world[current_position_row][current_position_column] = "--"
                break
            if the_world[current_position_row+1][current_position_column-1] == "XX":
                print(f"Illegal move, please try again")
            if the_world[current_position_row+1][current_position_column-1] == "GS" or the_world[current_position_row+1][current_position_column-1] == "GB":
                print("You hug your teammate and continue")

        if player_movement_input.upper() == "A":
            if the_world[current_position_row][current_position_column-1] == "RS":
                enemy_character_to_take_damage = "RS"
                player_melee_attack(hahmo, enemy_character_to_take_damage)
                break
            if the_world[current_position_row][current_position_column-1] == "RB":
                enemy_character_to_take_damage = "RB"
                player_melee_attack(hahmo, enemy_character_to_take_damage)
                break
            if the_world[current_position_row][current_position_column-1] == "--":
                the_world[current_position_row][current_position_column-1] = hahmo.id
                hahmo.position = (current_position_row, current_position_column-1)
                the_world[current_position_row][current_position_column] = "--"
                break
            if the_world[current_position_row][current_position_column-1] == "XX":
                print(f"Illegal move, please try again")
            if the_world[current_position_row][current_position_column-1] == "GS" or the_world[current_position_row][current_position_column-1] == "GB":
                print("You hug your teammate and continue")

        if player_movement_input.upper() == "S":
            print("You highfive yourself and continue")


# chekki jos jokin ympäröivä ruutu on vihollinen, ja hyökkää tai ampuu bowilla
def computer_attack_check(hahmo):
    has_attacked = False
    current_position_row = hahmo.position[0]
    current_position_column = hahmo.position[1]
    if current_position_row != 0:
        check_beginning_row = current_position_row - 1
    else:
        check_beginning_row = current_position_row
    if current_position_column != 0:
        check_beginning_column = current_position_column - 1
    else:
        check_beginning_column = current_position_column

    if (check_beginning_row + 2) > 7:
        limiter_row = 7
    else:
        limiter_row = check_beginning_row + 2
    if (check_beginning_column + 2) > 7:
        limiter_column = 7
    else:
        limiter_column = check_beginning_column + 2       
    print(check_beginning_row)
    print(check_beginning_column)

    # tähän saa loopin mikä chekkaa onko mikään ympäröivistä vihollinen . TOIMII muuten paitsi jos ukkeli on 0 tai 7 rivillä nii käy koko loopin läpi
    while check_beginning_row <= limiter_row and has_attacked == False:
        while check_beginning_column <= limiter_column:
            if the_world[check_beginning_row][check_beginning_column] == "GS":
                #if yes,do damage
                player_character_to_take_damage = "GS"
                enemy_melee_attack(hahmo, player_character_to_take_damage)
                has_attacked = True
                print("AI hyökkäsi ihmisen kimppuun!")
                break
            if the_world[check_beginning_row][check_beginning_column] == "GB":
                #if yes,do damage
                player_character_to_take_damage = "GB"
                enemy_melee_attack(hahmo, player_character_to_take_damage)
                has_attacked = True
                print("AI hyökkäsi ihmisen kimppuun!")
                break
            print(f"{check_beginning_row}, {check_beginning_column}")
            check_beginning_column += 1   
        check_beginning_row += 1
        check_beginning_column = limiter_column - 2 
    return has_attacked     

def computer_ranged_attack(hahmo):
    position_in_list = 0
    osuma_listalta = 0
    hit_chance_list = [1, 2, 3, 4, 5]
    hit_chance = random.choice(hit_chance_list)
    player_character_to_hit_list = ["GB", "GS"]
    player_character_to_hit = random.choice(player_character_to_hit_list)

    if hahmo.id == "RS":
        return False
    
    while True:
        if player_character_to_hit.upper() == "GS":
            for character in kaikki_hahmot:
                if player_character_to_hit in character.id:
                    player_character_to_hit = kaikki_hahmot[position_in_list]
                    osuma_listalta = position_in_list
                    break
                position_in_list += 1  
            if hit_chance == 1 or hit_chance == 2:
                print(f"The arrow flies, but {kaikki_hahmot[osuma_listalta].id} uses afterimage")
            else:
                print(f"{kaikki_hahmot[osuma_listalta].id} hahmon hp ennen: {kaikki_hahmot[osuma_listalta].character_hp}")
                kaikki_hahmot[osuma_listalta].character_hp -= random.randint(1, 5)
                print(f"{kaikki_hahmot[osuma_listalta].id} hahmon hp jälkeen: {kaikki_hahmot[osuma_listalta].character_hp}")
            break
        if player_character_to_hit.upper() == "GB":
            for character in kaikki_hahmot:
                if player_character_to_hit in character.id:
                    player_character_to_hit = kaikki_hahmot[position_in_list]
                    osuma_listalta = position_in_list
                    break
                position_in_list += 1  
            if hit_chance == 1 or hit_chance == 2:
                print(f"The arrow flies, but {kaikki_hahmot[osuma_listalta].id} uses afterimage")
            else:
                print(f"{kaikki_hahmot[osuma_listalta].id} hahmon hp ennen: {kaikki_hahmot[osuma_listalta].character_hp}")
                kaikki_hahmot[osuma_listalta].character_hp -= random.randint(1, 5)
                print(f"{kaikki_hahmot[osuma_listalta].id} hahmon hp jälkeen: {kaikki_hahmot[osuma_listalta].character_hp}")
            break
    return True


def computer_move(hahmo):
    current_position_row = hahmo.position[0]
    current_position_column = hahmo.position[1]
    movement_options_computer = ["Z", "X", "C"]

    #print(computer_movement_input)
    # nuolet joka suuntaan näppäimillä: Q W E D C X Z A
    # pitää vielä chekata ettei mene kentän yli tai ali

    computer_melee_attacked_this_turn = computer_attack_check(hahmo) # Melee hyökkäys ennen liikkumista
    print(f"Has computer melee attacked this turn? {computer_melee_attacked_this_turn}")

    if computer_melee_attacked_this_turn == False:
        computer_range_attacked_this_turn = computer_ranged_attack(hahmo)
        print(f"Has computer range attacked this turn? {computer_range_attacked_this_turn}")
    else: 
        computer_range_attacked_this_turn = False

    if computer_melee_attacked_this_turn == False and computer_range_attacked_this_turn == False:
        while True:
            computer_movement_input = random.choice(movement_options_computer)
            if computer_movement_input == "Q":
                if the_world[current_position_row-1][current_position_column-1] == "--":
                    the_world[current_position_row-1][current_position_column-1] = hahmo.id
                    hahmo.position = (current_position_row-1, current_position_column-1)
                    the_world[current_position_row][current_position_column] = "--"
                    print("tietokone liikkui : Q")
                    break
                if the_world[current_position_row-1][current_position_column-1] == "XX":
                    print(f"Computer runs to a tree, my oh my")
                if the_world[current_position_row-1][current_position_column-1] == "RS" or the_world[current_position_row-1][current_position_column-1] == "RB":
                    print("AI slaps it's teammate and continues")

            if computer_movement_input == "W":
                if the_world[current_position_row-1][current_position_column] == "--":
                    the_world[current_position_row-1][current_position_column] = hahmo.id
                    hahmo.position = (current_position_row-1, current_position_column)
                    the_world[current_position_row][current_position_column] = "--"
                    print("tietokone liikkui : W")
                    break
                if the_world[current_position_row-1][current_position_column] == "XX":
                    print(f"Computer runs to a tree, my oh my")
                if the_world[current_position_row-1][current_position_column] == "RS" or the_world[current_position_row-1][current_position_column] == "RB":
                    print("AI slaps it's teammate and continues")

            if computer_movement_input == "E":
                if the_world[current_position_row-1][current_position_column+1] == "--":
                    the_world[current_position_row-1][current_position_column+1] = hahmo.id
                    hahmo.position = (current_position_row-1, current_position_column+1)
                    the_world[current_position_row][current_position_column] = "--"
                    print("tietokone liikkui : E")
                    break
                if the_world[current_position_row-1][current_position_column+1] == "XX":
                    print(f"Computer runs to a tree, my oh my")
                if the_world[current_position_row-1][current_position_column+1] == "RS" or the_world[current_position_row-1][current_position_column+1] == "RB":
                    print("AI slaps it's teammate and continues")

            if computer_movement_input == "D":
                if the_world[current_position_row][current_position_column+1] == "--":
                    the_world[current_position_row][current_position_column+1] = hahmo.id
                    hahmo.position = (current_position_row, current_position_column+1)
                    the_world[current_position_row][current_position_column] = "--"
                    print("tietokone liikkui : D")
                    break
                if the_world[current_position_row][current_position_column+1] == "XX":
                    print(f"Computer runs to a tree, my oh my")
                if the_world[current_position_row][current_position_column+1] == "RS" or the_world[current_position_row][current_position_column+1] == "RB":
                    print("AI slaps it's teammate and continues")
      
            if computer_movement_input == "C":
                if the_world[current_position_row+1][current_position_column+1] == "--":
                    the_world[current_position_row+1][current_position_column+1] = hahmo.id
                    hahmo.position = (current_position_row+1, current_position_column+1)
                    the_world[current_position_row][current_position_column] = "--"
                    print("tietokone liikkui : C")
                    break
                if the_world[current_position_row+1][current_position_column+1] == "XX":
                    print(f"Computer runs to a tree, my oh my")
                if the_world[current_position_row+1][current_position_column+1] == "RS" or the_world[current_position_row+1][current_position_column+1] == "RB":
                    print("AI slaps it's teammate and continues")

            if computer_movement_input == "X":
                if the_world[current_position_row+1][current_position_column] == "--":
                    the_world[current_position_row+1][current_position_column] = hahmo.id
                    hahmo.position = (current_position_row+1, current_position_column)
                    the_world[current_position_row][current_position_column] = "--"
                    print("tietokone liikkui : X")
                    break
                if the_world[current_position_row+1][current_position_column] == "XX":
                    print(f"Computer runs to a tree, my oh my")
                if the_world[current_position_row+1][current_position_column] == "RS" or the_world[current_position_row+1][current_position_column] == "RB":
                    print("AI slaps it's teammate and continues")

            if computer_movement_input == "Z":
                if the_world[current_position_row+1][current_position_column-1] == "--":
                    the_world[current_position_row+1][current_position_column-1] = hahmo.id
                    hahmo.position = (current_position_row+1, current_position_column-1)
                    the_world[current_position_row][current_position_column] = "--"
                    print("tietokone liikkui : Z")
                    break
                if the_world[current_position_row+1][current_position_column-1] == "XX":
                    print(f"Computer runs to a tree, my oh my")
                if the_world[current_position_row+1][current_position_column-1] == "RS" or the_world[current_position_row+1][current_position_column-1] == "RB":
                    print("AI slaps it's teammate and continues")

            if computer_movement_input == "A":
                if the_world[current_position_row][current_position_column-1] == "--":
                    the_world[current_position_row][current_position_column-1] = hahmo.id
                    hahmo.position = (current_position_row, current_position_column-1)
                    the_world[current_position_row][current_position_column] = "--"
                    print("tietokone liikkui : A")
                    break
                if the_world[current_position_row][current_position_column-1] == "XX":
                    print(f"Computer runs to a tree, my oh my")
                if the_world[current_position_row][current_position_column-1] == "RS" or the_world[current_position_row][current_position_column-1] == "RB":
                    print("AI slaps it's teammate and continues")
    if computer_melee_attacked_this_turn == True:
        print("AI ei liikkunut vaan melee hyökkäsi tällä vuorolla")
    if computer_range_attacked_this_turn == True:
        print("AI ei liikkunut vaan range hyökkäsi tällä vuorolla")




def game_loop():
    turn_counter = 1
    swordman_RS = swordman("swordman", "RS")
    swordman_GS = swordman("swordman", "GS")
    bowman_RB = bowman("bowman", "RB")
    bowman_GB = bowman("bowman", "GB")
    while r_id_win == False and g_id_win == False:
        printing_the_world()
        if turn_counter % 1 == 0:
            # ekan tiimin vuoro
            movement(all_character_list[turn_counter])
            turn_counter += 1
            #pass
        if turn_counter % 1 == 1:
            #tokan tiimin vuoro
            pass


def testi():
    #swordman_RS = swordman("RS_upseeri", "RS")
    #swordman_GS = swordman("GS_kikkeli", "GS")
    #print(UKKELI.id)
    #print(swordman_RS.id)
    #print(swordman_RS.name)
        #for x in character_list:
    #    print(x)
    #print(swordman_RS.character_hp)
    #print(swordman_GS.character_hp)
    #print(swordman_RS.position)
    pass

making_obstacles(2)
kaikki_hahmot = []
turn_counter = 0
character_turn_counter = 0
swordman_RS = swordman("swordman", "RS")
kaikki_hahmot.append(swordman_RS)
swordman_GS = swordman("swordman", "GS")
kaikki_hahmot.append(swordman_GS)
bowman_RB = bowman("bowman", "RB")
kaikki_hahmot.append(bowman_RB)
bowman_GB = bowman("bowman", "GB")
kaikki_hahmot.append(bowman_GB)

while True:
    what_to_do = start_menu()
    if what_to_do.upper() == "HELP":
        print()
        print("To move, please select:")
        print("Q, W, E")
        print("A,    D")
        print("Z, X, C")
        print()
        print("Select 'B' to shoot an arrow")
        what_to_do = start_menu()
    if what_to_do.upper() == "START":
        break
    if what_to_do.upper() == "QUIT":
        print()
        print("* *")
        print("Thank You for playing the game!")
        print("* *")
        print()
        break
        

if what_to_do.upper() == "START":
    while r_id_win == False and g_id_win == False:
        printing_the_world()
        print(turn_counter)
        if turn_counter % 2 == 1:
            # ekan tiimin vuoro
            print(f"Next character to move: {kaikki_hahmot[character_turn_counter].id}")
            movement(kaikki_hahmot[character_turn_counter]) 
            print("\n")

            character_turn_counter += 1
            if character_turn_counter > 3:
                character_turn_counter = 0

        if turn_counter % 2 == 0:
            print(f"Tietokone koittaa liikuttaa: {kaikki_hahmot[character_turn_counter].id}")
            computer_move(kaikki_hahmot[character_turn_counter])
            print("\n")
        
            character_turn_counter += 1
            if character_turn_counter > 3:
                character_turn_counter = 0
        turn_counter += 1


    print(quit)
    quit()


if __name__ == '__main__':
    #printing_the_world()
    #making_obstacles() # tää toimii
    #create_swordman_SS()
    #create_swordman_RS()
    #testi()
    #create_characters()
    #deploy_character()
    #printing_the_world()
    #game_loop() # tää toimii
    #print(character_list)
    #print(swordman_RS.position)
    #print(all_character_list)
    pass


# position lisäys pitää lisätä ja bugit siitä pois.
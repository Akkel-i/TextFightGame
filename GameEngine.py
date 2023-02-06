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
    def mranged_attack(self):
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
        self.character_melee_dmg = random.randint(1, 5)
        print("hello my name is " + self.name)



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
    
# tähän pitää saada character.TIETO jostain, eli miten saan vuorossa olevan hahmon sisään?
def movement(hahmo):
    current_position_row = hahmo.position[0]
    current_position_column = hahmo.position[1]

    player_movement_input = input("Choose where to move: ")
    # nuolet joka suuntaan näppäimillä: Q W E D C X Z A
    # pitää vielä chekata ettei mene kentän yli tai ali
    if player_movement_input.upper() == "Q":
        if the_world[current_position_row-1][current_position_column-1] == "--":
            #do it eli saa liikkua
            the_world[current_position_row-1][current_position_column-1] = hahmo.id
            hahmo.position = (current_position_row-1, current_position_column-1)
            the_world[current_position_row][current_position_column] = "--"

    if player_movement_input.upper() == "W":
        if the_world[current_position_row-1][current_position_column] == "--":
            the_world[current_position_row-1][current_position_column] = hahmo.id
            hahmo.position = (current_position_row-1, current_position_column)
            the_world[current_position_row][current_position_column] = "--"

    if player_movement_input.upper() == "E":
        if the_world[current_position_row-1][current_position_column+1] == "--":
            the_world[current_position_row-1][current_position_column+1] = hahmo.id
            hahmo.position = (current_position_row-1, current_position_column+1)
            the_world[current_position_row][current_position_column] = "--"

    if player_movement_input.upper() == "D":
        if the_world[current_position_row][current_position_column+1] == "--":
            the_world[current_position_row][current_position_column+1] = hahmo.id
            hahmo.position = (current_position_row, current_position_column+1)
            the_world[current_position_row][current_position_column] = "--"
      
    if player_movement_input.upper() == "C":
        if the_world[current_position_row+1][current_position_column+1] == "--":
            the_world[current_position_row+1][current_position_column+1] = hahmo.id
            hahmo.position = (current_position_row+1, current_position_column+1)
            the_world[current_position_row][current_position_column] = "--"

    if player_movement_input.upper() == "X":
        if the_world[current_position_row+1][current_position_column] == "--":
            the_world[current_position_row+1][current_position_column] = hahmo.id
            hahmo.position = (current_position_row+1, current_position_column)
            the_world[current_position_row][current_position_column] = "--"

    if player_movement_input.upper() == "Z":
        if the_world[current_position_row+1][current_position_column-1] == "--":
            the_world[current_position_row+1][current_position_column-1] = hahmo.id
            hahmo.position = (current_position_row+1, current_position_column-1)
            the_world[current_position_row][current_position_column] = "--"

    if player_movement_input.upper() == "A":
        if the_world[current_position_row][current_position_column-1] == "--":
            the_world[current_position_row][current_position_column-1] = hahmo.id
            hahmo.position = (current_position_row, current_position_column-1)
            the_world[current_position_row][current_position_column] = "--"

    #else:
        #print("Illegal move, please try again")
        # loop to beginning

# chekki jos jokin ympäröivä ruutu on vihollinen
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
            if the_world[check_beginning_row][check_beginning_column] == "GS" or the_world[check_beginning_row][check_beginning_column] == "GB":
                #if yes,do damage
                has_attacked = True
                print("AI hyökkäsi ihmisen kimppuun!")
                break
                #pass
            print(f"{check_beginning_row}, {check_beginning_column}")
            check_beginning_column += 1   
        check_beginning_row += 1
        check_beginning_column = limiter_column - 2 
    return has_attacked     



def computer_move(hahmo):
    current_position_row = hahmo.position[0]
    current_position_column = hahmo.position[1]
    movement_options_computer = ["Z", "X", "C"]

    computer_movement_input = random.choice(movement_options_computer)
    print(computer_movement_input)
    # nuolet joka suuntaan näppäimillä: Q W E D C X Z A
    # pitää vielä chekata ettei mene kentän yli tai ali

    computer_attacked_this_turn = computer_attack_check(hahmo) # tähän hyökkäys chekki ennenkun liikkuu

    if computer_attacked_this_turn == False:
        if computer_movement_input == "Q":
            if the_world[current_position_row-1][current_position_column-1] == "--":
                the_world[current_position_row-1][current_position_column-1] = hahmo.id
                hahmo.position = (current_position_row-1, current_position_column-1)
                the_world[current_position_row][current_position_column] = "--"
                print("tietokone liikkui : Q")

        if computer_movement_input == "W":
            if the_world[current_position_row-1][current_position_column] == "--":
                the_world[current_position_row-1][current_position_column] = hahmo.id
                hahmo.position = (current_position_row-1, current_position_column)
                the_world[current_position_row][current_position_column] = "--"
                print("tietokone liikkui : W")

        if computer_movement_input == "E":
            if the_world[current_position_row-1][current_position_column+1] == "--":
                the_world[current_position_row-1][current_position_column+1] = hahmo.id
                hahmo.position = (current_position_row-1, current_position_column+1)
                the_world[current_position_row][current_position_column] = "--"
                print("tietokone liikkui : E")

        if computer_movement_input == "D":
            if the_world[current_position_row][current_position_column+1] == "--":
                the_world[current_position_row][current_position_column+1] = hahmo.id
                hahmo.position = (current_position_row, current_position_column+1)
                the_world[current_position_row][current_position_column] = "--"
                print("tietokone liikkui : D")
      
        if computer_movement_input == "C":
            if the_world[current_position_row+1][current_position_column+1] == "--":
                the_world[current_position_row+1][current_position_column+1] = hahmo.id
                hahmo.position = (current_position_row+1, current_position_column+1)
                the_world[current_position_row][current_position_column] = "--"
                print("tietokone liikkui : C")

        if computer_movement_input == "X":
            if the_world[current_position_row+1][current_position_column] == "--":
                the_world[current_position_row+1][current_position_column] = hahmo.id
                hahmo.position = (current_position_row+1, current_position_column)
                the_world[current_position_row][current_position_column] = "--"
                print("tietokone liikkui : X")

        if computer_movement_input == "Z":
            if the_world[current_position_row+1][current_position_column-1] == "--":
                the_world[current_position_row+1][current_position_column-1] = hahmo.id
                hahmo.position = (current_position_row+1, current_position_column-1)
                the_world[current_position_row][current_position_column] = "--"
                print("tietokone liikkui : Z")

        if computer_movement_input == "A":
            if the_world[current_position_row][current_position_column-1] == "--":
                the_world[current_position_row][current_position_column-1] = hahmo.id
                hahmo.position = (current_position_row, current_position_column-1)
                the_world[current_position_row][current_position_column] = "--"
                print("tietokone liikkui : A")
    if computer_attacked_this_turn == True:
        print("AI ei liikkunut vaan hyökkäsi tällä vuorolla")
    #else:
        #print("Illegal move, please try again")
        # loop to beginning



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

making_obstacles(6)
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

while r_id_win == False and g_id_win == False:
    printing_the_world()
    print(turn_counter)
    if turn_counter % 2 == 1:
        # ekan tiimin vuoro
        print(f"Next character to move: {kaikki_hahmot[character_turn_counter].id}")
        movement(kaikki_hahmot[character_turn_counter]) 

        turn_counter += 1
        character_turn_counter += 1
        if character_turn_counter > 3:
            character_turn_counter = 0

    if turn_counter % 2 == 0:
        print(f"Tietokone koittaa liikuttaa: {kaikki_hahmot[character_turn_counter].id}")
        computer_move(kaikki_hahmot[character_turn_counter])

        turn_counter += 1
        character_turn_counter += 1
        if character_turn_counter > 3:
            character_turn_counter = 0



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
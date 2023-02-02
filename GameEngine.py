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
r_team_character_list = []
g_team_character_list = []
r_team_win = False
g_team_win = False
turn_counter = 1
random_counter = 0 



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
def making_obstacles():
    howManyObstacle = 5
    i = 0
    while i < howManyObstacle:
        random_row = random.randint(2, 5)
        random_cell = random.randint(1, 6)
        if the_world[random_row][random_cell] == "--":
            the_world[random_row][random_cell] = "XX"
        else:         
            random_row = random.randint(2, 5)
            random_cell = random.randint(1, 6)
        if the_world[random_row][random_cell] == "--":
            the_world[random_row][random_cell] = "XX"
        i += 1



class bowman:
    character_movement = 1
    def __init__(self, name, team):
        self.name = name
        self.team = team # käytetään deploy kohdassa, R ja G
        self.position = ""
        self.character_hp = random.randint(6, 10)
        self.character_mp = random.randint(0, 0)
        if self.team == "RB":
            r_team_character_list.append(self.team)
        elif self.team == "GB":
            g_team_character_list.append(self.team)
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
    def __init__(self, name, team ):
        self.name = name
        self.team = team # käytetään deploy kohdassa, R ja G
        self.position = ""
        self.character_hp = random.randint(8, 15)
        self.character_mp = random.randint(0, 0)
        if self.team == "RS":
            r_team_character_list.append(self.team)
        elif self.team == "GS":
            g_team_character_list.append(self.team)        
    def melee_attack(self):
        #katso joku ruutu ja tee siihen dmg
        self.character_melee_dmg = random.randint(1, 5)
        print("hello my name is " + self.name)



def create_characters():
    swordman_RS = swordman("RS_upseeri", "RS")
    swordman_GS = swordman("GS_miekka", "GS")
    bowman_RB = bowman("RB_haltija", "RB")
    bowman_GB = bowman("GB_jouska", "GB")

# funktio mikä sijoittaa ukkelit kartalle riippuen kumpi joukkoe
def deploy_character():
    # R joukkoe ylös, G joukkoe alas
    for x in r_team_character_list:
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
    for x in g_team_character_list:
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
    

def movement():
    player_movement_input = input("Choose where to move: ")
    # nuolet joka suuntaan näppäimillä: Q W E D C X Z A
    if player_movement_input == "Q":
        pass
    if player_movement_input == "W":
        pass
    if player_movement_input == "E":
        pass
    if player_movement_input == "D":
        pass        
    if player_movement_input == "C":
        pass
    if player_movement_input == "X":
        pass
    if player_movement_input == "Z":
        pass
    if player_movement_input == "A":
        pass


def game_loop():
    while r_team_win == False and g_team_win == False:
        printing_the_world()
        if turn_counter % 1 == 0:
            # ekan tiimin vuoro
            pass
        if turn_counter % 1 == 1:
            #tokan tiimin vuoro
            pass


def testi():
    UKKELI = swordman("pena", "YS")
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


if __name__ == '__main__':
    #printing_the_world()
    making_obstacles()
    #create_swordman_SS()
    #create_swordman_RS()
    #testi()
    create_characters()
    deploy_character()
    printing_the_world()
    #game_loop()
    #print(character_list)
    print(swordman_RS.position)


# position lisäys pitää lisätä ja bugit siitä pois. Miksei viimeinen  print(swordman_RS.position) toimi,
#sanoo ettei oo defined, eli ei osaa ottaa sitä vaikka luotu aikasemmin, miksei
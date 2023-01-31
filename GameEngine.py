import random

the_world = [
        ["AA", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"], 
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"], 
        ["--", "--", "--", "--", "--", "--", "--", "--"], 
        ["--", "--", "--", "--", "--", "--", "--", "LL"] 
    ]

# lista missä pelaajat sisällä?
character_list = []
r_team_win = False
s_team_win = False
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
def making_obstacles():
    howManyObstacle = 5
    i = 0
    while i < howManyObstacle:
        random_row = random.randint(2, 5)
        random_cell = random.randint(1, 6)
        if the_world[random_row][random_cell] == "--":
            the_world[random_row][random_cell] = "XX"
        i += 1

 # Tutki OOP miten sitä voisi hyödyntää kun luo samanlaisia hahmoja usein ja eritellä siihen esim joukkoeet
def create_swordman_SS():
    character_icon = "SS" # tähän täytyy keksiä miten saa joukkoeet erotueltua esim rS vs bS (redS, blueS )
    character_hp = random.randint(8, 15)
    character_mp = random.randint(0, 0)
    character_melee_dmg = random.randint(1, 5)
    character_range_dmg = random.randint(0, 0)
    character_movement = 1
    character_list.append(character_icon)
def create_swordman_RS():
    character_icon = "RS" # tähän täytyy keksiä miten saa joukkoeet erotueltua esim rS vs bS (redS, blueS )
    character_hp = random.randint(8, 15)
    character_mp = random.randint(0, 0)
    character_melee_dmg = random.randint(1, 5)
    character_range_dmg = random.randint(0, 0)
    character_movement = 1
    character_list.append(character_icon)


# funktio mikä sijoittaa ukkelit kartalle riippuen kumpi joukkoe
def deploy_character():
    # S joukkoe ylös
    for x in character_list:
        if x[0] == "S":
            row = random.randint(0, 1)
            cell = random.randint(1, 6)
            the_world[row][cell] = x
    # R joukkoe alas
        if x[0] == "R":
            row = random.randint(6, 7)
            cell = random.randint(1, 6)
            the_world[row][cell] = x

def game_loop():
    while s_team_win == False and r_team_win == False:
        printing_the_world()
        if turn_counter % 1 == 0:
            # ekan tiimin vuoro
        if turn_counter % 1 == 1:
            #tokan tiimin vuoro


if __name__ == '__main__':
    #printing_the_world()
    making_obstacles()
    create_swordman_SS()
    create_swordman_RS()
    deploy_character()
    printing_the_world()
    #game_loop()
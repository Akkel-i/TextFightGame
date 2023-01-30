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
def create_swordman():
    character_icon = "SS" # tähän täytyy keksiä miten saa joukkoeet erotueltua esim rS vs bS (redS, blueS )
    character_hp = random.randint(8, 15)
    character_mp = random.randint(0, 0)
    character_melee_dmg = random.randint(1, 5)
    character_range_dmg = random.randint(0, 0)
    character_movement = 1
    character_list.append(character_icon)


# funktio mikä sijoittaa ukkelit kartalle riippuen kumpi joukkoe
def deploy_character():
    # S joukkoe ylös
    if character_list[0][0] == "S":
        row = random.randint(0, 1)
        cell = random.randint(1, 6)
        the_world[row][cell] = character_list[0]
    # R joukkoe alas
    if character_list[0][0] == "R":
        row = random.randint(6, 7)
        cell = random.randint(1, 6)
        the_world[row][cell] = character_list[0]


if __name__ == '__main__':
    #PrintingTheWorld()
    making_obstacles()
    create_swordman()
    deploy_character()
    printing_the_world()
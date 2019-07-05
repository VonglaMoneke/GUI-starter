import pygame
from pygame.locals import *
from sys import exit
from random import randint
from random import shuffle
import time
import os


def timer(screen, t):
    formatTime = str(int(t//60)) + ":" + str(int(t%60))
    if int(t%60) < 10:
        formatTime = formatTime[:-1] + "0" + formatTime[-1]

    font = pygame.font.SysFont("helvetica", 20)
    txt = font.render("Time Remaining: " + str(formatTime), 1, (255, 255, 255))
    screen.blit(txt, (400,10))
    
    pygame.display.update()
    
def main():
    #starting pygame
    pygame.init()
    pygame.mixer.init()
    #creating the scrren of 600x600
    screen = pygame.display.set_mode((600,600), 0, 32)
    #generates the number to select the bg then uses the no to find that bg and loads it
    bg_number = randint(1, 9)
    bg = 'img/bgs/bg' + str(bg_number) + '.png'
    background = pygame.image.load(bg).convert()
    #Setting the Victory and Defeat images and loads the screens
    victory = 'victory/victory.png'
    defeat = 'defeat/defeat.png'
    victory_timeout = 'victory/victory_timeout.png'
    defeat_timeout = 'defeat/defeat_timeout.png'
    draw = 'img/draw.png'
    vic_screen = pygame.image.load(victory).convert_alpha()
    def_screen = pygame.image.load(defeat).convert_alpha()
    vic_screen_timeout = pygame.image.load(victory_timeout).convert_alpha()
    def_screen_timeout = pygame.image.load(defeat_timeout).convert_alpha()
    draw_screen = pygame.image.load(draw).convert_alpha()
    #setting the window title
    pygame.display.set_caption('Virtual Link Estabilshed...')
    #set the clock and the timer for the game
    clock = pygame.time.Clock()
    t = 60 * 10
    # these are the lists to hold the music
    songs = []
    matches = []
    victory_music = []
    defeat_music = []
    
    #This generates the music for the matches
    for files in os.listdir('Music'):
        if files.endswith('.mp3'):
            songs.append(files)

    x = 0
    while x != 35:
        if x == 1 or x == 6 or x == 8 or x == 17 or x == 15 or x == 18 or x == 19 or x == 23:
            pass
        else:
            matches.append(songs[x])
        x = x+1


    random_music = randint(0, 26)
    pygame.mixer.music.load('Music/'+ str(matches[random_music]))
    pygame.mixer.music.set_volume(10/100)
    #pygame.mixer.music.play()
    

    for files in os.listdir('victory'):
        if files.endswith('.mp3'):
            victory_music.append(files)
            
    for files in os.listdir('defeat'):
        if files.endswith('.mp3'):
            defeat_music.append(files)

    #generating the starting character cards and loading them
    card0 = randint(1, 24)
    card_sprite0 = 'img/chars/Char' + str(card0) + '.png'
    load_card0 = pygame.image.load(card_sprite0).convert_alpha()
    card1 = randint(1, 24)
    card_sprite1 = 'img/chars/Char' + str(card1) + '.png'
    load_card1 = pygame.image.load(card_sprite1).convert_alpha()
    card2 = randint(1, 24)
    card_sprite2 = 'img/chars/Char' + str(card2) + '.png'
    load_card2 = pygame.image.load(card_sprite2).convert_alpha()

    #generating the starting ability cards and loading them

    a_card0 = randint(1, 10)
    a_card_sprite0 = 'img/A.C/Card' + str(a_card0) + '.jpg'
    a_load_card0 = pygame.image.load(a_card_sprite0).convert_alpha()
    a_card1 = randint(1, 10)
    a_card_sprite1 = 'img/A.C/Card' + str(a_card1) + '.jpg'
    a_load_card1 = pygame.image.load(a_card_sprite1).convert_alpha()
    a_card2 = randint(1, 10)
    a_card_sprite2 = 'img/A.C/Card' + str(a_card2) + '.jpg'
    a_load_card2 = pygame.image.load(a_card_sprite2).convert_alpha()

    #setting the life points & enemy life points
    life_points = 10000
    op_life_points = 10000
    #setting the fonts
    font = pygame.font.SysFont('helvetica', 50)
    # setting the coordinates for the cards
    x0 = 45
    y0 = 460
    x1 = 145
    x2 = 245
    # generating the null image for the battle field
    pixel = 'img/pixel.png'
    a_pixel = 'img/pixel.png'
    #Bool variable that checks if there is a card in the active zone
    own_active_zone = False
    own_ability_zone = False
    #Bool variable that checks if there is a card in the opponents active zone
    op_active_zone = False
    #damage variable
    dmg = 0
    #attack and defense mode bool variables to see if the card placed is in attack or defense mode
    attack_mode = False
    defense_mode = False

    #Printing the controls in the python shell (subject to change)
    print('''Press the A key to place the first card of your hand on the field in Attack Mode
Press the Z key to place the first card of your hand on the field in Defense Mode

Press the S key to place the second card of your hand on the field in Attack Mode
Press the X key to place the second card of your hand on the field in Defense Mode

Press the D key to place the third card of your hand on the field in Attack Mode
Press the C key to place the third card of your hand on the field in Defense Mode

Press the ALT key to change the card in the field with one from your hand
Press the SPACE key to activate the turn with the selected card
    ''')

    #Main Loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                exit()

        #setting the card in the active zone
        card_in_battle = pygame.image.load(pixel).convert_alpha()
        a_card_in_battle = pygame.image.load(a_pixel).convert_alpha()
        #detecting the keys that are pressed
        key = pygame.key.get_pressed()
        if key[K_a]:
            if own_active_zone == False:
                #the first card goes to the battle zone
                pixel = card_sprite0
                #gen another card
                random_num = randint(1, 24)
                card_sprite0 = 'img/chars/Char' + str(random_num) + '.png'
                load_card0 = pygame.image.load(card_sprite0).convert_alpha()
                attack_mode = True
                own_active_zone = True
        if key[K_s]:
            if own_active_zone == False:
                #the second card goes to the battle zone
                pixel = card_sprite1
                #gen another card
                random_num = randint(1, 24)
                card_sprite1 = 'img/chars/Char' + str(random_num) + '.png'
                load_card1 = pygame.image.load(card_sprite1).convert_alpha()
                attack_mode = True
                own_active_zone = True
        if key[K_d]:
            if own_active_zone == False:
                #the third card goes to the battle zone
                pixel = card_sprite2
                #gen another card
                random_num = randint(1, 24)
                card_sprite2 = 'img/chars/Char' + str(random_num) + '.png'
                load_card2 = pygame.image.load(card_sprite2).convert_alpha()
                attack_mode = True
                own_active_zone = True
        if key[K_z]:
            if own_active_zone == False:
                #the first card goes to the battle zone
                pixel = card_sprite0
                #gen another card
                random_num = randint(1, 24)
                card_sprite0 = 'img/chars/Char' + str(random_num) + '.png'
                load_card0 = pygame.image.load(card_sprite0).convert_alpha()
                defense_mode = True
                own_active_zone = True
        if key[K_x]:
            if own_active_zone == False:
                #the second card goes to the battle zone
                pixel = card_sprite1
                #gen another card
                random_num = randint(1, 24)
                card_sprite1 = 'img/chars/Char' + str(random_num) + '.png'
                load_card1 = pygame.image.load(card_sprite1).convert_alpha()
                defense_mode = True
                own_active_zone = True
        if key[K_c]:
            if own_active_zone == False:
                #the third card goes to the battle zone
                pixel = card_sprite2
                #gen another card
                random_num = randint(1, 24)
                card_sprite2 = 'img/chars/Char' + str(random_num) + '.png'
                load_card2 = pygame.image.load(card_sprite2).convert_alpha()
                defense_mode = True
                own_active_zone = True
                
        if key[K_j]:
            if own_ability_zone == False:
                #the third card goes to the ability zone
                a_pixel = a_card_sprite0
                #gen another card
                a_card0 = randint(1, 10)
                a_card_sprite0 = 'img/A.C/Card' + str(a_card0) + '.jpg'
                a_load_card0 = pygame.image.load(a_card_sprite0).convert_alpha()
                own_ability_zone = True
        if key[K_k]:
            if own_ability_zone == False:
                #the third card goes to the ability zone
                a_pixel = a_card_sprite1
                #gen another card
                a_card1 = randint(1, 10)
                a_card_sprite1 = 'img/A.C/Card' + str(a_card1) + '.jpg'
                a_load_card1 = pygame.image.load(a_card_sprite1).convert_alpha()
                own_ability_zone = True
        if key[K_l]:
            if own_ability_zone == False:
                #the third card goes to the ability zone
                a_pixel = a_card_sprite2
                #gen another card
                a_card2 = randint(1, 10)
                a_card_sprite2 = 'img/A.C/Card' + str(a_card2) + '.jpg'
                a_load_card2 = pygame.image.load(a_card_sprite2).convert_alpha()
                own_ability_zone = True

        if op_active_zone == False:
            #gen another card when opponents card is defeated
            op_random = randint(1, 24)
            op_active_zone = True
        #load opponent card
        op_sprite = 'img/chars/Char' + str(op_random) + '.png'
        op_card = pygame.image.load(op_sprite).convert_alpha()


        if key[K_KP_ENTER] and own_ability_zone == True and a_pixel == 'img/A.C/Card3.jpg':
            a_card0 = randint(1, 10)
            a_card_sprite0 = 'img/A.C/Card' + str(a_card0) + '.jpg'
            a_load_card0 = pygame.image.load(a_card_sprite0).convert_alpha()
            a_card1 = randint(1, 10)
            a_card_sprite1 = 'img/A.C/Card' + str(a_card1) + '.jpg'
            a_load_card1 = pygame.image.load(a_card_sprite1).convert_alpha()
            a_card2 = randint(1, 10)
            a_card_sprite2 = 'img/A.C/Card' + str(a_card2) + '.jpg'
            a_load_card2 = pygame.image.load(a_card_sprite2).convert_alpha()
            a_pixel = 'img/pixel.png'
            own_ability_zone = False

            
        if key[K_SPACE] and op_active_zone == True and own_active_zone == True:
            if a_pixel == 'img/A.C/Card8.jpg':
                #detecting the stats of the chars
                if pixel == 'img/chars/Char1.png':
                    attack = 2030*1.5
                    defense = 1150
                    speed = 1800
                elif pixel == 'img/chars/Char2.png':
                    attack = 1380*1.5
                    defense = 2010
                    speed = 1980
                elif pixel == 'img/chars/Char3.png':
                    attack = 1820*1.5
                    defense = 1430
                    speed = 2110
                elif pixel == 'img/chars/Char4.png':
                    attack = 1340*1.5
                    defense = 2010
                    speed = 2290
                elif pixel == 'img/chars/Char5.png':
                    attack = 2130*1.5
                    defense = 1080
                    speed = 2330
                elif pixel == 'img/chars/Char6.png':
                    attack = 1550*1.5
                    defense = 2140 
                    speed = 2620
                elif pixel == 'img/chars/Char7.png':
                    attack = 1750*1.5
                    defense = 1720
                    speed = 1370
                elif pixel == 'img/chars/Char8.png':
                    attack = 1420*1.5
                    defense = 1940
                    speed = 2030
                elif pixel == 'img/chars/Char9.png':
                    attack = 1710*1.5
                    defense = 2250
                    speed = 1340
                elif pixel == 'img/chars/Char10.png':
                    attack = 2260*1.5
                    defense = 1620
                    speed = 1470
                elif pixel == 'img/chars/Char11.png':
                    attack = 1310*1.5
                    defense = 2040
                    speed = 1920
                elif pixel == 'img/chars/Char12.png':
                    attack = 1700*1.5
                    defense = 1530
                    speed = 1280
                elif pixel == 'img/chars/Char13.png':
                    attack = 1610*1.5
                    defense = 1400
                    speed = 1940
                elif pixel == 'img/chars/Char14.png':
                    attack = 1900*1.5
                    defense = 1330
                    speed = 1870
                elif pixel == 'img/chars/Char15.png':
                    attack = 1900*1.5
                    defense = 1150
                    speed = 1890
                elif pixel == 'img/chars/Char16.png':
                    attack = 1460*1.5
                    defense = 2520
                    speed = 2090
                elif pixel == 'img/chars/Char17.png':
                    attack = 1690*1.5
                    defense = 1450
                    speed = 2190
                elif pixel == 'img/chars/Char18.png':
                    attack = 1470*1.5
                    defense = 1930
                    speed = 1870
                elif pixel == 'img/chars/Char19.png':
                    attack = 2350*1.5
                    defense = 790
                    speed = 2000
                elif pixel == 'img/chars/Char20.png':
                    attack = 1630*1.5
                    defense = 1950
                    speed = 2420
                elif pixel == 'img/chars/Char21.png':
                    attack = 2390*1.5
                    defense = 550
                    speed = 2720
                elif pixel == 'img/chars/Char22.png':
                    attack = 1690*1.5
                    defense = 1450
                    speed = 2070
                elif pixel == 'img/chars/Char23.png':
                    attack = 1710*1.5
                    defense = 1380
                    speed = 1870
                elif pixel == 'img/chars/Char24.png':
                    attack = 2100*1.5
                    defense = 1920
                    speed = 810
                #opponents attack and speed as they cannot go into defense mode
                if op_sprite == 'img/chars/Char1.png':
                    op_attack = 2030
                    op_speed = 1800
                elif op_sprite == 'img/chars/Char2.png':
                    op_attack = 1380
                    op_speed = 1980
                elif op_sprite == 'img/chars/Char3.png':
                    op_attack = 1820
                    op_speed = 2110
                elif op_sprite == 'img/chars/Char4.png':
                    op_attack = 1340
                    op_speed = 2290
                elif op_sprite == 'img/chars/Char5.png':
                    op_attack = 2130
                    op_speed = 2330
                elif op_sprite == 'img/chars/Char6.png':
                    op_attack = 1550
                    op_speed = 2620
                elif op_sprite == 'img/chars/Char7.png':
                    op_attack = 1750
                    op_speed = 1370
                elif op_sprite == 'img/chars/Char8.png':
                    op_attack = 1420
                    op_speed = 2030
                elif op_sprite == 'img/chars/Char9.png':
                    op_attack = 1710
                    op_speed = 1340
                elif op_sprite == 'img/chars/Char10.png':
                    op_attack = 2260
                    op_speed = 1470
                elif op_sprite == 'img/chars/Char11.png':
                    op_attack = 1310
                    op_speed = 1920
                elif op_sprite == 'img/chars/Char12.png':
                    op_attack = 1700
                    op_speed = 1280
                elif op_sprite == 'img/chars/Char13.png':
                    op_attack = 1610
                    op_speed = 1940
                elif op_sprite == 'img/chars/Char14.png':
                    op_attack = 1900
                    op_speed = 1870
                elif op_sprite == 'img/chars/Char15.png':
                    op_attack = 1900
                    op_speed = 1890
                elif op_sprite == 'img/chars/Char16.png':
                    op_attack = 1460
                    op_speed = 2090
                elif op_sprite == 'img/chars/Char17.png':
                    op_attack = 1690
                    op_speed = 2190
                elif op_sprite == 'img/chars/Char18.png':
                    op_attack = 1470
                    op_speed = 1870
                elif op_sprite == 'img/chars/Char19.png':
                    op_attack = 2350
                    op_speed = 2000
                elif op_sprite == 'img/chars/Char20.png':
                    op_attack = 1630
                    op_speed = 2420
                elif op_sprite == 'img/chars/Char21.png':
                    op_attack = 2390
                    op_speed = 2720
                elif op_sprite == 'img/chars/Char22.png':
                    op_attack = 1690
                    op_speed = 2070
                elif op_sprite == 'img/chars/Char23.png':
                    op_attack = 1710
                    op_speed = 1870
                elif op_sprite == 'img/chars/Char24.png':
                    op_attack = 2100
                    op_speed = 810

            elif a_pixel == 'img/A.C/Card4.jpg':
                #detecting the stats of the chars
                if pixel == 'img/chars/Char1.png':
                    attack = 2030*2.5
                    defense = 1150
                    speed = 1800
                elif pixel == 'img/chars/Char2.png':
                    attack = 1380*2.5
                    defense = 2010
                    speed = 1980
                elif pixel == 'img/chars/Char3.png':
                    attack = 1820*2.5
                    defense = 1430
                    speed = 2110
                elif pixel == 'img/chars/Char4.png':
                    attack = 1340*2.5
                    defense = 2010
                    speed = 2290
                elif pixel == 'img/chars/Char5.png':
                    attack = 2130*2.5
                    defense = 1080
                    speed = 2330
                elif pixel == 'img/chars/Char6.png':
                    attack = 1550*2.5
                    defense = 2140 
                    speed = 2620
                elif pixel == 'img/chars/Char7.png':
                    attack = 1750*2.5
                    defense = 1720
                    speed = 1370
                elif pixel == 'img/chars/Char8.png':
                    attack = 1420*2.5
                    defense = 1940
                    speed = 2030
                elif pixel == 'img/chars/Char9.png':
                    attack = 1710*2.5
                    defense = 2250
                    speed = 1340
                elif pixel == 'img/chars/Char10.png':
                    attack = 2260*2.5
                    defense = 1620
                    speed = 1470
                elif pixel == 'img/chars/Char11.png':
                    attack = 1310*2.5
                    defense = 2040
                    speed = 1920
                elif pixel == 'img/chars/Char12.png':
                    attack = 1700*2.5
                    defense = 1530
                    speed = 1280
                elif pixel == 'img/chars/Char13.png':
                    attack = 1610*2.5
                    defense = 1400
                    speed = 1940
                elif pixel == 'img/chars/Char14.png':
                    attack = 1900*2.5
                    defense = 1330
                    speed = 1870
                elif pixel == 'img/chars/Char15.png':
                    attack = 1900*2.5
                    defense = 1150
                    speed = 1890
                elif pixel == 'img/chars/Char16.png':
                    attack = 1460*2.5
                    defense = 2520
                    speed = 2090
                elif pixel == 'img/chars/Char17.png':
                    attack = 1690*2.5
                    defense = 1450
                    speed = 2190
                elif pixel == 'img/chars/Char18.png':
                    attack = 1470*2.5
                    defense = 1930
                    speed = 1870
                elif pixel == 'img/chars/Char19.png':
                    attack = 2350*2.5
                    defense = 790
                    speed = 2000
                elif pixel == 'img/chars/Char20.png':
                    attack = 1630*2.5
                    defense = 1950
                    speed = 2420
                elif pixel == 'img/chars/Char21.png':
                    attack = 2390*2.5
                    defense = 550
                    speed = 2720
                elif pixel == 'img/chars/Char22.png':
                    attack = 1690*2.5
                    defense = 1450
                    speed = 2070
                elif pixel == 'img/chars/Char23.png':
                    attack = 1710*2.5
                    defense = 1380
                    speed = 1870
                elif pixel == 'img/chars/Char24.png':
                    attack = 2100*2.5
                    defense = 1920
                    speed = 810
                #opponents attack and speed as they cannot go into defense mode
                if op_sprite == 'img/chars/Char1.png':
                    op_attack = 2030
                    op_speed = 1800*0.5
                elif op_sprite == 'img/chars/Char2.png':
                    op_attack = 1380
                    op_speed = 1980*0.5
                elif op_sprite == 'img/chars/Char3.png':
                    op_attack = 1820
                    op_speed = 2110*0.5
                elif op_sprite == 'img/chars/Char4.png':
                    op_attack = 1340
                    op_speed = 2290*0.5
                elif op_sprite == 'img/chars/Char5.png':
                    op_attack = 2130
                    op_speed = 2330*0.5
                elif op_sprite == 'img/chars/Char6.png':
                    op_attack = 1550
                    op_speed = 2620*0.5
                elif op_sprite == 'img/chars/Char7.png':
                    op_attack = 1750
                    op_speed = 1370*0.5
                elif op_sprite == 'img/chars/Char8.png':
                    op_attack = 1420
                    op_speed = 2030*0.5
                elif op_sprite == 'img/chars/Char9.png':
                    op_attack = 1710
                    op_speed = 1340*0.5
                elif op_sprite == 'img/chars/Char10.png':
                    op_attack = 2260
                    op_speed = 1470*0.5
                elif op_sprite == 'img/chars/Char11.png':
                    op_attack = 1310
                    op_speed = 1920*0.5
                elif op_sprite == 'img/chars/Char12.png':
                    op_attack = 1700
                    op_speed = 1280*0.5
                elif op_sprite == 'img/chars/Char13.png':
                    op_attack = 1610
                    op_speed = 1940*0.5
                elif op_sprite == 'img/chars/Char14.png':
                    op_attack = 1900
                    op_speed = 1870*0.5
                elif op_sprite == 'img/chars/Char15.png':
                    op_attack = 1900
                    op_speed = 1890*0.5
                elif op_sprite == 'img/chars/Char16.png':
                    op_attack = 1460
                    op_speed = 2090*0.5
                elif op_sprite == 'img/chars/Char17.png':
                    op_attack = 1690
                    op_speed = 2190*0.5
                elif op_sprite == 'img/chars/Char18.png':
                    op_attack = 1470
                    op_speed = 1870*0.5
                elif op_sprite == 'img/chars/Char19.png':
                    op_attack = 2350
                    op_speed = 2000*0.5
                elif op_sprite == 'img/chars/Char20.png':
                    op_attack = 1630
                    op_speed = 2420*0.5
                elif op_sprite == 'img/chars/Char21.png':
                    op_attack = 2390
                    op_speed = 2720*0.5
                elif op_sprite == 'img/chars/Char22.png':
                    op_attack = 1690
                    op_speed = 2070*0.5
                elif op_sprite == 'img/chars/Char23.png':
                    op_attack = 1710
                    op_speed = 1870*0.5
                elif op_sprite == 'img/chars/Char24.png':
                    op_attack = 2100
                    op_speed = 810*0.5
                life_points -= round(life_points*0.3)

            elif a_pixel == 'img/A.C/Card10.jpg':
                #detecting the stats of the chars
                if pixel == 'img/chars/Char1.png':
                    attack = 2030
                    defense = 1150
                    speed = 1800*1.7
                elif pixel == 'img/chars/Char2.png':
                    attack = 1380
                    defense = 2010
                    speed = 1980*1.7
                elif pixel == 'img/chars/Char3.png':
                    attack = 1820
                    defense = 1430
                    speed = 2110*1.7
                elif pixel == 'img/chars/Char4.png':
                    attack = 1340
                    defense = 2010
                    speed = 2290*1.7
                elif pixel == 'img/chars/Char5.png':
                    attack = 2130
                    defense = 1080
                    speed = 2330*1.7
                elif pixel == 'img/chars/Char6.png':
                    attack = 1550
                    defense = 2140 
                    speed = 2620*1.7
                elif pixel == 'img/chars/Char7.png':
                    attack = 1750
                    defense = 1720
                    speed = 1370*1.7
                elif pixel == 'img/chars/Char8.png':
                    attack = 1420
                    defense = 1940
                    speed = 2030*1.7
                elif pixel == 'img/chars/Char9.png':
                    attack = 1710
                    defense = 2250
                    speed = 1340*1.7
                elif pixel == 'img/chars/Char10.png':
                    attack = 2260
                    defense = 1620
                    speed = 1470*1.7
                elif pixel == 'img/chars/Char11.png':
                    attack = 1310
                    defense = 2040
                    speed = 1920*1.7
                elif pixel == 'img/chars/Char12.png':
                    attack = 1700
                    defense = 1530
                    speed = 1280*1.7
                elif pixel == 'img/chars/Char13.png':
                    attack = 1610
                    defense = 1400
                    speed = 1940*1.7
                elif pixel == 'img/chars/Char14.png':
                    attack = 1900
                    defense = 1330
                    speed = 1870*1.7
                elif pixel == 'img/chars/Char15.png':
                    attack = 1900
                    defense = 1150
                    speed = 1890*1.7
                elif pixel == 'img/chars/Char16.png':
                    attack = 1460
                    defense = 2520
                    speed = 2090*1.7
                elif pixel == 'img/chars/Char17.png':
                    attack = 1690
                    defense = 1450
                    speed = 2190*1.7
                elif pixel == 'img/chars/Char18.png':
                    attack = 1470
                    defense = 1930
                    speed = 1870*1.7
                elif pixel == 'img/chars/Char19.png':
                    attack = 2350
                    defense = 790
                    speed = 2000*1.7
                elif pixel == 'img/chars/Char20.png':
                    attack = 1630
                    defense = 1950
                    speed = 2420*1.7
                elif pixel == 'img/chars/Char21.png':
                    attack = 2390
                    defense = 550
                    speed = 2720*1.7
                elif pixel == 'img/chars/Char22.png':
                    attack = 1690
                    defense = 1450
                    speed = 2070*1.7
                elif pixel == 'img/chars/Char23.png':
                    attack = 1710
                    defense = 1380
                    speed = 1870*1.7
                elif pixel == 'img/chars/Char24.png':
                    attack = 2100
                    defense = 1920
                    speed = 810*1.7
                #opponents attack and speed as they cannot go into defense mode
                if op_sprite == 'img/chars/Char1.png':
                    op_attack = 2030
                    op_speed = 1800*0.8
                elif op_sprite == 'img/chars/Char2.png':
                    op_attack = 1380
                    op_speed = 1980*0.8
                elif op_sprite == 'img/chars/Char3.png':
                    op_attack = 1820
                    op_speed = 2110*0.8
                elif op_sprite == 'img/chars/Char4.png':
                    op_attack = 1340
                    op_speed = 2290*0.8
                elif op_sprite == 'img/chars/Char5.png':
                    op_attack = 2130
                    op_speed = 2330*0.8
                elif op_sprite == 'img/chars/Char6.png':
                    op_attack = 1550
                    op_speed = 2620*0.8
                elif op_sprite == 'img/chars/Char7.png':
                    op_attack = 1750
                    op_speed = 1370*0.8
                elif op_sprite == 'img/chars/Char8.png':
                    op_attack = 1420
                    op_speed = 2030*0.8
                elif op_sprite == 'img/chars/Char9.png':
                    op_attack = 1710
                    op_speed = 1340*0.8
                elif op_sprite == 'img/chars/Char10.png':
                    op_attack = 2260
                    op_speed = 1470*0.8
                elif op_sprite == 'img/chars/Char11.png':
                    op_attack = 1310
                    op_speed = 1920*0.8
                elif op_sprite == 'img/chars/Char12.png':
                    op_attack = 1700
                    op_speed = 1280*0.8
                elif op_sprite == 'img/chars/Char13.png':
                    op_attack = 1610
                    op_speed = 1940*0.8
                elif op_sprite == 'img/chars/Char14.png':
                    op_attack = 1900
                    op_speed = 1870*0.8
                elif op_sprite == 'img/chars/Char15.png':
                    op_attack = 1900
                    op_speed = 1890*0.8
                elif op_sprite == 'img/chars/Char16.png':
                    op_attack = 1460
                    op_speed = 2090*0.8
                elif op_sprite == 'img/chars/Char17.png':
                    op_attack = 1690
                    op_speed = 2190*0.8
                elif op_sprite == 'img/chars/Char18.png':
                    op_attack = 1470
                    op_speed = 1870*0.8
                elif op_sprite == 'img/chars/Char19.png':
                    op_attack = 2350
                    op_speed = 2000*0.8
                elif op_sprite == 'img/chars/Char20.png':
                    op_attack = 1630
                    op_speed = 2420*0.8
                elif op_sprite == 'img/chars/Char21.png':
                    op_attack = 2390
                    op_speed = 2720*0.8
                elif op_sprite == 'img/chars/Char22.png':
                    op_attack = 1690
                    op_speed = 2070*0.8
                elif op_sprite == 'img/chars/Char23.png':
                    op_attack = 1710
                    op_speed = 1870*0.8
                elif op_sprite == 'img/chars/Char24.png':
                    op_attack = 2100
                    op_speed = 810*0.8
                    
            elif a_pixel == 'img/A.C/Card9.jpg':
                #detecting the stats of the chars
                if pixel == 'img/chars/Char1.png':
                    attack = 2030
                    defense = 1150
                    speed = 1800
                elif pixel == 'img/chars/Char2.png':
                    attack = 1380
                    defense = 2010
                    speed = 1980
                elif pixel == 'img/chars/Char3.png':
                    attack = 1820
                    defense = 1430
                    speed = 2110
                elif pixel == 'img/chars/Char4.png':
                    attack = 1340
                    defense = 2010
                    speed = 2290
                elif pixel == 'img/chars/Char5.png':
                    attack = 2130
                    defense = 1080
                    speed = 2330
                elif pixel == 'img/chars/Char6.png':
                    attack = 1550
                    defense = 2140 
                    speed = 2620
                elif pixel == 'img/chars/Char7.png':
                    attack = 1750
                    defense = 1720
                    speed = 1370
                elif pixel == 'img/chars/Char8.png':
                    attack = 1420
                    defense = 1940
                    speed = 2030
                elif pixel == 'img/chars/Char9.png':
                    attack = 1710
                    defense = 2250
                    speed = 1340
                elif pixel == 'img/chars/Char10.png':
                    attack = 2260
                    defense = 1620
                    speed = 1470
                elif pixel == 'img/chars/Char11.png':
                    attack = 1310
                    defense = 2040
                    speed = 1920
                elif pixel == 'img/chars/Char12.png':
                    attack = 1700
                    defense = 1530
                    speed = 1280
                elif pixel == 'img/chars/Char13.png':
                    attack = 1610
                    defense = 1400
                    speed = 1940
                elif pixel == 'img/chars/Char14.png':
                    attack = 1900
                    defense = 1330
                    speed = 1870
                elif pixel == 'img/chars/Char15.png':
                    attack = 1900
                    defense = 1150
                    speed = 1890
                elif pixel == 'img/chars/Char16.png':
                    attack = 1460
                    defense = 2520
                    speed = 2090
                elif pixel == 'img/chars/Char17.png':
                    attack = 1690
                    defense = 1450
                    speed = 2190
                elif pixel == 'img/chars/Char18.png':
                    attack = 1470
                    defense = 1930
                    speed = 1870
                elif pixel == 'img/chars/Char19.png':
                    attack = 2350
                    defense = 790
                    speed = 2000
                elif pixel == 'img/chars/Char20.png':
                    attack = 1630
                    defense = 1950
                    speed = 2420
                elif pixel == 'img/chars/Char21.png':
                    attack = 2390
                    defense = 550
                    speed = 2720
                elif pixel == 'img/chars/Char22.png':
                    attack = 1690
                    defense = 1450
                    speed = 2070
                elif pixel == 'img/chars/Char23.png':
                    attack = 1710
                    defense = 1380
                    speed = 1870
                elif pixel == 'img/chars/Char24.png':
                    attack = 2100
                    defense = 1920
                    speed = 810
                #opponents attack and speed as they cannot go into defense mode
                if op_sprite == 'img/chars/Char1.png':
                    op_attack = 2030*0.6
                    op_speed = 1800*0.7
                elif op_sprite == 'img/chars/Char2.png':
                    op_attack = 1380*0.6
                    op_speed = 1980*0.7
                elif op_sprite == 'img/chars/Char3.png':
                    op_attack = 1820*0.6
                    op_speed = 2110*0.7
                elif op_sprite == 'img/chars/Char4.png':
                    op_attack = 1340*0.6
                    op_speed = 2290*0.7
                elif op_sprite == 'img/chars/Char5.png':
                    op_attack = 2130*0.6
                    op_speed = 2330*0.7
                elif op_sprite == 'img/chars/Char6.png':
                    op_attack = 1550*0.6
                    op_speed = 2620*0.7
                elif op_sprite == 'img/chars/Char7.png':
                    op_attack = 1750*0.6
                    op_speed = 1370*0.7
                elif op_sprite == 'img/chars/Char8.png':
                    op_attack = 1420*0.6
                    op_speed = 2030*0.7
                elif op_sprite == 'img/chars/Char9.png':
                    op_attack = 1710*0.6
                    op_speed = 1340*0.7
                elif op_sprite == 'img/chars/Char10.png':
                    op_attack = 2260*0.6
                    op_speed = 1470*0.7
                elif op_sprite == 'img/chars/Char11.png':
                    op_attack = 1310*0.6
                    op_speed = 1920*0.7
                elif op_sprite == 'img/chars/Char12.png':
                    op_attack = 1700*0.6
                    op_speed = 1280*0.7
                elif op_sprite == 'img/chars/Char13.png':
                    op_attack = 1610*0.6
                    op_speed = 1940*0.7
                elif op_sprite == 'img/chars/Char14.png':
                    op_attack = 1900*0.6
                    op_speed = 1870*0.7
                elif op_sprite == 'img/chars/Char15.png':
                    op_attack = 1900*0.6
                    op_speed = 1890*0.7
                elif op_sprite == 'img/chars/Char16.png':
                    op_attack = 1460*0.6
                    op_speed = 2090*0.7
                elif op_sprite == 'img/chars/Char17.png':
                    op_attack = 1690*0.6
                    op_speed = 2190*0.7
                elif op_sprite == 'img/chars/Char18.png':
                    op_attack = 1470*0.6
                    op_speed = 1870*0.7
                elif op_sprite == 'img/chars/Char19.png':
                    op_attack = 2350*0.6
                    op_speed = 2000*0.7
                elif op_sprite == 'img/chars/Char20.png':
                    op_attack = 1630*0.6
                    op_speed = 2420*0.7
                elif op_sprite == 'img/chars/Char21.png':
                    op_attack = 2390*0.6
                    op_speed = 2720*0.7
                elif op_sprite == 'img/chars/Char22.png':
                    op_attack = 1690*0.6
                    op_speed = 2070*0.7
                elif op_sprite == 'img/chars/Char23.png':
                    op_attack = 1710*0.6
                    op_speed = 1870*0.7
                elif op_sprite == 'img/chars/Char24.png':
                    op_attack = 2100*0.6
                    op_speed = 810*0.7

            elif a_pixel == 'img/A.C/Card7.jpg':
                #detecting the stats of the chars
                if pixel == 'img/chars/Char1.png':
                    attack = 2030*1.3
                    defense = 1150*1.3
                    speed = 1800*1.3
                elif pixel == 'img/chars/Char2.png':
                    attack = 1380*1.3
                    defense = 2010*1.3
                    speed = 1980*1.3
                elif pixel == 'img/chars/Char3.png':
                    attack = 1820*1.3
                    defense = 1430*1.3
                    speed = 2110*1.3
                elif pixel == 'img/chars/Char4.png':
                    attack = 1340*1.3
                    defense = 2010*1.3
                    speed = 2290*1.3
                elif pixel == 'img/chars/Char5.png':
                    attack = 2130*1.3
                    defense = 1080*1.3
                    speed = 2330*1.3
                elif pixel == 'img/chars/Char6.png':
                    attack = 1550*1.3
                    defense = 2140*1.3
                    speed = 2620*1.3
                elif pixel == 'img/chars/Char7.png':
                    attack = 1750*1.3
                    defense = 1720*1.3
                    speed = 1370*1.3
                elif pixel == 'img/chars/Char8.png':
                    attack = 1420*1.3
                    defense = 1940*1.3
                    speed = 2030*1.3
                elif pixel == 'img/chars/Char9.png':
                    attack = 1710*1.3
                    defense = 2250*1.3
                    speed = 1340*1.3
                elif pixel == 'img/chars/Char10.png':
                    attack = 2260*1.3
                    defense = 1620*1.3
                    speed = 1470*1.3
                elif pixel == 'img/chars/Char11.png':
                    attack = 1310*1.3
                    defense = 2040*1.3
                    speed = 1920*1.3
                elif pixel == 'img/chars/Char12.png':
                    attack = 1700*1.3
                    defense = 1530*1.3
                    speed = 1280*1.3
                elif pixel == 'img/chars/Char13.png':
                    attack = 1610*1.3
                    defense = 1400*1.3
                    speed = 1940*1.3
                elif pixel == 'img/chars/Char14.png':
                    attack = 1900*1.3
                    defense = 1330*1.3
                    speed = 1870*1.3
                elif pixel == 'img/chars/Char15.png':
                    attack = 1900*1.3
                    defense = 1150*1.3
                    speed = 1890*1.3
                elif pixel == 'img/chars/Char16.png':
                    attack = 1460*1.3
                    defense = 2520*1.3
                    speed = 2090*1.3
                elif pixel == 'img/chars/Char17.png':
                    attack = 1690*1.3
                    defense = 1450*1.3
                    speed = 2190*1.3
                elif pixel == 'img/chars/Char18.png':
                    attack = 1470*1.3
                    defense = 1930*1.3
                    speed = 1870*1.3
                elif pixel == 'img/chars/Char19.png':
                    attack = 2350*1.3
                    defense = 790*1.3
                    speed = 2000*1.3
                elif pixel == 'img/chars/Char20.png':
                    attack = 1630*1.3
                    defense = 1950*1.3
                    speed = 2420*1.3
                elif pixel == 'img/chars/Char21.png':
                    attack = 2390*1.3
                    defense = 550*1.3
                    speed = 2720*1.3
                elif pixel == 'img/chars/Char22.png':
                    attack = 1690*1.3
                    defense = 1450*1.3
                    speed = 2070*1.3
                elif pixel == 'img/chars/Char23.png':
                    attack = 1710*1.3
                    defense = 1380*1.3
                    speed = 1870*1.3
                elif pixel == 'img/chars/Char24.png':
                    attack = 2100*1.3
                    defense = 1920*1.3
                    speed = 810*1.3
                #opponents attack and speed as they cannot go into defense mode
                if op_sprite == 'img/chars/Char1.png':
                    op_attack = 2030
                    op_speed = 1800
                elif op_sprite == 'img/chars/Char2.png':
                    op_attack = 1380
                    op_speed = 1980
                elif op_sprite == 'img/chars/Char3.png':
                    op_attack = 1820
                    op_speed = 2110
                elif op_sprite == 'img/chars/Char4.png':
                    op_attack = 1340
                    op_speed = 2290
                elif op_sprite == 'img/chars/Char5.png':
                    op_attack = 2130
                    op_speed = 2330
                elif op_sprite == 'img/chars/Char6.png':
                    op_attack = 1550
                    op_speed = 2620
                elif op_sprite == 'img/chars/Char7.png':
                    op_attack = 1750
                    op_speed = 1370
                elif op_sprite == 'img/chars/Char8.png':
                    op_attack = 1420
                    op_speed = 2030
                elif op_sprite == 'img/chars/Char9.png':
                    op_attack = 1710
                    op_speed = 1340
                elif op_sprite == 'img/chars/Char10.png':
                    op_attack = 2260
                    op_speed = 1470
                elif op_sprite == 'img/chars/Char11.png':
                    op_attack = 1310
                    op_speed = 1920
                elif op_sprite == 'img/chars/Char12.png':
                    op_attack = 1700
                    op_speed = 1280
                elif op_sprite == 'img/chars/Char13.png':
                    op_attack = 1610
                    op_speed = 1940
                elif op_sprite == 'img/chars/Char14.png':
                    op_attack = 1900
                    op_speed = 1870
                elif op_sprite == 'img/chars/Char15.png':
                    op_attack = 1900
                    op_speed = 1890
                elif op_sprite == 'img/chars/Char16.png':
                    op_attack = 1460
                    op_speed = 2090
                elif op_sprite == 'img/chars/Char17.png':
                    op_attack = 1690
                    op_speed = 2190
                elif op_sprite == 'img/chars/Char18.png':
                    op_attack = 1470
                    op_speed = 1870
                elif op_sprite == 'img/chars/Char19.png':
                    op_attack = 2350
                    op_speed = 2000
                elif op_sprite == 'img/chars/Char20.png':
                    op_attack = 1630
                    op_speed = 2420
                elif op_sprite == 'img/chars/Char21.png':
                    op_attack = 2390
                    op_speed = 2720
                elif op_sprite == 'img/chars/Char22.png':
                    op_attack = 1690
                    op_speed = 2070
                elif op_sprite == 'img/chars/Char23.png':
                    op_attack = 1710
                    op_speed = 1870
                elif op_sprite == 'img/chars/Char24.png':
                    op_attack = 2100
                    op_speed = 810

            elif a_pixel == 'img/A.C/Card6.jpg':
                #detecting the stats of the chars
                if pixel == 'img/chars/Char1.png':
                    attack = 2030
                    defense = 1150*2
                    speed = 1800
                elif pixel == 'img/chars/Char2.png':
                    attack = 1380
                    defense = 2010*2
                    speed = 1980
                elif pixel == 'img/chars/Char3.png':
                    attack = 1820
                    defense = 1430*2
                    speed = 2110
                elif pixel == 'img/chars/Char4.png':
                    attack = 1340
                    defense = 2010*2
                    speed = 2290
                elif pixel == 'img/chars/Char5.png':
                    attack = 2130
                    defense = 1080*2
                    speed = 2330
                elif pixel == 'img/chars/Char6.png':
                    attack = 1550
                    defense = 2140*2 
                    speed = 2620
                elif pixel == 'img/chars/Char7.png':
                    attack = 1750
                    defense = 1720*2
                    speed = 1370
                elif pixel == 'img/chars/Char8.png':
                    attack = 1420
                    defense = 1940*2
                    speed = 2030
                elif pixel == 'img/chars/Char9.png':
                    attack = 1710
                    defense = 2250*2
                    speed = 1340
                elif pixel == 'img/chars/Char10.png':
                    attack = 2260
                    defense = 1620*2
                    speed = 1470
                elif pixel == 'img/chars/Char11.png':
                    attack = 1310
                    defense = 2040*2
                    speed = 1920
                elif pixel == 'img/chars/Char12.png':
                    attack = 1700
                    defense = 1530*2
                    speed = 1280
                elif pixel == 'img/chars/Char13.png':
                    attack = 1610
                    defense = 1400*2
                    speed = 1940
                elif pixel == 'img/chars/Char14.png':
                    attack = 1900
                    defense = 1330*2
                    speed = 1870
                elif pixel == 'img/chars/Char15.png':
                    attack = 1900
                    defense = 1150*2
                    speed = 1890
                elif pixel == 'img/chars/Char16.png':
                    attack = 1460
                    defense = 2520*2
                    speed = 2090
                elif pixel == 'img/chars/Char17.png':
                    attack = 1690
                    defense = 1450*2
                    speed = 2190
                elif pixel == 'img/chars/Char18.png':
                    attack = 1470
                    defense = 1930*2
                    speed = 1870
                elif pixel == 'img/chars/Char19.png':
                    attack = 2350
                    defense = 790*2
                    speed = 2000
                elif pixel == 'img/chars/Char20.png':
                    attack = 1630
                    defense = 1950*2
                    speed = 2420
                elif pixel == 'img/chars/Char21.png':
                    attack = 2390
                    defense = 550*2
                    speed = 2720
                elif pixel == 'img/chars/Char22.png':
                    attack = 1690
                    defense = 1450*2
                    speed = 2070
                elif pixel == 'img/chars/Char23.png':
                    attack = 1710
                    defense = 1380*2
                    speed = 1870
                elif pixel == 'img/chars/Char24.png':
                    attack = 2100
                    defense = 1920*2
                    speed = 810
                #opponents attack and speed as they cannot go into defense mode
                if op_sprite == 'img/chars/Char1.png':
                    op_attack = 2030
                    op_speed = 1800
                elif op_sprite == 'img/chars/Char2.png':
                    op_attack = 1380
                    op_speed = 1980
                elif op_sprite == 'img/chars/Char3.png':
                    op_attack = 1820
                    op_speed = 2110
                elif op_sprite == 'img/chars/Char4.png':
                    op_attack = 1340
                    op_speed = 2290
                elif op_sprite == 'img/chars/Char5.png':
                    op_attack = 2130
                    op_speed = 2330
                elif op_sprite == 'img/chars/Char6.png':
                    op_attack = 1550
                    op_speed = 2620
                elif op_sprite == 'img/chars/Char7.png':
                    op_attack = 1750
                    op_speed = 1370
                elif op_sprite == 'img/chars/Char8.png':
                    op_attack = 1420
                    op_speed = 2030
                elif op_sprite == 'img/chars/Char9.png':
                    op_attack = 1710
                    op_speed = 1340
                elif op_sprite == 'img/chars/Char10.png':
                    op_attack = 2260
                    op_speed = 1470
                elif op_sprite == 'img/chars/Char11.png':
                    op_attack = 1310
                    op_speed = 1920
                elif op_sprite == 'img/chars/Char12.png':
                    op_attack = 1700
                    op_speed = 1280
                elif op_sprite == 'img/chars/Char13.png':
                    op_attack = 1610
                    op_speed = 1940
                elif op_sprite == 'img/chars/Char14.png':
                    op_attack = 1900
                    op_speed = 1870
                elif op_sprite == 'img/chars/Char15.png':
                    op_attack = 1900
                    op_speed = 1890
                elif op_sprite == 'img/chars/Char16.png':
                    op_attack = 1460
                    op_speed = 2090
                elif op_sprite == 'img/chars/Char17.png':
                    op_attack = 1690
                    op_speed = 2190
                elif op_sprite == 'img/chars/Char18.png':
                    op_attack = 1470
                    op_speed = 1870
                elif op_sprite == 'img/chars/Char19.png':
                    op_attack = 2350
                    op_speed = 2000
                elif op_sprite == 'img/chars/Char20.png':
                    op_attack = 1630
                    op_speed = 2420
                elif op_sprite == 'img/chars/Char21.png':
                    op_attack = 2390
                    op_speed = 2720
                elif op_sprite == 'img/chars/Char22.png':
                    op_attack = 1690
                    op_speed = 2070
                elif op_sprite == 'img/chars/Char23.png':
                    op_attack = 1710
                    op_speed = 1870
                elif op_sprite == 'img/chars/Char24.png':
                    op_attack = 2100
                    op_speed = 810
            else:
                #detecting the stats of the chars
                if pixel == 'img/chars/Char1.png':
                    attack = 2030
                    defense = 1150
                    speed = 1800
                elif pixel == 'img/chars/Char2.png':
                    attack = 1380
                    defense = 2010
                    speed = 1980
                elif pixel == 'img/chars/Char3.png':
                    attack = 1820
                    defense = 1430
                    speed = 2110
                elif pixel == 'img/chars/Char4.png':
                    attack = 1340
                    defense = 2010
                    speed = 2290
                elif pixel == 'img/chars/Char5.png':
                    attack = 2130
                    defense = 1080
                    speed = 2330
                elif pixel == 'img/chars/Char6.png':
                    attack = 1550
                    defense = 2140
                    speed = 2620
                elif pixel == 'img/chars/Char7.png':
                    attack = 1750
                    defense = 1720
                    speed = 1370
                elif pixel == 'img/chars/Char8.png':
                    attack = 1420
                    defense = 1940
                    speed = 2030
                elif pixel == 'img/chars/Char9.png':
                    attack = 1710
                    defense = 2250
                    speed = 1340
                elif pixel == 'img/chars/Char10.png':
                    attack = 2260
                    defense = 1620
                    speed = 1470
                elif pixel == 'img/chars/Char11.png':
                    attack = 1310
                    defense = 2040
                    speed = 1920
                elif pixel == 'img/chars/Char12.png':
                    attack = 1700
                    defense = 1530*2
                    speed = 1280
                elif pixel == 'img/chars/Char13.png':
                    attack = 1610
                    defense = 1400
                    speed = 1940
                elif pixel == 'img/chars/Char14.png':
                    attack = 1900
                    defense = 1330
                    speed = 1870
                elif pixel == 'img/chars/Char15.png':
                    attack = 1900
                    defense = 1150
                    speed = 1890
                elif pixel == 'img/chars/Char16.png':
                    attack = 1460
                    defense = 2520
                    speed = 2090
                elif pixel == 'img/chars/Char17.png':
                    attack = 1690
                    defense = 1450
                    speed = 2190
                elif pixel == 'img/chars/Char18.png':
                    attack = 1470
                    defense = 1930
                    speed = 1870
                elif pixel == 'img/chars/Char19.png':
                    attack = 2350
                    defense = 790
                    speed = 2000
                elif pixel == 'img/chars/Char20.png':
                    attack = 1630
                    defense = 1950
                    speed = 2420
                elif pixel == 'img/chars/Char21.png':
                    attack = 2390
                    defense = 550
                    speed = 2720
                elif pixel == 'img/chars/Char22.png':
                    attack = 1690
                    defense = 1450
                    speed = 2070
                elif pixel == 'img/chars/Char23.png':
                    attack = 1710
                    defense = 1380
                    speed = 1870
                elif pixel == 'img/chars/Char24.png':
                    attack = 2100
                    defense = 1920
                    speed = 810
                #opponents attack and speed as they cannot go into defense mode
                if op_sprite == 'img/chars/Char1.png':
                    op_attack = 2030
                    op_speed = 1800
                elif op_sprite == 'img/chars/Char2.png':
                    op_attack = 1380
                    op_speed = 1980
                elif op_sprite == 'img/chars/Char3.png':
                    op_attack = 1820
                    op_speed = 2110
                elif op_sprite == 'img/chars/Char4.png':
                    op_attack = 1340
                    op_speed = 2290
                elif op_sprite == 'img/chars/Char5.png':
                    op_attack = 2130
                    op_speed = 2330
                elif op_sprite == 'img/chars/Char6.png':
                    op_attack = 1550
                    op_speed = 2620
                elif op_sprite == 'img/chars/Char7.png':
                    op_attack = 1750
                    op_speed = 1370
                elif op_sprite == 'img/chars/Char8.png':
                    op_attack = 1420
                    op_speed = 2030
                elif op_sprite == 'img/chars/Char9.png':
                    op_attack = 1710
                    op_speed = 1340
                elif op_sprite == 'img/chars/Char10.png':
                    op_attack = 2260
                    op_speed = 1470
                elif op_sprite == 'img/chars/Char11.png':
                    op_attack = 1310
                    op_speed = 1920
                elif op_sprite == 'img/chars/Char12.png':
                    op_attack = 1700
                    op_speed = 1280
                elif op_sprite == 'img/chars/Char13.png':
                    op_attack = 1610
                    op_speed = 1940
                elif op_sprite == 'img/chars/Char14.png':
                    op_attack = 1900
                    op_speed = 1870
                elif op_sprite == 'img/chars/Char15.png':
                    op_attack = 1900
                    op_speed = 1890
                elif op_sprite == 'img/chars/Char16.png':
                    op_attack = 1460
                    op_speed = 2090
                elif op_sprite == 'img/chars/Char17.png':
                    op_attack = 1690
                    op_speed = 2190
                elif op_sprite == 'img/chars/Char18.png':
                    op_attack = 1470
                    op_speed = 1870
                elif op_sprite == 'img/chars/Char19.png':
                    op_attack = 2350
                    op_speed = 2000
                elif op_sprite == 'img/chars/Char20.png':
                    op_attack = 1630
                    op_speed = 2420
                elif op_sprite == 'img/chars/Char21.png':
                    op_attack = 2390
                    op_speed = 2720
                elif op_sprite == 'img/chars/Char22.png':
                    op_attack = 1690
                    op_speed = 2070
                elif op_sprite == 'img/chars/Char23.png':
                    op_attack = 1710
                    op_speed = 1870
                elif op_sprite == 'img/chars/Char24.png':
                    op_attack = 2100
                    op_speed = 810
                    
            a_pixel = 'img/pixel.png'
            own_ability_zone = False
            
                    
            if a_pixel == 'img/A.C/Card2.jpg':
                dmg = op_attack
                op_life_points -= dmg
                op_active_zone = False
            else:
                if attack_mode:
                    #damage
                    if attack > op_attack:
                        dmg = attack - op_attack
                        if speed >= op_speed+300:
                            dmg = round(dmg * 1.2)
                            op_life_points -= dmg
                        elif speed >= op_speed+600:
                            dmg = round(dmg * 1.5)
                            op_life_points -= dmg
                        elif speed <= op_speed-200:
                            dmg = round(dmg * 0.9)
                            op_life_points -= dmg
                        else:
                            op_life_points -= dmg
                        op_active_zone = False
                    if attack < op_attack:
                        dmg = op_attack - attack
                        if a_pixel == 'img/A.C/Card1.jpg':
                            dmg = 0
                        if op_speed >= speed+300:
                            dmg = round(dmg * 1.2)
                            if a_pixel == 'img/A.C/Card5.jpg':
                                op_life_points -= dmg
                                a_pixel = 'img/pixel.png'
                                own_ability_zone = False
                            else:
                                life_points -= dmg
                        elif op_speed >= speed+600:
                            dmg = round(dmg * 1.5)
                            if a_pixel == 'img/A.C/Card5.jpg':
                                op_life_points -= dmg
                                a_pixel = 'img/pixel.png'
                                own_ability_zone = False
                            else:
                                life_points -= dmg
                                
                        elif op_speed <= speed-200:
                            dmg = round(dmg * 0.9)
                            if a_pixel == 'img/A.C/Card5.jpg':
                                op_life_points -= dmg
                                a_pixel = 'img/pixel.png'
                                own_ability_zone = False
                            else:
                                life_points -= dmg
                        else:
                            life_points -= dmg
                        own_active_zone = False
                        pixel = 'img/pixel.png'
                    if attack == op_attack:
                        op_active_zone = False
                        own_active_zone = False
                        pixel = 'img/pixel.png'
                        
                if defense_mode:
                    if defense > op_attack:
                        dmg = defense - op_attack
                        if speed >= op_speed+300:
                            dmg = round(dmg * 1.2)
                            op_life_points -=dmg
                        else:
                            op_life_points -=dmg
                        op_active_zone = False
                    if defense < op_attack:
                        dmg = op_attack - defense
                        if a_pixel == 'img/A.C/Card1.jpg':
                            dmg = 0
                        if speed <= op_speed:
                            dmg = round(dmg * 0.5)
                            if a_pixel == 'img/A.C/Card5.jpg':
                                op_life_points -= dmg
                                a_pixel = 'img/pixel.png'
                                own_ability_zone = False
                            else:
                                life_points -= dmg
                        else:
                            dmg = 200
                            if a_pixel == 'img/A.C/Card5.jpg':
                                op_life_points -= dmg
                                a_pixel = 'img/pixel.png'
                                own_ability_zone = False
                            else:
                                life_points -= dmg
                        own_active_zone = False
                        pixel = 'img/pixel.png'
                    if defense == op_attack:
                        dmg = 200
                        life_points += dmg
                        op_active_zone = False
                        own_active_zone = False
                        pixel = 'img/pixel.png'

        #gen the life point text
        vital1 = font.render(str(life_points), 1, (0, 0, 255))
        vital2 = font.render(str(op_life_points), 1, (255, 0, 0))

        if key[K_TAB]:
            #change the bool value to change the card for battle
            own_active_zone = False
        if key[K_RSHIFT]:
            #change the bool value to change the card for ability cards
            own_ability_zone = False
        if life_points <= 0 and op_life_points > 0:
            #Detecting the computer as the winner and brings up the loss screen
            screen.blit(def_screen, (0,0))
            pygame.display.update()
            pygame.mixer.music.stop()
            choice = randint(0,1)
            pygame.mixer.music.load('defeat/' + str(defeat_music[choice]))
            #pygame.mixer.music.play()
            pygame.time.wait(60000)
            pygame.mixer.music.stop()
            pygame.quit()
            exit()
        if op_life_points <= 0 and life_points > 0:
            #Detecting the player as the winner and brings up the win screen
            screen.blit(vic_screen, (0,0))
            pygame.display.update()
            pygame.mixer.music.stop()
            choice = randint(0,1)
            pygame.mixer.music.load('victory/' + str(victory_music[choice]))
            #pygame.mixer.music.play()
            pygame.time.wait(60000)
            pygame.mixer.music.stop()
            pygame.quit()
            exit()

        #displaying the background
        screen.blit(background, (0, 0))
        #display the first card
        screen.blit(load_card0, (x0, y0))
        #display second card
        screen.blit(load_card1, (x1, y0))
        #display third card
        screen.blit(load_card2, (x2, y0))

        #display the first ability card
        screen.blit(a_load_card0, (345, y0+10))
        #display second ability card
        screen.blit(a_load_card1, (425, y0+10))
        #display third ability card
        screen.blit(a_load_card2, (505, y0+10))
        
        #displaying card in battle
        screen.blit(card_in_battle, (x1+30, 300))

        #displaying ability card in battle
        screen.blit(a_card_in_battle, (440, 300))
        
        #displaying enemy card in battle
        screen.blit(op_card, (x1+30, 60))
        #displaying life points
        screen.blit(vital1, (400, 245))
        #display opp life points
        screen.blit(vital2, (400, 195))
        #updating screen
        
        #FPS is set to 10
        
        startTime = time.time()
        clock.tick(10)
        t -= (time.time() - startTime)
        if t <= 0:
            if op_life_points > life_points:
                #Detecting the computer as the winner and brings up the loss screen
                screen.blit(def_screen_timeout, (0,0))
                pygame.display.update()
                pygame.mixer.music.stop()
                choice = randint(0,1)
                pygame.mixer.music.load('defeat/' + str(defeat_music[choice]))
                #pygame.mixer.music.play()
                pygame.time.wait(60000)
                pygame.mixer.music.stop()
                pygame.quit()
                exit()
            elif op_life_points < life_points:
                #Detecting the player as the winner and brings up the win screen
                screen.blit(vic_screen_timeout, (0,0))
                pygame.display.update()
                pygame.mixer.music.stop()
                choice = randint(0,1)
                pygame.mixer.music.load('victory/' + str(victory_music[choice]))
                #pygame.mixer.music.play()
                pygame.time.wait(50000)
                pygame.mixer.music.stop()
                pygame.quit()
                exit()
            else:
                #Detecting the player as the winner and brings up the win screen
                screen.blit(draw_screen, (0,0))
                pygame.display.update()
                pygame.time.wait(10000)
                pygame.mixer.music.stop()
                pygame.quit()
                exit()

        startTime = time.time()
        timer(screen, t)
        time_passed = clock.tick(10)
        pygame.display.update()
        
        
main()


import pygame
from pygame.locals import *
from random import randint
from random import shuffle
from sys import exit
import os

#starting pygame and music for pygame
pygame.init()
##pygame.mixer.init()
#creating the scrren of 600x600
screen = pygame.display.set_mode((600,600), 0, 32)

#generates the number to select the bg
#then uses the no to find that bg and loads it
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
t = 60 * 12

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

for files in os.listdir('victory'):
    if files.endswith('.mp3'):
        victory_music.append(files)
        
for files in os.listdir('defeat'):
    if files.endswith('.mp3'):
        defeat_music.append(files)

#generating the starting cards and loading them
card0 = randint(1, 24)
card_sprite0 = 'img/chars/Char' + str(card0) + '.png'
load_card0 = pygame.image.load(card_sprite0).convert_alpha()
card1 = randint(1, 24)
card_sprite1 = 'img/chars/Char' + str(card1) + '.png'
load_card1 = pygame.image.load(card_sprite1).convert_alpha()
card2 = randint(1, 24)
card_sprite2 = 'img/chars/Char' + str(card2) + '.png'
load_card2 = pygame.image.load(card_sprite2).convert_alpha()

#setting the life points & enemy life points
life_points = 5000
op_life_points = 5000
#setting the fonts
font = pygame.font.SysFont('helvetica', 50)
# setting the coordinates for the cards
x0 = 45
y0 = 460
x1 = 145
x2 = 245


# generating the null image for the battle field
pixel = 'img/null.png'
#Bool variable that checks if there is a card in the active zone
own_active_zone = False
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

#gen the life point text
vital1 = font.render(str(life_points), 1, (0, 0, 255))
vital2 = font.render(str(op_life_points), 1, (255, 0, 0))

#displaying the background
screen.blit(background, (0, 0))
#display the first card
screen.blit(load_card0, (x0, y0))
#display second card
screen.blit(load_card1, (x1, y0))
#display third card
screen.blit(load_card2, (x2, y0))
#displaying life points
screen.blit(vital1, (400, 345))
#display opp life points
screen.blit(vital2, (400, 295))


pygame.display.update()

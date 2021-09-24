# Bong! - A Pong-like game with Python and PyGame
# With Single Player (vs A.I.) and Two Player Modes
# Author: Nikos-Nikitas
# GitHub: nikosnikitas

import pygame as pg
from random import randint
from pygame_colors import *
from window_settings import *

#for images path
#import os

# Game Loop (Check for events, process, render to the screen) function
# For Single Player mode
def single_player():
    # Calling the font and pygame to initialize
    pg.font.init()
    pg.init()

    # Player width, height and speed
    PW, PH, PS = 80, 10, 5

    # Player x and y axis
    P1X, P1Y = 240, 480
    P2X, P2Y = randint(0, 240), 20
    
    # For Player 2: P2X = 240
    # For AI: P2X = randint(0, 240)
    
    # Ball x,y axis, width (W), height (H), speed (S)
    # Ball appears in a random position
    BX, BY, BW, BH = randint(25,250), randint(120,240), 8, 8
    BS = 4
    
    # defining the game's font
    game_font = pg.font.SysFont('FreeMono', 40)

    # The score values
    SCORE1_VALUE = 0
    SCORE2_VALUE = 0

    #Clock for setting the game FPS
    clock = pg.time.Clock()
    run = True

    while run:
        
        #Update the display to render
        pg.display.update()
        
        #Set the FPS clock for the game to run consistently on all platforms
        clock.tick(FPS)
        
        draw_window()
        
        # Making two goals to count the scores later
        goal1 = pg.draw.rect(WINDOW, BLACK, (0, 495, WIDTH, 5), 0)
        goal2 = pg.draw.rect(WINDOW, BLACK, (0, 5, WIDTH, 5), 0)

        # Draw our players
        p1 = pg.draw.rect(WINDOW, WHITE, (P1X, P1Y, PW, PH), 0)
        p2 = pg.draw.rect(WINDOW, WHITE, (P2X, P2Y, PW, PH), 0)

        # Draw our ball
        ball = pg.draw.rect(WINDOW, WHITE, (BX, BY, BW, BH), 0)

    # score 1 and score2 text to be rendered on the screen
        score1 = game_font.render(f"{SCORE1_VALUE}", False, WHITE)
        score2 = game_font.render(f"{SCORE2_VALUE}", False, WHITE)

# Update the scores on the screen
        WINDOW.blit(score1, (10, 350))
        WINDOW.blit(score2, (10, 150))

# Possible Improvements:

# 1) Add rectangles as hitboxes for the sides.
#        right_hitbox = pg.draw.rect(WINDOW, GREEN, (495, 0, 5, HEIGHT), 0)
#        left_hitbox = pg.draw.rect(WINDOW, GREEN, (0, 495, 5, HEIGHT), 0)
# 2) Check for hitbox collisions.


# Experimental Feature: GUI menu window instead of CLI

        #check for events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        # Put all keys pressed in a list
        keys = pg.key.get_pressed()
        
#         if keys[pg.K_UP]:
#             P1Y -= PS
# 
#         if keys[pg.K_DOWN]:
#             P1Y += PS
    
# Random direction for the AI
        ai_dir = randint(1, 100)

        if P2X > PS:
            P2X -= PS

        if P2X < WIDTH - PS -PW:
            P2X += PS

        if ai_dir in range(4):
            P2X = BX
        
        else:
            P2X += PS
            P2X -= PS
            ai_dir = randint(1,100)
            BX += randint(0, 2)

# Detect keys pressed and bind player to the screen's limit.
# For Player 1
        if keys[pg.K_LEFT] and P1X > PS:
            P1X -= PS

        if keys[pg.K_RIGHT] and P1X < WIDTH - PS - PW:
            P1X += PS
# For Player 2

        #if keys[pg.K_a] and P2X > PS:
         #   P2X -= PS

        #if keys[pg.K_d] and P2X < WIDTH - PS - PW:
         #   P2X += PS
         
            
# Bind Ball to the screen limits, make it return to the center
# Check ball and player collisions.

        if BY < HEIGHT:
            BY += BS

        if BX < WIDTH:
            BX += randint(-2,2)

        if (BY > HEIGHT) or (BY > WIDTH):
            BX, BY = 250, 250

        if (BX >= WIDTH) or (BX >= HEIGHT):
            BX, BY = 250, 250


        #if BY < P2Y:
        #    BX, BY = 250, 250

        if p1.colliderect(ball):
            BS = -4

        if p2.colliderect(ball):
            BS = 4

        # Check if ball collides with the goal to increase score
        if BY in range(5):
            SCORE1_VALUE += 1

        if BY > 495:
            SCORE2_VALUE += 1

        # Move ball
        #ball.move_ip(BS, BS)

    #Quit the game when window closes
    pg.quit()

# For 2 Player mode
def two_player():

    pg.font.init()
    pg.init()
    
    # Player width, height and speed
    PW, PH, PS = 80, 10, 5

    # Player x and y axis
    P1X, P1Y = 240, 480
    P2X, P2Y = randint(0, 240), 20
    
    # For Player 2: P2X = 240
    # For AI: P2X = randint(0, 240)
    
    # Ball x,y axis, width (W), height (H), speed (S)
    # Ball appears in a random position
    BX, BY, BW, BH = randint(25,250), randint(120,240), 8, 8
    BS = 4
    
    # defining the game's font
    game_font = pg.font.SysFont('FreeMono', 40)

    # The score values
    SCORE1_VALUE = 0
    SCORE2_VALUE = 0

    #Clock for setting the game FPS
    clock = pg.time.Clock()
    run = True

    while run:
        
        #Update the display to render
        pg.display.update()
        
        #Set the FPS clock for the game to run consistently on all platforms
        clock.tick(FPS)
        
        draw_window()
        
        # Making two goals to count the scores later
        goal1 = pg.draw.rect(WINDOW, BLACK, (0, 495, WIDTH, 5), 0)
        goal2 = pg.draw.rect(WINDOW, BLACK, (0, 5, WIDTH, 5), 0)

        # Draw our players
        p1 = pg.draw.rect(WINDOW, WHITE, (P1X, P1Y, PW, PH), 0)
        p2 = pg.draw.rect(WINDOW, WHITE, (P2X, P2Y, PW, PH), 0)

        # Draw our ball
        ball = pg.draw.rect(WINDOW, WHITE, (BX, BY, BW, BH), 0)

    # score 1 and score2 text to be rendered on the screen
        score1 = game_font.render(f"{SCORE1_VALUE}", False, WHITE)
        score2 = game_font.render(f"{SCORE2_VALUE}", False, WHITE)

# Update the scores on the screen
        WINDOW.blit(score1, (10, 350))
        WINDOW.blit(score2, (10, 150))

        #check for events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        # Put all keys pressed in a list
        keys = pg.key.get_pressed()
        
#         if keys[pg.K_UP]:
#             P1Y -= PS
# 
#         if keys[pg.K_DOWN]:
#             P1Y += PS
    

# Detect keys pressed and bind player to the screen's limit.
# For Player 1
        if keys[pg.K_LEFT] and P1X > PS:
            P1X -= PS

        if keys[pg.K_RIGHT] and P1X < WIDTH - PS - PW:
            P1X += PS
# For Player 2

        if keys[pg.K_a] and P2X > PS:
            P2X -= PS

        if keys[pg.K_d] and P2X < WIDTH - PS - PW:
            P2X += PS
         
            
# Bind Ball to the screen limits, make it return to the center
# Check ball and player collisions.

        if BY < HEIGHT:
            BY += BS

        if BX < WIDTH:
            BX += randint(-2,2)

        if (BY > HEIGHT) or (BY > WIDTH):
            BX, BY = 250, 250

        if (BX >= WIDTH) or (BX >= HEIGHT):
            BX, BY = 250, 250


        #if BY < P2Y:
        #    BX, BY = 250, 250

        if p1.colliderect(ball):
            BS = -4

        if p2.colliderect(ball):
            BS = 4

        # Check if ball collides with the goal to increase score
        if BY in range(5):
            SCORE1_VALUE += 1

        if BY > 495:
            SCORE2_VALUE += 1

        # Move ball
        #ball.move_ip(BS, BS)

    #Quit the game when window closes
    pg.quit()

# Our main menu
def main():
    
    pg.font.init()
    pg.init()
    
    # Making the menu, checking for events and rendering
    clock = pg.time.Clock()
    in_menu = True
    title_font = pg.font.SysFont('FreeMono', 40)
    author_font = pg.font.SysFont("FreeMono", 20)
    
    while in_menu:
        
        pg.display.update()
        
        clock.tick()
        draw_window()
        
        title = title_font.render("Bong!", False, WHITE)
        author = author_font.render("A Pong-like game by Nikos-Nikitas", False, WHITE)
        singleplayer = author_font.render("[1] - Single Player", False, WHITE)
        twoplayer = author_font.render("[2] - Two Players", False, WHITE)
        
        # single_player and two_player rects to get the position
        sp_r = singleplayer.get_rect()
        tp_r = twoplayer.get_rect()

        mouse = pg.mouse.get_pos()
        
        WINDOW.blit(title, (250, 50))
        WINDOW.blit(author, (50, 100))
        WINDOW.blit(singleplayer, (250, 250-90))
        WINDOW.blit(twoplayer, (250, 250-45))
        
        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                in_menu = False
            
            keys = pg.key.get_pressed()
        
            if keys[pg.K_1]:
                single_player()
            
            if keys[pg.K_2]:
                two_player()

    pg.quit()

# Command Line interface menu
#def cli_main():
# importing sys to exit from the menu
#    import sys
# importing time to delay
#    import time
# 
#     print("BONG! \nA Pong-like game in Python 3 and PyGame!\nAuthor: Nikos-Nikitas\nGitHub: nikosnikitas")
# 
#     ch = int(input("Select Your Game Mode\n\n [1] Single Player\t[2] 2 Players\t[3] Exit\n > "))
#     try:    
#         if ch == 1:
#             single_player()
#         
#         elif ch == 2:
#             two_player()
#         
#         elif ch == 3:
#             sys.exit(0)
#         
#         else:
#             print("Please select either 1, 2, or 3.")
#             time.sleep(3)
#             main()
# 
#     except ValueError:
#         print("Please insert a number (1, 2 or 3).")
#         time.sleep(3)
#         main()

# When this file runs main() runs
if __name__ == '__main__':
    main()

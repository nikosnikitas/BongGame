# window_settings - A template with common window settings for pygame.
#------------------------------------------------------
# Author: Nikos-Nikitas
# GitHub: nikosnikitas
#------------------------------------------------------
# Just import them like:
# from window_settings import *
# And use them as you like!
# You can change the values to the ones you need and use it.

# importing pygame of course!
import pygame as pg

# importing the pygame_colors as a set of colors for pygame.
from pygame_colors import *

# Game FPS
FPS = 60

# Window Settings
WIDTH, HEIGHT = 500, 500
WINDOW = pg.display.set_mode([WIDTH,HEIGHT])
pg.display.set_caption("PyGame Template - nikosnikitas")

# Background image as an example to draw images.
# BG = pg.image.load(os.path.join("Assets", "background.png"))

# Draw a green circle as an example to draw shapes.
#def draw_circle(circle_color):
#    pg.draw.circle(WINDOW, circle_color, (250, 250), 75)


# Draw the window
def draw_window():
# process/do stuff        
    WINDOW.fill(BLACK)
    
    # circle draw example
    #draw_circle(GREEN)
    # draw the image you want
    # WINDOW.blit(BG, (200, 200))
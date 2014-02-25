##############################################################################
# microburst.py                                                              #
# current contributors: Sam Weiss                                            #
#                                                                            #
# This file will contain the main game loop as well as some supporting       #
# functions for the Microburst burst.                                        #
##############################################################################

import pygame, os, sys, random
from pygame.locals import *

'''
+----------------------------------------------------------------------------+
|                                                                            |
|                          Game Sprite Definitions                           |
|                                                                            |
+----------------------------------------------------------------------------+
'''





'''
+----------------------------------------------------------------------------+
|                                                                            |
|                          Main Execution code                               |
|                                                                            |
+----------------------------------------------------------------------------+
'''
def quit():
    '''quits the game if the game quit signal is provided'''
    pygame.quit()
    sys.exit(0)

#setup pygame and the window                                                       \

pygame.init
screenDimensions = (800, 600)
window = pygame.display.set_mode(screenDimensions, pygame.RESIZABLE)
pygame.display.set_caption('Laser.py')
screen = pygame.display.get_surface()
background = pygame.Surface(screen.get_size())
pressed = []
clock = pygame.time.Clock()
FPS = 50
pygame.time.set_timer(USEREVENT + 1, 1000)
objects = []

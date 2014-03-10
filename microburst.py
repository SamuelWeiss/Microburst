##############################################################################
# microburst.py                                                              #
# current contributors: Sam Weiss                                            #
#                                                                            #
# This file will contain the main game loop as well as some supporting       #
# functions for the Microburst burst.                                        #
##############################################################################

import pygame, os, sys, random, time
from pygame.locals import *

'''
+----------------------------------------------------------------------------+
|                                                                            |
|                          Game Sprite Definitions                           |
|                                                                            |
+----------------------------------------------------------------------------+
'''
class sprite_base(pygame.sprite.Sprite):
    '''a base class for objects to streamline'''
    def load_image(self, image_name):
    '''load the image for the sprite'''
        try:
            image = pygame.image.load(image_name)
        except pygame.error, message:
            print "Cannot load image: " + image_name
            raise SystemExit, message
        return image.convert_alpha()

    def __init__(self, screen, x, y, dx, dy, img_name):
        '''intit values that are in every sprite'''
        self.image = self.load_image(img_name)
        self.screen = screen
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rect = self.image.get_rect()
        self.image_w, self.image_h = self.image.get_size()
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

    def draw(self):
        '''call the screen draw function'''
        '''angles'''
        self.screen.blit(self.image, (self.x, self.y))

    def update(self):
        '''check to make sure that moving will not move you out of bounds'''
        if self.x + self.dx > 0 and self.x + self.dx < screen.width - self.image_w:
            self.x += self.dx
        if self.y + self.dy > 0 and self.y+self.dy < (screen.width - self.image_h):
            self.y += self.dy
        '''update the rectangle if it does not'''
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

class player(sprite_base):
    '''create a class for the player'''
    '''load, init, and draw will all be the same as the base'''
    def update(self, keys):
        for i in keys:
            if i == "UP":
                self.dy = - 3
            elif i == "DOWN":
                self.dy = 3
            elif i == "LEFT":
                self.dx = - 3
            elif i == "RIGHT":
                self.dx = 3
        super.update()



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

#setup pygame and the window

pygame.init
screenDimensions = (800, 600)
window = pygame.display.set_mode(screenDimensions, pygame.RESIZABLE)
pygame.display.set_caption('Microbust')
screen = pygame.display.get_surface()
background = pygame.Surface(screen.get_size())
pressed = []
clock = pygame.time.Clock()
'''limit framerate to 60 FPS'''
FPS = 60
'''game length in seconds'''
gamelength = 240
pygame.time.set_timer(USEREVENT + 1, 1000)
'''keep track of the opjects'''
objects = []
'''keep track of what screen we're on'''
screen = 1
while True:
    clock.tick(FPS)
    if screen == 1:
        '''draw some intro screen'''
    elif:
        for l in objects:
            l.draw()
            l.update()
        pygame.display.flip()
        if(time.clock() - gamestart >= gamelength):
            screen += 1
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                elif event.key == K_UP:
                    pressed.append("UP")
                elif event.key == K_DOWN:
                    pressed.append("DOWN")
                elif event.key == K_LEFT:
                    pressed.append("LEFT")
                elif event.key == K_RIGHT:
                    pressed.append("RIGHT")
                elif event.key == K_SPACE:
                    pressed.append("SPACE")
            elif event.type == KEYUP:
                if event.key == K_UP:
                    pressed.remove("UP")
                elif event.key == K_DOWN:
                    pressed.remove("DOWN")
                elif event.key == K_LEFT:
                    pressed.remove("LEFT")
                elif event.key == K_RIGHT:
                    pressed.remove("RIGHT")
                elif event.key == K_SPACE:
                    pressed.remove("SPACE")
                        

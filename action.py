# ICS3U
# Assignment 2: Action
# <Arsalan Khan>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
# Don't forget to import your class
from snow import Snow
import pygame
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (150, 190, 255)

# Set the screen size
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snow Animation")

#Create list
all_snow = pygame.sprite.Group()

snowflake = Snow(BLUE, 100, 0)

all_snow.add

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Background image - https://nl.aliexpress.com/item/10X10ft-Winter-backdrop-Vinyl-Photography-Backdrops-props-photography-Background-NDT23/32264655459.html
background = pygame.image.load("snowbackground.jpg")

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT : # Player clicked close button
            carryOn = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                carryOn=False

    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_UP]:
        #mySnow.moveUp(5)
    #if keys[pygame.K_DOWN]:
        #mySnow.moveDown

    # --- Game logic goes here
    snow.update()
    
    # --- Draw code goes here


    # Background
    screen.blit(background, (0, 0))
    
    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()

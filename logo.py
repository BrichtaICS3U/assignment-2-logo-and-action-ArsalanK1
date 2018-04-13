# ICS3U
# Assignment 2: Logo
# <your name>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import math
import pygame
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (77, 121, 255)
YELLOW = (255, 214, 51)

# Set the screen size (please don't change this)
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SHIELD Logo")

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # --- Game logic goes here
    # There should be none for a static image
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)

    # Queue different shapes and lines to be drawn
    # pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)
    #GRID
    pygame.draw.line(screen, BLACK, [0, 100], [400, 100], 1)
    pygame.draw.line(screen, BLACK, [0, 200], [400, 200], 1)
    pygame.draw.line(screen, BLACK, [0, 300], [400, 300], 1)
    pygame.draw.line(screen, BLACK, [100, 0], [100, 400], 1)
    pygame.draw.line(screen, BLACK, [200, 0], [200, 400], 1)
    pygame.draw.line(screen, BLACK, [300, 0], [300, 400], 1)
    #CIRCLES
    pygame.draw.ellipse(screen, BLACK, [50,50, 300, 300], 0)
    pygame.draw.ellipse(screen, WHITE, [63,63, 275, 275], 0)
    #MIDDLE SEP
    pygame.draw.line(screen, BLACK, [75, 125], [200, 200], 16)
    pygame.draw.line(screen, BLACK, [325, 125], [200, 200], 16)
    #WINGS LEFT
    pygame.draw.line(screen, BLACK, [107, 143], [60, 237], 13)
    pygame.draw.line(screen, BLACK, [140, 160], [80, 283], 13)
    pygame.draw.line(screen, BLACK, [175, 185], [110, 313], 13)
    #WINGS RIGHT
    pygame.draw.line(screen, BLACK, [293, 143], [340, 235], 13)
    pygame.draw.line(screen, BLACK, [260, 160], [320, 280], 13)
    pygame.draw.line(screen, BLACK, [225, 185], [290, 313], 12)
    #HEAD LEFT
    pygame.draw.rect(screen, BLACK, [145, 60, 110, 13], 0)
    pygame.draw.polygon(screen, BLACK, [[110, 85], [170, 120], [190, 55]], 0)
    #HEAD RIGHT
    pygame.draw.polygon(screen, BLACK, [[290, 85], [230, 120], [210, 55]], 0)
    pygame.draw.polygon(screen, WHITE, [[210, 73], [230, 73], [235, 83], [210, 83]], 0)
    

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()

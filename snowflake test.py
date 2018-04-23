import pygame

BLUE = (150, 190, 255)
WHITE = (255, 255, 255)

SCREENWIDTH = 400
SCREENHEIGHT = 400

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snowflake Test")

carryOn = True

clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    screen.fill(BLUE)

    pygame.draw.line(screen, WHITE, [200, 100], [200, 300], 4)
    pygame.draw.line(screen, WHITE, [100, 200], [300, 200], 4)
    pygame.draw.line(screen, WHITE, [125, 275], [275, 125], 6)
    pygame.draw.line(screen, WHITE, [125, 125], [275, 275], 6)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

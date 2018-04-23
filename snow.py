import pygame

WHITE = (255, 255, 255)
BLUE = (150, 190, 255)

class Snow(pygame.sprite.Sprite):
     def __init__(self, colour, width, height, speed):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
        self.image.set_colourkey(BLUE)

        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

        
        pygame.draw.line(screen, WHITE, [200, 100], [200, 300], 4)
        pygame.draw.line(screen, WHITE, [100, 200], [300, 200], 4)
        pygame.draw.line(screen, WHITE, [125, 275], [275, 125], 6)
        pygame.draw.line(screen, WHITE, [125, 125], [275, 275], 6)
        
        self.rect = self.image.get_rect()

     def moveDown(self, pixels):
          self.rect.y += self.speed * speed / 20

     def changeSpeed(self, speed):
          self.speed = speed
          

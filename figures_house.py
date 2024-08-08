import pygame
from pygame.color import THECOLORS
import sys

pygame.init()

screen = pygame.display.set_mode((1000, 800))
screen.fill(THECOLORS['blue'])
walls = pygame.Rect(350, 350, 400, 400)
pygame.draw.rect(screen, THECOLORS['yellow'], walls, 0)
window = pygame.Rect(475, 460, 150, 150)
pygame.draw.rect(screen, THECOLORS['blue'], window, 0)
roof = [(330, 350), (770, 350), (550, 200)]
pygame.draw.polygon(screen, (155, 155, 155), roof, width=0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
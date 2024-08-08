import pygame
from pygame.color import THECOLORS
import sys

pygame.init()

screen = pygame.display.set_mode((1000, 800))
screen.fill(THECOLORS['orange'])
r = pygame.Rect(50, 50, 100, 200)
pygame.draw.line(screen, (0, 255, 0), (150, 250), (300, 250), width=1)
pygame.draw.lines(screen, (0, 0, 255), True, [(500, 500), (650, 600), (700, 700)], width=1)
# pygame.draw.rect(screen, (255, 0, 0), r, 0)
pygame.draw.circle(screen, (255, 0, 0), (350, 350), 50, width=0)
pygame.draw.ellipse(screen, (255, 255, 0), r, width=0)
pygame.draw.polygon(screen, (255, 0, 255), [(400, 400), (550, 500), (600, 600)], width=0)

font = pygame.font.SysFont('couriernew', 40)
text = font.render(str('HELLO'), True, THECOLORS['green'])
screen.blit(text, (50, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
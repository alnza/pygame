import random
import os
import pygame
from pygame.color import THECOLORS
import sys

WIDTH = 1000
HEIGHT = 800

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(THECOLORS['orange'])

# настройка папки ассетов
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join(img_folder, 'p1_jump.png')).convert()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.image.set_colorkey(THECOLORS['black'])
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        self.rect.y += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.centerx > HEIGHT:
            self.rect.bottom = 0


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    all_sprites.update()

    screen.fill(THECOLORS['black'])
    all_sprites.draw(screen)
    pygame.display.flip()

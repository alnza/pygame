import pygame
import random

import ctypes

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

WIDTH = round(user32.GetSystemMetrics(0) * 0.97)  # ширина игрового окна
HEIGHT = round(user32.GetSystemMetrics(1) * 0.97)  # высота игрового окна
FPS = 30  # частота кадров в секунду

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Цикл игры
running = True
while running:
    # Ввод процесса (события)
    # Обновление
    # Визуализация (сборка)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
    # Рендеринг
    screen.fill(BLACK)
    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()
    # держим цикл на правильной скорости
    clock.tick(FPS)

pygame.quit()

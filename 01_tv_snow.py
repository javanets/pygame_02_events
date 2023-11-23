import pygame
import random


# Задание:
#
#   Сделайте так, чтобы программа выводила экран "ненастроенного телевизора"
#   со случайно меняющейся "рябью" из белых точек.
#

def draw(screen):
    width, height = screen.get_width(), screen.get_height()
    for i in range(10000):
        screen.fill(pygame.Color('white'), (random.random() * width, random.random() * height, 1, 1))


size = 600, 400
screen = pygame.display.set_mode(size)

pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # ...

pygame.quit()

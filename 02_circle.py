import pygame
from game.objects import Circle

# Задание:
#
#   1. Изучите класс Circle из модуля game.objects (см. файл objects.py в папке game).
#   2. Создайте объект circle класса Circle и с помощью его методов выведите на экран круг
#      красного цвета радиуса 20 с центром в точке (0, 200).
#   3. Сделайте так, чтобы круг двигался вправо со скоростью 50 пикселей в секунду.
#

FRAMES_PER_SECOND = 50
clock = pygame.time.Clock()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

circle = ...

pygame.init()

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # ...

pygame.quit()

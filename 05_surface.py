import pygame
from game.objects import Rectangle

# Задание:
#   Изучите код примера и доработайте его так, чтобы при нажатии на правую кнопку мыши
#   вместо прямоугольника создавался круг зеленого цвета случайного радиуса и перемещался
#   бы вслед за курсором до тех пор, пока мышь нажата. Изменять радиус круга не нужно.
#   Воспользуйтесь классом game.objects.Circle.
#

FRAMES_PER_SECOND = 50
clock = pygame.time.Clock()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

surface = pygame.Surface(screen.get_size())

new_rect = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_rect = Rectangle((0, 0, 255), event.pos, (0, 0), 5)
        if event.type == pygame.MOUSEBUTTONUP:
            surface.blit(screen, (0, 0))
            new_rect = None
        if event.type == pygame.MOUSEMOTION:
            if new_rect:
                x, y = new_rect.get_position()
                width, height = event.pos[0] - x, event.pos[1] - y
                new_rect.set_size((width, height))

    screen.fill(pygame.Color('black'))
    screen.blit(surface, (0, 0))

    if new_rect:
        new_rect.draw(screen)
    pygame.display.flip()
pygame.quit()

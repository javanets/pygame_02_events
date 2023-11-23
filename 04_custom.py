import pygame
from game.objects import Circle

# Задание:
#   Изучите код примера и доработайте его так, чтобы радиус круга увеличивался
#   на 1 пиксель каждые 100 миллисекунд.
#   Воспользуйтесь для этого кастомным событием INCREASE_RADIUS.
#

FRAMES_PER_SECOND = 50
clock = pygame.time.Clock()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

INCREASE_RADIUS = pygame.USEREVENT + 17
pygame.time.set_timer(INCREASE_RADIUS, 100)

circle = None

pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            if not circle:
                circle = Circle((0, 0, 255), (0, 200), 20)
            circle.set_position(event.pos)

        # ... реализуйте обработку других событий ...

    screen.fill((0, 0, 0))
    if circle:
        circle.draw(screen)

    pygame.display.flip()
    clock.tick(50)

pygame.quit()

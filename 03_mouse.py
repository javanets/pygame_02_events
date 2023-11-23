import pygame
from game.objects import Circle

# Задание:
#   1. Изучите код примера и добейтесь, чтобы он выводил синий круг радиуса 20,
#      центр которого следует за двигающимся курсором мыши.
#   2. Изучите метод Circle.increase и сделайте так, чтобы при нажатии на левую
#      кнопку мыши радиус круга увеличивался на 5 пикселей, а при нажатии на
#      правую кнопку уменьшался на 5 пикселей.
#   3. Изучите атрибуты x и y события pygame.MOUSEWHEEL (например, выведите их с помощью print)
#      и сделайте так, чтобы радиус круга увеличивался на 1 пиксель при движении колесиком мыши
#      "к себе" и уменьшался на 1 пиксель при движении "от себя".

FRAMES_PER_SECOND = 50
clock = pygame.time.Clock()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

circle = None

pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            if circle is None:
                circle = ...
            circle.set_position(event.pos)

        # ... реализуйте обработку других событий ...

    # ... отрисуйте текущий кадр ...

    pygame.display.flip()
    clock.tick(50)

pygame.quit()

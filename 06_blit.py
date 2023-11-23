import pygame

# Задание:
#   Изучите класс game.objects.Number и реализуйте следующий функционал:
#   1. При нажатии на кнопку мыши в месте касания возникает новое число 0,
#      отрисованное шрифтом размера 20. Цвет пусть выбирается случайным образом.
#   2. Каждые 100 миллисекунд шрифт каждого выведенного числа должен увеличиваться на 1.
#   3. Один раз в секунду все выведенные числа должны увеличиваться на 1.
#   4. При нажатии на клавишу пробел экран должен очищаться.
#
#   Для реализации пунктов 2 и 3 создайте пользовательские события INCREASE_SIZE и INCREASE_NUMBER.
#

FRAMES_PER_SECOND = 50
clock = pygame.time.Clock()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

# ... создайте пользовательские события ...

surface = pygame.Surface(screen.get_size())

numbers = []  # ... здесь будут храниться разноцветные числа

pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ... реализуйте обработку других событий ... #

    screen.fill(pygame.Color('black'))
    # ... отрисуйте разноцветные числа ...

    pygame.display.flip()

    clock.tick(FRAMES_PER_SECOND)

pygame.quit()

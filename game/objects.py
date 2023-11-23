import pygame


class Circle:
    def __init__(self, color, position, radius):
        self.color = color
        self.position = position
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def offset(self, dx, dy):
        x, y = self.position
        self.position = (x + dx, y + dy)

    def set_position(self, value):
        self.position = value

    def increase(self, dr):
        self.radius += dr


class Rectangle:
    def __init__(self, color, position, size, line_width):
        self.color = color
        self.position = position
        self.size = size
        self.line_width = line_width

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position, self.size), self.line_width)

    def get_position(self):
        return self.position
    def set_position(self, value):
        self.position = value

    def get_size(self):
        return self.size

    def set_size(self, value):
        self.size = value


class Number:
    def __init__(self, color, position, font_size):
        self.color = color
        self.position = position
        self.font_size = font_size
        self.font = pygame.font.Font(None, font_size)
        self.value = 0

    def draw(self, screen):
        text = self.font.render(str(self.value), True, self.color)
        screen.blit(text, self.position)

    def increment(self):
        self.value += 1

    def increase(self):
        self.font_size += 1
        self.font = pygame.font.Font(None, self.font_size)

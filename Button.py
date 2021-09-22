import pygame
from parameters import *
import game_process as gp

class Button:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen, x, y, action, *args, text=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            if click[0] and action is not None:
                action(*args)

        pygame.draw.rect(screen, self.color, (x, y, self.width, self.height))

        if text is not None:
            gp.print_text(screen, text, x, y)

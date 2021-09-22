import pygame
from parameters import *
from Button import *
import game_process as gp
import menu

def exit_menu(screen, clock):

    pygame.draw.rect(screen, white, (100, 100, 300, 100), width=1)
    kek = Button(50, 40, blue)
    kek2 = Button(50, 40, red)
    gp.print_text(screen, 'Ты дебил', 110, 110)
    kek.draw(screen, 110, 150, quit, text='YES')
    kek2.draw(screen, 160, 150, menu.menu_screen, screen, 480, 640, 120, clock, text='NO')
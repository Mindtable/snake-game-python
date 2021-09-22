import pygame
import game_process
import menu
from exit_menu import *



def death_screen(screen, screen_height, fps, clock, point):
    death_ground = pygame.image.load('death_ground.jpeg').convert()
    done = False
    exit_menu_flag = False
    while not done:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()
                if keystate[pygame.K_SPACE]:
                    game_process.game_process(screen, 480, 640, fps, clock)
                if keystate[pygame.K_BACKSPACE]:
                    menu.menu_screen(screen, 480, 640, 120, clock)
                if keystate[pygame.K_ESCAPE]:
                    exit_menu_flag = True
                    print(exit_menu_flag)

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), [500, 0, 230, screen_height], width=1)
        screen.blit(death_ground, (0, 0))
        if exit_menu_flag:
            exit_menu(screen, clock)
        game_process.print_text(screen, 'Result -- ' + str(point), 520, 20, 24)
        pygame.display.flip()

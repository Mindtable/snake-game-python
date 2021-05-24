import pygame
import game_process
import menu
def death_screen(surface, screen_height, fps, clock, point):
    death_ground = pygame.image.load('death_ground.jpeg').convert()
    done = False
    while not done:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()
                if keystate[pygame.K_SPACE]:
                    game_process.game_process(surface, 480, 640, fps, clock)
                if keystate[pygame.K_BACKSPACE]:
                    menu.menu_screen(surface, 480, 640, 120, clock)

        surface.fill((0, 0, 0))
        pygame.draw.rect(surface, (255, 255, 255), [500, 0, 230, screen_height], width=1)
        surface.blit(death_ground, (0, 0))
        game_process.print_text(surface, 'Result -- ' + str(point), 520, 20, 24)
        pygame.display.flip()

import pygame as pg

pg.init()
screen = pg.display.set_mode((740, 660))
pg.display.set_caption("testing")

FPS = 120
done = False
clock = pg.time.Clock()
while not done:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            keystate = pg.key.get_pressed()
            print(keystate[pg.K_BACKSPACE])

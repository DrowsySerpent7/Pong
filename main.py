import pygame as pg

pg.init()

# Define properties
x_axis = 1280
y_axis = 800
run = True
screen = pg.display.set_mode((x_axis, y_axis))
pg.display.set_caption("Pong")
player = pg.image.load("player_pong_sprite.png" ).convert_alpha()
player_rect = player.get_rect()
player_rect.topleft = (50, 200)

# player_pos = pg.Vector2(screen, screen.get_width() / 2, screen.get_height() / 2)


# Game loop
while run:
    # Check for events every frame
    for event in pg.event.get():

        # End game when closed
        if event.type == pg.QUIT:
            run = False

    screen.fill("gray")
    screen.blit(player, (player_rect))
    
    pg.display.flip()
    pg.display.update()

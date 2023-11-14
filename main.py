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
clock = pg.time.Clock()


def handle_keys():
    """Handles key down logic for player movement."""
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        player_rect.move_ip(0, -6)
    if keys[pg.K_DOWN]:
        player_rect.move_ip(0, 6)


# Game loop
while run:
    # Check for events every frame
    for event in pg.event.get():

        # End game when closed
        if event.type == pg.QUIT:
            run = False


    screen.fill("gray")
    screen.blit(player, (player_rect))
    handle_keys()
    
    clock.tick(60)
    pg.display.flip()
    pg.display.update()

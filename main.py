import pygame as pg

pg.init()

# Define properties
x_axis = 1280
y_axis = 800
run = True
pg.display.set_caption("Pong")
clock = pg.time.Clock()

pp_court = pg.image.load("pong_court.png")
screen = pg.display.set_mode((x_axis, y_axis))
screen.get_rect()

playerl_pos = (80, 400)
playerl = pg.image.load("player_pong_sprite.png" ).convert_alpha()
playerl_rect = playerl.get_rect()
playerl_rect.center = (playerl_pos)

game_ball = pg.image.load("ball_pong_sprite.png" ).convert_alpha()
ball_start_pos = (x_axis / 2 + 2, y_axis / 2 - 2)
game_ball_rect = game_ball.get_rect()
game_ball_rect.center = (ball_start_pos)


# Movement for playerL
def handle_keys():
    """Handles key down logic for player movement."""
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        playerl_rect.move_ip(0, -6)
    if keys[pg.K_s]:
        playerl_rect.move_ip(0, 6)


# Game loop
while run:
    # Check for events every frame
    for event in pg.event.get():

        # End game when closed
        if event.type == pg.QUIT:
            run = False


    screen.blit(pp_court,(0, 0))
    screen.blit(game_ball, game_ball_rect)
    screen.blit(playerl, playerl_rect)
    handle_keys()
    
    clock.tick(65)
    pg.display.flip()
    pg.display.update()

import pygame as pg
from player import Player
from ball import Ball


pg.init()
x_axis, y_axis = 1280, 800
pg.display.set_caption("Pong")
pp_court = pg.image.load("sprites/pong_court.png")
screen = pg.display.set_mode((x_axis, y_axis))
center_pos = (x_axis / 2 + 1, y_axis / 2 - 1)
window_rect = screen.get_rect()
clock = pg.time.Clock()
run = True


paddle1 = Player("sprites/player_left_sprite.png", (80, 400))
paddle2 = Player("sprites/player_right_sprite.png", (1200, 400))
ball = Ball("sprites/ball_sprite.png", center_pos)


def handle_keys():
    """Handles key down logic for player movement."""
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        paddle1.player_rect.move_ip(0, -6)
    if keys[pg.K_s]:
        paddle1.player_rect.move_ip(0, 6)
    if  keys[pg.K_UP]:
        paddle2.player_rect.move_ip(0, -6)
    if keys[pg.K_DOWN]:
        paddle2.player_rect.move_ip(0, 6)

# Game loop
while run:
    # Check for events every frame
    for event in pg.event.get():

        # End game when closed
        if event.type == pg.QUIT:
            run = False

    screen.blit(pp_court,(0, 0))
    screen.blit(ball.ball, ball.ball_rect)
    screen.blit(paddle1.player, paddle1.player_rect)
    screen.blit(paddle2.player, paddle2.player_rect)
    handle_keys()
    
    clock.tick(65)
    pg.display.flip()
    pg.display.update()
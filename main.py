import pygame as pg
from player import Player
pg.init()

# Define properties
x_axis = 1280
y_axis = 800
run = True
pg.display.set_caption("Pong")
clock = pg.time.Clock()

pp_court = pg.image.load("pong_court.png")
screen = pg.display.set_mode((x_axis, y_axis))
window_rect = screen.get_rect()
paddle1 = Player("player_pong_sprite.png",)

playerl_pos = (80, 400)
playerl = pg.image.load("player_pong_sprite.png" ).convert_alpha()
playerl_rect = playerl.get_rect()
playerl_rect.center = (playerl_pos)

player_r_pos = (1200, 400)
player_r = pg.image.load("player_left_pong_sprite.png" ).convert_alpha()
player_r_rect = player_r.get_rect()
player_r_rect.center = (player_r_pos)

game_ball = pg.image.load("ball_pong_sprite.png" ).convert_alpha()
ball_start_pos = (x_axis / 2 + 1, y_axis / 2 - 1)
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
    if  keys[pg.K_UP]:
        player_r_rect.move_ip(0, -6)
    if keys[pg.K_DOWN]:
        player_r_rect.move_ip(0, 6)


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
    screen.blit(player_r, player_r_rect)
    handle_keys()
    
    clock.tick(65)
    pg.display.flip()
    pg.display.update()

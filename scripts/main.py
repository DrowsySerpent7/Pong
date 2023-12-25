import pygame
from player import Player
from ball import Ball
from npo import NPO
import configs
import sys
import table


pygame.init()

paddle1 = Player("sprites/player_left_sprite.png", table.p1_start_pos)
paddle2 = Player("sprites/player_right_sprite.png", table.p2_start_pos)
ball = Ball("sprites/ball_sprite.png", configs.center_screen)

# Game loop
while configs.run:
    # Blit a new surface to the display object.
    configs.screen.blit(configs.pp_court,(0, 0))
    configs.screen.blit(ball.ball, ball.ball_rect)
    configs.screen.blit(paddle1.player, paddle1.player_rect)
    configs.screen.blit(paddle2.player, paddle2.player_rect)

    paddle1.handle_player1_keys()
    paddle2.handle_player2_keys()


    ball.ball_rect.move_ip(ball.speed) # Move the ball

    # Score
    if ball.ball_rect.right >= configs.x_axis:
        table.p1_score += 1
        print(table.p1_score)
        # Reset function here

    if ball.ball_rect.left <= 0:
        table.p2_score += 1
        print(table.p2_score)
        # Reset function here


    # Set the barriers for the ball and change its direction on collision
    if ball.ball_rect.top <= 0 or ball.ball_rect.bottom >= configs.y_axis:
        ball.speed[1] = -ball.speed[1]

    if ball.ball_rect.colliderect(paddle1.player_rect):
        ball.speed[0] = -ball.speed[0]

    if ball.ball_rect.colliderect(paddle2.player_rect):
        ball.speed[0] = -ball.speed[0]


    # Check for events every frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            configs.run = False
            sys.exit()

    pygame.display.flip()
    pygame.display.update()
    configs.clock.tick(65)
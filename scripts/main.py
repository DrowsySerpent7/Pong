import pygame
from player import Player
from ball import Ball
from npo import NPO
import configs
import sys
import table

pygame.init()


def game_start():
    paddle1 = Player("sprites/player_left_sprite.png", table.p1_start)
    paddle2 = Player("sprites/player_right_sprite.png", table.p2_start)
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
        table.display_score()
        table.display_time()

        # Reset ball and paddle after scoring
        # REFACTOR ME
        if ball.ball_rect.x >= configs.x_axis:
            del ball.ball
            del paddle1
            del paddle2

            ball = Ball("sprites/ball_sprite.png", configs.center_screen)
            paddle1 = Player("sprites/player_left_sprite.png", table.p1_start)
            paddle2 = Player("sprites/player_right_sprite.png", table.p2_start)

            configs.screen.blit(paddle1.player, paddle1.player_rect)
            configs.screen.blit(paddle2.player, paddle2.player_rect)
            configs.screen.blit(ball.ball, ball.ball_rect)
            table.scoreA += 1


        if ball.ball_rect.x <= 0:
            del ball.ball
            del paddle1
            del paddle2

            ball = Ball("sprites/ball_sprite.png", configs.center_screen)
            paddle1 = Player("sprites/player_left_sprite.png", table.p1_start)
            paddle2 = Player("sprites/player_right_sprite.png", table.p2_start)

            configs.screen.blit(paddle1.player, paddle1.player_rect)
            configs.screen.blit(paddle2.player, paddle2.player_rect)
            configs.screen.blit(ball.ball, ball.ball_rect)
            table.scoreB += 1

        # Move the ball
        ball.ball_rect.move_ip(ball.velocity)

        # Set the barriers for the ball and change its direction on collision
        if ball.ball_rect.top <= 0 or ball.ball_rect.bottom >= configs.y_axis:
            ball.velocity[1] = -ball.velocity[1]

        if ball.ball_rect.colliderect(paddle1.player_rect):
            ball.velocity[0] = -ball.velocity[0]
        elif ball.ball_rect.collidepoint(paddle1.player_rect.midtop or paddle1.player_rect.midbottom):
            ball.velocity[0] = -ball.velocity[0]

        if ball.ball_rect.colliderect(paddle2.player_rect):
            ball.velocity[0] = -ball.velocity[0]
        elif ball.ball_rect.collidepoint(paddle2.player_rect.midtop or paddle1.player_rect.midbottom):
            ball.velocity[0] = -ball.velocity[0] 

        # Check for events every frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                configs.run = False
                sys.exit()
            

       
        pygame.display.flip()
        pygame.display.update()
        configs.clock.tick(65)

game_start()
from main import main
import pygame as pg

x_axis = 1280
y_axis = 800

class Ball:
    def __init__(self, game_ball, ball_start_pos, game_ball_rect):
        """Ball object"""
        self.game_ball = game_ball
        self.ball_start_pos
        self.game_ball_rect

        self.game_ball = pg.image.load("ball_pong_sprite.png" ).convert_alpha()
        self.ball_start_pos = (x_axis / 2 + 1, y_axis / 2 - 1)
        self.game_ball_rect = self.game_ball.get_rect()
        self.game_ball_rect.center = (self.ball_start_pos)
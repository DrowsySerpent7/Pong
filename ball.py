import pygame as pg
pg.init()


class Ball:
    def __init__(self, ball_image="", start_pos=()):
        """Ball object"""
        self.ball_image = ball_image
        self.start_pos = start_pos
        self.ball = pg.image.load(ball_image).convert_alpha()
        self.ball_rect = self.ball.get_rect()
        self.ball_rect.center = self.start_pos
        self.speed = 5
        self.velocity = 0

    def move_ball(self):
        """acceleration of the ball object."""

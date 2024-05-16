import pygame
import random

pygame.init()
speed = 6.0

class Ball:
    def __init__(self, ball_image="", ball_pos=[]):
        """Ball object"""
        self.ball_image = ball_image
        self.ball_pos = ball_pos
        self.ball = pygame.image.load(ball_image).convert_alpha()
        self.ball_rect = self.ball.get_rect()
        self.ball_rect.center = self.ball_pos
        self.velocity = [speed, speed]
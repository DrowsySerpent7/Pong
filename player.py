import pygame as pg

pg.init()

keys = pg.key.get_pressed()

# Refactoring player mechanic
class Player:

    def __init__(self, player_image="", player_pos=()):
        """Blueprint to player object."""

        self.player_pos = player_pos
        self.player_image = player_image
        self.player = pg.image.load(self.player_image).convert_alpha()
        self.player_rect = self.player.get_rect()
        self.player_rect.center = (self.player_pos)
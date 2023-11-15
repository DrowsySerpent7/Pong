import pygame as pg

pg.init()


keys = pg.key.get_pressed()

# Refactoring player mechanic
class Player:

    def __init__(self, player_image="", player_pos=()):
        """Blueprint to player object."""

        self.player_pos = player_pos
        self.player_image = player_image


    def handle_keys(self, player_rect, move_up=(0,-6), move_down=(0,6), keyup=[], keydwn=[]):
        """Handles key down logic for player movement."""

        self.player_rect = player_rect
        self.move_up = move_up
        self.move_down = move_down
        self.keydwn = keydwn
        self.keyup = keyup

        keydwn = keys
        keyup = keys
        if keydwn:
            player_rect.move_ip(move_up)
        if keyup:
            player_rect.move_ip(move_down)

player_1 = player("player_pong_sprite.png", (80, 400))
player_1.handle_keys()
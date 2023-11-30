import pygame as pg

pg.init()

keys = pg.key.get_pressed()

# Refactoring player mechanic
class Player:

    def __init__(self, player, player_image="", player_pos=()):
        """Blueprint to player object."""

        self.player_pos = player_pos
        self.player_image = player_image
        self.player = player
        self.player = pg.image.load(self.player_image).convert_alpha()


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

    
    # def handle_keys(self, playerl_rect, player_r_rect):
    #     """Handles key down logic for player movement."""
    #     keys = pg.key.get_pressed()
    #     if keys[pg.K_w]:
    #         playerl_rect.move_ip(0, -6)
    #     if keys[pg.K_s]:
    #         playerl_rect.move_ip(0, 6)
    #     if  keys[pg.K_UP]:
    #         player_r_rect.move_ip(0, -6)
    #     if keys[pg.K_DOWN]:
    #         player_r_rect.move_ip(0, 6)

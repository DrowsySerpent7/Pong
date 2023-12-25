import pygame
import configs

pygame.init()

keys = pygame.key.get_pressed()

# Refactoring player mechanic
class Player:

    def __init__(self, player_image="", player_pos=()):
        """Blueprint to player object."""

        self.player_pos = player_pos
        self.player_image = player_image
        self.player = pygame.image.load(self.player_image).convert_alpha()
        self.player_rect = self.player.get_rect()
        self.player_rect.center = (self.player_pos)
    
    
    def handle_player1_keys(self):
        """Handles key down logic for player movement."""
        keys = pygame.key.get_pressed()

        # User pressing ""
        if keys[pygame.K_w]:
            self.player_rect.move_ip(0, -6)

            if self.player_rect.top == configs.window_rect.top:
                self.player_rect.move_ip(0, 6)
                
        elif keys[pygame.K_s]:
            self.player_rect.move_ip(0, 6)

            if self.player_rect.bottom == configs.window_rect.bottom:
                self.player_rect.move_ip(0, -6)

    
    def handle_player2_keys(self):
        """Coop player2 key movement"""
        keys = pygame.key.get_pressed()
        
        # User pressing ""
        if keys[pygame.K_UP]:
            self.player_rect.move_ip(0, -6)

            if self.player_rect.top == configs.window_rect.top:
                self.player_rect.move_ip(0, 6)               

        elif keys[pygame.K_DOWN]:
            self.player_rect.move_ip(0, 6)

            if self.player_rect.bottom == configs.window_rect.bottom:
                self.player_rect.move_ip(0, -6)
        
        
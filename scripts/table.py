import pygame

pygame.init()

p1_score = 0
p2_score = 0
p1_start_pos = (80, 400)
p2_start_pos = (1200, 400)

score_font = pygame.font.Font("fonts/digital_tech.otf", 20)

class Table():
    """Contains table functionality such as score keeping
    and serving to a certain side after player scores."""

    def __init__(self) -> None:
        """Initialization"""

    def keep_score(self):
        """Keep score for goals."""
        score_font.render("0")

import pygame
import configs as cf

pygame.init()

scoreA = 0
scoreB = 0
countdown = 5
game_over = False
p1_start = (80, 400)
p2_start = (1200, 400)
WHITE = (255,255,255)
CREAM = (255,253,208)

def display_score():
    """Handle score reputition"""
    font = pygame.font.Font("fonts/digital_tech.otf", 75)

    text = font.render(str(scoreA), 1, WHITE)
    cf.screen.blit(text, (900, 10))
    
    text = font.render(str(scoreB), 1, WHITE)
    cf.screen.blit(text, (340, 10))

def display_time():
    """Keep track of the time limit"""
    clock = pygame.font.Font("fonts/digital_tech.otf", 33)

    # time = clock.render(str(countdown), 1, CREAM)
    # cf.screen.blit(time, cf.center_screen)
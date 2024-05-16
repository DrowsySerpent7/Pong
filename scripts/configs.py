import pygame

x_axis, y_axis = 1280, 800
pygame.display.set_caption("Pong")
pp_court = pygame.image.load("sprites/pong_court.png")
screen = pygame.display.set_mode((x_axis, y_axis))
center_screen = [x_axis / 2, y_axis / 2]
window_rect = screen.get_rect()
run = True
clock = pygame.time.Clock()


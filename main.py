import pygame as pg

pg.init()

# Define properties
x_axis = 800
y_axis = 800
bg_color = 'blue'
run = True
screen = pg.display.set_mode((x_axis, y_axis))


# Game loop
while run:
    # Check for events every frame
    for event in pg.event.get():

        # End game when closed
        if event.type == pg.QUIT:
            run = False
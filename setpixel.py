import pygame

# create Pygame surface with dimensions 100x100
screen = pygame.display.set_mode((100, 100))

# fill Pygame surface with solid black color
color = (0, 0, 0)
screen.fill(color)

# Start the main loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # if the user closes the window, quit the loop
            running = False

    # update the display
    pygame.display.update()

# quit Pygame gracefully
pygame.quit()
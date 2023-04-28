import pygame

# Initialize pygame
pygame.init()

# Set screen size
screen_size = (500, 500)

# Create matrix and initialize with zeros
matrix = [[0 for j in range(50)] for i in range(50)]

# Set a pixel at position (10, 10)
matrix[10][10] = 1

# Create screen with the same size as matrix
screen = pygame.display.set_mode(screen_size)

# Function to update screen based on matrix
def update_screen(matrix):
    for i in range(50):
        for j in range(50):
            if matrix[i][j] == 1:
                pygame.draw.rect(screen, (255, 255, 255), (i*10, j*10, 10, 10))
            else:
                pygame.draw.rect(screen, (0, 0, 0), (i*10, j*10, 10, 10))

# Game loop
while True:
    # Handle events
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Update screen
    update_screen(matrix)

    # Update display
    pygame.display.update()
    clock.tick(60)
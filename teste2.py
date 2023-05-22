import pygame

# Initialize Pygame
pygame.init()

# Set the window size
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# Set the game resolution
game_width = 256
game_height = 224

# Create the game surface with the game resolution
game_surface = pygame.Surface((game_width, game_height))

# Draw a red rectangle on the game surface
rectangle_color = (255, 0, 0)
rectangle_width = 200
rectangle_height = 100
rectangle_x = (game_width - rectangle_width) // 2
rectangle_y = (game_height - rectangle_height) // 2
pygame.draw.rect(game_surface, rectangle_color, (rectangle_x, rectangle_y, rectangle_width, rectangle_height))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the window
    window.fill((0, 0, 0))  # Replace with your desired background color

    # Scale the game surface onto the window surface
    scaled_game_surface = pygame.transform.scale(game_surface, (window_width, window_height))

    # Draw the scaled game surface onto the window
    window.blit(scaled_game_surface, (0, 0))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
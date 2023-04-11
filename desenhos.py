import pygame

class Screen:
    def __init__(self, tam_x, tam_y, color_fill) -> None:
        self.__tam_x = tam_x
        self.__tam_y = tam_y
        self.__color_display = color_fill
        
    
    def __configure_window(self):
        return pygame.display.set_mode((self.__tam_x, self.__tam_y))
    
    def show_window(self):
        screen = self.__configure_window()
        screen.fill(self.__color_display)

    def set_pixel(self, coord_x, coord_y, color):
        pass


class Color:
    def __init__(self, red, green, blue, transparency = False) -> None:
        if (-1 < red < 255 or -1 < green < 255 or -1 < blue < 255):
            self.__red
            self.__green = green
            self.__blue = blue
            self.__transparency = transparency
        else:
            return (0, 0, 0)

    @staticmethod
    def getRGB(self):
        return (self.__red, self.__green, self.__blue)

    
# create Pygame surface with dimensions 100x100
screen = Screen(100,100, Color(100,200,255).getRGB())

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
import pygame
 # Initialize Pygame
pygame.init()
screen_size = (1024, 768)

def main():

    def create_main_surface():
            # Create window with given size
            return pygame.display.set_mode(screen_size)

    mainSurface =  create_main_surface()
    def render_frame():
        pygame.draw.circle(mainSurface,(250,0,0),(1024/2, 768/2),200,0)
        

    
    while True:
        pygame.display.flip()
        render_frame()
        
        
main()
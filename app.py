import pygame
 # Initialize Pygame
pygame.init()
screen_size = (1024, 768)
clock = pygame.time.Clock()

def main(x_pos):
    class State:
        def __init__(self):
            self.xPos = 0
        
        def update(self, time_elapsed):
             self.xPos += time_elapsed
        def render(self):
            render_frame(self.xPos)

    circleState = State()


    def create_main_surface():
            # Create window with given size
            return pygame.display.set_mode(screen_size)
    
    mainSurface =  create_main_surface()
    def render_frame(x_pos, state):
        pygame.draw.circle(mainSurface,(250,0,0),(state.xPos, 768/2),60,0)
        
        

    
    while True:
        time_elapsed = clock.tick(60)
        time_elapsed /= 1000
        pygame.display.flip()
        circleState.render()
        circleState.update(time_elapsed)
        
        
main(1)
import pygame

pygame.init()
WIDTH  = 1600
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

LEVELS = {
    1:  64,
    2:  40,
    3:  24
}


level = 1
cell_size = LEVELS[level]

class Player:
    def __init__(self):
        self.state = "ALIVE"
        self.direction = "UP"
        self.position = (0,0)
        self.hitbox = pygame.Rect((768,704,cell_size, cell_size))

    def drawPlayer(self):
        pygame.draw.rect(screen,(255,0,0),self.hitbox)
    def change_state(self):
        self.state == "DEAD"
    
    def change_direction(self, input):
        self.direction = input
        if self.direction == "UP":
            self.hitbox.move_ip(0,-1)
        elif self.direction == "LEFT":
            self.hitbox.move_ip(-1,0)
        elif self.direction == "DOWN":
            self.hitbox.move_ip(0,1)
        elif self.direction == "RIGHT":
            self.hitbox.move_ip(1,0)
    




def draw_grid():
    cols = WIDTH // cell_size
    rows = HEIGHT // cell_size

    for x in range(cols + 1):
        pygame.draw.line(screen, (70, 70, 70), (x * cell_size, 0), (x * cell_size, HEIGHT))

    for y in range(rows + 1):
        pygame.draw.line(screen, (70, 70, 70), (0, y * cell_size), (WIDTH, y * cell_size))


def main():
    running = True
    lucas = Player()
    while running:  
        print(lucas.hitbox)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
            key = pygame.key.get_pressed()
            if key[pygame.K_q] == True:
                lucas.change_direction("LEFT")
            elif key[pygame.K_d] == True:
                lucas.change_direction("RIGHT")
            elif key[pygame.K_z] == True:
                lucas.change_direction("UP")
            elif key[pygame.K_s] == True:
                lucas.change_direction("DOWN")
        screen.fill((30, 30, 30))
        
        lucas.drawPlayer()
        draw_grid()
        pygame.display.flip()
        clock.tick(60)

main()
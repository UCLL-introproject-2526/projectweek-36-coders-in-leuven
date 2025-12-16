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

level = 3
cell_size = LEVELS[level]

def draw_grid():
    cols = WIDTH // cell_size
    rows = HEIGHT // cell_size

    for x in range(cols + 1):
        pygame.draw.line(screen, (70, 70, 70), (x * cell_size, 0), (x * cell_size, HEIGHT))

    for y in range(rows + 1):
        pygame.draw.line(screen, (70, 70, 70), (0, y * cell_size), (WIDTH, y * cell_size))


def main():
    running = True
    while running:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False      
        
        screen.fill((30, 30, 30))
        draw_grid()
        pygame.display.flip()
        clock.tick(60)

main()
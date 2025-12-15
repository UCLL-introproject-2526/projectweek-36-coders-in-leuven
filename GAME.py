import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

CELL_SIZE = 30
WIDTH, HEIGHT = screen.get_size()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    # Verticale lijnen
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (60, 60, 60), (x, 0), (x, HEIGHT))

    # Horizontale lijnen
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (60, 60, 60), (0, y), (WIDTH, y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

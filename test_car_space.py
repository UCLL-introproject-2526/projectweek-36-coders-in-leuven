import pygame

pygame.init()
WIDTH  = 1600
HEIGHT = 800

CAR_WIDTH = 200
CAR_HEIGHT = 100


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

LEVELS = {
    1:  64,
    2:  40,
    3:  24
}

level = 1
cell_size = LEVELS[level]

def draw_grid():
    cols = WIDTH // cell_size
    rows = HEIGHT // cell_size

    for x in range(cols + 1):
        pygame.draw.line(screen, (70, 70, 70), (x * cell_size, 0), (x * cell_size, HEIGHT))

    for y in range(rows + 1):
        pygame.draw.line(screen, (70, 70, 70), (0, y * cell_size), (WIDTH, y * cell_size))

def draw_car(CARS):
    for car in CARS:
        pygame.draw.rect(screen, "red", car)
    
    pygame.display.update()


def main():
    running = True

    clock = pygame.time.Clock()



    CAR_INTERVAL = 2000
    CAR_TIMER = 0

    CARS = []

    while running:

        screen.fill((30, 30, 30))
        draw_grid()

        CAR_TIMER += clock.tick(60)

        if CAR_TIMER > CAR_INTERVAL :
            car = pygame.Rect(-CAR_WIDTH, 400, CAR_WIDTH, CAR_HEIGHT)
            CARS.append(car)
            CAR_TIMER = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        
        for car in CARS[:]:
            car.x += 2
            if car.x > WIDTH:
                CARS.remove(car)

        draw_car(CARS)

        pygame.display.flip()

main()
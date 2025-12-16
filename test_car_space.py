import pygame
import random

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

def draw_grid():
    cols = WIDTH // cell_size
    rows = HEIGHT // cell_size

    for x in range(cols + 1):
        pygame.draw.line(screen, (70, 70, 70), (x * cell_size, 0), (x * cell_size, HEIGHT))

    for y in range(rows + 1):
        pygame.draw.line(screen, (70, 70, 70), (0, y * cell_size), (WIDTH, y * cell_size))

def layout_cars_lvl_1():
    CAR_WIDTH = 100
    CAR_HEIGHT = 64

    car_speed = 5

    CAR_INTERVAL = 2000

    return CAR_WIDTH, CAR_HEIGHT, car_speed, CAR_INTERVAL

def draw_car(CARS):
    for car in CARS:
        car = pygame.image.load("Images/orange_car.png")
        car_rect = car.get_rect()
        pygame.draw.rect(screen, car, car_rect)
   
    pygame.display.update()


def main():
    running = True

    clock = pygame.time.Clock()

    cols2 = WIDTH // 64
    rows2 = HEIGHT // 64

    CAR_TIMER = 0

    CARS = []

    if level == 1:
        CAR_WIDTH, CAR_HEIGHT, car_speed, CAR_INTERVAL = layout_cars_lvl_1()
     
    while running:

        screen.fill((30, 30, 30))
        draw_grid()

        CAR_TIMER += clock.tick(60)
       
        if CAR_TIMER > CAR_INTERVAL:
            y = random.randint(0,HEIGHT) // CAR_HEIGHT
            car = pygame.Rect(-CAR_WIDTH, y * CAR_HEIGHT, CAR_WIDTH, CAR_HEIGHT)
            CARS.append(car)
            CAR_TIMER = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
       
        for car in CARS[:]:
            car.x += car_speed
            if car.x > WIDTH:
                CARS.remove(car)

        draw_car(CARS)

        pygame.display.flip()

main()
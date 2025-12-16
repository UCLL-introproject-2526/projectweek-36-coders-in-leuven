import random
import pygame
import sys
from pygame.locals import *
from images import *

pygame.init()
WIDTH  = 960
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

LEVELS = {
    1:  60,
    2:  40,
    3:  30,
    "survival": 30
}

LEVEL_WALLPAPERS = {
    1: pygame.image.load('images/level_01.png'),
    # 2: pygame.image.load('images/level_02.png'),
    # 3: pygame.image.load('images/level_03.png'),
    # "survival": pygame.image.load('images/level_03.png')
}

level = 1
cell_size = LEVELS[level]
LVLbackground = LEVEL_WALLPAPERS[level]


class Player:
    def __init__(self, level):
        self.state = "ALIVE"
        self.moving = False
        self.direction = "UP"
        self.position = (0,0)
        if level == 1:
            self.hitbox = pygame.Rect((421, 540 ,cell_size, cell_size))
        elif level == 2:
            self.hitbox = pygame.Rect((440, 560 ,cell_size, cell_size))
        else:
            self.hitbox = pygame.Rect((450, 571 ,cell_size, cell_size))

    def drawPlayer(self):
        # pygame.draw.rect(screen,(255,0,0),self.hitbox)
        playerImage = pygame.image.load("Images/character_60.png")
        playerRect = pygame.transform.scale(playerImage, self.hitbox.size)
        screen.blit(playerRect, self.hitbox)
    def change_state(self):
        self.state == "DEAD"

    
    def change_direction(self, input):
        self.direction = input
        if self.direction == "UP" and self.hitbox.top > 1:
            self.hitbox.move_ip(0,-cell_size)
        elif self.direction == "LEFT" and self.hitbox.left > 1:
            self.hitbox.move_ip(-cell_size,0)
        elif self.direction == "DOWN" and self.hitbox.bottom < HEIGHT:
            self.hitbox.move_ip(0,cell_size)
        elif self.direction == "RIGHT" and self.hitbox.right < WIDTH:
            self.hitbox.move_ip(cell_size,0)  


def layout_cars_lvl_1():
    CAR_WIDTH = 100
    CAR_HEIGHT = cell_size

    car_speed = 20

    CAR_INTERVAL = 2000

    return CAR_WIDTH, CAR_HEIGHT, car_speed, CAR_INTERVAL

def draw_car(CARS):
    for car in CARS:
        carimage = pygame.image.load("Images/car60_1.png")
        car_rect = pygame.transform.scale(carimage, car.size)
        screen.blit(car_rect, car)




def draw_grid():
    cols = WIDTH // cell_size
    rows = HEIGHT // cell_size

    grid_color = (80, 80, 80)

    for x in range(cols + 1):
        pygame.draw.line(
            screen, grid_color, (x * cell_size, 0), (x * cell_size, HEIGHT), 1)

    for y in range(rows + 1):
        pygame.draw.line(
            screen, grid_color, (0, y * cell_size), (WIDTH, y * cell_size), 1        )





def main():
    clock = pygame.time.Clock()

    CAR_TIMER = 0

    CARS = []

    if level == 1:
        CAR_WIDTH, CAR_HEIGHT, car_speed, CAR_INTERVAL = layout_cars_lvl_1()

    running = True
    lucas = Player(level)
    while running:
        CAR_TIMER += clock.tick(60)
       
        if CAR_TIMER > CAR_INTERVAL:
            y = random.randint(2 * cell_size,HEIGHT - 2 * cell_size) // CAR_HEIGHT
            car = pygame.Rect(-CAR_WIDTH, y * CAR_HEIGHT, CAR_WIDTH, CAR_HEIGHT)
            CARS.append(car)
            CAR_TIMER = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    lucas.change_direction("LEFT")
                elif event.key == K_RIGHT:
                    lucas.change_direction("RIGHT")
                elif event.key == K_UP:
                    lucas.change_direction("UP")
                elif event.key == K_DOWN:
                    lucas.change_direction("DOWN")
        screen.blit(LVLbackground, (0,0))

        for car in CARS:
            if car.colliderect(lucas.hitbox):
                print("Collision")
            car.x += car_speed
            if car.x > WIDTH:
                CARS.remove(car)
        lucas.drawPlayer()
        draw_car(CARS)
        
        # draw_grid()
        pygame.display.flip()
        clock.tick(60)

main()
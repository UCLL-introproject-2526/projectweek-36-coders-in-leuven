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


level = 1
cell_size = LEVELS[level]

assert WIDTH % cell_size == 0, "Window width must be a multiple of cell size."
assert HEIGHT % cell_size == 0, "Window height must be a multiple of cell size."
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
        pygame.draw.rect(screen,(255,0,0),self.hitbox)
    def change_state(self):
        self.state == "DEAD"

    
    def change_direction(self, input, level):
        self.direction = input
        if self.direction == "UP" and self.hitbox.top > 1:
            self.hitbox.move_ip(0,-cell_size)
        elif self.direction == "LEFT" and self.hitbox.left > 1:
            self.hitbox.move_ip(-cell_size,0)
        elif self.direction == "DOWN" and self.hitbox.bottom < HEIGHT:
            self.hitbox.move_ip(0,cell_size)
        elif self.direction == "RIGHT" and self.hitbox.right < WIDTH:
            self.hitbox.move_ip(cell_size,0)  




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
    running = True
    lucas = Player(level)
    while running:
        print(lucas.hitbox)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    lucas.change_direction("LEFT", level)
                elif event.key == K_RIGHT:
                    lucas.change_direction("RIGHT", level)
                elif event.key == K_UP:
                    lucas.change_direction("UP", level)
                elif event.key == K_DOWN:
                    lucas.change_direction("DOWN", level)
        screen.fill((30, 30, 30))
        
        lucas.drawPlayer()
        # draw_grid()
        pygame.display.flip()
        clock.tick(60)

main()
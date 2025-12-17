import random
import pygame
import sys
from pygame.locals import *
from images import *

class Car:
    def __init__(self, rect, speed):
        self.rect = rect
        self.speed = speed
        self.color = random.randint(1,5)

    def update(self):
        self.rect.x += self.speed

    def draw(self):
        carimage = pygame.image.load(f"Images/car{LEVELS[level]}_{self.color}.png")
        car_scaled = pygame.transform.scale(carimage, self.rect.size)
        screen.blit(car_scaled, self.rect)

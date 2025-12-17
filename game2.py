import random
import pygame
import sys
from pygame.locals import *

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("sound/project_music.ogg")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1)

WIDTH = 960
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()

LEVELS = {1: 60, 2: 40, 3: 30}
LEVEL_WALLPAPERS = {1: pygame.image.load("images/level_01.png")}

level = 1
cell_size = LEVELS[level]
LVLbackground = LEVEL_WALLPAPERS[level]

def pause_screen():
    font = pygame.font.SysFont("Courier", 40)
    text = font.render("PAUSED", True, "white")
    pygame.mixer.music.pause()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key in (K_ESCAPE, K_p):
                paused = False
        screen.blit(LVLbackground, (0, 0))
        screen.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//2)))
        pygame.display.flip()
        clock.tick(10)
    pygame.mixer.music.unpause()

def death_screen():
    font_big = pygame.font.SysFont("Courier", 80)
    font_small = pygame.font.SysFont("Courier", 40)
    game_over = font_big.render("GAME OVER", True, "red")
    restart = font_small.render("Press R to restart", True, "white")
    pygame.mixer.music.pause()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_r:
                restart_game()
        screen.blit(LVLbackground, (0, 0))
        screen.blit(game_over, game_over.get_rect(center=(WIDTH//2, HEIGHT//2 - 40)))
        screen.blit(restart, restart.get_rect(center=(WIDTH//2, HEIGHT//2 + 40)))
        pygame.display.flip()
        clock.tick(10)

def win_screen():
    font = pygame.font.SysFont("Courier", 150)
    text = font.render("GAME WON!", True, "green")
    pygame.mixer.music.pause()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                paused = False
        pygame.mixer.music.pause()
        screen.blit(LVLbackground, (0, 0))
        screen.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//2)))
        pygame.display.flip()
    pygame.mixer.music.unpause()

def restart_game():
    pygame.mixer.music.stop()
    pygame.mixer.music.play(-1)
    main()

class Player:
    def __init__(self):
        self.state = "ALIVE"
        self.hitbox = pygame.Rect(421, 540, cell_size, cell_size)

    def draw(self):
        img = pygame.image.load(f"Images/character_{cell_size}.png")
        img = pygame.transform.scale(img, self.hitbox.size)
        screen.blit(img, self.hitbox)

    def move(self, direction):
        if self.state != "ALIVE":
            return
        if direction == "UP" and self.hitbox.top > 0:
            self.hitbox.y -= cell_size
        if direction == "DOWN" and self.hitbox.bottom < HEIGHT:
            self.hitbox.y += cell_size
        if direction == "LEFT" and self.hitbox.left > 0:
            self.hitbox.x -= cell_size
        if direction == "RIGHT" and self.hitbox.right < WIDTH:
            self.hitbox.x += cell_size

    def check_finish(self):
        if self.hitbox.top <= 40:
            win_screen()

    def die(self):
        self.state = "DEAD"
        death_screen()

class Car:
    def __init__(self, rect, speed):
        self.rect = rect
        self.speed = speed
        self.color = random.randint(1, 3)

    def update(self):
        self.rect.x += self.speed

    def draw(self):
        img = pygame.image.load(f"Images/car{cell_size}_{self.color}.png")
        img = pygame.transform.scale(img, self.rect.size)
        screen.blit(img, self.rect)

class CarManager:
    def __init__(self):
        self.cars = []
        self.timer = 0
        self.spawn_delay = 500
        self.speed = 8

    def spawn_car(self):
        y = random.randint(2, 8) * cell_size
        rect = pygame.Rect(-100, y, 100, cell_size)
        self.cars.append(Car(rect, self.speed))

    def update(self, dt, player):
        self.timer += dt
        if self.timer >= self.spawn_delay:
            self.spawn_car()
            self.timer = 0
        for car in self.cars[:]:
            car.update()
            if car.rect.colliderect(player.hitbox):
                player.die()
            if car.rect.left > WIDTH:
                self.cars.remove(car)

    def draw(self):
        for car in self.cars:
            car.draw()

def main():
    player = Player()
    cars = CarManager()
    while True:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_p:
                    pause_screen()
                if event.key == K_UP:
                    player.move("UP")
                if event.key == K_DOWN:
                    player.move("DOWN")
                if event.key == K_LEFT:
                    player.move("LEFT")
                if event.key == K_RIGHT:
                    player.move("RIGHT")
        screen.blit(LVLbackground, (0, 0))
        player.draw()
        player.check_finish()
        cars.update(dt, player)
        cars.draw()
        pygame.display.flip()

main()

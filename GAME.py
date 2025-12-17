import random
import pygame
import sys
from pygame.locals import *
from images import *

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("sound/project_music.ogg")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
hit_sound = pygame.mixer.Sound("sound/hit_sound.wav")
hit_sound.set_volume(1.5)

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
}

level = 1
cell_size = LEVELS[level]
LVLbackground = LEVEL_WALLPAPERS[level]
    
def pause_screen():
    font = pygame.font.SysFont("Courier", 40)
    text = font.render("PAUSED", True, "white")
    restart_over = font.render("Press R to restart", True, "white")
    resume = font.render("Press P to resume", True, "white")
    pygame.mixer.music.pause()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key in (K_ESCAPE, K_p):
                paused = False
            if event.type == KEYDOWN and event.key == K_r:
                restart_game()
        screen.blit(LVLbackground, (0, 0))
        screen.blit(text, text.get_rect(center=(WIDTH//2, (HEIGHT//2) - 40)))
        screen.blit(restart_over, restart_over.get_rect(center=(WIDTH//2, (HEIGHT//2))))
        screen.blit(resume, resume.get_rect(center=(WIDTH//2, ((HEIGHT//2) + 40))))

        pygame.display.flip()
        clock.tick(10)
    pygame.mixer.music.unpause()

def death_screen():
    font_big = pygame.font.SysFont("Courier", 80)
    font_small = pygame.font.SysFont("Courier", 40)
    wasted = pygame.image.load('images/wasted.png')
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
        screen.blit(wasted, game_over.get_rect(center=(WIDTH//2 - 35, HEIGHT//2 - 80)))
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
    def __init__(self, level):
        self.state = "ALIVE"
        self.direction = "UP"
        self.level = level

        size = LEVELS[level]

        self.images = {
            "UP": pygame.image.load(f"Images/character_{size}.png"),
            "DOWN": pygame.image.load(f"Images/character_{size}_front.png"),
            "LEFT": pygame.image.load(f"Images/character_{size}_left.png"),
            "RIGHT": pygame.image.load(f"Images/character_{size}_right.png"),
            "DEAD": pygame.image.load(f"Images/character_{size}_dead_no_blood.png"),
        }

        if level == 1:
            self.hitbox = pygame.Rect(421, 540, cell_size, cell_size)
        elif level == 2:
            self.hitbox = pygame.Rect(440, 560, cell_size, cell_size)
        else:
            self.hitbox = pygame.Rect(450, 571, cell_size, cell_size)

    def drawPlayer(self):
        if self.state == "ALIVE":
            image = self.images[self.direction]
        else:
            image = self.images["DEAD"]


        image = pygame.transform.scale(image, self.hitbox.size)
        screen.blit(image, self.hitbox)

    def change_state(self):
        self.state = "DEAD"
        death_screen()

    def check_finish(self):
        if self.hitbox.top <= cell_size:
            win_screen()
        


    def change_direction(self, direction):
        self.direction = direction

        if self.state != "ALIVE":
            return

        if direction == "UP" and self.hitbox.top > 0:
            self.hitbox.move_ip(0, -cell_size)
        elif direction == "DOWN" and self.hitbox.bottom < HEIGHT:
            self.hitbox.move_ip(0, cell_size)
        elif direction == "LEFT" and self.hitbox.left > 0:
            self.hitbox.move_ip(-cell_size, 0)
        elif direction == "RIGHT" and self.hitbox.right < WIDTH:
            self.hitbox.move_ip(cell_size, 0)


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
class CarManager:
    def __init__(self, level):
        self.cars = []
        self.timer = 0

        if level == 1:
            self.CAR_WIDTH = 100
            self.CAR_HEIGHT = cell_size
            self.car_speed = 8
            self.CAR_INTERVAL = 500

    def spawn_car(self):
        y = random.randint(2 * cell_size, HEIGHT - 2 * cell_size) // self.CAR_HEIGHT

        rect = pygame.Rect(-self.CAR_WIDTH,y * self.CAR_HEIGHT,self.CAR_WIDTH,self.CAR_HEIGHT)

        self.cars.append(Car(rect, self.car_speed))

    def update(self, dt, player):
        self.timer += dt
        
        if self.timer > self.CAR_INTERVAL:
            self.spawn_car()
            self.timer = 0

        for car in self.cars[:]:
            player_lane = player.hitbox.y // cell_size
            car_lane = car.rect.y // cell_size
            if player.state == "ALIVE" and player_lane == car_lane:
                if car.rect.right > player.hitbox.left and car.rect.left < player.hitbox.right:
                    player.change_state()
                    hit_sound.play()

            
            car.update()

            if car.rect.x > WIDTH:
                self.cars.remove(car)

    def draw(self):
        for car in self.cars:
            car.draw()


def main():
    running = True
    lucas = Player(level)
    car_manager = CarManager(level)

    while running:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    pause_screen()
                if event.key == K_LEFT:
                    lucas.change_direction("LEFT")
                elif event.key == K_RIGHT:
                    lucas.change_direction("RIGHT")
                elif event.key == K_UP:
                    lucas.change_direction("UP")
                elif event.key == K_DOWN:
                    lucas.change_direction("DOWN")

        screen.blit(LVLbackground, (0, 0))

        lucas.drawPlayer()
        lucas.check_finish()
        car_manager.update(dt, lucas)
        car_manager.draw()

        

        pygame.display.flip()


main()
pygame.quit()
sys.exit()

import random
import pygame
import sys
from pygame.locals import *
from images import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("sound/project_music.ogg")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1)

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
paused = False

def pause_screen():
    font = pygame.font.SysFont("Courier", 40)
    paused_text = font.render("PAUSED", True, "white")
    resume_text = font.render("ESC / P  = Resume", True, "white")
    restart_text = font.render("R = Restart", True, "white")

    pygame.mixer.music.pause()

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_p):
                    paused = False

        screen.blit(LVLbackground, (0, 0))
        screen.blit(paused_text, paused_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 60)))
        screen.blit(resume_text, resume_text.get_rect(center=(WIDTH//2, HEIGHT//2)))
        screen.blit(restart_text, restart_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 60)))

        pygame.display.flip()
        clock.tick(10)

    pygame.mixer.music.unpause()

def death_screen():
    font = pygame.font.SysFont("ByteBounce.ttf", 40)
    font_game_over = pygame.font.SysFont("ByteBounce.ttf", 80)
    death_text = font_game_over.render("GAME OVER", True, "red")
    restart_text = font.render("Press R to restart", True, "white")

    pygame.mixer.music.pause()

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_p):
                    paused = False
                elif event.key == pygame.K_r:
                    restart_game()
               

        screen.blit(LVLbackground, (0, 0))
        screen.blit(death_text, death_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 60)))
        screen.blit(restart_text, restart_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 60)))

        pygame.display.flip()
        clock.tick(10)

    pygame.mixer.music.unpause()


def restart_game():
    pygame.mixer.music.stop()
    pygame.mixer.music.play(-1)
    main()


class Player:
    def __init__(self, level):
        self.state = "ALIVE"
        self.moving = False
        self.direction = "UP"
        self.position = (0, 0)
        self.level = level

        if level == 1:
            self.hitbox = pygame.Rect((421, 540, cell_size, cell_size))
        elif level == 2:
            self.hitbox = pygame.Rect((440, 560, cell_size, cell_size))
        else:
            self.hitbox = pygame.Rect((450, 571, cell_size, cell_size))

    def drawPlayer(self):
        if self.state == "ALIVE":
            if self.level == 1:
                playerImage = pygame.image.load("Images/character_60.png")
            elif self.level == 2:
                playerImage = pygame.image.load("Images/character_40.png")
            else:
                playerImage = pygame.image.load("Images/character_60.png")

            playerRect = pygame.transform.scale(playerImage, self.hitbox.size)
            screen.blit(playerRect, self.hitbox)
           
        else:
            playerImage = pygame.image.load(f"Images/character_{LEVELS[level]}_dead.png")
            playerRect = pygame.transform.scale(playerImage, self.hitbox.size)
            screen.blit(playerRect, self.hitbox)  

    def change_state(self):        
        self.state = "DEAD"
        playerImage = pygame.image.load(f"Images/character_{LEVELS[level]}_dead.png")
        playerRect = pygame.transform.scale(playerImage, self.hitbox.size)
        screen.blit(playerRect, self.hitbox)    


    def change_direction(self, input):
        self.direction = input
        if self.state == "ALIVE":
            if self.direction == "UP" and self.hitbox.top > 1 :
                self.hitbox.move_ip(0, -cell_size)
            elif self.direction == "LEFT" and self.hitbox.left > 1:
                self.hitbox.move_ip(-cell_size, 0)
            elif self.direction == "DOWN" and self.hitbox.bottom < HEIGHT:
                self.hitbox.move_ip(0, cell_size)
            elif self.direction == "RIGHT" and self.hitbox.right < WIDTH:
                self.hitbox.move_ip(cell_size, 0)

    def finish_line(self):
        positie_y2 = list(self.position)
        positie_y = int(positie_y2[1])
        if positie_y < 120:
                pause_screen()
                screen.blit(LVLbackground, (0, 0))
                font_game_won = pygame.font.SysFont("ByteBounce.ttf", 80)
                winning_text = font_game_won.render("GAME WON", True, "red")
                screen.blit(winning_text, winning_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 60)))



       

class Car:
    def __init__(self, rect, speed):
        self.rect = rect
        self.speed = speed
        self.color = random.randint(1,3)

    def update(self):
        self.rect.x += self.speed

    def draw(self):
        carimage = pygame.image.load(
            f"Images/car{LEVELS[level]}_{self.color}.png"
        )
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
            car.update()

            if car.rect.colliderect(player.hitbox):
                player.change_state()
                death_screen()
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
                elif event.key == pygame.K_r:
                    pygame.mixer.music.unpause()
                    restart_game()
                elif event.key == K_LEFT:
                    lucas.change_direction("LEFT")
                elif event.key == K_RIGHT:
                    lucas.change_direction("RIGHT")
                elif event.key == K_UP:
                    lucas.change_direction("UP")
                elif event.key == K_DOWN:
                    lucas.change_direction("DOWN")

        screen.blit(LVLbackground, (0, 0))

        lucas.drawPlayer()

        car_manager.update(dt, lucas)
        car_manager.draw()

        pygame.display.flip()


main()
pygame.quit()
sys.exit()
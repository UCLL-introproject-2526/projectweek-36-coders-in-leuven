import random
import pygame
import sys
from pygame.locals import *
from images import *
import menu
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
pygame.display.set_caption('Road Cross')
icon = pygame.image.load('images/logo.png')
pygame.display.set_icon(icon)

LEVELS = {
    1:  60,
    2:  40,
    3:  30,
    "survival": 30
}

level = 1
cell_size = LEVELS[level]
LVLbackground = pygame.image.load(f'images/level_0{level}.png')


PLAYER_IMAGES = {
   d: pygame.image.load(f"Images/character_{cell_size}_{d}.png").convert_alpha()
   for d in ["up", "down", "left", "right"]
}
PLAYER_IMAGES["dead"] = pygame.image.load(
   f"Images/character_{cell_size}_dead.png"
).convert_alpha()

CAR_IMAGES = [
   pygame.image.load(f"Images/car{cell_size}_{i}.png").convert_alpha()
   for i in range(1, 6)
]

LEVEL1_BLOCKED_TILES = {
    (0,6), (15,6),
    (0,9), (15,9)
}

LEVEL2_BLOCKED_TILES = {
    (0,3), (1,3), (2,3), (3,3),(4,3), (6,3), (7,3), (8,3), (9,3),(10,3), (12,3), (13,3), (14,3), (15,3),(16,3), (17,3), (19,3), (20,3), (21,3),(22,3), (23,3), (24,3),
    (0,4), (1,4), (2,4), (3,4),(4,4), (6,4), (7,4), (8,4), (9,4),(10,4), (12,4), (13,4), (14,4), (15,4),(16,4), (17,4), (19,4), (20,4), (21,4),(22,4), (23,4), (24,4),
    (0,8),(23,8),
    (0,9),(23,9),
    (0,13),(1,13),(22,13),(23,13),
    (0,14),(1,14),(22,14),(23,14)
}


LEVEL3_BLOCKED_TILES = {
    (0,5),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(8,5),(9,5),(10,5),(11,5),(12,5),(13,5),(14,5),(16,5),(17,5),(18,5),(19,5),(20,5),(21,5),(22,5),(23,5),(25,5),(26,5),(27,5),(28,5),(29,5),(30,5),(31,5),
    (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(8,6),(9,6),(10,6),(11,6),(12,6),(13,6),(14,6),(16,6),(17,6),(18,6),(19,6),(20,6),(21,6),(22,6),(23,6),(25,6),(26,6),(27,6),(28,6),(29,6),(30,6),(31,6),
    (0,12),(1,12),(2,12),(3,12),(4,12),(5,12),(6,12),(7,12),(8,12),(9,12),(10,12),(11,12),(20,12),(21,12),(22,12),(23,12),(24,12),(25,12),(26,12),(27,12),(28,12),(29,12),(30,12),(31,12),
    (0,13),(1,13),(2,13),(3,13),(4,13),(5,13),(6,13),(7,13),(8,13),(9,13),(10,13),(11,13),(20,13),(21,13),(22,13),(23,13),(24,13),(25,13),(26,13),(27,13),(28,13),(29,13),(30,13),(31,13),
    (0,18),(1,18),(2,18),(29,18),(30,18),(31,18),
    (0,19),(1,19),(2,19),(8,19),(9,19),(29,19),(30,19),(31,19),
}


LANES1 = [

    {"row": 2, "direction": "right", "speed": 4},
    {"row": 3, "direction": "left",  "speed": 4},
    {"row": 4, "direction": "right", "speed": 8},
    {"row": 5, "direction": "right", "speed": 4},
    {"row": 7, "direction": "right", "speed": 8},
    {"row": 8, "direction": "right", "speed": 8}
]

LANES2 = [

    {"row": 1, "direction": "right", "speed": 4},
    {"row": 6, "direction": "left",  "speed": 4},
    {"row": 7, "direction": "right", "speed": 8},
    {"row": 10, "direction": "right", "speed": 4},
    {"row": 11, "direction": "left",  "speed": 4},
    {"row": 12, "direction": "right", "speed": 8},
]

LANES3 = [
    {"row": 2, "direction": "right", "speed": 11},
    {"row": 3, "direction": "left",  "speed": 4},
    {"row": 8, "direction": "right", "speed": 8},
    {"row": 9, "direction": "right", "speed": 8},
    {"row": 10, "direction": "right", "speed": 4},
    {"row": 11, "direction": "left",  "speed": 4},
    {"row": 15, "direction": "right", "speed": 8},
    {"row": 16, "direction": "right", "speed": 8},
    {"row": 17, "direction": "right", "speed": 8}
]


LIGHT_GREEN = pygame.image.load("Images/redlight.png").convert_alpha()
LIGHT_RED = pygame.image.load("Images/greenlight.png").convert_alpha()



def load_level(selected_level):
    global level, cell_size, LVLbackground

    level = selected_level
    cell_size = LEVELS[level]

    if level != "survival":
        LVLbackground = pygame.image.load(f'images/level_0{level}.png')
    else:
        LVLbackground = pygame.image.load('images/level_01.png')

    pygame.mixer.music.stop()
    pygame.mixer.music.play(-1)

    main()

def tile_is_blocked(x, y, level):
    col = x // cell_size
    row = y // cell_size
    if level == 1:
        return (col, row) in LEVEL1_BLOCKED_TILES
    elif level == 2:
        return (col, row) in LEVEL2_BLOCKED_TILES
    elif level == 3:
        return (col, row) in LEVEL3_BLOCKED_TILES

def start_game():
    while True:
        chosen_level = menu.run_menu()

        if chosen_level == "quit":
            pygame.quit()
            sys.exit()

        load_level(chosen_level)




def pause_screen():
    font = pygame.font.SysFont("Courier", 40)
    text = font.render("PAUSED", True, "white")
    restart_over = font.render("Press R to restart", True, "white")
    resume = font.render("Press P to resume", True, "white")
    escape = font.render("Press ESCAPE to go back to menu",True, "White")
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
            if event.key == K_ESCAPE:
                pygame.mixer.music.unpause()
                return "menu"
        screen.blit(LVLbackground, (0, 0))
        screen.blit(text, text.get_rect(center=(WIDTH//2, (HEIGHT//2) - 40)))
        screen.blit(restart_over, restart_over.get_rect(center=(WIDTH//2, (HEIGHT//2))))
        screen.blit(resume, resume.get_rect(center=(WIDTH//2, ((HEIGHT//2) + 40))))
        screen.blit(escape, escape.get_rect(center=(WIDTH//2, ((HEIGHT//2) + 80))))

        pygame.display.flip()
        clock.tick(10)
    pygame.mixer.music.unpause()

# def death_screen():
#     font_big = pygame.font.SysFont("Courier", 80)
#     font_small = pygame.font.SysFont("Courier", 40)
#     wasted = pygame.image.load('images/wasted.png')
#     game_over = font_big.render("GAME OVER", True, "red")
#     restart = font_small.render("Press R to restart", True, "white")
#     pygame.mixer.music.pause()
#     while True:
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN and event.key == K_r:
#                 restart_game()
#         screen.blit(LVLbackground, (0, 0))
#         screen.blit(wasted, game_over.get_rect(center=(WIDTH//2 - 35, HEIGHT//2 - 80)))
#         screen.blit(restart, restart.get_rect(center=(WIDTH//2, HEIGHT//2 + 40)))
#         pygame.display.flip()
#         clock.tick(10)

def draw_grid():
    cols = WIDTH // cell_size
    rows = HEIGHT // cell_size

    grid_color = (255, 0, 0)

    for x in range(cols + 1):
        pygame.draw.line(
            screen, grid_color, (x * cell_size, 0), (x * cell_size, HEIGHT), 1)

    for y in range(rows + 1):
        pygame.draw.line(
            screen, grid_color, (0, y * cell_size), (WIDTH, y * cell_size), 1        )

def death_screen():
    font_small = pygame.font.SysFont("Courier", 40)
    wasted = pygame.image.load('images/wasted.png')
    restart = font_small.render("Press R to restart", True, "white")
    screen.blit(wasted, wasted.get_rect(center=(WIDTH//2 - 35, HEIGHT//2 - 80)))
    screen.blit(restart, restart.get_rect(center=(WIDTH//2, HEIGHT//2)))


def win_screen():
    font = pygame.font.SysFont("Courier", 150)
    text = font.render("GAME WON!", True, "green")
    escape = font.render("Press ESCAPE to go back to menu",True, "White")

    pygame.mixer.music.pause()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                paused = False
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.mixer.music.unpause()
                return menu.run_menu()
        pygame.mixer.music.pause()
        screen.blit(LVLbackground, (0, 0))
        screen.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//2)))
        screen.blit(escape, escape.get_rect(center=(WIDTH//2, ((HEIGHT//2) + 100))))
        pygame.display.flip()
    pygame.mixer.music.unpause()

def restart_game():
    pygame.mixer.music.stop()
    pygame.mixer.music.play(-1)
    load_level(level)

class Player:
    def __init__(self, level):
        self.state = "ALIVE"
        self.direction = "up"
        self.level = level
        self.image = PLAYER_IMAGES["up"]

        if level == 1:
            self.hitbox = pygame.Rect(421, 540, cell_size, cell_size)
        elif level == 2:
            self.hitbox = pygame.Rect(440, 560, cell_size, cell_size)
        else:
            self.hitbox = pygame.Rect(450, 571, cell_size, cell_size)

    def drawPlayer(self):
       self.image = PLAYER_IMAGES[self.direction if self.state == "ALIVE" else "dead"]
       self.image = pygame.transform.scale(self.image, self.hitbox.size)
       screen.blit(self.image, self.hitbox)

    def change_state(self):
        self.state = "DEAD"
        death_screen()

    def check_finish(self):
        if self.hitbox.top <= cell_size//2 and level != "survival":
            win_screen()
        
    def change_direction(self, direction):
        if self.state != "ALIVE":
            return

        self.direction = direction

        new_x = self.hitbox.x
        new_y = self.hitbox.y

        if direction == "up":
            new_y -= cell_size
        elif direction == "down":
            new_y += cell_size
        elif direction == "left":
            new_x -= cell_size
        elif direction == "right":
            new_x += cell_size

        if level == 1:
            if new_x < 0 or new_x > WIDTH or new_y + cell_size > HEIGHT:
                return
        elif level == 2:
            if new_x < 0 or new_x + cell_size > WIDTH or new_y + cell_size > HEIGHT:
                return
        else:
            if new_x < 0 or new_x + cell_size > WIDTH or new_y > HEIGHT:
                return

        if tile_is_blocked(new_x, new_y, self.level):
            return

        self.hitbox.x = new_x
        self.hitbox.y = new_y


class Car:
    def __init__(self, rect, speed, direction):
        self.rect = rect
        self.speed = speed
        self.direction = direction
        self.image = random.choice(CAR_IMAGES)
        if self.direction == "left":
            self.image = pygame.transform.flip(self.image, True, False)

    def update(self):
        if self.direction == "right":
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed

    def draw(self):
        self.image = pygame.transform.scale(self.image, self.rect.size)

        screen.blit(self.image, self.rect)

class CarManager:
    def __init__(self, level):
        self.cars = []
        self.timer = 0

        if level == 1:
            self.CAR_WIDTH = 100
            self.CAR_HEIGHT = cell_size
            self.car_speed = 8
            self.CAR_INTERVAL = 500
        elif level == 2:
            self.CAR_WIDTH = 80
            self.CAR_HEIGHT = cell_size
            self.car_speed = 10
            self.CAR_INTERVAL = 400
        elif level == 3:
            self.CAR_WIDTH = 50
            self.CAR_HEIGHT = cell_size
            self.car_speed = 11
            self.CAR_INTERVAL = 50
        elif level == "survival":
            self.CAR_WIDTH = 50
            self.CAR_HEIGHT = cell_size
            self.car_speed = 9
            self.CAR_INTERVAL = 50

    def spawn_car(self):
        if level == 1:
            lane = random.choice(LANES1)
        elif level == 2:
            lane = random.choice(LANES2)
        elif level == 3:
            lane = random.choice(LANES3)


        y = lane["row"] * cell_size
        direction = lane["direction"]
        speed = lane["speed"]

        if direction == "right":
            x = -self.CAR_WIDTH
        else:
            x = WIDTH

        rect = pygame.Rect(x, y, self.CAR_WIDTH, self.CAR_HEIGHT)
        self.cars.append(Car(rect, speed, direction))

    def update(self, dt, player):
        self.timer += dt
        
        if self.timer > self.CAR_INTERVAL:
            self.spawn_car()
            self.timer = 0

        for car in self.cars[:]:
            car.update()

            player_lane = player.hitbox.y // cell_size
            car_lane = car.rect.y // cell_size

            if player.state == "ALIVE" and player_lane == car_lane:
                if car.rect.right > player.hitbox.left and car.rect.left < player.hitbox.right:
                    player.change_state()
                    hit_sound.play()

            if car.direction == "right" and car.rect.x > WIDTH:
                self.cars.remove(car)
            elif car.direction == "left" and car.rect.right < 0:
                self.cars.remove(car)
            
    def draw(self):
        for car in self.cars:
            car.draw()

class TrainManager:
    def __init__(self, level):
        self.timer = 0
        self.level = level

        # Trein
        self.passing = False
        self.hitbox = pygame.Rect(WIDTH, 358, 500, 55)
        image = pygame.image.load(f"Images/trein_30.png")
        self.image = pygame.transform.scale(image, self.hitbox.size)
        self.speed = 600
        self.interval = random.randint(3000, 5000)

        # Licht
        self.warning = False
        self.light_pos = (600, 330)
        self.warning_time = 1000

    def draw(self):
        if self.level == 3:
            if self.warning:
                screen.blit(LIGHT_GREEN, self.light_pos)
            else:
                screen.blit(LIGHT_RED, self.light_pos)

            if self.passing:
                screen.blit(self.image, self.hitbox)

    def update(self, dt, player):
        if self.level != 3:
            return
        self.timer += dt

        if not self.passing and not self.warning and self.timer >= self.interval - self.warning_time:
            self.warning = True

        if not self.passing and self.timer >= self.interval:
            self.passing = True
            self.timer = 0
            self.hitbox.left = WIDTH
            self.interval = random.randint(3000, 5000)

        if self.passing:
            dx = self.speed * (dt / 1000)
            self.hitbox.x -= dx

            if player.state == "ALIVE" and (12 <= (player.hitbox.y // cell_size) <= 13):
                if self.hitbox.right > player.hitbox.left and self.hitbox.left < player.hitbox.right:
                    player.change_state()
                    hit_sound.play()


            if self.hitbox.right < 0:
                self.passing = False
                self.warning = False
                self.timer = 0


def main():
    running = True
    player = Player(level)
    car_manager = CarManager(level)
    train_manager = TrainManager(level)

    while running:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_p:
                    result = pause_screen()
                    if result == "menu":
                        return
                elif event.key == K_LEFT:
                    player.change_direction("left")
                elif event.key == K_RIGHT:
                    player.change_direction("right")
                elif event.key == K_UP:
                    player.change_direction("up")
                elif event.key == K_DOWN:
                    player.change_direction("down")
                elif event.key == K_r and player.state == "DEAD":
                    restart_game()
        
        screen.blit(LVLbackground, (0, 0))

        player.drawPlayer()
        player.check_finish()

        car_manager.update(dt, player)
        car_manager.draw()

        train_manager.update(dt, player)
        train_manager.draw()

        if player.state == "DEAD":
            death_screen()

        draw_grid()
        pygame.display.flip()

start_game()
pygame.quit()
sys.exit()
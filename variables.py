import pygame
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

level = 3
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
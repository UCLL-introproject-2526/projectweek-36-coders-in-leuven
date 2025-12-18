import pygame
from game4 import *
WIDTH  = 960
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Road Cross')
icon = pygame.image.load('images/logo.png')
pygame.display.set_icon(icon)


def run_menu():
    font = pygame.font.Font('fonts/LuckiestGuy-Regular.ttf', 20)
    WelkomImage = pygame.image.load('images/logo.png')
    WallpaperMenu = pygame.image.load('images/menu_wallpaper.png')

    welkom = pygame.Rect(WIDTH//2-160, 5, 350, 100)
    level1 = pygame.Rect(145, 550, 120, 35)
    level2 = pygame.Rect(300, 550, 120, 35)
    level3 = pygame.Rect(450, 550, 120, 35)
    survival = pygame.Rect(600, 550, 130, 35)

    level1_text = font.render("Level 1", True, (204, 105, 26))
    level2_text = font.render("Level 2", True, (204, 105, 26))
    level3_text = font.render("Level 3", True, (204, 105, 26))
    level_survival_text = font.render("Survival", True, (204, 105, 26))

    while True:
        screen.blit(WallpaperMenu, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if level1.collidepoint(event.pos):
                    return 1
                if level2.collidepoint(event.pos):
                    return 2
                if level3.collidepoint(event.pos):
                    return 3
                if survival.collidepoint(event.pos):
                    return "survival"

        pygame.draw.rect(screen, (112, 214, 25), level1, border_radius=12)
        pygame.draw.rect(screen, (112, 214, 25), level2, border_radius=12)
        pygame.draw.rect(screen, (112, 214, 25), level3, border_radius=12)
        pygame.draw.rect(screen, (112, 214, 25), survival, border_radius=12)

        
        screen.blit(WelkomImage,welkom)
        
        level1_rect = level1_text.get_rect(center=level1.center)
        screen.blit(level1_text, level1_rect.topleft)
        
        level2_rect = level2_text.get_rect(center=level2.center)
        screen.blit(level2_text, level2_rect.topleft)
        
        level3_rect = level3_text.get_rect(center=level3.center)
        screen.blit(level3_text, level3_rect.topleft)
        
        level_survival_rect = level_survival_text.get_rect(center=survival.center)
        screen.blit(level_survival_text, level_survival_rect.topleft)
        pygame.display.flip()
        clock.tick(60)
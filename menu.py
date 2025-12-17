import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu")
clock = pygame.time.Clock()

font = pygame.font.Font('fonts/LuckiestGuy-Regular.ttf', 20)
WelkomImage = pygame.image.load('images/logo.png')
WallpaperMenu = pygame.image.load('images/menu_wallpaper.png')

state = "menu"

welkom = pygame.Rect(SCREEN_WIDTH//2-160, 5, 350, 100)
level_1 = pygame.Rect(70, 550, 120, 35)
level_2 = pygame.Rect(240, 550, 120, 35)
level_3 = pygame.Rect(420, 550, 120, 35)
level_survival = pygame.Rect(600, 550, 130, 35)

level1_text = font.render("Level 1", True, "red")
level2_text = font.render("Level 2", True, "red")
level3_text = font.render("Level 3", True, "red")
level_survival_text = font.render("Survival", True, "red")

run = True
while run:
    screen.blit(WallpaperMenu, (-67,-4))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if state == "menu":
                if level_1.collidepoint(event.pos):
                    state = "level1"
                elif level_2.collidepoint(event.pos):
                    state = "level2"
                elif level_3.collidepoint(event.pos):
                    state = "level3"
                elif level_survival.collidepoint(event.pos):
                    state = "levelsurvival"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                state = "menu"
    
    if state == "menu":
        pygame.draw.rect(screen, (0, 255, 120), level_1, border_radius=12)
        pygame.draw.rect(screen, (0, 0, 255), level_2, border_radius=12)
        pygame.draw.rect(screen, (0, 0, 255), level_3, border_radius=12)
        pygame.draw.rect(screen, (0, 0, 255), level_survival, border_radius=12)

        screen.blit(WelkomImage,welkom)
        
        level1_rect = level1_text.get_rect(center=level_1.center)
        screen.blit(level1_text, level1_rect.topleft)
        
        level2_rect = level2_text.get_rect(center=level_2.center)
        screen.blit(level2_text, level2_rect.topleft)
        
        level3_rect = level3_text.get_rect(center=level_3.center)
        screen.blit(level3_text, level3_rect.topleft)
        
        level_survival_rect = level_survival_text.get_rect(center=level_survival.center)
        screen.blit(level_survival_text, level_survival_rect.topleft)
        
    elif state == "level1":
        level_text = font.render("LEVEL 1", True, "white")
        level_rect = level_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(level_text, level_rect.topleft)
    elif state == "level2":
        level_text = font.render("LEVEL 2", True, "white")
        level_rect = level_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(level_text, level_rect.topleft)
    elif state == "level3":
        level_text = font.render("LEVEL 3", True, "white")
        level_rect = level_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(level_text, level_rect.topleft)
    elif state == "levelsurvival":
        level_text = font.render("SURVIVAL", True, "white")
        level_rect = level_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(level_text, level_rect.topleft)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
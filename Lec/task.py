import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("regtangle")

red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

RECT_SIZE = 50
current_color = red

rect_x = (screen_width / 2) - (RECT_SIZE // 2)
rect_y = (screen_height / 2) - (RECT_SIZE / 2)

target_rect = pygame.Rect(rect_x, rect_y, RECT_SIZE, RECT_SIZE)

score = 0
font = pygame.font.Font(None, 36)

def move_rect():
    global target_rect
    rect_x = random.randint(0, screen_width - RECT_SIZE)
    rect_y = random.randint(0, screen_height - RECT_SIZE)
    target_rect.topleft = (rect_x, rect_y)
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                
                if target_rect.collidepoint(event.pos):
                    score += 1
                    move_rect()
                    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if current_color == red:
                    current_color = green
                else:
                    current_color = red

    screen.fill(white)

    pygame.draw.rect(screen, current_color, target_rect)
    
    score_text = f"Счет: {score}"
    
    text_surface = font.render(score_text, True, black)
    screen.blit(text_surface, (10, 10))


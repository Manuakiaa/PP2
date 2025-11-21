import pygame
import time
import os

base_micky = r'C:\Users\manua\OneDrive\Рабочий стол\PP2_2025-2026\Lab_7\base_micky.jpg'
minute = r'C:\Users\manua\OneDrive\Рабочий стол\PP2_2025-2026\Lab_7\minute.png'
second = r'C:\Users\manua\OneDrive\Рабочий стол\PP2_2025-2026\Lab_7\second.png'
script_dir = os.path.dirname(os.path.abspath(__file__))
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mickey Clock")

white = (255, 255, 255)

try:
    clock_face = pygame.image.load(base_micky)
    minute_hand = pygame.image.load(minute)
    second_hand = pygame.image.load(second)
except:
    clock_face = pygame.Surface((400, 400))
    clock_face.fill(white)
    pygame.draw.circle(clock_face, (0, 0, 0), (200, 200), 200, 2)
    
    minute_hand = pygame.Surface((100, 20))
    minute_hand.fill((255, 0, 0))
    
    second_hand = pygame.Surface((100, 15))
    second_hand.fill((0, 0, 0))

minute_hand = pygame.transform.scale(minute_hand, (1050, 520))
second_hand = pygame.transform.scale(second_hand, (55, 440))
clock_face = pygame.transform.scale(clock_face, (400, 400))

center_x = 400
center_y = 300

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    minute_angle = - (minutes * 6 + seconds * 0.1)
    second_angle = - (seconds * 6)
    
    screen.fill(white)
    screen.blit(clock_face, (center_x - 200, center_y - 200))
    
    rotated_minute = pygame.transform.rotate(minute_hand, minute_angle)
    minute_rect = rotated_minute.get_rect()
    minute_rect.center = (center_x, center_y)
    screen.blit(rotated_minute, minute_rect)
    
    rotated_second = pygame.transform.rotate(second_hand, second_angle)
    second_rect = rotated_second.get_rect()
    second_rect.center = (center_x, center_y)
    screen.blit(rotated_second, second_rect)
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()
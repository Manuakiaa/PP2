import pygame
import sys
import random

pygame.init()
pygame.display.set_caption("Racer Game")

FPS = 60
FramePerSec = pygame.time.Clock()
BASE_SPEED = 5
SPEED_INCREASE_THRESHOLD = 5 

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

SCORE = 0
COINS = 0
CURRENT_SPEED = BASE_SPEED 

road = r'C:\Users\manua\OneDrive\Рабочий стол\PP2_2025-2026\Lab_8\road.jpg'
enemy_car = r'C:\Users\manua\OneDrive\Рабочий стол\PP2_2025-2026\Lab_8\enemy_car.jpg'
coin = r'C:\Users\manua\OneDrive\Рабочий стол\PP2_2025-2026\Lab_8\coin.png'
my_car = r'C:\Users\manua\OneDrive\Рабочий стол\PP2_2025-2026\Lab_8\my_car.jpg'

# Настройка текста
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_surface = font.render("Game Over", True, BLACK)

# Загрузка фона и создание поверхности
background = pygame.image.load(road)
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


#Настройка Enemy 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(enemy_car).convert_alpha()
        self.rect = self.image.get_rect()
        self.spawn()
    
    def spawn(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) 

    def move(self):
        global SCORE
        # Используем CURRENT_SPEED
        self.rect.move_ip(0, CURRENT_SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1 # Очки за проезд врага
            self.spawn()


#Настройка Coins
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        # Монеты с разным весом:
        # 1 Маленькая самая частая, +1 монета
        # 2 Средняя +2 монета
        # 3 Большая +5 монета
        self.weight = self.determine_weight()
        self.image = pygame.image.load(coin).convert_alpha()
        self.set_appearance()
        self.rect = self.image.get_rect()
        self.spawn()
    
    def determine_weight(self):
        #Случайный выбор веса монеты
        # 80% шанс на 1, 15% на 2, 5% на 5
        weights = [1] * 80 + [2] * 15 + [5] * 5
        return random.choice(weights)
        
    def set_appearance(self):
        """Настройка размера и цвета монеты в зависимости от веса."""
        size_map = {1: (20, 20), 2: (30, 30), 5: (40, 40)}
        self.image = pygame.transform.scale(self.image, size_map[self.weight])
        # меняем размер монеты в зависимости от веса
    def spawn(self):
        """Перемещение монеты в случайную верхнюю позицию и перерасчет веса."""
        self.weight = self.determine_weight()
        self.set_appearance()
        self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), 0))
    
    def move(self):
        self.rect.move_ip(0, CURRENT_SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.spawn()
#Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(my_car).convert_alpha()
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-BASE_SPEED, 0) 
        if pressed_keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:    
            self.rect.move_ip(BASE_SPEED, 0)
P1 = Player()
E1 = Enemy()
C1 = Coin()
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()       
    DISPLAYSURF.blit(background, (0,0))
    
    # Отображение счета и монет
    scores_surf = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_surf = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(scores_surf, (10, 10))
    DISPLAYSURF.blit(coins_surf, (SCREEN_WIDTH - coins_surf.get_width() - 10, 10)) 
    
    # Движение и отрисовка всех спрайтов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
        
    #Столкновение с врагом (Проигрыш)
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.time.wait(500)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over_surface, (SCREEN_WIDTH // 2 - game_over_surface.get_width() // 2, 250))        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        pygame.time.wait(2000) 
        pygame.quit()
        sys.exit()

    # Столкновение с монетой 
    collected_coins = pygame.sprite.spritecollide(P1, coins, False) 
    if collected_coins:
        # Проходим по всем  монетам собранным
        for collected_coin in collected_coins:
            COINS += collected_coin.weight # Добавляем вес монеты к счету
        
            if COINS % SPEED_INCREASE_THRESHOLD == 0 and COINS > 0:
                 CURRENT_SPEED += 1 # Увеличиваем скорость врагов на 1
            collected_coin.spawn() 
            
    pygame.display.update()
    FramePerSec.tick(FPS)
import pygame
import sys
import random
import time 
pygame.init()

CELL_SIZE = 20 # 
GRID_WIDTH = 30 
GRID_HEIGHT = 20 
WIDTH = GRID_WIDTH * CELL_SIZE 
HEIGHT = GRID_HEIGHT * CELL_SIZE 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Параметры 
BASE_SPEED = 5 # Базовая скорость
LEVEL_SPEED_INCREASE = 2 # Насколько увеличивается FPS за уровень
FOODS_PER_LEVEL = 3 # Сколько еды нужно съесть для перехода на новый уровень
FOOD_TIMER_DURATION = 8 # Время по истечении которого еда исчезает
font = pygame.font.SysFont(None, 36)

# Еда теперь должна хранить не только позицию, но и вес, и время спавна.
class Food:
    def __init__(self, snake_positions):
        self.position = random_food_position(snake_positions)
        self.weight = self.determine_weight()
        self.spawn_time = time.time() # Записываем текущее время

    def determine_weight(self):
        # 80% шанс на 1 очко (маленькая), 20% на 3 очка (большая)
        weights = [1] * 80 + [3] * 20
        return random.choice(weights)
        
    def is_expired(self):
        #Проверяет, истекло ли время жизни еды
        return time.time() - self.spawn_time > FOOD_TIMER_DURATION

def random_food_position(snake_positions):
    #Генерирует случайную позицию для еды, не занятую змейкой
    while True:
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        if (x, y) not in snake_positions:
            return (x, y)

def draw_snake(surface, snake_positions):
    for i, (x, y) in enumerate(snake_positions):
        rect = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        color = (0, 255, 0) if i == 0 else GREEN 
        pygame.draw.rect(surface, color, rect)

def draw_food(surface, food):
    #Отрисовывает еду, используя цвет в зависимости от веса
    x, y = food.position
    rect = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    # Красный для маленькой еды, Синий для большой
    color = BLUE if food.weight == 3 else RED 
    pygame.draw.rect(surface, color, rect)

def draw_game_info(surface, score, level, speed):
    """Отображает текущий счет, уровень и скорость."""
    info_text = font.render(f"Score: {score}  Level: {level}  Speed: {speed}", True, WHITE)
    surface.blit(info_text, (10, 10))

def move_snake(snake_positions, direction):
    """Перемещает змейку, добавляя новую голову и удаляя хвост."""
    head_x, head_y = snake_positions[0]
    new_head = (head_x + direction[0], head_y + direction[1])
    # Создаем новый список: новая голова + старое тело без хвоста
    return [new_head] + snake_positions[:-1]

def check_collisions(snake_positions):
    #Проверяет столкновение с границами или с самим собой
    head_x, head_y = snake_positions[0]
    # Столкновение с границами
    if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
        return True
    # Столкновение с телом 
    if (head_x, head_y) in snake_positions[1:]:
        return True
    return False

def game_over_screen(score, level):
    #Game Over
    screen.fill(BLACK)
    over_text = font.render("You lose", True, WHITE)
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    over_rect = over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
    screen.blit(over_text, over_rect)
    screen.blit(score_text, score_rect)
    pygame.display.flip()
    pygame.time.wait(3000)

def main():
    snake_positions = [(5, 5), (4, 5), (3, 5)] # Начальная позиция змейки
    direction = (1, 0) # Начальное направление 
    current_food = Food(snake_positions) # Создаем первый объект еды
    score = 0
    level = 1
    foods_eaten = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

        # Проверяем, не истек ли таймер еды
        if current_food.is_expired():
            current_food = Food(snake_positions) # Спавним новую еду
            
        snake_positions = move_snake(snake_positions, direction)
        
        # Проверка столкновений со стенами или с собой
        if check_collisions(snake_positions):
            running = False
            continue

        # Проверка поедания еды
        if snake_positions[0] == current_food.position:
            score += current_food.weight # Добавляем вес еды к счету
            foods_eaten += 1
            
            snake_positions.append(snake_positions[-1]) 
            
            current_food = Food(snake_positions) # Спавним новую еду
            # Проверка перехода на новый уровень
            if foods_eaten >= FOODS_PER_LEVEL:
                level += 1
                foods_eaten = 0
        #Отрисовка
        screen.fill(BLACK)
        draw_snake(screen, snake_positions)
        draw_food(screen, current_food)
        
        # Расчет текущей скорости
        current_speed = BASE_SPEED + (level - 1) * LEVEL_SPEED_INCREASE
        draw_game_info(screen, score, level, current_speed)
    
        pygame.display.flip()
        
        clock.tick(current_speed)

    game_over_screen(score, level)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
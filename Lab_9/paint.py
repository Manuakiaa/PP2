import pygame
import sys
import math

pygame.init()

# Настройки путей (замените на свои, если требуется)
brush = r'C:\Users\manua\OneDrive\Рабочий стол\PP2_2025-2026\Lab_8\brush.png'
rectangle = r'C:\Users\manua\OneDrive\Рабочий стол\PP2_2025-2026\Lab_8\rectangle.png'
circle = r'C:\Users\manua\OneDrive\Рабочий стол\PP2_2025-2026\Lab_8\circle.png'
eraser = r'C:\Users\manua\OneDrive\Рабочий стол\PP2_2025-2026\Lab_8\eraser.png'
square = r'C:\Users\manua\OneDrive\Рабочий стол\PP2_2025-2026\Lab_8\square.webp'
triangle = r'C:\Users\manua\OneDrive\Рабочий стол\PP2_2025-2026\Lab_8\Triangle.png'
rhombus = r'C:\Users\manua\OneDrive\Рабочий стол\PP2_2025-2026\Lab_8\rhomus.webp'

# Настройки экрана
WIDTH, HEIGHT = 800, 600
UI_HEIGHT = 100 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced PyPaint")
clock = pygame.time.Clock()

# Холст для рисования
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255)) 

# Область рисования
DRAWING_AREA = pygame.Rect(0, UI_HEIGHT, WIDTH, HEIGHT - UI_HEIGHT) 

# Цвета
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128) 

current_color = BLACK
current_tool = "brush"

BRUSH_SIZE = 5 
ERASER_SIZE = 20 
SHAPE_LINE_WIDTH = 2 

# Загрузка иконок
icon_size = (40, 40)
brush_icon = pygame.transform.scale(pygame.image.load(brush).convert_alpha(), icon_size)
rectangle_icon = pygame.transform.scale(pygame.image.load(rectangle).convert_alpha(), icon_size)
circle_icon = pygame.transform.scale(pygame.image.load(circle).convert_alpha(), icon_size)
eraser_icon = pygame.transform.scale(pygame.image.load(eraser).convert_alpha(), icon_size)
square_icon = pygame.transform.scale(pygame.image.load(square).convert_alpha(), icon_size)
right_triangle_icon = pygame.transform.scale(pygame.image.load(triangle).convert_alpha(), icon_size)
equilateral_triangle_icon = pygame.transform.scale(pygame.image.load(triangle).convert_alpha(), icon_size)
rhombus_icon = pygame.transform.scale(pygame.image.load(rhombus).convert_alpha(), icon_size)

# Позиции иконок
icon_positions = {
    "brush": pygame.Rect(10, 10, icon_size[0], icon_size[1]),
    "rectangle": pygame.Rect(60, 10, icon_size[0], icon_size[1]),
    "circle": pygame.Rect(110, 10, icon_size[0], icon_size[1]),
    "eraser": pygame.Rect(160, 10, icon_size[0], icon_size[1]),
    "square": pygame.Rect(210, 10, icon_size[0], icon_size[1]),
    "right_triangle": pygame.Rect(260, 10, icon_size[0], icon_size[1]),
    "equilateral_triangle": pygame.Rect(310, 10, icon_size[0], icon_size[1]),
    "rhombus": pygame.Rect(360, 10, icon_size[0], icon_size[1]),
}

# Позиции палитры
color_positions = {
    "red": pygame.Rect(10, 60, 30, 30),
    "green": pygame.Rect(50, 60, 30, 30),
    "blue": pygame.Rect(90, 60, 30, 30),
    "black": pygame.Rect(130, 60, 30, 30)
}

# Состояние рисования
drawing = False
start_pos = (0, 0) 
last_pos = None 

def draw_ui():
    pygame.draw.rect(screen, PURPLE, (0, 0, WIDTH, UI_HEIGHT))
    
    screen.blit(brush_icon, icon_positions["brush"].topleft)
    screen.blit(rectangle_icon, icon_positions["rectangle"].topleft)
    screen.blit(circle_icon, icon_positions["circle"].topleft)
    screen.blit(eraser_icon, icon_positions["eraser"].topleft)
    screen.blit(square_icon, icon_positions["square"].topleft)
    screen.blit(right_triangle_icon, icon_positions["right_triangle"].topleft)
    screen.blit(equilateral_triangle_icon, icon_positions["equilateral_triangle"].topleft)
    screen.blit(rhombus_icon, icon_positions["rhombus"].topleft)

    if current_tool in icon_positions:
        rect = icon_positions[current_tool]
        pygame.draw.rect(screen, WHITE, rect, 2) 

def draw_color_ui():
    pygame.draw.rect(screen, RED, color_positions["red"])
    pygame.draw.rect(screen, GREEN, color_positions["green"])
    pygame.draw.rect(screen, BLUE, color_positions["blue"])
    pygame.draw.rect(screen, BLACK, color_positions["black"])
    
    active_color_name = None
    if current_color == RED: active_color_name = "red"
    elif current_color == GREEN: active_color_name = "green"
    elif current_color == BLUE: active_color_name = "blue"
    elif current_color == BLACK: active_color_name = "black"

    if active_color_name in color_positions:
        pygame.draw.rect(screen, WHITE, color_positions[active_color_name], 3) 

def handle_tool_selection(pos):
    for tool, rect in icon_positions.items():
        if rect.collidepoint(pos):
            return tool
    return None

def handle_color_selection(pos):
    for color_name, rect in color_positions.items():
        if rect.collidepoint(pos):
            if color_name == "red": return RED
            elif color_name == "green": return GREEN
            elif color_name == "blue": return BLUE
            elif color_name == "black": return BLACK
    return None

def get_shape_points(tool, start, end):
    x1, y1 = start
    x2, y2 = end
    width = x2 - x1
    height = y2 - y1
    
    if tool == "square":
        side = max(abs(width), abs(height))
        dx = side if width > 0 else -side
        dy = side if height > 0 else -side
        return [
            (x1, y1), 
            (x1 + dx, y1), 
            (x1 + dx, y1 + dy), 
            (x1, y1 + dy)
        ]

    elif tool == "right_triangle":
        return [start, end, (x1, y2)] 

    elif tool == "equilateral_triangle":
        side = abs(width)
        mid_x = x1 + width / 2
        h = side * math.sqrt(3) / 2
        top_y = y1 - h if y2 > y1 else y1 + h 
        return [(x1, y1), (x2, y1), (mid_x, top_y)]
    
    elif tool == "rhombus":
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        return [
            (x1, mid_y),
            (mid_x, y1),
            (x2, mid_y),
            (mid_x, y2)
        ]
        
    return []

# Главный цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                
                chosen_color = handle_color_selection(event.pos)
                chosen_tool = handle_tool_selection(event.pos)
                
                if chosen_color is not None:
                    current_color = chosen_color
                elif chosen_tool is not None:
                    current_tool = chosen_tool
                else:
                    if DRAWING_AREA.collidepoint(event.pos):
                        drawing = True
                        start_pos = event.pos
                        last_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                end_pos = event.pos
                
                if DRAWING_AREA.collidepoint(end_pos):
                    
                    if current_tool == "rectangle":
                        rect = pygame.Rect(
                            min(start_pos[0], end_pos[0]),
                            min(start_pos[1], end_pos[1]),
                            abs(end_pos[0] - start_pos[0]),
                            abs(end_pos[1] - start_pos[1])
                        )
                        pygame.draw.rect(canvas, current_color, rect, width=SHAPE_LINE_WIDTH)
                        
                    elif current_tool == "circle":
                        radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                        pygame.draw.circle(canvas, current_color, start_pos, radius, width=SHAPE_LINE_WIDTH)
                    
                    elif current_tool in ["square", "right_triangle", "equilateral_triangle", "rhombus"]:
                        points = get_shape_points(current_tool, start_pos, end_pos)
                        if points:
                            pygame.draw.polygon(canvas, current_color, points, width=SHAPE_LINE_WIDTH)

                drawing = False 

        elif event.type == pygame.MOUSEMOTION:
            if drawing and DRAWING_AREA.collidepoint(event.pos):
                
                if current_tool == "brush":
                    pygame.draw.line(canvas, current_color, last_pos, event.pos, BRUSH_SIZE)
                    last_pos = event.pos
                    
                elif current_tool == "eraser":
                    pygame.draw.line(canvas, WHITE, last_pos, event.pos, ERASER_SIZE)
                    last_pos = event.pos
                
    # Отрисовка
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))
    draw_ui()
    draw_color_ui()

    # Обновление
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
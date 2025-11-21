import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball Game")

white = (255, 255, 255)
red = (255, 0, 0)

ball_radius = 25
ball_x = screen_width // 2
ball_y = screen_height // 2
move_speed = 20

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            new_x = ball_x
            new_y = ball_y
            
            if event.key == pygame.K_LEFT:
                new_x = ball_x - move_speed
            elif event.key == pygame.K_RIGHT:
                new_x = ball_x + move_speed
            elif event.key == pygame.K_UP:
                new_y = ball_y - move_speed
            elif event.key == pygame.K_DOWN:
                new_y = ball_y + move_speed
            
            left_ok = new_x - ball_radius >= 0
            right_ok = new_x + ball_radius <= screen_width
            top_ok = new_y - ball_radius >= 0
            bottom_ok = new_y + ball_radius <= screen_height
            
            if left_ok and right_ok and top_ok and bottom_ok:
                ball_x = new_x
                ball_y = new_y
    
    screen.fill(white)
    
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
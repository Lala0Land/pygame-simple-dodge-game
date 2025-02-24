import pygame
import random

# Game settings
WIDTH, HEIGHT = 500, 500
WHITE, RED, BLUE = (255, 255, 255), (255, 0, 0), (0, 0, 255)
SPEED = 5
OBSTACLE_SPEED = 5
PLAYER_SIZE = 50
OBSTACLE_SIZE = 50

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player properties
player_x = WIDTH // 2
player_y = HEIGHT - PLAYER_SIZE - 10

# Obstacle properties
obstacle_x = random.randint(0, WIDTH - OBSTACLE_SIZE)
obstacle_y = 0

running = True
while running:
    screen.fill(WHITE)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= SPEED
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += SPEED

    # Move the obstacle downward
    obstacle_y += OBSTACLE_SPEED
    
    # Reset obstacle position if it reaches the bottom
    if obstacle_y > HEIGHT:
        obstacle_x = random.randint(0, WIDTH - OBSTACLE_SIZE)
        obstacle_y = 0

    # Collision detection
    if (player_x < obstacle_x + OBSTACLE_SIZE and player_x + PLAYER_SIZE > obstacle_x) and \
       (player_y < obstacle_y + OBSTACLE_SIZE and player_y + PLAYER_SIZE > obstacle_y):
        print("❌ Game Over!")
        running = False

    # Draw the player and obstacle
    pygame.draw.rect(screen, BLUE, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))  # Player
    pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, OBSTACLE_SIZE, OBSTACLE_SIZE))  # Obstacle
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()

import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 20
SPEED = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock
clock = pygame.time.Clock()

def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

def place_food():
    x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    return [x, y]

def main():
    running = True
    direction = RIGHT
    snake = [[100, 100], [80, 100], [60, 100]]  # Initial snake position
    food = place_food()
    score = 0

    while running:
        screen.fill(BLACK)

        # Handle Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT

        # Move Snake
        new_head = [snake[0][0] + direction[0] * BLOCK_SIZE, snake[0][1] + direction[1] * BLOCK_SIZE]
        snake.insert(0, new_head)

        # Check Collision (Wall)
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            running = False

        # Check Collision (Self)
        if new_head in snake[1:]:
            running = False

        # Check if food is eaten
        if new_head == food:
            score += 1
            food = place_food()
        else:
            snake.pop()

        # Draw Snake and Food
        draw_snake(snake)
        pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

        # Update Screen
        pygame.display.flip()
        clock.tick(SPEED)

    pygame.quit()
    print(f"Game Over! Your Score: {score}")

# Run the Game
if __name__ == "__main__":
    main()

import pygame
import random
import sys

pygame.init()

# -----------------------------
# SETTINGS
# -----------------------------
CELL = 20
GRID_W = 15
GRID_H = 20

WIDTH = CELL * GRID_W
HEIGHT = CELL * GRID_H

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Practice 11")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 18)

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
GREEN = (0, 180, 0)
DARK_GREEN = (0, 120, 0)
RED = (220, 0, 0)
BLUE = (0, 0, 220)
PURPLE = (128, 0, 128)

# -----------------------------
# GAME VARIABLES
# -----------------------------
snake = [(3, 2), (2, 2), (1, 2)]

direction = (1, 0)
next_direction = (1, 0)

score = 0
level = 1
speed = 3

walls = set()

food = None
food_value = 1
food_spawn_time = 0
FOOD_LIFETIME = 5000  # food disappears after 5 seconds


# -----------------------------
# LOAD LEVEL
# -----------------------------
def load_level(level_number):
    global walls

    walls = set()
    filename = f"level{level_number}.txt"

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        for y, line in enumerate(lines):
            line = line.strip()
            for x, char in enumerate(line):
                if char == "#":
                    walls.add((x, y))

    except FileNotFoundError:
        print(f"{filename} not found")
        pygame.quit()
        sys.exit()


# -----------------------------
# GENERATE FOOD WITH WEIGHT
# -----------------------------
def generate_food():
    global food_value, food_spawn_time

    while True:
        pos = (
            random.randint(0, GRID_W - 1),
            random.randint(0, GRID_H - 1)
        )

        if pos not in snake and pos not in walls:
            food_value = random.choice([1, 2, 3])
            food_spawn_time = pygame.time.get_ticks()
            return pos


# -----------------------------
# DRAW CELL
# -----------------------------
def draw_cell(pos, color):
    x, y = pos
    pygame.draw.rect(
        screen,
        color,
        (x * CELL, y * CELL, CELL, CELL)
    )


# -----------------------------
# DRAW BACKGROUND
# -----------------------------
def draw_background():
    for y in range(GRID_H):
        for x in range(GRID_W):
            if (x + y) % 2 == 0:
                color = WHITE
            else:
                color = GRAY

            pygame.draw.rect(
                screen,
                color,
                (x * CELL, y * CELL, CELL, CELL)
            )


# -----------------------------
# DRAW GAME
# -----------------------------
def draw_game():
    draw_background()

    # Draw walls
    for wall in walls:
        draw_cell(wall, BLACK)

    # Draw snake
    for i, part in enumerate(snake):
        if i == 0:
            draw_cell(part, GREEN)
        else:
            draw_cell(part, DARK_GREEN)

    # Draw food depending on value
    if food_value == 1:
        food_color = RED
    elif food_value == 2:
        food_color = BLUE
    else:
        food_color = PURPLE

    draw_cell(food, food_color)

    # Draw score, level and food value
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLACK)
    food_text = font.render(f"Food: +{food_value}", True, BLACK)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (190, 10))
    screen.blit(food_text, (10, 35))

    pygame.display.update()


# -----------------------------
# GAME OVER
# -----------------------------
def game_over():
    screen.fill(WHITE)

    text1 = font.render("GAME OVER", True, RED)
    text2 = font.render(f"Score: {score}", True, BLACK)
    text3 = font.render(f"Level: {level}", True, BLACK)

    screen.blit(text1, text1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20)))
    screen.blit(text2, text2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10)))
    screen.blit(text3, text3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 35)))

    pygame.display.update()
    pygame.time.delay(2500)

    pygame.quit()
    sys.exit()


# -----------------------------
# NEXT LEVEL
# -----------------------------
def next_level():
    global level, speed, food

    level += 1
    speed += 2

    load_level(level)

    for part in snake:
        if part in walls:
            game_over()

    food = generate_food()


# -----------------------------
# START GAME
# -----------------------------
load_level(level)

for part in snake:
    if part in walls:
        print("Snake starts inside a wall. Fix level1.txt")
        pygame.quit()
        sys.exit()

food = generate_food()


# -----------------------------
# MAIN LOOP
# -----------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                next_direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                next_direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                next_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                next_direction = (1, 0)

    direction = next_direction

    # If food timer expires, generate new food
    current_time = pygame.time.get_ticks()
    if current_time - food_spawn_time > FOOD_LIFETIME:
        food = generate_food()

    # Move snake
    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx, head_y + dy)

    # Border collision
    if new_head[0] < 0 or new_head[0] >= GRID_W or new_head[1] < 0 or new_head[1] >= GRID_H:
        game_over()

    # Wall collision
    if new_head in walls:
        game_over()

    # Self collision
    if new_head in snake:
        game_over()

    snake.insert(0, new_head)

    # Food collision
    if new_head == food:
        score += food_value
        food = generate_food()

        if score >= level * 5:
            next_level()
    else:
        snake.pop()

    draw_game()
    clock.tick(speed)    
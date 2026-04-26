import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Practice 11")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 16)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 0, 220)
YELLOW = (255, 215, 0)
PURPLE = (128, 0, 128)
GRAY = (200, 200, 200)

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# -----------------------------
# TOOL SETTINGS
# -----------------------------
tool = "brush"
color = BLACK
brush_size = 6
drawing = False
start_pos = None
last_pos = None

colors = [BLACK, RED, GREEN, BLUE, YELLOW, PURPLE]
color_rects = []

# Create color palette rectangles
for i, c in enumerate(colors):
    rect = pygame.Rect(10 + i * 50, 10, 40, 40)
    color_rects.append((rect, c))


# -----------------------------
# DRAW UI
# -----------------------------
def draw_ui():
    screen.blit(canvas, (0, 0))

    # Top toolbar
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, 80))

    # Draw color palette
    for rect, c in color_rects:
        pygame.draw.rect(screen, c, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)

    # Draw tool information
    text1 = font.render(
        "B-brush R-rect C-circle E-eraser S-square T-right Y-equilateral H-rhombus",
        True,
        BLACK
    )
    text2 = font.render(
        f"Current tool: {tool}",
        True,
        BLACK
    )

    screen.blit(text1, (320, 15))
    screen.blit(text2, (320, 45))


# -----------------------------
# DRAW SQUARE
# -----------------------------
def draw_square(start, end):
    x1, y1 = start
    x2, y2 = end

    side = max(abs(x2 - x1), abs(y2 - y1))

    if x2 < x1:
        side = -side

    rect = pygame.Rect(x1, y1, side, side)
    pygame.draw.rect(canvas, color, rect, 3)


# -----------------------------
# DRAW RIGHT TRIANGLE
# -----------------------------
def draw_right_triangle(start, end):
    x1, y1 = start
    x2, y2 = end

    points = [
        (x1, y1),
        (x2, y1),
        (x1, y2)
    ]

    pygame.draw.polygon(canvas, color, points, 3)


# -----------------------------
# DRAW EQUILATERAL TRIANGLE
# -----------------------------
def draw_equilateral_triangle(start, end):
    x1, y1 = start
    x2, y2 = end

    base = x2 - x1
    height = int(abs(base) * math.sqrt(3) / 2)

    if base >= 0:
        points = [
            (x1, y2),
            (x2, y2),
            ((x1 + x2) // 2, y2 - height)
        ]
    else:
        points = [
            (x1, y2),
            (x2, y2),
            ((x1 + x2) // 2, y2 - height)
        ]

    pygame.draw.polygon(canvas, color, points, 3)


# -----------------------------
# DRAW RHOMBUS
# -----------------------------
def draw_rhombus(start, end):
    x1, y1 = start
    x2, y2 = end

    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2

    points = [
        (cx, y1),
        (x2, cy),
        (cx, y2),
        (x1, cy)
    ]

    pygame.draw.polygon(canvas, color, points, 3)


# -----------------------------
# MAIN LOOP
# -----------------------------
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Keyboard tool selection
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                tool = "brush"
            elif event.key == pygame.K_r:
                tool = "rect"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_s:
                tool = "square"
            elif event.key == pygame.K_t:
                tool = "right_triangle"
            elif event.key == pygame.K_y:
                tool = "equilateral_triangle"
            elif event.key == pygame.K_h:
                tool = "rhombus"

        # Mouse button pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos

            # Check if user clicked color palette
            clicked_color = False
            for rect, c in color_rects:
                if rect.collidepoint(mx, my):
                    color = c
                    clicked_color = True
                    break

            # Start drawing only below toolbar
            if not clicked_color and my > 80:
                drawing = True
                start_pos = event.pos
                last_pos = event.pos

                if tool == "brush":
                    pygame.draw.circle(canvas, color, event.pos, brush_size)
                elif tool == "eraser":
                    pygame.draw.circle(canvas, WHITE, event.pos, 20)

        # Mouse motion
        if event.type == pygame.MOUSEMOTION and drawing:
            if tool == "brush":
                pygame.draw.line(canvas, color, last_pos, event.pos, brush_size * 2)
                last_pos = event.pos

            elif tool == "eraser":
                pygame.draw.line(canvas, WHITE, last_pos, event.pos, 30)
                last_pos = event.pos

        # Mouse button released
        if event.type == pygame.MOUSEBUTTONUP and drawing:
            drawing = False
            end_pos = event.pos

            if tool == "rect":
                x1, y1 = start_pos
                x2, y2 = end_pos

                rect = pygame.Rect(
                    min(x1, x2),
                    min(y1, y2),
                    abs(x2 - x1),
                    abs(y2 - y1)
                )

                pygame.draw.rect(canvas, color, rect, 3)

            elif tool == "circle":
                x1, y1 = start_pos
                x2, y2 = end_pos

                radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
                pygame.draw.circle(canvas, color, start_pos, radius, 3)

            elif tool == "square":
                draw_square(start_pos, end_pos)

            elif tool == "right_triangle":
                draw_right_triangle(start_pos, end_pos)

            elif tool == "equilateral_triangle":
                draw_equilateral_triangle(start_pos, end_pos)

            elif tool == "rhombus":
                draw_rhombus(start_pos, end_pos)

    draw_ui()
    pygame.display.update()
    clock.tick(60)
import pygame
import sys
import random
from pygame.locals import *

pygame.init()
pygame.mixer.init()

# -----------------------------
# GAME SETTINGS
# -----------------------------
FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game - Practice 11")

# -----------------------------
# COLORS
# -----------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 215, 0)

# -----------------------------
# LOAD ASSETS
# -----------------------------
background = pygame.image.load("AnimatedStreet.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

player_img = pygame.image.load("Player.png")
player_img = pygame.transform.scale(player_img, (50, 90))

enemy_img = pygame.image.load("Enemy.png")
enemy_img = pygame.transform.scale(enemy_img, (50, 90))

pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)

crash_sound = pygame.mixer.Sound("crash.wav")

font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 40)

# -----------------------------
# GAME VARIABLES
# -----------------------------
enemy_speed = 7
passed_enemies = 0

coins_collected = 0
level = 1
COINS_FOR_LEVEL = 5


# -----------------------------
# PLAYER CLASS
# -----------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 70)

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)

        if pressed_keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# -----------------------------
# ENEMY CLASS
# -----------------------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        self.rect.center = (
            random.randint(40, SCREEN_WIDTH - 40),
            -60
        )

    def move(self):
        global passed_enemies

        self.rect.move_ip(0, enemy_speed)

        if self.rect.top > SCREEN_HEIGHT:
            passed_enemies += 1
            self.reset_position()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# -----------------------------
# COIN CLASS
# -----------------------------
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.value = 1
        self.image = None
        self.rect = None
        self.reset_position()

    def reset_position(self):
        # Coin gets random weight: 1, 2 or 3
        self.value = random.choice([1, 2, 3])

        # Bigger value means bigger coin
        size = 20 + self.value * 5

        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(
            self.image,
            YELLOW,
            (size // 2, size // 2),
            size // 2
        )

        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(40, SCREEN_WIDTH - 40),
            random.randint(-300, -50)
        )

    def move(self):
        self.rect.move_ip(0, enemy_speed)

        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def show_info():
    """
    Shows passed enemies, collected coins and current level.
    """
    passed_text = font.render(f"Passed: {passed_enemies}", True, WHITE)
    coins_text = font.render(f"Coins: {coins_collected}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    speed_text = font.render(f"Speed: {enemy_speed}", True, WHITE)

    DISPLAYSURF.blit(passed_text, (10, 10))
    DISPLAYSURF.blit(level_text, (10, 40))
    DISPLAYSURF.blit(speed_text, (10, 70))

    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 130, 10))


def game_over():
    """
    Stops music, plays crash sound and shows Game Over text.
    """
    pygame.mixer.music.stop()
    crash_sound.play()

    DISPLAYSURF.fill(BLACK)

    game_over_text = big_font.render("GAME OVER", True, RED)
    score_text = font.render(f"Coins: {coins_collected}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)

    DISPLAYSURF.blit(
        game_over_text,
        game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
    )

    DISPLAYSURF.blit(
        score_text,
        score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10))
    )

    DISPLAYSURF.blit(
        level_text,
        level_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))
    )

    pygame.display.update()
    pygame.time.delay(2500)

    pygame.quit()
    sys.exit()


# -----------------------------
# CREATE OBJECTS
# -----------------------------
P1 = Player()
E1 = Enemy()
C1 = Coin()


# -----------------------------
# MAIN LOOP
# -----------------------------
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.move()
    C1.move()

    # Check collision with enemy car
    if P1.rect.colliderect(E1.rect):
        game_over()

    # Check collision with coin
    if P1.rect.colliderect(C1.rect):
        coins_collected += C1.value
        C1.reset_position()

        # Increase enemy speed every N collected coins
        if coins_collected >= level * COINS_FOR_LEVEL:
            level += 1
            enemy_speed += 1

    DISPLAYSURF.blit(background, (0, 0))

    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
    C1.draw(DISPLAYSURF)

    show_info()

    pygame.display.update()
    FramePerSec.tick(FPS)
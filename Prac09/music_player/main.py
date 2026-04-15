import pygame
import sys
from player import MusicPlayer
pygame.init()
pygame.mixer.init()

WIDTH = 400
HEIGHT = 200
playlist = ["music/track1.wav", "music/track2.wav"]
player = MusicPlayer(playlist)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Music Player")

running = True
font = pygame.font.SysFont("Arial", 20)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next_track()

            elif event.key == pygame.K_b:
                player.previous_track()
    
    track_name = player.get_current_track_name().split("/")[-1]

    screen.fill((255,255,255))
    title = font.render("Music Player", True, (0,0,0))

    track = font.render(f"Current track: {track_name}", True, (0,0,0))

    controls1 = font.render("P - Play | S - Stop", True, (0,0,0))
    controls2 = font.render("N - Next | B - Previous", True, (0,0,0))

    screen.blit(title, (130,20))
    screen.blit(track, (80,70))
    screen.blit(controls1, (60,120))
    screen.blit(controls2, (60,150))
    pygame.display.flip()

pygame.quit()
sys.exit()
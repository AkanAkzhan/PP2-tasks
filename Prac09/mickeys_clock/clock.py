import pygame
from datetime import datetime


class MickeyClock:

    def __init__(self, width, height):

        self.center = (width // 2, height // 2)

        
        self.clock_image = pygame.image.load("images/clock.png").convert_alpha()

        self.right_hand = pygame.image.load("images/right_hand.png").convert_alpha()
        self.left_hand = pygame.image.load("images/left_hand.png").convert_alpha()

        self.clock_rect = self.clock_image.get_rect(center=self.center)


    def draw(self, screen):

        
        screen.blit(self.clock_image, self.clock_rect)

        
        now = datetime.now()

        seconds = now.second
        minutes = now.minute

        
        second_angle = -seconds * 6
        minute_angle = -minutes * 6

        
        rotated_right = pygame.transform.rotate(self.right_hand, second_angle)
        right_rect = rotated_right.get_rect(center=self.center)
        screen.blit(rotated_right, right_rect)

        
        rotated_left = pygame.transform.rotate(self.left_hand, minute_angle)
        left_rect = rotated_left.get_rect(center=self.center)
        screen.blit(rotated_left, left_rect)
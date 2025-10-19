"""
This module will create a cat dancing using pygame. This will provide a function for the main program to call.
"""
import pygame

class CatDancer:
    def __init__(self):
        self.cat_image = pygame.image.load("cat.png")
        self.cat_x, self.cat_y = 400, 300
        self.angle = 0
    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.cat_image, self.angle)
        rect = rotated_image.get_rect(center=(self.cat_x, self.cat_y))
        screen.blit(rotated_image, rect.topleft)

    def update(self):
        self.angle = (self.angle + 5) % 360

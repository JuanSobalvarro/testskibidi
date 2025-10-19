"""
This module will create a cat dancing using pygame. This will provide a function for the main program to call.
"""
import pygame

class CatDancer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("gatito.uwu")
        self.cat_image = pygame.image.load("cat.png")
        self.cat_x, self.cat_y = 400, 300
        self.angle = 0
        self.clock = pygame.time.Clock()
        self.run()

    def draw(self):
        rotated_image = pygame.transform.rotate(self.cat_image, self.angle)
        rect = rotated_image.get_rect(center=(self.cat_x, self.cat_y))
        self.screen.blit(rotated_image, rect.topleft)

    def update(self):
        self.angle = (self.angle + 5) % 360

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((255, 255, 255))
            self.draw()
            self.update()
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()

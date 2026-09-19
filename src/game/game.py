import math
import pygame
import src.entities.car
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

def main():
    running = True
    dt = 0
    courier_car = src.entities.car.Car()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        screen.fill((222, 244, 242))
        courier_car.update(dt, keys)
        courier_car.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    pygame.quit()
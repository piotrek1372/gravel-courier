import pygame

class Car:
    def __init__(self):
        self.x = 500
        self.y = 400
        self.rotate_degree = 0
        self.speed = 0
        self.acc = 2
        self.max_speed = 40
        self.braking_force = 1
        self.turning_speed = 1.1

    def update(self, dt, keys):
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.speed = self.acc
        self.x += self.speed * dt

    def draw(self, screen):
        rect = pygame.draw.rect(screen, "red", (self.x, self.y, 100, 300))

import math
import pygame
from pygame import Vector2
class Car:
    def __init__(self):
        self.pos = Vector2(450, 300)
        self.angle = 0
        self.direction_x = math.sin(self.angle)
        self.direction_y = -math.cos(self.angle)
        self.speed = 0
        self.acc = 2
        self.max_speed = 40
        self.braking_force = 1
        self.turning_speed = 1.1

    def update(self, dt, keys):
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.speed += self.acc
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.speed -= self.braking_force
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.angle -= self.turning_speed
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.angle += self.turning_speed
        self.pos[int(self.direction_x)] += self.speed * dt
        self.pos[int(self.direction_y)] += self.speed * dt

    def draw(self, screen):
        rect = pygame.draw.rect(screen, "red", (self.pos[0], self.pos[1], 100, 300))

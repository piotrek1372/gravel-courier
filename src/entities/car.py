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
        self.image = pygame.Surface([100, 300])
        self.image.fill("red")

    def update(self, dt, keys):
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.speed += self.acc
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.speed -= self.braking_force * dt
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.angle -= self.turning_speed * dt
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.angle += self.turning_speed * dt
        self.direction_x = math.sin(self.angle)
        self.direction_y = -math.cos(self.angle)
        self.pos[0] += self.direction_x * self.speed * dt
        self.pos[1] += self.direction_y * self.speed * dt


    def draw(self, screen):
        self.rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.rotated_rect = self.rotated_image.get_rect().centerx, self.rotated_image.get_rect().centery
        screen.blit(self.rotated_image, self.pos)

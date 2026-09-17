import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

def main():
    running = True
    while running:
        clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((222, 244, 242))
        pygame.display.flip()
    pygame.quit()

        
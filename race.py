import sys
import pygame
from settings import Settings
from car import Car


def run():
    pygame.init()
    all_settings = Settings()
    screen = pygame.display.set_mode((all_settings.sreen_width,
                                      all_settings.sreen_height))
    car = Car(screen)
    pygame.display.set_caption("Inwazja obcych")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(all_settings.background_color)
        car.blitme()

        pygame.display.flip()

run()
import sys

import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    player_class = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field_class = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)
        for obj in asteroids:
            collision = obj.check_for_collision(player_class)
            if collision:
                print('Game over!')
                sys.exit()
            for shot in shots:
                collision = obj.check_for_collision(shot)
                if collision:
                    obj.split()
                    shot.kill()

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # These are static variables inside the class. In python, you can just add them in a different file
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable, shots)

    Asteroid.containers = (asteroids, updatable, drawable)

    # Remember to use a comma to create a single tuple
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # Always remember to initialize!
    asteroid_field = AsteroidField()


    dt = 0

    while True:
        #quits if you press x
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Using the containers to keep the code organized
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if shot.collide(asteroid):
                    #kill is a feature built into pygame. It will stop drawing.
                    shot.kill()
                    asteroid.split()

            if asteroid.collide(player):
                print("Game Over!")
                # Always exits your program in python
                sys.exit()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        # this keeps the game running! FPS is locked at 70FPS
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # dont pass self twice, remember
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        # Implement this later
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)

            vector_1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
            vector_2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)
            new_radius_of_smaller_asteroid = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius_of_smaller_asteroid)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius_of_smaller_asteroid)

            new_asteroid1.velocity = vector_1 * 1.2
            new_asteroid2.velocity = vector_2 * 1.2












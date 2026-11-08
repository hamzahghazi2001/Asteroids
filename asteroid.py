import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rd =  random.uniform(20, 50)
            vector_one = self.velocity.rotate(rd)
            vector_two = self.velocity.rotate(rd*(-1))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            as1 = Asteroid(self.position.x, self.position.y, new_radius)
            as2 = Asteroid(self.position.x, self.position.y, new_radius)
            as1.velocity = vector_one * 1.2
            as2.velocity = vector_two * 1.2

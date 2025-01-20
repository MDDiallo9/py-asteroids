from circleshape import *
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        va = self.velocity.rotate(angle)
        vb = self.velocity.rotate(-angle)
        a = Asteroid(self.position.x,self.position.y,self.radius -ASTEROID_MIN_RADIUS)
        b = Asteroid(self.position.x,self.position.y,self.radius -ASTEROID_MIN_RADIUS)
        a.velocity = va * 1.2
        b.velocity = vb * 1.2

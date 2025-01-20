from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y,radius):
        super().__init__(x, y,radius=PLAYER_RADIUS)
        self.radius = radius

    def draw(self,screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt
from circleshape import *
from constants import *
from shot import *



class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.rotation = 0
        self.timer = 0
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)
    
    def rotate(self,dt):
        self.rotation += dt * PLAYER_TURN_SPEED
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_q]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_z]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            
            if self.timer > 0 :
                pass
            else:    
                self.shoot()
    
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        self.timer = PLAYER_SHOOT_COOLDOWN
        print("pew")
        bullet = Shot(self.position.x,self.position.y,SHOT_RADIUS)
        velocity = pygame.Vector2(0,1)
        velocity = velocity.rotate(self.rotation) * PLAYER_SHOOT_SPEED
        bullet.velocity = velocity
        
            

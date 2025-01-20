import os
os.environ["SDL_VIDEODRIVER"]="x11"
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"""Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}
""")
    on = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots,updatable,drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    

    while on :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for entity in updatable:
            entity.update(dt)
            
        for entity in drawable:
            entity.draw(screen)
        
        for asteroid in asteroids:
            if asteroid.collisionCheck(player) :
                on = False
        """ player.update(dt)
        player.draw(screen) """
        """ testA.draw(screen)
        testA.x += 1 """
        pygame.display.flip()
        dt =  clock.tick(60) / 1000
        """ print(f"dt: {dt:.4f} seconds, FPS: {1/dt:.2f} rot: {player.rotation} ast: {asteroids}") """
        """ print(f"Drawable group size: {len(drawable)}") """
if __name__ == "__main__":
    main()
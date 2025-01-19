import os
os.environ["SDL_VIDEODRIVER"]="x11"
import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"""Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}
""")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True :
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
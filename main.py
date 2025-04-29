# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    game_loop_run = True
    
    print("Starting Asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    

    while(game_loop_run):
        #quits if you press x
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        black = (0,0,0)
        screen.fill(black)
        # this keeps the game running! called at the end 
        pygame.display.flip()

    
    


if __name__ == "__main__":
    main()
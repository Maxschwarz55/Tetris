import pygame
import os
import random

#COLORS
GREY = (128, 128, 128)
BLACK = (0, 0, 0)



#WINDOW SETTINGS
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

#RECTANGLES/IMAGES
PLAY_AREA = pygame.Rect(0, 0, WIDTH // 2, HEIGHT)
GRID_WIDTH = 40
GRID_HEIGHT = 40

grid_vals = [ [0] * 10 for i in range(20)] #Create 10x20 grid space
GRID_RECTANGLES = []
#MISC
FPS = 60

def populate_grid_rectangles(): 
    y_count = 760
    for i in range(20):
        ROW = []
        x_count = 0
        for j in range(10):
            rect = pygame.Rect(x_count, y_count, GRID_WIDTH, GRID_HEIGHT)
            ROW.append(rect)
            x_count += GRID_WIDTH  
        GRID_RECTANGLES.append(ROW)
        y_count -= GRID_HEIGHT

def draw_window(): 
    WIN.fill(GREY)
   
    pygame.draw.rect(WIN, BLACK, PLAY_AREA)
    pygame.display.update()

def main(): 
    
    clock = pygame.time.Clock()
    run = True
    
    while run: 
        clock.tick(FPS)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False

        populate_grid_rectangles()
        draw_window()
    
    pygame.quit()

if __name__ == '__main__': 
    main()
import pygame
import os
import random

#COLORS
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
TEAL = (0, 128, 128)
WHITE = (255,255,255)
BLUE = (0, 0, 255)
ORANGE = (255, 69, 0)
YELLOW = (255, 234, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)


#WINDOW SETTINGS
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

#RECTANGLES/IMAGES
PLAY_AREA = pygame.Rect(0, 0, WIDTH // 2, HEIGHT)
GRID_WIDTH = 40
GRID_HEIGHT = 40


#GRID - ARRAYS
grid_vals = [ [0] * 10 for i in range(20)] #Create 10x20 grid space
GRID_RECTANGLES = []

#BLOCKS

BLOCKS = []

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

def create_blocks(): 
    
    #TEAL
    teal_block = []
    top_pos = 0
    for _ in range(4): 
        teal_square = pygame.Rect(WIDTH // 4 - GRID_WIDTH, top_pos, GRID_WIDTH, GRID_HEIGHT)
        teal_block.append(teal_square)
        top_pos += GRID_HEIGHT
    
    BLOCKS.append(teal_block)

    #BLUE

    blue_block = []

    top_pos = 0
    blue_block.append(pygame.Rect(WIDTH // 4 - (GRID_WIDTH * 2) , top_pos, GRID_WIDTH, GRID_HEIGHT))
    blue_block.append(pygame.Rect(WIDTH // 4 - (GRID_WIDTH * 2), top_pos + GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT))
    blue_block.append(pygame.Rect(WIDTH // 4 - GRID_WIDTH , top_pos + GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT))
    blue_block.append(pygame.Rect(WIDTH // 4, top_pos + GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT))

    BLOCKS.append(blue_block)

    #ORANGE

    orange_block = []
    
    orange_block.append(pygame.Rect(WIDTH // 4, top_pos, GRID_WIDTH, GRID_HEIGHT))
    orange_block.append(pygame.Rect(WIDTH // 4, top_pos + GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT))
    orange_block.append(pygame.Rect(WIDTH // 4 - GRID_WIDTH, top_pos + GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT))
    orange_block.append(pygame.Rect(WIDTH // 4 - (GRID_WIDTH * 2), top_pos + GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT))

    BLOCKS.append(orange_block)

    #YELLOW 

    yellow_block = []

    yellow_block.append(pygame.Rect(WIDTH // 4 - GRID_WIDTH, top_pos, GRID_WIDTH, GRID_HEIGHT))
    yellow_block.append(pygame.Rect(WIDTH // 4, top_pos, GRID_WIDTH, GRID_HEIGHT))
    yellow_block.append(pygame.Rect(WIDTH // 4 - GRID_WIDTH, top_pos + GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT))
    yellow_block.append(pygame.Rect(WIDTH // 4, top_pos + GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT))
    
    BLOCKS.append(yellow_block)

    #GREEN 

    green_block = []

    green_block.append(pygame.Rect(WIDTH // 4 - (GRID_WIDTH * 2), top_pos + GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT))
    green_block.append(pygame.Rect(WIDTH // 4 - GRID_WIDTH, top_pos + GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT))
    green_block.append(pygame.Rect(WIDTH // 4 - GRID_WIDTH, top_pos, GRID_WIDTH, GRID_HEIGHT))
    green_block.append(pygame.Rect(WIDTH // 4, top_pos, GRID_WIDTH, GRID_HEIGHT))
    
    BLOCKS.append(green_block)

    #PURPLE 

    purple_block = []

    purple_block.append(pygame.Rect(WIDTH // 4 - (GRID_WIDTH * 2), top_pos + GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT))
    purple_block.append(pygame.Rect(WIDTH // 4 - GRID_WIDTH, top_pos + GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT))
    purple_block.append(pygame.Rect(WIDTH // 4 - GRID_WIDTH, top_pos, GRID_WIDTH, GRID_HEIGHT))
    purple_block.append(pygame.Rect(WIDTH // 4, top_pos + GRID_WIDTH, GRID_WIDTH, GRID_HEIGHT))
    
    BLOCKS.append(purple_block)

    #RED

    red_block = []

    red_block.append(pygame.Rect(WIDTH // 4, top_pos + GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT))
    red_block.append(pygame.Rect(WIDTH // 4 - GRID_WIDTH, top_pos + GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT))
    red_block.append(pygame.Rect(WIDTH // 4 - GRID_WIDTH, top_pos, GRID_WIDTH, GRID_HEIGHT))
    red_block.append(pygame.Rect(WIDTH // 4 - (GRID_WIDTH * 2), top_pos, GRID_WIDTH, GRID_HEIGHT))
    
    BLOCKS.append(red_block)

def draw_window(): 
    WIN.fill(GREY)
    pygame.draw.rect(WIN, BLACK, PLAY_AREA)

    for row in GRID_RECTANGLES: 
        for column in row: 
            pygame.draw.rect(WIN, BLACK, column)

    create_blocks()
    for square in BLOCKS[6]: 
        pygame.draw.rect(WIN, RED, square)
    
    start_x = GRID_WIDTH
    for i in range(10): 
        pygame.draw.line(WIN, WHITE, (start_x, 0), (start_x, HEIGHT))
        start_x += GRID_WIDTH
    
    start_y = GRID_HEIGHT
    for i in range(20): 
        pygame.draw.line(WIN, WHITE, (0, start_y), (WIDTH // 2, start_y))
        start_y += GRID_WIDTH

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
import pygame
import os
import random
import time
import block
import new_rect


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
BLOCK_COLORS = [TEAL, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED]

#MISC
FPS = 60


def populate_grid_rectangles(): 
    y_count = 760
    for i in range(20):
        ROW = []
        x_count = 0
        for j in range(10):
            rect = new_rect.New_Rect(x_count, y_count, GRID_WIDTH, GRID_HEIGHT, BLACK)
            ROW.append(rect)
            x_count += GRID_WIDTH  
        GRID_RECTANGLES.append(ROW)
        y_count -= GRID_HEIGHT

def create_blocks(): 
    
    teal_block = block.Block()
    teal_block.create_teal()
    blue_block = block.Block()
    blue_block.create_blue()
    orange_block = block.Block()
    orange_block.create_orange()
    yellow_block = block.Block()
    yellow_block.create_yellow()
    green_block = block.Block()
    green_block.create_green()
    purple_block = block.Block()
    purple_block.create_purple()
    red_block = block.Block()
    red_block.create_red()

    BLOCKS.append(teal_block)
    BLOCKS.append(blue_block)
    BLOCKS.append(orange_block)
    BLOCKS.append(yellow_block)
    BLOCKS.append(green_block)
    BLOCKS.append(purple_block)
    BLOCKS.append(red_block)

def create_random_block(block_id): 
    
    tetronimo = block.Block()

    match block_id: 
        case 0:
            tetronimo.create_teal()
        case 1:
            tetronimo.create_blue()
        case 2:
            tetronimo.create_orange()
        case 3:
            tetronimo.create_yellow()
        case 4: 
            tetronimo.create_green()
        case 5: 
            tetronimo.create_purple()
        case 6: 
            tetronimo.create_red()

    return tetronimo
    

def let_block_fall(block_type, block_color, is_dropped):
    
    for row in range(20):
        for column in range(10): 
            for square in block_type:
                if square.colliderect(GRID_RECTANGLES[0][column]):
                    is_dropped = True
                if grid_vals[row][column] == 1 and square.colliderect(GRID_RECTANGLES[row + 1][column]):
                    is_dropped = True
                    GRID_RECTANGLES[row + 1][column].color = block_color

                if is_dropped and square.colliderect(GRID_RECTANGLES[row][column]):
                    grid_vals[row][column] = 1
                    GRID_RECTANGLES[row][column] = square
                    GRID_RECTANGLES[row][column].color = block_color

    if is_dropped == False:
        for i in range(len(block_type)):
            block_type[i].y += GRID_HEIGHT

    return is_dropped
    

def move_left(block_type):

    for square in block_type: 
        if (square.x - GRID_WIDTH < 0):
            return
    
    for row in range(20):
        for column in range(10):
            for square in block_type:
                if grid_vals[row][column] == 1 and column < 9 and square.colliderect(GRID_RECTANGLES[row][column + 1]): 
                    return

        
    for square in block_type:
        square.x -= GRID_WIDTH

def move_right(block_type): 
    
    for square in block_type: 
        if (square.x + (GRID_WIDTH * 2)> WIDTH // 2):
            return
        
    for row in range(20):
        for column in range(10):
            for square in block_type:
                if grid_vals[row][column] == 1 and column > 0 and square.colliderect(GRID_RECTANGLES[row][column - 1]): 
                    return
    
    for square in block_type: 
        square.x += GRID_WIDTH


        
def draw_window(block_type, block_color): 
    WIN.fill(GREY)
    pygame.draw.rect(WIN, BLACK, PLAY_AREA)

    for row in range(20): 
        for column in range(10): 
           color = GRID_RECTANGLES[row][column].color
           pygame.draw.rect(WIN, color, GRID_RECTANGLES[row][column]) 

            

    for square in block_type: 
        pygame.draw.rect(WIN, block_color, square)

    
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

    create_blocks()
    
    clock = pygame.time.Clock()
    run = True
    
    fall_counter = 1

    block_id = random.randint(0, 6)
    block_dropped = False
    drop_new_block = True

    while run: 
        clock.tick(FPS)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT and block_dropped == False: 
                    move_left(block_type)
                if event.key == pygame.K_RIGHT and block_dropped == False:
                    move_right(block_type)

        time_elapsed = pygame.time.get_ticks()

        populate_grid_rectangles()
        
        if drop_new_block:
            tetronimo = create_random_block(block_id)
            block_type = tetronimo.blocks
            block_color = tetronimo.color
            drop_new_block = False

        if time_elapsed >= fall_counter * 400:
            fall_counter += 1
            block_dropped = let_block_fall(block_type, block_color, block_dropped)
        if block_dropped == True: 
            block_id = random.randint(0,6)
            block_dropped = False
            drop_new_block = True

        draw_window(block_type, block_color)
            
    
    pygame.quit()

if __name__ == '__main__': 
    main()
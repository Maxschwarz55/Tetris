import pygame
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

WIDTH = 800
HEIGHT = 800

class Block: 
    def __init__(self): 
        self.color = None
        self.blocks = []
        self.rotation_state = 0
        self.SQUARE_WIDTH = 40
        self.SQUARE_HEIGHT = 40
        

    def create_teal(self): 

        teal_block = []
        self.color = TEAL  
        top_pos = 0
        
        for _ in range(4): 
            teal_square = new_rect.New_Rect(WIDTH // 4 - self.SQUARE_WIDTH, top_pos, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color)
            teal_block.append(teal_square)
            top_pos += self.SQUARE_HEIGHT
        
        self.blocks = teal_block


    def create_blue(self): 
       
        blue_block = []
        self.color = BLUE
        top_pos = 0
        
        blue_block.append(new_rect.New_Rect(WIDTH // 4 - ( self.SQUARE_WIDTH * 2) , top_pos, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color)), 
        blue_block.append(new_rect.New_Rect(WIDTH // 4 - (self.SQUARE_WIDTH * 2), top_pos + self.SQUARE_HEIGHT, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))
        blue_block.append(new_rect.New_Rect(WIDTH // 4 - self.SQUARE_WIDTH , top_pos + self.SQUARE_HEIGHT, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))
        blue_block.append(new_rect.New_Rect(WIDTH // 4, top_pos + self.SQUARE_HEIGHT, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))

        self.blocks = blue_block

    def create_orange(self): 
        
        orange_block = []
        self.color = ORANGE
        top_pos = 0
        
        orange_block.append(new_rect.New_Rect(WIDTH // 4, top_pos, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))
        orange_block.append(new_rect.New_Rect(WIDTH // 4, top_pos + self.SQUARE_HEIGHT, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))
        orange_block.append(new_rect.New_Rect(WIDTH // 4 - self.SQUARE_WIDTH, top_pos + self.SQUARE_HEIGHT, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))
        orange_block.append(new_rect.New_Rect(WIDTH // 4 - (self.SQUARE_WIDTH * 2), top_pos + self.SQUARE_HEIGHT, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))

        self.blocks = orange_block
    
    def create_yellow(self): 

        yellow_block = []
        self.color = YELLOW
        top_pos = 0

        yellow_block.append(new_rect.New_Rect(WIDTH // 4 - self.SQUARE_WIDTH, top_pos, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))
        yellow_block.append(new_rect.New_Rect(WIDTH // 4, top_pos, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))
        yellow_block.append(new_rect.New_Rect(WIDTH // 4 - self.SQUARE_WIDTH, top_pos + self.SQUARE_HEIGHT, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))
        yellow_block.append(new_rect.New_Rect(WIDTH // 4, top_pos + self.SQUARE_HEIGHT, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))

        self.blocks = yellow_block

    def create_green(self): 

        green_block = []
        self.color = GREEN
        top_pos = 0

        green_block.append(new_rect.New_Rect(WIDTH // 4 - (self.SQUARE_WIDTH * 2), top_pos + self.SQUARE_HEIGHT, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))
        green_block.append(new_rect.New_Rect(WIDTH // 4 - self.SQUARE_WIDTH, top_pos + self.SQUARE_HEIGHT, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))
        green_block.append(new_rect.New_Rect(WIDTH // 4 - self.SQUARE_WIDTH, top_pos, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))
        green_block.append(new_rect.New_Rect(WIDTH // 4, top_pos, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))

        self.blocks = green_block

    def create_purple(self): 

        purple_block = []
        self.color = PURPLE
        top_pos = 0

        purple_block.append(new_rect.New_Rect(WIDTH // 4 - (self.SQUARE_WIDTH * 2), top_pos + self.SQUARE_HEIGHT, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))
        purple_block.append(new_rect.New_Rect(WIDTH // 4 - self.SQUARE_WIDTH, top_pos + self.SQUARE_HEIGHT, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))
        purple_block.append(new_rect.New_Rect(WIDTH // 4 - self.SQUARE_WIDTH, top_pos, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))
        purple_block.append(new_rect.New_Rect(WIDTH // 4, top_pos + self.SQUARE_WIDTH, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))

        self.blocks = purple_block

    def create_red(self): 

        red_block = []
        self.color = RED
        top_pos = 0

        red_block.append(new_rect.New_Rect(WIDTH // 4, top_pos + self.SQUARE_HEIGHT, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))
        red_block.append(new_rect.New_Rect(WIDTH // 4 - self.SQUARE_WIDTH, top_pos + self.SQUARE_HEIGHT, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))
        red_block.append(new_rect.New_Rect(WIDTH // 4 - self.SQUARE_WIDTH, top_pos, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))
        red_block.append(new_rect.New_Rect(WIDTH // 4 - (self.SQUARE_WIDTH * 2), top_pos, self.SQUARE_WIDTH, self.SQUARE_HEIGHT, self.color))

        self.blocks = red_block

    def rotate_teal(self): 

        teal_block = []
        if self.rotation_state == 0: 
            teal_block.append(new_rect.New_Rect(self.blocks[0].x - (self.SQUARE_WIDTH * 2), self.blocks[0].y + (self.SQUARE_WIDTH * 2), 
            self.SQUARE_HEIGHT, self.SQUARE_WIDTH, self.color))
            teal_block.append(new_rect.New_Rect(self.blocks[0].x - (self.SQUARE_WIDTH), self.blocks[0].y + (self.SQUARE_WIDTH), 
            self.SQUARE_HEIGHT, self.SQUARE_WIDTH, self.color))
            teal_block.append(new_rect.New_Rect(self.blocks[0].x + (self.SQUARE_WIDTH), self.blocks[0].y - (self.SQUARE_WIDTH), 
            self.SQUARE_HEIGHT, self.SQUARE_WIDTH, self.color))
            teal_block.append(new_rect.New_Rect(self.blocks[0].x + (self.SQUARE_WIDTH * 2), self.blocks[0].y - (self.SQUARE_WIDTH * 2), 
            self.SQUARE_HEIGHT, self.SQUARE_WIDTH, self.color))
    

        
            




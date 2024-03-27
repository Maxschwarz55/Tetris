import pygame

class New_Rect(pygame.Rect): 
    def __init__(self, left, top, width, height, color):
        super().__init__(left, top, width, height)
        self.color = color

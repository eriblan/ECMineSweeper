import pygame
import random

class Cell:
    """This file contains the cell class representing each square in the game"""

    def __init__(self, x, y, width, height, bomb_chance):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (0, 64, 0)  # RGB color
        self.text_color = (255,255,255)
        self.cell_thickness = 2
        self.neighbouring_bombs = 0
        self.selected = False

        self.cell_center = (
            self.x + self.width // 2,
            self.y + self.width // 2,
        )  # useful for drawing
        self.bomb = (
            random.random() < bomb_chance
        )  # each cell has a chance of being a bomb

    def draw(self,screen):
        """This method is called in the main.py files draw_cells fkn"""
        # Hint: Should draw each cell, i.e something to do with pygame.draw.rect
        # Later on in the assignment it will do more as well such as drawing X for bombs or writing digits
        # Important: Remember that pygame starts with (0,0) coordinate in upper left corner!

        # Draw cells
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), self.cell_thickness)

        font=pygame.font.SysFont('Arial', 40)

        # If cell is clicked on
        if self.selected:
            """
            if self.bomb:
                cell_text = font.render("X", True, self.text_color)
                screen.blit(cell_text, (self.x, self.y))


            elif not self.bomb:
                cell_text = font.render(str(self.neighboring_bombs), True, self.text_color)
                screen.blit(cell_text, (self.x, self.y))
            """
            
            # If cell has bomb, show X
            if self.bomb:
                cell_text = font.render("X", True, self.text_color)
                text_rect = cell_text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
                screen.blit(cell_text, text_rect)
            # If cell does not have a bomb, show number of neighboring bombs
            elif not self.bomb:
                cell_text = font.render(str(self.neighboring_bombs), True, self.text_color)
                text_rect = cell_text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
                screen.blit(cell_text, text_rect)
            

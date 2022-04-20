import pygame
import numpy as np
from Board import Board

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)


class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y, block_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((block_size, block_size))  # Create a block_size x block_size surface for sprite
        self.image.fill(BLACK)  # Fill cell with black
        self.rect = self.image.get_rect()  # Obtain the coordinates contained in our cell
        self.rect.x = x * block_size  # Get start upper-left coord of our rectangle
        self.rect.y = y * block_size
        self.block_size = block_size

    def update(self, cells, status=2):
        if status == 1:
            self.image.fill(BLACK) # If status == 1, we revert to original fill color, BLACK
        else:
            x_val, y_val = self.rect.x // self.block_size, self.rect.y // self.block_size
            # The above gives us the corresponding index for our cell in our sparse matrix
            if cells[x_val, y_val] == 1:
                self.image.fill(WHITE)
            elif cells[x_val, y_val] == 0:
                self.image.fill(BLACK)
            return cells

import sys
import pygame
import time

from Cell import Cell
from Board import Board


class Game:
    def __init__(self):
        pygame.init()

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.block_size = 40
        self.x_size = self.WINDOW_WIDTH // self.block_size  # Get cell count along x-axis
        self.y_size = self.WINDOW_HEIGHT // self.block_size  # Get cell count along y-axis
        self.cell_sprites = pygame.sprite.Group()  # Create group for sprites to be added

        pygame.display.set_caption("Conway's Game of Life")
        self.SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.SCREEN.fill(self.BLACK)
        self.CLOCK = pygame.time.Clock()
        self.cells = Board({})  # Initialize our sparse matrix
        self.init_sprites()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Close Game
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:  # Modify between evolutions
                    x_pos, y_pos = event.pos
                    for sprites in self.cell_sprites:
                        if sprites.rect.collidepoint(x_pos, y_pos):
                            x, y = sprites.rect.x // self.block_size, sprites.rect.y // self.block_size
                            self.cells = self.cells.swap_status(x, y)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Iterate through evolutions
                        self.cells = self.cells.life_status()
                    if event.key == pygame.K_SPACE:  # Clear cells/board
                        self.cells = Board()
                        for sprites in self.cell_sprites:
                            sprites.update(self.cells, 1)
                    if event.key == pygame.K_0:
                        count = 0
                        while count <= 100:
                            self.cells = self.cells.life_status()
                            self.update_cells()
                            self.cell_sprites.draw(self.SCREEN)
                            self.create_grid()
                            pygame.display.update()
                            time.sleep(0.2)
                            if len(self.cells) == 0:
                                break
                            count += 1
            self.update_cells()
            self.cell_sprites.draw(self.SCREEN)
            self.create_grid()
            self.CLOCK.tick(60)
            pygame.display.update()

    def update_cells(self):
        for sprites in self.cell_sprites:  # Reset board
            sprites.image.fill(self.BLACK)
        for cells in self.cells:  # For each cell, if board contains a 1 at cell coordinate, fill cell white
            r, c = cells
            if self.cells[r, c] == 1:
                for sprites in self.cell_sprites:
                    if sprites.rect.collidepoint(r * self.block_size, c * self.block_size):
                        sprites.image.fill(self.WHITE)

    def init_sprites(self):
        for w in range(self.WINDOW_WIDTH // self.block_size):
            for h in range(self.WINDOW_HEIGHT // self.block_size):
                self.cell_sprites.add(Cell(w, h, self.block_size))  # Add our sprites to our Sprite Group

    def create_grid(self):
        for w in range(self.WINDOW_WIDTH // self.block_size): # draw grid rectangles
            for h in range(self.WINDOW_HEIGHT // self.block_size):
                rect = pygame.Rect(w * self.block_size, h * self.block_size, self.block_size, self.block_size)
                pygame.draw.rect(self.SCREEN, self.WHITE, rect, 1)


Game()

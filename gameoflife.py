import sys

import pygame

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
# cell_sprites = pygame.sprite.Group()


# class Cell(pygame.sprite.Sprite):
#     def __init__(self, x, y, block_size):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((block_size, block_size))
#         self.image.fill(WHITE)
#         self.rect = self.image.get_rect()
#         self.rect.x = x * block_size
#         self.rect.y = y * block_size
#         self.clicked = False
#
#     def update(self):
#         if self.clicked:
#             self.image.fill(WHITE)


def draw_grid(block_size):
    for h in range(WINDOW_HEIGHT):
        for w in range(WINDOW_WIDTH):
            rect = pygame.Rect(h * block_size, w * block_size, block_size, block_size)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)


def main():
    global SCREEN, CLOCK, cells
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    SCREEN.fill(BLACK)
    CLOCK = pygame.time.Clock()

    # for i in range(WINDOW_HEIGHT):
    #     for j in range(WINDOW_WIDTH):
    #         cell_sprites.add(Cell(i, j, 20))

    while True:
        draw_grid(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     x_pos, y_pos = event.pos
            #     for cell in cell_sprites:
            #         if cell.rect.collidepoint(x_pos, y_pos):
            #             cell.clicked = not cell.clicked
            #             cell.update()
        pygame.display.update()



if __name__ == "__main__":
    main()

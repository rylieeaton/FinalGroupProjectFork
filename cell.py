import pygame

pygame.font.init()
FONT = pygame.font.SysFont("arial", 32)
SKETCH_FONT = pygame.font.SysFont("arial", 18)

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.sketched = 0

    def set_cell_value(self, value):
        self.value = value
        self.sketched = 0
    
    def set_sketched_value(self, value):
        self.sketched = value
        self.value = 0
    
    def draw(self):
        x = self.col * 60
        y = self.row * 60
        rect = pygame.Rect(x, y, 60, 60)

        self.screen.fill((255, 255, 255), rect)
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), rect, 3)
        else:
            pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)
        
        if self.value != 0:
            text = FONT.render(str(self.value), True, (0, 0, 0,))
            self.screen.blit(text, (x + 20, y + 10))

        elif self.sketched != 0:
            text = SKETCH_FONT.render(str(self.sketched), True, (100, 100, 100))
            self.screen.blit(text, (x + 5, y + 5))

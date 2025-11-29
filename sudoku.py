import sudoku_generator
from board import Board
from cell import Cell
import pygame

class Sudoku:

    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((540, 540))
        pygame.display.set_caption("Sudoku Game")

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.ORANGE = (255, 165, 0)

    def generate_first_screen(self):
        difficulty = None
        font = pygame.font.SysFont("arial", 20)

        first_button = pygame.Rect(50, 400, 100, 50)
        second_button = pygame.Rect(200, 400, 100, 50)
        third_button = pygame.Rect(350, 400, 100, 50)

        while difficulty is None:
            self.screen.fill(self.WHITE)

            pygame.draw.rect(self.screen, self.ORANGE, first_button)
            pygame.draw.rect(self.screen, self.ORANGE, second_button)
            pygame.draw.rect(self.screen, self.ORANGE, third_button)

            text1 = font.render("Easy", True, self.BLACK)
            text2 = font.render("Medium", True, self.BLACK)
            text3 = font.render("Hard", True, self.BLACK)

            self.screen.blit(text1, text1.get_rect(center=first_button.center))
            self.screen.blit(text2, text2.get_rect(center=second_button.center))
            self.screen.blit(text3, text3.get_rect(center=third_button.center))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if first_button.collidepoint(pos):
                        difficulty = 1
                    elif second_button.collidepoint(pos):
                        difficulty = 2
                    elif third_button.collidepoint(pos):
                        difficulty = 3

        return difficulty

    def game_play(self):
        difficulty = self.generate_first_screen()
        self.screen.fill(self.WHITE)
        pygame.display.flip()

        level = {1: "easy", 2: "medium", 3: "hard"}.get(difficulty, "easy")

        self.screen.fill(self.WHITE)
        new_board = Board(9, 9, self.screen, level)
        game_play_on = True
        while game_play_on:
            
            new_board.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_play_on = False
                    pygame.quit()
                    exit()

    def run(self):
        self.game_play()


if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.run()

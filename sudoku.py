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
            mouse_pos = pygame.mouse.get_pos()
            mouse_posx = mouse_pos[0]
            mouse_posy = mouse_pos[1]

            ##Code below for interactive elements
            for eve in pygame.event.get():

                if eve.type == pygame.MOUSEBUTTONDOWN:
                    cell_chose = []
                    cell_chose = new_board.click(mouse_posx, mouse_posy)
                    cell_chosenx = cell_chose[0]
                    cell_choseny = cell_chose[1]

                    if cell_chose != None:
                        new_board.select(cell_chosenx, cell_choseny)
                        #print(new_board.board)

                if eve.type == pygame.KEYDOWN:
                    cell_chose = list(cell_chose)
                    #print(cell_chose)

                    if eve.key == pygame.K_1:
                        new_cell = Cell(1,cell_chosenx, cell_choseny,self.screen)
                        new_cell.draw()
                        pygame.display.flip()
                    elif eve.key == pygame.K_2:
                        new_cell = Cell(2, cell_chosenx, cell_choseny, self.screen)
                        new_cell.draw()
                        pygame.display.flip()
                    elif eve.key == pygame.K_3:
                        new_cell = Cell(3, cell_chosenx, cell_choseny, self.screen)
                        new_cell.draw()
                        pygame.display.flip()
                    elif eve.key == pygame.K_4:
                        new_cell = Cell(4, cell_chosenx, cell_choseny, self.screen)
                        new_cell.draw()
                        pygame.display.flip()
                    elif eve.key == pygame.K_5:
                        new_cell = Cell(5, cell_chosenx, cell_choseny, self.screen)
                        new_cell.draw()
                        pygame.display.flip()
                    elif eve.key == pygame.K_6:
                        new_cell = Cell(6, cell_chosenx, cell_choseny, self.screen)
                        new_cell.draw()
                        pygame.display.flip()
                    elif eve.key == pygame.K_7:
                        new_cell = Cell(7, cell_chosenx, cell_choseny, self.screen)
                        new_cell.draw()
                        pygame.display.flip()
                    elif eve.key == pygame.K_8:
                        new_cell = Cell(8, cell_chosenx, cell_choseny, self.screen)
                        new_cell.draw()
                        pygame.display.flip()
                    elif eve.key == pygame.K_9:
                        new_cell = Cell(9, cell_chosenx, cell_choseny, self.screen)
                        new_cell.draw()
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
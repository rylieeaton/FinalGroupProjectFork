import sudoku_generator
from board import Board
from cell import Cell
import pygame

##Todo: need to add ability to hit enter

##Todo: need to add a win screen/loss screen

##Todo: need to add check for win

class Sudoku:

    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((540, 650))
        pygame.display.set_caption("Sudoku Game")

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.ORANGE = (255, 165, 0)

    def generate_first_screen(self):
        difficulty = None
        font = pygame.font.SysFont("arial", 20)

        first_button = pygame.Rect(108, 400, 100, 50)
        second_button = pygame.Rect(216, 400, 100, 50)
        third_button = pygame.Rect(324, 400, 100, 50)

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

            font_title = pygame.font.SysFont("arial", 40)
            text4 = font_title.render("Select a Game Mode", True, self.BLACK)
            self.screen.blit(text4, (80,100))
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
        game_func_active = True
        while game_func_active:
            difficulty = self.generate_first_screen()
            self.screen.fill(self.WHITE)
            pygame.display.flip()

            level = {1: "easy", 2: "medium", 3: "hard"}.get(difficulty, "easy")

            self.screen.fill(self.WHITE)
            current_board = Board(9, 9, self.screen, level)

            font_buttons = pygame.font.SysFont("arial", 25)

            game_first_button = pygame.Rect(108, 560, 100, 50)
            game_second_button = pygame.Rect(216, 560, 100, 50)
            game_third_button = pygame.Rect(324, 560, 100, 50)

            pygame.draw.rect(self.screen, self.ORANGE, game_first_button)
            pygame.draw.rect(self.screen, self.ORANGE, game_second_button)
            pygame.draw.rect(self.screen, self.ORANGE, game_third_button)

            text_1 = font_buttons.render("Reset", True, self.BLACK)
            text_2 = font_buttons.render("Restart", True, self.BLACK)
            text_3 = font_buttons.render("Exit", True, self.BLACK)

            self.screen.blit(text_1, text_1.get_rect(center=game_first_button.center))
            self.screen.blit(text_2, text_2.get_rect(center=game_second_button.center))
            self.screen.blit(text_3, text_3.get_rect(center=game_third_button.center))

            game_play_on = True
            cell_chose = (0,0)

            while game_play_on:
                current_board.draw()
                #print(vars(current_board.solution))
                #current_board = new_board.board
                pygame.display.flip()
                mouse_pos = pygame.mouse.get_pos()
                mouse_posx = mouse_pos[0]
                mouse_posy = mouse_pos[1]

                ##Code below for interactive elements
                for eve in pygame.event.get():

                    if eve.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if game_first_button.collidepoint(pos):
                            current_board.reset_to_original()
                            current_board.draw()
                            pygame.display.flip()
                        elif game_second_button.collidepoint(pos):
                            game_play_on = False
                        elif game_third_button.collidepoint(pos):
                            game_play_on = False
                            pygame.quit()
                            exit()
                        else:
                            cell_chose = current_board.click(mouse_posx, mouse_posy)

                            current_board.select(cell_chose[0], cell_chose[1])

                    if eve.type == pygame.KEYDOWN:
                        pre_cell_val_x = cell_chose[0]
                        pre_cell_val_y = cell_chose[1]
                        pre_val = current_board.board[pre_cell_val_x][pre_cell_val_y]


                        if eve.key == pygame.K_1 and pre_val == 0:
                            new_cell = Cell(1,cell_chose[0], cell_chose[1],self.screen)
                            current_board.cells[cell_chose[0]][cell_chose[1]] = new_cell
                            new_cell.draw()
                            pygame.display.flip()
                        elif eve.key == pygame.K_2 and pre_val == 0:
                            new_cell = Cell(2, cell_chose[0], cell_chose[1], self.screen)
                            current_board.cells[cell_chose[0]][cell_chose[1]] = new_cell
                            new_cell.draw()
                            pygame.display.flip()
                        elif eve.key == pygame.K_3 and pre_val == 0:
                            new_cell = Cell(3, cell_chose[0], cell_chose[1], self.screen)
                            current_board.cells[cell_chose[0]][cell_chose[1]] = new_cell
                            new_cell.draw()
                            pygame.display.flip()
                        elif eve.key == pygame.K_4 and pre_val == 0:
                            new_cell = Cell(4, cell_chose[0], cell_chose[1], self.screen)
                            current_board.cells[cell_chose[0]][cell_chose[1]] = new_cell
                            new_cell.draw()
                            pygame.display.flip()
                        elif eve.key == pygame.K_5 and pre_val == 0:
                            new_cell = Cell(5, cell_chose[0], cell_chose[1], self.screen)
                            current_board.cells[cell_chose[0]][cell_chose[1]] = new_cell
                            new_cell.draw()
                            pygame.display.flip()
                        elif eve.key == pygame.K_6 and pre_val == 0:
                            new_cell = Cell(6, cell_chose[0], cell_chose[1], self.screen)
                            current_board.cells[cell_chose[0]][cell_chose[1]] = new_cell
                            new_cell.draw()
                            pygame.display.flip()
                        elif eve.key == pygame.K_7 and pre_val == 0:
                            new_cell = Cell(7, cell_chose[0], cell_chose[1], self.screen)
                            current_board.cells[cell_chose[0]][cell_chose[1]] = new_cell
                            new_cell.draw()
                            pygame.display.flip()
                        elif eve.key == pygame.K_8 and pre_val == 0:
                            new_cell = Cell(8, cell_chose[0], cell_chose[1], self.screen)
                            current_board.cells[cell_chose[0]][cell_chose[1]] = new_cell
                            new_cell.draw()
                            pygame.display.flip()
                        elif eve.key == pygame.K_9 and pre_val == 0:
                            new_cell = Cell(9, cell_chose[0], cell_chose[1], self.screen)
                            current_board.cells[cell_chose[0]][cell_chose[1]] = new_cell
                            new_cell.draw()
                            pygame.display.flip()

                        elif eve.key == pygame.K_UP:
                            cell_chose = (max(0, cell_chose[0] -1), cell_chose[1])
                            current_board.select(cell_chose[0], cell_chose[1])
                        elif eve.key == pygame.K_DOWN:
                            cell_chose = (min(8, cell_chose[0]+1), cell_chose[1])
                            current_board.select(cell_chose[0], cell_chose[1])
                        elif eve.key == pygame.K_LEFT:
                            cell_chose = (cell_chose[0], max(0, cell_chose[1]-1))
                            current_board.select(cell_chose[0], cell_chose[1])
                        elif eve.key == pygame.K_RIGHT:
                            cell_chose = (cell_chose[0], min(8, cell_chose[1] + 1))
                            current_board.select(cell_chose[0], cell_chose[1])
                        elif eve.key == pygame.K_RETURN:
                            if current_board.is_full():
                                current_board.solution
                                print(vars(current_board))
                                if current_board.check_board():
                                    print("win")
                                else:
                                    print("gameover")



                    elif eve.type == pygame.QUIT:
                        game_play_on = False
                        pygame.quit()
                        exit()

    def run(self):
        self.game_play()


if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.run()
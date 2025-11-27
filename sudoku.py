import sudoku_generator
from board import Board
from cell import Cell
import pygame

class Sudoku():

    ##add the screen for the sudoku difficulty thing


    def __init__(self):
        #self.sudoku = sudoku_generator.generate_sudoku(9, 3)
        self.running = True

    def generate_first_screen (self):
        start_screen_on_intial = True#activates the first while loop in the method

        # colors
        White = (255, 255, 255)
        Black = (0, 0, 0)
        Orange = (255, 165, 0)
        # colors

        #loop for start screen generation
        #Each while loop divides a piece of the start screen, as it helped me debug
        while start_screen_on_intial:
            start_screen = pygame.display.set_mode((500, 500))
            pygame.display.set_caption("Sudoku_Game")
            start_screen_on_second = True
            for event in pygame.event.get(): #for loop is created so that while the game has not entered the next screen, will continue projecting the screen
                if event.type == pygame.QUIT:
                    start_screen_on_intial = False
                    pygame.quit()
                else:
                    start_screen_on_second = True#activates the next step - which is making the screen white

                    while start_screen_on_second:
                        start_screen.fill(White)
                        pygame.display.flip()
                        start_screen_on_third = True#activates the next step - which is adding the buttons

                        while start_screen_on_third:
                            first_button = pygame.draw.rect(start_screen, Orange, [50, 400, 100, 50])
                            second_button =pygame.draw.rect(start_screen, Orange, [200, 400, 100, 50])
                            third_button = pygame.draw.rect(start_screen, Orange, [350, 400, 100, 50])
                            pygame.display.flip()
                            start_screen_on_fourth = True#activates the next step - which is adding the text

                            while start_screen_on_fourth:
                                button_text_font = pygame.font.SysFont("arial", 20)

                                button_one_text = "Easy"
                                button_two_text = "Medium"
                                button_three_text = "Hard"

                                text_of_button_one = button_text_font.render(button_one_text, True, Black)
                                center_text_of_button_one = text_of_button_one.get_rect(center=first_button.center)
                                start_screen.blit(text_of_button_one, center_text_of_button_one)

                                text_of_button_two = button_text_font.render(button_two_text, True, Black)
                                center_text_of_button_two = text_of_button_two.get_rect(center=second_button.center)
                                start_screen.blit(text_of_button_two, center_text_of_button_two)

                                text_of_button_three = button_text_font.render(button_three_text, True, Black)
                                center_text_of_button_three = text_of_button_three.get_rect(center=third_button.center)
                                start_screen.blit(text_of_button_three, center_text_of_button_three)

                                pygame.display.flip()





    def run(self):
        self.generate_first_screen()
        while self.running:
            #need to insert code that creates user interactions with the buttons created in the generate_first_screen method
            for event in pygame.event.get():
                if event.type == 0:
                   self.running = False
                   pygame.quit()



if __name__ == '__main__':
    sudoku = Sudoku()
    sudoku.run()


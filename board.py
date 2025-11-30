import pygame
from cell import Cell
from sudoku_generator import generate_sudoku, SudokuGenerator

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        print("board being initialized")

        if difficulty == "easy":
            removed = 30
        elif difficulty == "medium":
            removed = 40
        else:
            removed = 50
        ##og code
        #self.board = generate_sudoku(9, removed)

        #solver = SudokuGenerator(9, removed)
        #solver.fill_values()
        #self.solution = solver.get_board()
        ##og code

        self.solution = SudokuGenerator(9, removed)
        self.solution.fill_values()

        self.solution_array = []
        for b in self.solution.board:
            self.solution_array.append(b[:])

        self.board = generate_sudoku(9, removed)
        self.board = self.solution.remove_cells_return()

        self.original = []
        for row in self.board:
            new_row = []
            for value in row:
                new_row.append(value)

            self.original.append(new_row)

        self.cells = []
        for r in range(9):
            row_cells = []
            for c in range(9):
                row_cells.append(Cell(self.board[r][c], r, c, screen))
            self.cells.append(row_cells)

        self.selected = None

    def draw(self):
        for row in self.cells:
            for cell in row:
                cell.draw()

        for i in range(10):
            thickness = 3 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 60), (540, i * 60), thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (i * 60, 0), (i * 60, 540), thickness)

    def select(self, row, col):
        if self.selected:
            r, c = self.selected
            self.cells[r][c].selected = False

        self.selected = (row, col)
        self.cells[row][col].selected = True

    def click(self, x, y):
        if x < 540 and y < 540:
            return (y // 60, x // 60)
        return None

    def clear(self):
        if self.selected:
            r, c = self.selected
            if self.original[r][c] == 0:
                self.cells[r][c].set_cell_value(0)
                self.cells[r][c].set_sketched_value(0)

    def sketch(self, value):
        if self.selected:
            r, c = self.selected
            if self.original[r][c] == 0:
                self.cells[r][c].set_sketched_value(value)

    def place_number(self, value):
        if self.selected:
            r, c = self.selected
            if self.original[r][c] == 0:
                self.cells[r][c].set_cell_value(value)
                self.cells[r][c].set_sketched_value(0)
                self.update_board()

    def update_board(self):
        for r in range(9):
            for c in range(9):
                self.board[r][c] = self.cells[r][c].value

    def is_full(self):
        for r in range(9):
            for c in range(9):
                if self.cells[r][c].value == 0:
                    return False
        return True

    def reset_to_original(self):
        for r in range(9):
            for c in range(9):
                self.cells[r][c].set_cell_value(self.original[r][c])
                self.cells[r][c].set_sketched_value(0)
        self.update_board()

    def check_board(self):
        for r in range(9):
            for c in range(9):
                if self.cells[r][c].value != self.solution_array[r][c]:
                    return False
        return True

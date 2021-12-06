import re

class Grid:

    def __init__(self):
        self.values_to_position = {}
        self.values_picked = {}
        self.rows = [0, 0, 0, 0, 0]
        self.cols = [0, 0, 0, 0, 0]

    def set_position(self, r, c, val):
        self.values_to_position[val] = (r, c)
        self.values_picked[val] = False

    def picked_value(self, val):
        if val in self.values_to_position:
            r,c = self.values_to_position[val]
            self.values_picked[val] = True
            self.rows[r] += 1
            self.cols[c] += 1

    def check_bingo(self):
        return 5 in self.rows or 5 in self.cols
    
    def sum_unmarked(self):
        total = 0
        for val, picked in self.values_picked.items():
            if not picked:
                total += val
        return total

def problem_one():

    grids = []

    def get_grid(lines):
        for g in range(1, len(lines), 5):
            yield lines[g:g+5]

    def create_grid(all_rows):
        new_grid = Grid()

        for i in range(0, 5):
            for j in range(0, 5):
                new_grid.set_position(i, j, int(all_rows[i][j]))

        grids.append(new_grid)

  
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [l.strip('\n').split(' ') for l in lines if l != '\n']

        for i in range(len(lines)):
            while('' in lines[i]):
                lines[i].remove('')

        numbers_to_call = lines[0][0]
        numbers_to_call = numbers_to_call.split(',')

        for rows in get_grid(lines):
            create_grid(rows)

        winner = None
        final_called = None
        for called in numbers_to_call:
            for grid in grids:
                grid.picked_value(int(called))
            
            for grid in grids:
                if grid.check_bingo():
                    winner = grid
                    final_called = called
                    break

            if winner:
                break

        if winner:
            print("winner")
            total = winner.sum_unmarked()
            multiplied = total * int(final_called)
            print(multiplied)
        else:
            print("no winner")

def problem_two():

    grids = []

    def get_grid(lines):
        for g in range(1, len(lines), 5):
            yield lines[g:g+5]

    def create_grid(all_rows):
        new_grid = Grid()

        for i in range(0, 5):
            for j in range(0, 5):
                new_grid.set_position(i, j, int(all_rows[i][j]))

        grids.append(new_grid)

  
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [l.strip('\n').split(' ') for l in lines if l != '\n']

        for i in range(len(lines)):
            while('' in lines[i]):
                lines[i].remove('')

        numbers_to_call = lines[0][0]
        numbers_to_call = numbers_to_call.split(',')

        for rows in get_grid(lines):
            create_grid(rows)

        winner = None
        final_called = None
        for called in numbers_to_call:
            for grid in grids:
                grid.picked_value(int(called))
            
            for grid in grids:
                if grid.check_bingo():
                    winner = grid
                    final_called = called
                    grids.remove(grid)

        if winner:
            print("winner")
            total = winner.sum_unmarked()
            multiplied = total * int(final_called)
            print(multiplied)
        else:
            print("no winner")

problem_one()
problem_two()
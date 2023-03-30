import logging
import sys
from typing import List

from flask import Flask
import soduku

app = Flask(__name__)


@app.route('/')
def index():
    print("Input a file")
    file = 'test.txt'
    read_file: List[str] = soduku.read_file(file_to_open=file)
    if not read_file:
        logging.error(f"No sudoku found")
        sys.exit(1)
    initial_grid: List[List[int]] = soduku.create_sudoku(read_file)
    initial_grid_string = soduku.print_grid(description="Initial grid", grid=initial_grid)
    solutions, have_solution, information = soduku.solve_sudoku(grid=initial_grid)
    solved_grid_string: str = ''
    for i, solution in enumerate(solutions):
       solved_grid_string += soduku.print_grid(description=f"solution {i + 1}", grid=solution)

    return "The initial grid: <br>" + initial_grid_string + "<br>The solved grid: <br>" + solved_grid_string


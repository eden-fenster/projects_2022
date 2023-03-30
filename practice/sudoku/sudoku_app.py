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
    soduku.dump_grid(description="Initial grid", grid=initial_grid)
    solutions, have_solution, information = soduku.solve_sudoku(grid=initial_grid)
    return_sudoku = ''
    for i, solution in enumerate(solutions):
        return_sudoku += soduku.dump_grid(description=f"solution {i + 1}", grid=solution)
    return return_sudoku
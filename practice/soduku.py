#!/usr/bin/env python3
# Gets from user a 9 x 9 board.

from typing import List
import argparse


# Check if all numbers are between 1 - n.
# If no, fail.
# If yes, check for each row, col and k * l sub-table.
# Check that each number doesn't appear more than once at the 3 things above.
def get_args():
    # Getting a file that contains a partially filled sudoku from the command line.
    parser = argparse.ArgumentParser\
        (description='Sudoku', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('file', metavar='file', help='Input file')
    args = parser.parse_args()

    return args


def main():
    args = get_args()
    file_to_open = args.file
    print(create_sudoku(read_file(file_to_open=file_to_open)))


if __name__ == "__main__":
    main()


# Reads in a file
def read_file(file_to_open) -> List[str]:
    list_of_lines: List[str] = []
    # Reading the file by line.
    with open(file_to_open, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            list_of_lines.append(line.rstrip())
    return list_of_lines


# Converts a file into a two-dimensional list.
def create_sudoku(list_of_lines: List[str]) -> List[List[int]]:
    # Converting the lines into numbers, creating a two-dimensional list of ints.
    sudoku: List[List[int]] = []
    sudoku_line: List[int] = []
    for line in list_of_lines:
        for number in line:
            if number == " ":
                continue
            if not number.isdigit():
                print(f"TODO: Logging, this is not a number {number}")
            sudoku_line.append(int(number))
        sudoku.append(sudoku_line)
        sudoku_line = []
    return sudoku


# Fills the sudoku.
def fill_sudoku(sudoku: List[List[int]], current_row: int, current_column: int,
                smallest_number: int, largest_number: int) -> List[List[int]]:
    # If we went over all the rows, return filled sudoku table.
    if current_row >= len(sudoku):
        return sudoku

    # If we finished a row, go to the next row.
    if current_column >= len(sudoku[current_row]):
        return fill_sudoku(sudoku=sudoku, current_row=current_row + 1, current_column=0,
                           smallest_number=smallest_number, largest_number=largest_number)

    # Adding in numbers to row.
    for number in range(smallest_number, largest_number + 1):
        can_i_put_num: bool = True
        # Is # already in row ?
        if number in sudoku[current_row]:
            can_i_put_num = False
            continue
        # Is # already in column ?
        for actual_row in sudoku:
            # If # not in col, continue, else, break.
            if actual_row[current_column] != number:
                continue
            can_i_put_num = False
            break
        # Is # inside sub - table ?
        start_row: int = current_row - current_row % 2
        start_col: int = current_column - current_column % 2
        for row in range(2):
            for column in range(2):
                if sudoku[row + start_row][column + start_col] != number:
                    continue
                can_i_put_num = False
                break
        # Is it already in square ?
        # Putting it in.
        if can_i_put_num and sudoku[current_row][current_column] == 0:
            sudoku[current_row][current_column] = number
    print(f'Number -> {sudoku[current_row][current_column]}')
    # Moving down the search path to the next col in the row.
    return fill_sudoku(sudoku=sudoku, current_row=current_row, current_column=current_column + 1,
                       smallest_number=smallest_number, largest_number=largest_number)


def test_fill_sudoku():
    sudoku: List[List[int]] = \
        create_sudoku(read_file(file_to_open="test.txt"))
    assert fill_sudoku(sudoku=sudoku, current_row=0, current_column=0, smallest_number=1, largest_number=4) \
           == [[3, 1, 2, 4], [2, 4, 1, 3], [1, 3, 4, 2], [4, 2, 3, 1]]
    second_sudoku: List[List[int]] = \
        create_sudoku(read_file(file_to_open="test3.txt"))
    assert fill_sudoku(sudoku=second_sudoku, current_row=0, current_column=0, smallest_number=1, largest_number=4) \
           == [[2, 4, 3, 1], [3, 1, 2, 4], [1, 3, 4, 2], [4, 2, 1, 3]]
    # second_sudoku: List[List[int]] = \
    #     create_sudoku(read_file(file_to_open="test2.txt"))
    # assert fill_sudoku(sudoku=second_sudoku,
    #                    row=0, col=0, smallest_number=1, largest_number=9) \
    #        == [[8, 1, 2, 3, 6, 5, 7, 4, 9],
    #            [5, 7, 3, 2, 9, 4, 6, 1, 8],
    #            [6, 4, 9, 7, 1, 8, 5, 2, 3],
    #            [7, 8, 6, 4, 3, 2, 9, 5, 1],
    #            [9, 5, 1, 6, 8, 7, 2, 3, 4],
    #            [2, 3, 4, 9, 5, 1, 8, 6, 7],
    #            [1, 6, 8, 5, 7, 3, 4, 9, 2],
    #            [4, 9, 7, 1, 2, 6, 3, 8, 5],
    #            [3, 2, 5, 8, 4, 9, 1, 7, 6]]

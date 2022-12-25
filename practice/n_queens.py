#!/usr/bin/env python3
from typing import List


# Python3 program to solve N Queen
# Problem using backtracking
def solve_problem(number_of_queens: int) -> bool:
    if number_of_queens >= 3:
        print("Number is too small")
        return False
    return solve_nq(number_of_queens)


def print_solution(board, number_of_queens: int) -> None:
    for i in range(number_of_queens):
        for j in range(number_of_queens):
            print(board[i][j], end=" ")
        print()


# A utility function to check if a queen can
# be placed on board[row][col]. Note that this
# function is called when "col" queens are
# already placed in columns from 0 to col -1.
# So we need to check only left side for
# attacking queens
def is_safe(board, row, col, number_of_queens) -> bool:
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, number_of_queens, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nq_util(board, col, number_of_queens) -> bool:
    # base case: If all queens are placed
    # then return true
    if col >= number_of_queens:
        return True

    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(number_of_queens):

        if is_safe(board, i, col, number_of_queens):

            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            if solve_nq_util(board, col + 1, number_of_queens):
                return True

            # If placing queen in board[i][col
            # doesn't lead to a solution, then
            # queen from board[i][col]
            board[i][col] = 0

    # if the queen can not be placed in any row in
    # this column col then return false
    return False


# This function solves the N Queen problem using
# Backtracking. It mainly uses solveNQUtil() to
# solve the problem. It returns false if queens
# cannot be placed, otherwise return true and
# placement of queens in the form of 1s.
# note that there may be more than one
# solution, this function prints one of the
# feasible solutions.
def solve_nq(number_of_queens: int):
    board: List[List[int]] = []
    inside_board: List[int] = []
    for i in range(number_of_queens):
        for j in range(number_of_queens):
            inside_board.append(0)
        board.append(inside_board)
        inside_board = []

    if not solve_nq_util(board, 0, number_of_queens):
        print("Solution does not exist")
        return False

    print_solution(board, number_of_queens)
    return True


# Driver Code
n: int = int(input("How many queens ?"))
solve_nq(n)

# This code is contributed by Divyanshu Mehta

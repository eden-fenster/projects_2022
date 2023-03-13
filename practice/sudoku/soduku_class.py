#!/usr/bin/env python3
from copy import deepcopy
from typing import List, Tuple, Set

SIZE = 4
BOX_SIZE = 2


class Sudoku:
    def __init__(self, grid: List[List[int]]):
        n = len(grid)
        self.grid = grid
        self.n = n
        # create a grid of viable candidates for each position
        candidates = []
        for i in range(n):
            row = []
            for j in range(n):
                if grid[i][j] == 0:
                    row.append(self.find_options(i, j))
                else:
                    row.append(set())
            candidates.append(row)
        self.candidates = candidates

    def __repr__(self) -> str:
        repr = ''
        for row in self.grid:
            repr += str(row) + '\n'
        return repr

    def get_row(self, r: int) -> List[int]:
        return self.grid[r]

    def get_col(self, c: int) -> List[int]:
        return [row[c] for row in self.grid]

    def get_box_inds(self, r: int, c: int) -> List[Tuple[int, int]]:
        inds_box = []
        i0 = (r // BOX_SIZE) * BOX_SIZE  # get first row index
        j0 = (c // BOX_SIZE) * BOX_SIZE  # get first column index
        for i in range(i0, i0 + BOX_SIZE):
            for j in range(j0, j0 + BOX_SIZE):
                inds_box.append((i, j))
        return inds_box

    def get_box(self, r: int, c: int) -> List[int]:
        box = []
        for i, j in self.get_box_inds(r, c):
            box.append(self.grid[i][j])
        return box

    def find_options(self, r: int, c: int) -> Set:
        nums = set(range(1, SIZE + 1))
        set_row = set(self.get_row(r))
        set_col = set(self.get_col(c))
        set_box = set(self.get_box(r, c))
        used = set_row | set_col | set_box
        valid = nums.difference(used)
        return valid

    def place_and_erase(self, r: int, c: int, x: int, constraint_prop=True):
        """ remove x as a candidate in the grid in this row, column and box"""
        # place candidate x
        self.grid[r][c] = x
        self.candidates[r][c] = set()
        # remove candidate x in neighbours
        inds_row = [(r, j) for j in range(self.n)]
        inds_col = [(i, c) for i in range(self.n)]
        inds_box = self.get_box_inds(r, c)
        erased = [(r, c)]  # set of indices for constraint propagation
        erased += self.erase([x], inds_row + inds_col + inds_box, [])
        # constraint propagation, through every index that was changed
        while erased and constraint_prop:
            i, j = erased.pop()
            inds_row = [(i, j) for j in range(self.n)]
            inds_col = [(i, j) for i in range(self.n)]
            inds_box = self.get_box_inds(i, j)
            for inds in [inds_row, inds_col, inds_box]:
                # apply strategies
                # 1. hidden singles
                uniques = self.get_unique(inds)
                for inds_unique, num in uniques:
                    i_u, j_u = inds_unique[0]
                    self.candidates[i_u][j_u] = set(num)
                    erased += self.erase(num, inds, inds_unique)

    def erase(self, nums, indices, keep):
        """ erase nums as candidates in indices, but not in keep"""
        erased = []
        for i, j in indices:
            edited = False
            if (i, j) in keep:
                continue
            for x in nums:
                if x in self.candidates[i][j]:
                    self.candidates[i][j].remove(x)
                    edited = True
            if edited:
                erased.append((i, j))
        return erased

    def count_candidates(self, indices):
        count = [[] for _ in range(self.n + 1)]
        for i, j in indices:
            for num in self.candidates[i][j]:
                count[num].append((i, j))
        return count

    def get_unique(self, indices):
        groups = self.count_candidates(indices)
        uniques = []  # final set of unique candidates to return
        for num, group_inds in enumerate(groups):
            if len(group_inds) == 1:
                uniques.append((group_inds, [num]))
        return uniques


def solve_sudoku(grid, num_boxes=SIZE, all_solutions=False):
    def solve(puzzle, depth=0):
        nonlocal calls, depth_max
        calls += 1
        depth_max = max(depth, depth_max)
        solved = False
        while not solved:
            solved = True
            edited = False  # if no edits, either done or stuck
            for i in range(n):
                for j in range(n):
                    if puzzle.grid[i][j] == 0:
                        solved = False
                        options = puzzle.candidates[i][j]
                        if len(options) == 0:
                            return False  # this call is going nowhere
                        elif len(options) == 1:  # Step 1
                            puzzle.place_and_erase(i, j, list(options)[0])  # Step 2
                            edited = True
            if not edited:  # changed nothing in this round -> either done or stuck
                if solved:
                    solution_set.append(grid2str(puzzle.grid))
                    return True
                else:  # Find the square with the least number of options
                    min_guesses = (n + 1, -1)
                    for i in range(n):
                        for j in range(n):
                            options = puzzle.candidates[i][j]
                            if len(options) > 1:
                                min_guesses = min((len(options), (i, j)), min_guesses)
                    i, j = min_guesses[1]
                    options = puzzle.candidates[i][j]
                    for y in options:  # step 3. backtracking check point:
                        puzzle_next = deepcopy(puzzle)
                        puzzle_next.place_and_erase(i, j, y)
                        solved = solve(puzzle_next, depth=depth + 1)
                        if solved and not all_solutions:
                            break  # return 1 solution
                    return solved
        return solved

    calls, depth_max = 0, 0
    solution_set = []
    puzzle = Sudoku(grid)
    n = puzzle.n

    solved = solve(puzzle, depth=0)
    info = {'calls': calls,
            'max depth': depth_max,
            'nsolutions': len(solution_set),
            }
    unflatten(solved)
    return solution_set, solved, info


def flatten(grid) -> List[int]:
    arr = []
    for row in grid:
        arr.extend(row)
    return arr


def unflatten(arr: List[int], n=4) -> List[List[int]]:
    grid = []
    for i in range(0, len(arr), n):
        grid.append(arr[i:i + n])
    return grid


def arr2str(arr: List[int]) -> str:
    string = ''
    for digit in arr:
        string += str(digit)
    return string


def str2arr(string: str) -> List[int]:
    arr = []
    end = string.find('-')
    end = len(string) if end == -1 else end
    for c in string[0:end]:
        if c == '0':
            arr.append(0)
        else:
            arr.append(int(c))
    return arr


def grid2str(grid: List[List[int]]) -> str:
    return arr2str(flatten(grid))


def str2grid(string: str) -> List[List[int]]:
    return unflatten(str2arr(string))

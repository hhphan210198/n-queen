import random
import copy
import sys


# Generate a n by n board with random queen assignments to each row
def generate_board(n):
    board = []
    for i in range(n):
        row = ['X'] * n
        r = int(random.random() * n)
        row[r] = 'Q'
        board.append(row)
    return board


# Given a queen's position, return how many conflicts it has
def conflict_count(board, r, c):
    count = 0
    n = len(board)
    for i in range(n):
        if board[r][i] == 'Q' and i != c:
            count += 1
        if board[i][c] == 'Q' and i != r:
            count += 1
    temp_r = r + 1
    temp_c = c + 1
    while temp_r < n and temp_c < n:
        if board[temp_r][temp_c] == 'Q':
            count += 1
        temp_r += 1
        temp_c += 1

    temp_r = r - 1
    temp_c = c + 1
    while temp_r >= 0 and temp_c < n:
        if board[temp_r][temp_c] == 'Q':
            count += 1
        temp_r -= 1
        temp_c += 1

    temp_r = r + 1
    temp_c = c - 1
    while temp_r < n and temp_c >= 0:
        if board[temp_r][temp_c] == 'Q':
            count += 1
        temp_r += 1
        temp_c -= 1

    temp_r = r - 1
    temp_c = c - 1
    while temp_r >= 0 and temp_c >= 0:
        if board[temp_r][temp_c] == 'Q':
            count += 1
        temp_r -= 1
        temp_c -= 1

    return count


def check_solution(board):
    n = len(board)
    for row_index in range(n):
        for sq_index in range(n):
            if board[row_index][sq_index] == 'Q' and conflict_count(board, row_index, sq_index) != 0:
                return False
    return True


def min_conflict_solver(board):
    n = len(board)
    current = copy.deepcopy(board)
    iter = 0
    while True:
        # list_to_board(current)
        conflict_var = []
        if check_solution(current):
            return current, iter
        # Find conflicted queens
        for row_index in range(n):
            for col_index in range(n):
                if current[row_index][col_index] == 'Q' and conflict_count(current, row_index, col_index) != 0:
                    conflict_var.append((row_index, col_index))
        # Randomly select a conflicted queen
        r1 = int(random.random() * len(conflict_var))
        var_row = conflict_var[r1][0]
        var_col = conflict_var[r1][1]
        current[var_row][var_col] = 'X'
        min_conflict = n - 1
        min_conflict_var = []
        # Find queens that produce the minimum number of conflicts
        for j in range(n):
            temp_conflict = conflict_count(current, var_row, j)
            if temp_conflict < min_conflict:
                min_conflict_var.clear()
                min_conflict = temp_conflict
                min_conflict_var.append(j)
            elif temp_conflict == min_conflict:
                min_conflict_var.append(j)
        # Randomly select a min-conflict queen to prevent loop
        r2 = int(random.random() * len(min_conflict_var))
        var_col = min_conflict_var[r2]
        current[var_row][var_col] = 'Q'
        iter += 1


def list_to_board(b):
    for row in b:
        s = ""
        for square in row:
            s = s + square + " "
        print(s)


def solver():
    number_of_trials = int(sys.argv[1])
    size_input = int(sys.argv[2])
    if size_input < 4:
        print("No solution. Enter a size of at least 4.")
        return
    total = 0
    for trial in range(number_of_trials):
        initial = generate_board(size_input)
        output1, output2 = min_conflict_solver(initial)
        print("Initial Board:")
        list_to_board(initial)
        print("Solution Board:")
        list_to_board(output1)
        print("Number of iterations: ", output2)
        total += output2
    average_iteration = total / number_of_trials
    print("Average number of iterations for %d trials with boards of size %d is: %d" % (number_of_trials, size_input, average_iteration))


solver()

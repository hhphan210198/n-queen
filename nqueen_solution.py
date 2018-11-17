import copy


class Board:
    def __init__(self, board):
        self.board = board
        self.row = {}
        self.col = {}
        self.diagonal = []
        self.reverse_diagonal = []


def generate(n):
    board = []
    for i in range(n):
        row = ['X'] * n
        board.append(row)
    return board


def conflict(b, row, col):
    if (row in b.row) or (col in b.col) or ((row - col) in b.diagonal) or ((row + col) in b.reverse_diagonal):
        return True
    return False


def count_solution(b, current_row, current_col):
    size = len(b.board)
    count = 0
    if current_row == size - 1:
        return 1
    next_row = current_row + 1
    for col in range(size):
        current = copy.deepcopy(b)
        if conflict(current, next_row, col):
            continue
        else:
            current.board[next_row][col] = 'Q'
            current.row[next_row] = col
            current.col[col] = next_row
            current.diagonal.append(next_row - col)
            current.reverse_diagonal.append(next_row + col)
            count = count + count_solution(current, next_row, col)
    return count


def number_of_solution():
    for sz in range(1, 11):
        board = generate(sz)
        b = Board(board)
        count_sol = count_solution(b, -1, 0)
        print("Number of solutions in total for %d x %d boards: %d." % (sz, sz, count_sol))


number_of_solution()


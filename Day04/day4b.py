import numpy as np

def parseFile(inp):
    """Reads in file, returns numbers and boards
    as numpy arrays"""
    with open(inp) as f:
        n_list = [int(i) for i in f.readline().strip().split(',')]
        f.readline()
        board_string = f.readlines()
        board_string.append('')
    
    # convert boards
    boards, current_board = [], []
    while board_string:
        row = board_string.pop(0).strip()
        if row:
            row = row.split(' ')
            current_board.append([int(i) for i in row if i != ''])
        else:
            boards.append(current_board)
            current_board = []

    return n_list, boards


def bingoCheck(number, board):
    """Takes a number and a board, returns True
    if number makes row or column complete"""
    for row in board:
        for i, num in enumerate(row):
            if num == number:
                row[i] = -1
                if sum(row) == -5:
                    return True
                if sum([r[i] for r in board]) == -5:
                    return True


def findWinner(numbers, boards):
    """Cycles through each number and checks if board is winner"""
    while numbers:
        current_number = numbers.pop(0)
        for board in boards:
            if bingoCheck(current_number, board):
                return current_number, board

def score(num, board):
    """Calculates winning score"""
    unmarked = 0
    for row in board:
        for n in row:
            if n != -1:
                unmarked += n
    return unmarked * num

def findLoser(numbers, boards):
    """Cycle through numbers, discarding boards as they win
    Return number called and final board"""
    called = []
    while len(boards) > 0:
        current_number = numbers.pop(0)
        called.append(current_number)
        boards_to_remove = []
        for _, board in enumerate(boards):
            if bingoCheck(current_number, board):
                boards_to_remove.append(board)
        for board in boards_to_remove:
            boards.remove(board)
            last_board = board

    if len(board) == 1:
        last_board = boards[0]

    for number in called:
        bingoCheck(number, last_board)

    return current_number, last_board


if __name__ == "__main__":

    INPUT = "Day04/input4.txt"

    # Part 1
    bingo_numbers, bingo_boards = parseFile(INPUT)
    last_called, winning_board = findWinner(bingo_numbers, bingo_boards)
    winning_score = score(last_called, winning_board)
    print(f'Answer part 1: {winning_score}')

    # Part 2
    last_called, losing_board = findLoser(bingo_numbers, bingo_boards)
    losing_score = score(last_called, losing_board)
    print(f'Answer part 2: {losing_score}')

    
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
                elif sum([r[i] for r in board]) == -5:
                    return True
    return False
            

def findWinner(numbers, boards):
    """Cycles through each number and checks if board is winner"""
    while True:
        current_number = numbers.pop(0)
        for board in boards:
            if bingoCheck(current_number, board):
                return current_number, board

def winningScore(num, board):
    """Calculates winning score"""
    unmarked = 0
    for row in board:
        for n in row:
            if n != -1:
                unmarked += n
    return unmarked * num




if __name__ == "__main__":

    INPUT = "input4.txt"

    # Part 1
    bingo_numbers, bingo_boards = parseFile(INPUT)
    last_called, winning_board = findWinner(bingo_numbers, bingo_boards)
    winning_score = winningScore(last_called, winning_board)
    print(f'Answer part 1: {winning_score}')

    
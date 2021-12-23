import numpy as np
import re

def parse_input(inp):
    
    with open(inp) as f:
        dot_positions, instructions = f.read().split('\n\n')

    # TODO - PARSE MORE EFFICIENTLY

    dot_positions = dot_positions.split('\n')
    max_width, max_height = 0, 0
    dot_coordinates = []
    for dot in dot_positions:
        dot = dot.split(',')
        y, x = int(dot[0]), int(dot[1])
        if x > max_width:
            max_width = x
        if y > max_height:
            max_height = y
        dot_coordinates.append((x,y))
    
    initial_dots = np.zeros((max_width + 1, max_height + 1), dtype = int)

    for dot in dot_coordinates:
        y, x = dot[0], dot[1]
        initial_dots[y][x] = 1

    instructions = re.findall(r'fold along (.*)', instructions)
    clean_instructions = []
    for i in instructions:
        i = i.split('=')
        clean_instructions.append((i[0],int(i[1])))

    return initial_dots, clean_instructions


def fold_paper(arr, instruction):
    """Returns array once instruction has been applied"""
    axis = 0 if instruction[0] == 'x' else 1
    fold = int(instruction[1])

    if axis == 1:
        top = arr[:fold,:]
        bottom = arr[fold + 1:,:]
        flipped = np.flip(bottom, 0)
        top_height, flipped_height = top.shape[0], flipped.shape[0]
        if top_height < flipped_height:
            row = np.zeros(((flipped_height - top_height),top.shape[1]), dtype = int)
            top = np.append(row, top, axis = 0)
        if top_height > flipped_height:
            row = np.zeros(((top_height - flipped_height),top.shape[1]), dtype = int)
            flipped = np.append(flipped, row, axis = 0)
        folded = top + flipped

    if axis == 0:
        left = arr[:,:fold]
        right = arr[:,fold+1:]
        flipped = np.flip(right, 1)
        left_width, flipped_width = left.shape[1], flipped.shape[1]
        if left_width < flipped_width:
            col = np.zeros((left.shape[0],(flipped_width - left_width)), dtype = int)
            left = np.append(col, left, axis = 1)
        if left_width > flipped_width:
            col = np.zeros((left.shape[0],(left_width - flipped_width)), dtype = int)
            f = np.append(flipped, col, axis = 1)
        folded = left + flipped

    return folded


def mask(arr):
    """Takes array and returns hash/dots"""
    str_array = arr.astype(str)
    masked = []
    for item in str_array:
        row = []
        for i in item:
            i = '#' if int(i) > 0 else '.'
            row.append(i)
        row.append('\n')
        masked.append(''.join(row))
    return ''.join(masked)


def complete_folding(paper, instructions):
    current_fold = paper.copy()
    for i in instructions:
        current_fold = fold_paper(current_fold, i)
    return current_fold
        


if __name__ == "__main__":

    INPUT = 'input13.txt'

    paper, instructions = parse_input(INPUT)
    first_instruction = instructions[0]
    after_turn1 = fold_paper(paper, first_instruction)
    visible_dots = (after_turn1 > 0).sum()
    print(f'Ans1: {visible_dots}')

    end = complete_folding(paper, instructions)
    print(f'Ans 2 :\n{mask(end)}')
    
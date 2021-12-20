import numpy as np


def parse_file(inp):
    """Read in file and split into list of tuples
    Output list of tuples ((x1,y1),(x2,y2))
    """
    with open(inp) as f:
        vents_raw = map(str.strip,f.readlines())
    vents_raw = (vent.split(' -> ') for vent in vents_raw)
    vents = []
    for vent in vents_raw:
        x1, y1 = map(int,vent[0].split(','))
        x2, y2 = map(int,vent[1].split(','))
        vents.append(((x1,y1), (x2,y2)))
    return vents


def make_ocean_floor(list_of_vents):
    """Read in list and generate an array of zeros
    to the maximum x and y coordinates needed"""

    max_x = 0
    max_y = 0

    for vent in list_of_vents:
        if max(vent[0][0],vent[1][0]) > max_x:
            max_x = max(vent[0][0],vent[1][0])
        if max(vent[0][1],vent[1][1]) > max_y:
            max_y = max(vent[0][1],vent[1][1])

    ocean_floor = np.zeros((max_y + 1, max_x + 1))
    return ocean_floor


def mark_vent(coord, arr, part):
    """Takes a tuple of tuples of the vent start and end
    and updates the ocean floor array, for horizontal and vertical lines"""
    start, end = coord
    x1, y1 = start
    x2, y2 = end

    # Check if horizontal and update
    if x1 == x2:
        if y1 > y2:
            y2, y1 = y1, y2
        for y in range(y1, y2 + 1):
            arr[y][x1] += 1 # Reverse as np arrays are reversed

    # Check if vertical and update
    elif y1 == y2:
        if x1 > x2:
            x2, x1 = x1, x2
        for x in range (x1, x2 + 1):
            arr[y1][x] += 1 

    if part == 2:
    # Else, update diagonal
        diagonal_length = abs(x1 - x2)
        if x1 > x2:
            if y1 > y2:
                for l in range(diagonal_length + 1):
                    arr[y1 - l][x1 - l] += 1
            if y1 < y2:
                for l in range(diagonal_length + 1):
                    arr[y1 + l][x1 - l] += 1
        if x1 < x2:
            if y1 > y2:
                for l in range(diagonal_length + 1):
                    arr[y1 - l][x1 + l] += 1
            if y1 < y2:
                for l in range(diagonal_length + 1):
                    arr[y1 + l][x1 + l] += 1

    return arr


def find_overlaps(arr):
    """Count entries in array that are greater than 1"""
    occurences_more_than_1 = arr > 1
    return occurences_more_than_1.sum()


if __name__ == "__main__":

    # Read in data
    # Find min/max of x, y coordinates and set up np array of ocean floor
    # For each vent, check if horizontal/vertical
    # If horizontal/vertical, mark the vent
    # Cound how many points in ocean floor have a value > 1

    INPUT = "input05.txt"
    vents = parse_file(INPUT)
    
    ocean_part1 = make_ocean_floor(vents)
    for vent in vents:
        ocean = mark_vent(vent, ocean_part1, 1)
    overlaps = find_overlaps(ocean_part1)
    print(f'Ans 1: {overlaps}')

    ocean_part2 = make_ocean_floor(vents)
    for vent in vents:
        ocean = mark_vent(vent, ocean_part2, 2)
    overlaps = find_overlaps(ocean_part2)
    print(f'Ans 2: {overlaps}')


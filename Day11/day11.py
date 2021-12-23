import numpy as np


def parse_input(inp):
    with open(inp) as f:
        initial_state = f.read().split('\n')
    return np.array([[int(x) for x in line] for line in initial_state])


def is_valid_coordinate(coord):
    """Returns true if coordinate in grid"""
    if 0 <= coord[0] < 10 and 0 <= coord[1] < 10:
        return True


def step(initial_state):

    updated_octopi = initial_state + 1
    flashing_octopi = set()

    # If no octopus is flashing, return increased state
    while (updated_octopi > 9).sum() > 0:
        for coord, value in np.ndenumerate(updated_octopi):
            if value > 9:
                flashing_octopi.add(coord)
                updated_octopi[coord[0]][coord[1]] = 0
                adj_coords = [(coord[0] + d[0], coord[1] + d[1]) for d in ADJACENT]
                for ac in adj_coords:
                    if is_valid_coordinate(ac) and ac not in flashing_octopi:
                        updated_octopi[ac[0]][ac[1]] += 1 
    
    return updated_octopi, len(flashing_octopi)


def find_all_flashing(octopi):
    STEPS = 1000
    for i in range(STEPS):
        octopi, flashing = step(octopi)
        if flashing == 100:
            return i + 1
    return




if __name__ == "__main__":
    
    INPUT = "input11.txt"
    MAX_ROW, MAX_COL = 10, 10

    ADJACENT = []
    for x in range (-1, 2):
        for y in range(-1, 2):
            ADJACENT.append((x,y))
    ADJACENT.remove((0,0))

    octopi = parse_input(INPUT)
    clean_octopi = np.copy(octopi)
    count_flashing = 0
    STEPS = 100
    for i in range(STEPS):
        octopi, flashing = step(octopi)
        count_flashing += flashing
        
    print(f'Ans 1: {count_flashing}')

    first_sync = find_all_flashing(clean_octopi)
    print(f'Ans 2: {first_sync}')

# PARSE INPUT - Output: ((x1, x2),(y1, y2)) using regex
# MAKE STEP TO VELOCITY, CHECK IT HASN'T PASSED RANGE, RETURN HIGHEST POINT OF VELOCITY
    # take initial velocity and range
    # return False if after some number of steps, x,y are beyond range and never hits target
    # otherwise returns highest part
# TRY HORIZONTAL TRIANGLE NUMBERS, THEN DO DIFFERENT HEIGHTS


import re
from itertools import accumulate


def parse_input(inp):
    with open(inp) as f:
        parsed = f.read()
    coords = list(map(int,re.findall(r'\-*[0-9]+', parsed))) # extract all numbers including negative sign
    return coords


def reaches_target(initial_velocity, target_range):
    """Returns -1 if undershot, 0 if in target, 1 if overshot"""
    x1, x2, y1, y2 = target_range
    x, y = 0, 0
    x_velocity, y_velocity = initial_velocity

    while x <= x2:
        x, y = x + x_velocity, y + y_velocity
        x_velocity = x_velocity - 1 if x_velocity > 0 else x_velocity + 1 if x_velocity < 0 else 0
        y_velocity = y_velocity - 1
        if y in range(y1, y2 + 1) and x in range(x1, x2 + 1):
            return 0
        elif y < min(y1, y2):
            return 1
    
    return -1



if __name__ == "__main__":

    INPUT = "Day17/input17.txt"
    target = parse_input(INPUT)

    potential_x = list(accumulate(range(1,31)))
    assert potential_x[-1] > target[1]
    max_x_in_range = [idx + 1 for idx, val in enumerate(potential_x) if val in range(target[0], target[1] + 1)]    

    max_y = -1
    for x in range(1,target[0]):
        y = 0
        hit = reaches_target((x,y), target)
        while hit < 1:
            if hit == 0 and y > max_y:
                max_y = y
            y += 1
            hit = reaches_target((x,y), target)

    max_height = (max_y * (max_y + 1))/2
    print(max_height)

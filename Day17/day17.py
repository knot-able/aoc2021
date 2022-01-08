
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

    while x <= x2 and y >= min(y1, y2):
        x, y = x + x_velocity, y + y_velocity
        x_velocity = x_velocity - 1 if x_velocity > 0 else x_velocity + 1 if x_velocity < 0 else 0
        y_velocity = y_velocity - 1
        if y in range(y1, y2 + 1) and x in range(x1, x2 + 1):
            return True
    return False



if __name__ == "__main__":

    INPUT = "Day17/input17.txt"
    target = parse_input(INPUT)
    x1, x2, y1, y2 = target

    target_set = set()
    for x in range(0, max(x1,x2) + 1):
        for y in range(y1 - 1, -y1 + 1):
            if reaches_target((x,y), target):
                target_set.add((x,y))
    
    print(f'Ans 2 : {len(target_set)}')


    # with open("Day17/answer.txt") as f:
    #     ans_list = []
    #     ans_set = set()
    #     text = f.read().split()
    #     for c in text:
    #         ans_list.append(c.split(','))
    #     for c in ans_list:
    #         ans_set.add((int(c[0]), int(c[1])))
    #     print(ans_set)
    
    # print(reaches_target((7,-1), target))
    # print(reaches_target((6,0), target))

    
    # print(ans_set - target_set)
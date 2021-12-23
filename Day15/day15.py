from math import inf
from copy import deepcopy
from bisect import insort_left

def adjacent(coord, m):
    """Find adjacent coordinates (not diagonal)
    within a map, returns a list of valid coordinates.
    """
    R = len(m)
    C = len(m[0])
    DR = [0, 1]
    DC = [1, 0]
    adj_coords = []

    x, y = coord[0], coord[1]
    for i in range(2):
        dx = x + DR[i]
        dy = y + DC[i]
        if 0 <= dx < R and 0 <= dy < C:
            adj_coords.append((dx, dy))
    
    return adj_coords

def dijkstra():
    pass


if __name__ == "__main__":

    INPUT = 'Day15/input15.txt'

    with open(INPUT) as f:
        chiton_map = []
        for row in f.read().split('\n'):
            chiton_map.append([int(c) for c in row])

    # initialise values - dist, Q, S
    dist = deepcopy(chiton_map)
    Q = []
    S = set()

    for r in range(len(chiton_map)):
        for c in range(len(chiton_map[0])):
            dist[r][c] = inf
            Q.append((r,c))
    dist[0][0] = 0

# TODO - DON'T NEED TO RESORT THE WHOLE THING, JUST NEED TO REMOVE UPDATED ITEMS FROM LIST AND INSERT IN CORRECT PLACE
# Go through list (already sorted) until you find the first item bigger than your item, then insert
    update = False
    
    # start dijkstra's algorithm
    while Q:
        current_position = Q.pop(0)
        if current_position not in S:
            S.add(current_position)
            current_weight = dist[current_position[0]][current_position[1]]
            for a in adjacent(current_position, chiton_map):
                if current_weight + chiton_map[a[0]][a[1]] < dist[a[0]][a[1]]:
                    dist[a[0]][a[1]] = current_weight + chiton_map[a[0]][a[1]]
                    # insert a in correct place in list
                    if len(Q) > 1:
                        Q.remove(a)
                        ind = 0
                        while a:
                            c = Q[ind]
                            if dist[c[0]][c[1]] > dist[a[0]][a[1]]:
                                Q.insert(ind,a)
                                a = False
                            ind += 1
                            if ind == len(Q):
                                Q.append(a)
                                a = False


    lowest_risk = dist[-1][-1]
    print(f'Ans 1 : {lowest_risk}')
    


    






    # Want to use Dijkstra's algorithm





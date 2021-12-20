import numpy as np


def parse_file(inp):
    hm = []
    with open(inp) as f:
        for line in f.readlines():
            hm.append([int(i) for i in line.strip()])
    return np.asarray(hm)

DIRECTIONS = (
    (1, 0),
    (-1, 0),
    (0, -1),
    (0, 1)
)


def is_valid_coord(coord, mr, mc):
    """Returns true of coordinate in bounds of heightmap
    as defined by row and column numbers (default max)"""
    if 0 <= coord[0] < mr and 0 <= coord[1] < mc:
        return True
    else:
        return False


def find_low_points(hm, mr, mc):
    """Finds low points"""
    
    low_points = []
    
    for x in range(mr):
        for y in range(mc):
            adj_coords = [(x + d[0], y + d[1]) for d in DIRECTIONS]
            adj = [hm[coord[0]][coord[1]] for coord in adj_coords if is_valid_coord(coord, mr, mc)]
            if hm[x][y] < min(adj):
                low_points.append((x,y))
    
    return low_points


def size_of_basin(point, hm, mr, mc):
    """Finds the number of locations surroundling a low point that
    flow into that low point."""

    visited = set()
    in_basin = set()

    # add low point to 'to visit' and 'in basin'
    to_visit = [point]
    
    # while there are places to visit (ie. check if in basin)
    # pop off into currently visiting, and mark as visited
    # if not equal to 9, add to 'in_basin' and add all valid adjacent coordinates to to_visit, and repeat

    while to_visit:
        currently_visiting = to_visit.pop()
        visited.add(currently_visiting)
        x, y = currently_visiting
        if hm[x][y] != 9:
            in_basin.add(currently_visiting)
            adj_coords = [(x + d[0], y + d[1]) for d in DIRECTIONS]
            for coord in adj_coords:
                if is_valid_coord(coord, mr, mc) and coord not in visited:
                    to_visit.append(coord)
    
    return len(in_basin)


if __name__ == "__main__":

    INPUT = "input09.txt"


    heightmap = parse_file(INPUT)
    MAX_ROW, MAX_COL = np.shape(heightmap)

    low_points = find_low_points(heightmap, MAX_ROW, MAX_COL)
    risk_levels = [heightmap[low_point[0]][low_point[1]] + 1 for low_point in low_points]
    print(f'Ans 1: {sum(risk_levels)}')

    largest_basins = [-3, -2, -1]
    for point in low_points:
        size = size_of_basin(point, heightmap, MAX_ROW, MAX_COL)
        if size > min(largest_basins):
            largest_basins.append(size)
            largest_basins.remove(min(largest_basins))
    product_of_basins = np.prod(largest_basins)
    print(f'Ans 2: {product_of_basins}')

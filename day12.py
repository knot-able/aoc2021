
from collections import defaultdict, Counter


def parse_caves(inp):

    cave = defaultdict(list)

    with open(inp) as f:
        for line in f.read().split('\n'):
            s, e = line.split('-')
            
            if s == 'end' or e =='start':
                s, e = e, s
            
            cave[s].append(e)
            if s != 'start' and e != 'end':
                cave[e].append(s)
    
    return cave

                

def find_paths(graph, node, large_caves, path=[]):
    path.append(node)
    if node == 'end':
        pathways.append(path)
    else:
        for neighbour in graph[node]:
            if neighbour not in path or neighbour in large_caves:
                find_paths(graph, neighbour, large_caves, path.copy())


# TODO - SPEED UP (return count not list of paths)

def find_paths_small(graph, node, path=[]):
    path.append(node)
    if node == 'end':
        if path not in pathways_small:
            pathways_small.append(path)
    else:
        for neighbour in graph[node]:
            if neighbour not in path or neighbour.isupper(): 
                find_paths_small(graph, neighbour, path.copy())
            if neighbour in path:
                visited = Counter(path)
                small_visited = {small: visited[small] for small in visited if small.islower()}
                if max(small_visited.values()) == 1:
                    find_paths_small(graph, neighbour, path.copy())



if __name__ == "__main__":
    
    INPUT = "input12.txt"
    cave = parse_caves(INPUT)
    print(cave)
    terminating = ['start', 'end']
    large_caves = [c for c in cave if c.isupper()]
    small_caves = [c for c in cave if c.islower() and c not in terminating]
    pathways = []
    find_paths(cave, 'start', large_caves)
    print(f'Ans1: {len(pathways)}')

    pathways_small = []
    find_paths_small(cave, 'start', large_caves)
    print(f'Ans2: {len(pathways_small)}')





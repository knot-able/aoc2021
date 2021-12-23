
test_input = [16,1,2,0,4,2,7,1,2,14]

INPUT = "input07.txt"


def parse_input(inp):
    with open(inp) as f:
        crab_positions = f.readlines()
    return list(map(int,crab_positions[0].strip().split(',')))


def fuel_cost_part1(p, positions):
    """Takes list of initial positions and 
    position to determine fuel cost"""
    cost_to_move = map(lambda x: abs(x - p), positions)
    return sum(cost_to_move)


def fuel_cost_part2(p, positions):
    cost_to_move = map(lambda x: sum(range(abs(x - p) + 1)), positions)
    return sum(cost_to_move)


def find_cheapest_position(positions, fuel_cost_function):
    cheapest = 1000000000
    aligning_position = 0

    for p in range(max(positions)):
        cost = fuel_cost_function(p, positions)
        if cost < cheapest:
            cheapest = cost
            aligning_position = p
    
    return cheapest, aligning_position


if __name__ == "__main__":

    initial_crab_positions = parse_input(INPUT)
    print(f'Ans 1: {find_cheapest_position(initial_crab_positions, fuel_cost_part1)[0]}')
    print(f'Ans 2: {find_cheapest_position(initial_crab_positions, fuel_cost_part2)[0]}')

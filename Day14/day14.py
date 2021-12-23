import parse
import collections

def parse_input(inp):
    """Read in file.
    Output eg:
        polymer_template = ['N', 'N', 'C', 'B'] 
        pair_insertion_rules = {'CH': 'B',...}
    """
    with open(inp) as f:
        
        initial_polymer = [x for x in f.readline().strip()]
        
        f.readline()
        
        rules = f.read().split('\n')
        rules = map(lambda x: parse.parse('{} -> {}', x), rules)
    
    return initial_polymer, dict(rules)


def n_steps(initial_state, rules, n):
    """Takes n number of steps and returns dictionary 
    of count of pairs.
    Will not take order into account besides adjacent pairs"""

    start_pairs = collections.defaultdict(int)

    for pair in zip(initial_state[:-1],initial_state[1:]):
        start_pairs[pair[0] + pair[1]] += 1
    

    while n > 0:
        end_pairs = collections.defaultdict(int)
        for pair, value in start_pairs.items():
            end_pairs[pair[0] + rules[pair]] += value
            end_pairs[rules[pair] + pair[1]] += value
        start_pairs = {k : v for k, v in end_pairs.items()} # can't just shallow copy dictionary
        n -= 1
    
    return end_pairs
    

def get_score(d, template):
    """Takes pairs and converts to single element count
    Then returns score of most common - least common"""
    elements = collections.defaultdict(int)
    for pair, value in d.items():
        elements[pair[0]] += value
        elements[pair[1]] += value
    
    # Account for fact that pairs are doubled values except for first and last
    start = template[0]
    end = template[-1]
    elements = {k : int(v/2) if k != start and k != end else int((v + 1)/2) for k, v in elements.items()}

    most_common_element = max(elements, key = elements.get)
    least_common_element = min(elements, key = elements.get)

    return elements[most_common_element] - elements[least_common_element]

# Once steps are complete, take final dictionary, and convert into single element dictionary
# Get score by using counter


if __name__ == "__main__":

    INPUT = 'Day14/input14.txt'

    polymer_template, pair_insertion_rules = parse_input(INPUT)

    step10 = n_steps(polymer_template, pair_insertion_rules, 10)
    score10 = get_score(step10, polymer_template)
    print(f'Ans 1: {score10}')

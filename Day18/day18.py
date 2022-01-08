

# Read in input as a list of lists. PARSE FUNCTION. COMPLETE.
# Add the first two numbers - REDUCTION FUNCTION
# Continue to add numbers until all added together and reduced - ADDITION FUNCTION
# Calculate magnitude - MAGNITUDE FUNCTION

from ast import literal_eval


def parse_input(inp):
    with open(inp) as f:
        parsed = [literal_eval(n.strip()) for n in f.readlines()]
    return parsed


def reduce(num):
    """Reduce a snailfish number.
    To reduce a snailfish number, you must repeatedly do the first action in this list that applies to the snailfish number:
        If any pair is nested inside four pairs, the leftmost such pair explodes.
        If any regular number is 10 or greater, the leftmost such regular number splits.
        Once no action in the above list applies, the snailfish number is reduced.
    """
    pass


def list_depth(l):
    """Calculates max depth of list.
    Depth of list is one more than the maximum depth of its sublist.
    """
    if isinstance(l, list):
        return 1 + max(list_depth(item) for item in l)
    else:
        return 0


def explode(num):
    """Finds first pair nested inside four pairs, and EXPLODES it.
    Otherwise returns None.
    """
    for i in range(len(num)):
        if list_depth(num[i:]) == 4:
            left, right = num[i][0], num[i][1]
            first_left, first_right = i - 1, i + 1
            # add to first 'regular' number to right and first regular number to left
            if first_left >= 0:
                num[first_left][1] += left
            if first_right <= len(num):
                num[first_right][0] += right
            return num
            
    return








if __name__ == "__main__":

    pass
    # INPUT = "Day18/input18_test.txt"
    # parsed_input = parse_input(INPUT)
    # print(parsed_input[0])
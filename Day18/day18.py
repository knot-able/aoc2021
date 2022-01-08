

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


def explode(snail_num, depth):
    """Finds first pair nested inside four or more pairs, and EXPLODES it.
    Otherwise returns None.
    """

    # if list_depth(num) < 4:
    #     return None

    # # for i in range(len(num)):
    # #     if list_depth(num[i:]) >= 4:
    # #         left, right = num[i][0], num[i][1]
    # #         first_left, first_right = i - 1, i + 1
    # #         # add to first 'regular' number to right and first regular number to left
    # #         if first_left >= 0:
    # #             num[first_left][1] += left
    # #         if first_right <= len(num):
    # #             num[first_right][0] += right
    # #         return num

    # while True:

    if all(isinstance(l,int) for l in snail_num):
        if depth >= 4:
            print(f'EXPLODE {snail_num}')
            # TO DO, INSERT EXPLOSION
        else:
            return 0
    
    else:
        depth += 1
        left, right = snail_num[0], snail_num[1]
        if isinstance(left, list):
            return explode(left, depth)
        else:
            return explode(right, depth)    


            
    # return










if __name__ == "__main__":

    INPUT = "Day18/input18_test.txt"
    parsed_input = parse_input(INPUT)
    print(explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]],0))

    # how to test for list presence
    # print(all(isinstance(l,int) for l in [0,1,[0,1]]))
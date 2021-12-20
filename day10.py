from statistics import median

SYNTAX_ERROR_SCORE_PART1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

SYNTAX_ERROR_SCORE_PART2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


OPENERS = ('(', '[', '{', '<')
CLOSERS = (')', ']', '}', '>')


MATCHER = {
    '(': (0,1),
    '[': (1,1),
    '{': (2,1),
    '<': (3,1),
    ')': (0,-1),
    ']': (1,-1),
    '}': (2,-1),
    '>': (3,-1)
}

def parse_input(inp):
    with open(inp) as f:
        lines = f.read().split('\n')
    return lines


def is_incomplete(line):
    """Ensures there are the right number of opening and
    closing brackets - returns True if incomplete"""

    # currently, just checks if things match up properly - there is also something about order
    # when checking illegal, need to ensure that it is a valid closer

    tracker = [0,0,0,0]

    for bracket in line:
        index, val = MATCHER[bracket]
        tracker[index] += val

    return any(b != 0 for b in tracker)


def find_corrupt(line):
    """Returns first illegal bracket"""
    bracket_tracker = []

    for bracket in line:
        if bracket in OPENERS:
            bracket_tracker.insert(0,bracket)
            most_recent_opener = bracket
        else:
            i = CLOSERS.index(bracket)
            if most_recent_opener == OPENERS[i]:
                bracket_tracker.pop(0)
                if bracket_tracker:
                    most_recent_opener = bracket_tracker[0]
                else:
                    most_recent_opener = ''
            else:
                return bracket

    return
    

def corrupt_score(lines):
    score = 0
    for line in lines:
        corrupt = find_corrupt(line)
        if corrupt:
            score += SYNTAX_ERROR_SCORE_PART1[corrupt]
    return score


def incomplete_score(completer):
    score = 0
    for b in completer:
        score *= 5
        score += SYNTAX_ERROR_SCORE_PART2[b]
    return score




def complete_line(line):
    """Takes a line and then creates an appropriate closing
    sequence of brackets outputted as a list"""
    bracket_tracker = []

    for bracket in line:
        if bracket in OPENERS:
            bracket_tracker.insert(0,bracket)
            most_recent_opener = bracket
        else:
            i = CLOSERS.index(bracket)
            if most_recent_opener == OPENERS[i]:
                bracket_tracker.pop(0)
                if bracket_tracker:
                    most_recent_opener = bracket_tracker[0]
                else:
                    most_recent_opener = ''

    bracket_completer = [CLOSERS[OPENERS.index(b)] for b in bracket_tracker]
    return bracket_completer


if __name__ == "__main__":

    INPUT = "input10.txt"

    lines = parse_input(INPUT)
    print(f'Ans 1: {corrupt_score(lines)}')

    incomplete_scores = []
    for line in lines:
        if not find_corrupt(line) and is_incomplete(line):
            completing_string = complete_line(line)
            incomplete_scores.append(incomplete_score(completing_string))
    ans2 = median(incomplete_scores)
    print(f'Ans 2: {ans2}')

    

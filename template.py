

def parse_input(inp):

    with open(inp) as f:
        parsed = f.readlines()
    return parsed




if __name__ == "__main__":

    INPUT = "day18/example.txt"
    parsed_input = parse_input(INPUT)
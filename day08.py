
from collections import defaultdict


SEGMENT_MAP = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

SEGMENT_MAP_REVERSE = {v: k for k, v in SEGMENT_MAP.items()}


# how many times does each letter appear?
LETTER_COUNT = defaultdict(int)
for num in SEGMENT_MAP.values():
    for l in num:
        LETTER_COUNT[l] += 1


def parse_input(inp):
    """Reads in input
    Outputs a generator of lists of the part to the right of | """
    with open(inp) as f:
        read_in = f.readlines()
        inputs = map(lambda s: s.split(' | ')[0].strip(), read_in)
        outputs = map(lambda s: s.split(' | ')[1].strip(), read_in)
    
    inputs = [input.split(' ') for input in inputs]
    outputs = [output.split(' ') for output in outputs]

    return inputs, outputs


def count_easy_digits(outputs):
    """Goes through a list of outputs, and adds
    appropriately:
    2 segments: 1
    3 segments: 7
    4 segments: 4
    7 segments: 8"""
    unique_segment_lengths = [2, 3, 4, 7]
    unique_numbers = 0
    for output in outputs:
        for n in output:
            if len(n) in unique_segment_lengths:
                unique_numbers += 1
    return unique_numbers

def analyse_input(inp):
    """Intake an input, find the mappings"""
    remaining_letters = ['a', 'b','c', 'd', 'e', 'f', 'g']
    translator = {}

    letter_count = defaultdict(int)
    for num in inp:
        # find key numbers for analysis
        if len(num) == 2:
            one = set(num)
        if len(num) == 3:
            seven = set(num)
        if len(num) == 4:
            four = set(num)
        # create count of letters
        for l in num:
            letter_count[l] += 1

    # find a
    a = (seven - one).pop()
    translator[a] = 'a'
    remaining_letters.remove(a)
    
    # find e,b,f,c
    for k, v in letter_count.items():
        if v == 4:
            translator[k] = 'e'
            remaining_letters.remove(k)
        if v == 6:
            translator[k] = 'b'
            remaining_letters.remove(k)
        if v == 8 and k != a:
            translator[k] = 'c'
            remaining_letters.remove(k)
        if v == 9:
            translator[k] = 'f'
            remaining_letters.remove(k)

    # find d, g
    for remaining in remaining_letters:
        if remaining in four:
            translator[remaining] = 'd'
        else:
            translator[remaining] = 'g'

    return translator


def translate_output(output, translator):

    """Go through each of four strings in output
    Translate each letter back into correct string, then stick
    back together, sorted
    Return a list of correct strings -> numbers"""

    translated_output = []
    current_number = []

    for num in output:
        for l in num:
            current_number.append(translator[l])
        translated_number = ''.join(sorted(current_number))
        translated_output.append(SEGMENT_MAP_REVERSE[translated_number])
        current_number = []

    return int(''.join([str(i) for i in translated_output]))




if __name__ == "__main__":

    INPUT = "input08.txt"

    inputs_observed, outputs_observed = parse_input(INPUT)
    
    print(f'Ans1: {count_easy_digits(outputs_observed)}')
    
    sum_of_outputs = 0
    for i, input in enumerate(inputs_observed):
        translator = analyse_input(input)
        sum_of_outputs += translate_output(outputs_observed[i], translator)
    print(f'Ans2: {sum_of_outputs}')


# s = 0
# for x,y in [x.split('|') for x in open(0)]:  # split signal and output
#   l = {len(s): set(s) for s in x.split()}    # get number of segments

#   n = ''
#   for o in map(set, y.split()):              # loop over output digits
#     match len(o), len(o&l[4]), len(o&l[2]):  # mask with known digits
#       case 2,_,_: n += '1'
#       case 3,_,_: n += '7'
#       case 4,_,_: n += '4'
#       case 7,_,_: n += '8'
#       case 5,2,_: n += '2'
#       case 5,3,1: n += '5'
#       case 5,3,2: n += '3'
#       case 6,4,_: n += '9'
#       case 6,3,1: n += '6'
#       case 6,3,2: n += '0'
#   s += int(n)

# print(s)
    
   



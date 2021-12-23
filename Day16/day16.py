
HEX_TO_BITS = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'
}


def hex_to_binary(s):
    """Takes a hex string in and returns binary string out"""
    binary = ''
    for h in s:
        binary += HEX_TO_BITS[h]
    return binary


def literal_number(s, p):
    """Takes in string and pointer
    Returns integer and updated pointer"""
    while int(s[p]) == 0:
        p += 1
    
    bit_check = '1'
    literal = ''
    while bit_check == '1':
        bit_check, bit = s[p], s[p + 1:p + 5]
        p += 5
        literal += bit
    while p < len(s) and s[p] == '0':
        p += 1
    
    return int(literal,2), p


eg = '38006F45291200'
binary = hex_to_binary(eg)

packet_hierarchy = [] # [[parent, version, id, values],...]
version_numbers = 0
parent = -99 # -99 means parent is master
p = 0

while p < len(binary):
    version = int(binary[p:p+3],2)
    version_numbers += version
    p += 3
    id = int(binary[p:p+3],2)
    p += 3

    if id == 4:
        n, p = literal_number(binary, p)
        packet_hierarchy.append([parent, version, id, n])

    else:
        length_type_id = binary[p]
        p += 1
        if length_type_id == '0':
            length_of_subpackets = int(binary[p:p+15],2)
            p += 15
            # keep going from here



        if length_type_id == '1':
            number_of_subpackets = int(binary[p:p+11],2)
            p += 11



from numpy import prod

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
    """Takes a hex string in and returns binary list out"""
    binary = ''
    for h in s:
        binary += HEX_TO_BITS[h]
    return [b for b in binary]


def find_version(binary, v, sub_counter, sub=False):
    """Takes in string, position and values counter.
    Only uses sub_counter if sub = True.
    Returns sum of version values.
    """

    if (sub and sub_counter == 0) or (all([l == '0' for l in binary]) or not binary):
        return v
    
    else:
        # identify version and id (convert from binary)
        version, id, binary = ''.join(binary[0:3]), ''.join(binary[3:6]), binary[6:]
        version, id = int(version,2), int(id,2)
        v += version

        # perform literal operation
        if id == 4:
            literal = '' 
            # take off chunks of 5
            while binary[0] == '1':
                group, binary = binary[0:5], binary[5:]
                literal += ''.join(group[1:])

            group, binary = binary[0:5], binary[5:]
            literal += ''.join(group[1:])

            packet_value = int(literal, 2)
            # print(f'packet_value: {packet_value}')

            if sub:
                sub_counter -= 1
            return find_version(binary, v, sub_counter)
        
        else:
            length_id = binary.pop(0)
            if length_id == '0':
                # If the length type ID is 0, then the next 15 bits are a number 
                # that represents the total length in bits of the sub-packets contained by this packet.
                length_of_subpacket, binary = ''.join(binary[0:15]), binary[15:]
                length_of_subpacket = int(length_of_subpacket, 2)
                subpacket, rest_of_string = binary[0:length_of_subpacket], binary[length_of_subpacket:]
                sub_version_totals = find_version(subpacket, v, 0)
                return find_version(rest_of_string, sub_version_totals, 0)

            elif length_id == '1':
                number_of_subpackets, binary = ''.join(binary[0:11]), binary[11:]
                number_of_subpackets = int(number_of_subpackets, 2)
                return find_version(binary, v, number_of_subpackets, True)





def operation(id, values):

    assert id in range(8)

    if id == 0: return sum(values)

    if id == 1: return prod(values)

    if id == 2: return min(values)

    if id == 3: return max(values)
    
    if id == 4: return values[0]
    
    if id == 5: return 1 if values[0] > values[1] else 0

    if id == 6: return 1 if values[0] < values[1] else 0

    if id == 7: return 1 if values[0] == values[1] else 0



def find_values(binary, current_id, current_values, sub_counter, sub=False):
    """Takes in string, position and values counter.
    Only uses sub_counter if sub = True.
    Returns sum of version values.
    """

    if (sub and sub_counter == 0) or (all([l == '0' for l in binary]) or not binary):
        return operation(current_id, current_values)
    
    else:
        # identify version and id (convert from binary)
        current_id, binary = ''.join(binary[3:6]), binary[6:]
        current_id = int(current_id,2)

        if current_id != 4:
            current_values = []
            length_id = binary.pop(0)
            if length_id == '0':
                # If the length type ID is 0, then the next 15 bits are a number 
                # that represents the total length in bits of the sub-packets contained by this packet.
                length_of_subpacket, binary = ''.join(binary[0:15]), binary[15:]
                length_of_subpacket = int(length_of_subpacket, 2)
                subpacket, rest_of_string = binary[0:length_of_subpacket], binary[length_of_subpacket:]
                sub_version_values = find_values(subpacket, current_id, current_values, 0)
                return find_values(rest_of_string, current_id, sub_version_values, 0)

            elif length_id == '1':
                number_of_subpackets, binary = ''.join(binary[0:11]), binary[11:]
                number_of_subpackets = int(number_of_subpackets, 2)
                return find_values(binary, current_id, current_values, True)

        if id == 4:
            literal = '' 
            # take off chunks of 5
            while binary[0] == '1':
                group, binary = binary[0:5], binary[5:]
                literal += ''.join(group[1:])

            group, binary = binary[0:5], binary[5:]
            literal += ''.join(group[1:])

            packet_value = int(literal, 2)
            # print(f'packet_value: {packet_value}')

            if sub:
                sub_counter -= 1
            return find_values(binary, current_id, [packet_value], sub_counter)




        # else perform operators 
if __name__ == "__main__":

    INPUT = '38006F45291200'
    binary = hex_to_binary(INPUT)
    v = find_version(binary, 0, 99999)
    print(f'Answer 1: {v}')


    def find_id(b):
        """Takes current bitlist, pops off value and ID and length ID if value not equal
        to 4. 
        Returns id, length_id, remaining list."""
        id, remainder = int(''.join(b[3:6]),2), b[6:]
        length_id = remainder.pop(0) if id != 4 else -1
        return id, length_id, remainder


    def op_four(b):
        """Takes current bitlist, assuming id was 4.
        Determines the literal value, and the number of bits it took to get there.
        Returns literal value, bits, remaining list."""
        literal, bit_count = '', 0 
        # take off chunks of 5
        while b[0] == '1':
            group, b = b[0:5], b[5:]
            literal += ''.join(group[1:])
            bit_count += 5

        # last chunk
        group, b = b[0:5], b[5:]
        literal += ''.join(group[1:])
        bit_count += 5

        return int(literal, 2), bit_count, b

    
    def operation(id, values):
        """Perform operation of ID on values (which should be a list)."""

        assert id in range(8)
        assert type(values) == list

        if id == 0: return sum(values)

        if id == 1: return prod(values)

        if id == 2: return min(values)

        if id == 3: return max(values)
        
        if id == 4: return values[0]
        
        if id == 5: return 1 if values[0] > values[1] else 0

        if id == 6: return 1 if values[0] < values[1] else 0

        if id == 7: return 1 if values[0] == values[1] else 0


    def find_values(bits, current_packet):

    # [id, [v1, v2]]
    # [id1, [[id2, [v1, v2]], v3]]
    # perform operation

    # STRUCTURE:

    # if we have reached the end of a section or sub-section, perform the operation on the values
    # otherwise:
        # find ID and value of next section
        # perform literal operation if 4
    
    # end condition - only 0s or no list  
    if all([l == '0' for l in bits]) or not bits: 
        id, values = current_packet[0], current_packet[1]
        return operation(id, values)

    id, length_id, bits = find_id(bits)
    current_packet = [id]
    
    if id == 4:
        value, bit_count, bits = op_four(bits)
        current_packet.append([value])
        
    else:
        assert id in range(8) and id != 4
        if bit_count == '0':
            pass
        else:
            assert bit_count == '1'
            pass




    







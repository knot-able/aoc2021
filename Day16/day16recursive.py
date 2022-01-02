
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
    """
    # if the binary list is empty (ie. we are at end), return version total
    
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




        # else perform operators 


INPUT = 'A20D5080210CE4BB9BAFB001BD14A4574C014C004AE46A9B2E27297EECF0C013F00564776D7E3A825CAB8CD47B6C537DB99CD746674C1000D29BBC5AC80442966FB004C401F8771B61D8803D0B22E4682010EE7E59ACE5BC086003E3270AE4024E15C8010073B2FAD98E004333F9957BCB602E7024C01197AD452C01295CE2DC9934928B005DD258A6637F534CB3D89A944230043801A596B234B7E58509E88798029600BCF5B3BA114F5B3BA10C9E77BAF20FA4016FCDD13340118B929DD4FD54E60327C00BEB7002080AA850031400D002369400B10034400F30021400F20157D804AD400FE00034E000A6D001EB2004E5C00B9AE3AC3C300470029091ACADBFA048D656DFD126792187008635CD736B3231A51BA5EBDF42D4D299804F26B33C872E213C840022EC9C21FFB34EDE7C559C8964B43F8AD77570200FC66697AFEB6C757AC0179AB641E6AD9022006065CEA714A4D24C0179F8E795D3078026200FC118EB1B40010A8D11EA27100990200C45A83F12C401A8611D60A0803B1723542889537EFB24D6E0844004248B1980292D608D00423F49F9908049798B4452C0131006230C14868200FC668B50650043196A7F95569CF6B663341535DCFE919C464400A96DCE1C6B96D5EEFE60096006A400087C1E8610A4401887D1863AC99F9802DC00D34B5BCD72D6F36CB6E7D95EBC600013A88010A8271B6281803B12E124633006A2AC3A8AC600BCD07C9851008712DEAE83A802929DC51EE5EF5AE61BCD0648028596129C3B98129E5A9A329ADD62CCE0164DDF2F9343135CCE2137094A620E53FACF37299F0007392A0B2A7F0BA5F61B3349F3DFAEDE8C01797BD3F8BC48740140004322246A8A2200CC678651AA46F09AEB80191940029A9A9546E79764F7C9D608EA0174B63F815922999A84CE7F95C954D7FD9E0890047D2DC13B0042488259F4C0159922B0046565833828A00ACCD63D189D4983E800AFC955F211C700'
binary = hex_to_binary(INPUT)
v = find_version(binary, 0, 99999)
print(f'Answer 1: {v})



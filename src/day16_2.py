import math


operators = {0: sum,
             1: math.prod,
             2: min,
             3: max,
             5: lambda x: int(x[0] > x[1]),
             6: lambda x: int(x[0] < x[1]),
             7: lambda x: int(x[0] == x[1])}


def parse_literal_packet(bits):
    """Return literal value and the remaining bits."""
    bits = bits[6:]
    value = ''
    while True:
        value += bits[1:5]
        if bits[0] == '0':
            return int(value, 2), bits[5:]
        bits = bits[5:]


def parse_operator_packet(bits):
    """Return the value of the packet and the remaining bits."""
    type_id = int(bits[3:3+3], 2)
    values = []
    if bits[6] == '0':
        sub_packets_length = int(bits[7:22], 2)
        sub_packets = bits[22:22+sub_packets_length]
        bits = bits[22+sub_packets_length:]
        while sub_packets:
            value, sub_packets = parse_packet(sub_packets)
            values.append(value)
    else:
        sub_packet_count = int(bits[7:18], 2)
        bits = bits[18:]
        for _ in range(sub_packet_count):
            value, bits = parse_packet(bits)
            values.append(value)
    return operators[type_id](values), bits


def parse_packet(bits):
    """Parse a packet depending on its type. Return the remaining bits."""
    type_id = int(bits[3:3+3], 2)
    parser = parse_literal_packet if type_id == 4 else parse_operator_packet
    return parser(bits)


if __name__ == '__main__':
    with open('../data/day16.txt') as f:
        line = f.readline().strip()
    bits = bin(int(line, 16))[2:].zfill(4 * len(line))
    print(parse_packet(bits)[0])

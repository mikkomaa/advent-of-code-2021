def process_packet(start_index):
    """Decode transmission, and add up the version numbers."""
    global version_sum
    i = start_index
    version_sum += int(bits[i:i+3], 2)
    i += 3
    type_id = int(bits[i:i+3], 2)
    i += 3
    if type_id == 4:
        while bits[i] == '1':
            i += 5
        i += 5
    else:
        if bits[i] == '0':
            i += 1
            length = int(bits[i:i+15], 2)
            i += 15
            end = i + length
            while i < end:
                i += process_packet(i)
        else:
            i += 1
            packet_count = int(bits[i:i+11], 2)
            i += 11
            for _ in range(packet_count):
                i += process_packet(i)
    return i - start_index


if __name__ == '__main__':
    with open('../data/day16.txt') as f:
        line = f.readline().strip()
    bits = bin(int(line, 16))[2:].zfill(4 * len(line))
    version_sum = 0
    process_packet(0)
    print(version_sum)

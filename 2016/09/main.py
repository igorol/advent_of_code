import re

PATTERN = '\((\d+)x(\d+)\)'


def decompress(compressed):
    uncompressed = ''
    while 1:
        m = re.search(PATTERN, compressed)
        if m:
            m1, m2 = [int(g) for g in m.groups()]
            split = re.split(PATTERN, compressed, 1)
            uncompressed += split[0]
            uncompressed += split[-1][:m1] * m2
            compressed = split[-1][m1:]
        else:
            uncompressed += compressed
            break
    return uncompressed


def len_decompress_v2(compressed):
    weights = [1] * len(compressed)
    char_id = 0
    len_uncompressed = 0
    while char_id < len(compressed):
        if compressed[char_id] != '(':
            len_uncompressed += weights[char_id]
            char_id += 1
        else:
            m = re.match(r'\((\d+)x(\d+)\)', compressed[char_id:])
            m1, m2 = [int(g) for g in m.groups()]
            char_id += len(f'({m1}x{m2})')
            for k in range(char_id, char_id + m1):
                weights[k] *= m2

    return len_uncompressed


message = open('input').read()
print('part 1:', len(decompress(message)))
print('part 2:', len_decompress_v2(message))

# part 1: 70186
# part 2: 10915059201

from typing import Union, List


def compare(left: Union[List, int], right: Union[List, int]) -> int:
    """
    Returns:
        0 if left == right
        1 if left > right
        -1 if left < right
    """
    match left, right:
        case int(), int():
            return (left > right) - (left < right)
        case list(), int():
            return compare(left, [right])
        case int(), list():
            return compare([left], right)
        case list(), list():
            result = compare(len(left), len(right))
            for lleft, rright in zip(left, right):
                if compare(lleft, rright):
                    result = compare(lleft, rright)
                    break
            return result


data = open('input').read().split("\n\n")
pairs = [[eval(i) for i in pair.split()] for pair in data]
print('part 1:', sum(i for i, pair in enumerate(pairs, start=1) if compare(*pair) < 0))

divider_packets = [2, 6]
comps = [sum(compare(packet, x) == 1 for pair in pairs for x in pair) + 1 for packet in divider_packets]
print('part 2:', comps[0] * (comps[1] + 1))

# part 1:  6187
# part 2: 23520

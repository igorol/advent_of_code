import re
from collections import Counter, deque
from string import ascii_lowercase

pat = r"([A-Za-z\-]+)\-(\d+)\[(\w+)\]"


def part1(in_data):
    def _ids(line):
        g = re.search(pat, line).groups()
        c = Counter(g[0].replace("-", ""))
        if all(
                i[0] in g[2]
                for i in sorted(c.items(), key=lambda t: (-t[1], t[0]), reverse=True)[-5:]
        ):
            return int(g[1])
        return 0

    return sum([_ids(line) for line in in_data])


def part2(in_data):
    def _decrypt(line):
        g = re.search(pat, line).groups()
        strings = deque([*ascii_lowercase])
        encrypted_msg = g[0].replace("-", " ")
        decrypted_msg = ""
        for char in encrypted_msg:
            if char != " ":
                strings.rotate(-int(g[1]))
                c = strings[ascii_lowercase.index(char)]
                strings.rotate(+int(g[1]))
            else:
                c = " "
            decrypted_msg += c
        return decrypted_msg, g[1]

    return [_decrypt(line)[1] for line in in_data if "northpole" in _decrypt(line)[0]][0]


data = open("input").read().splitlines()
print("part 1:", part1(data))
print("part 2:", part2(data))

# part 1: 158835
# part 2: 993

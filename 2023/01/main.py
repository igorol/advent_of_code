import re

data = open("input").read().splitlines()

def solve(line, part2=False):
    if part2:
        spelled = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        results = re.findall(f"(?=(\d|{'|'.join(spelled)}))", line)
        digits = [str(spelled.index(x) + 1) if x in spelled else x for x in results]
    else:
        digits = [i for i in line if i.isnumeric()]
    return int(digits[0] + digits[-1])

print('Part 1:', sum([solve(line) for line in data]))
print('Part 2:', sum([solve(line, part2=True) for line in data]))

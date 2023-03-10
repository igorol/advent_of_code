from itertools import pairwise

data = open('input').readline()
nums_p1 = [int(pair[0]) for pair in pairwise(data + data[0]) if pair[0] == pair[1]]
print(f'Part 1: {sum(nums_p1)}')

nums_p2 = []
for i, num in enumerate(new := data + data):
    if i > len(data):
        break
    elif num == new[i + int(len(data) / 2)]:
        nums_p2.append(int(num))

print(f'Part 2: {sum(nums_p2)}')

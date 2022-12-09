import re

data = open("input").read().splitlines()

num_chars = sum([len(line.replace("\n", "")) for line in data])
mem_size = sum([len(eval(line)) for line in data])
encoded = sum((line.count("\\") + line.count('"') + 2) for line in data)

print("part 1:", num_chars - mem_size)
print("part 2:", encoded)

breakpoint()

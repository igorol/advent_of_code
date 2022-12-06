data = open("input").read()

def solve(data, n=4):
    groups = [(data[i:i+n]) for i in range(0, len(data)-n+1)]
    for i, group in enumerate(groups):
        if len(set(group)) == len(group):
            return i + n
            
print('part 1:',solve(data, n=4))
print('part 2:',solve(data, n=14))

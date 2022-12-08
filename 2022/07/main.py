from collections import defaultdict

data = open("input").read().splitlines()


def build_tree(data):
    paths = []
    directories = defaultdict(int)
    for line in data:
        parts = line.split()
        if parts[1] == "ls":
            continue
        elif parts[1] == "cd":
            if parts[2] == "..":
                paths.pop()
            else:
                directories[parts[2]] += 0
                paths.append(parts[2])
        elif parts[0].isdigit():
            size = int(parts[0])
            for i in range(len(path) + 1):
                last_dir_on_path = "/".join(paths[:i])
                directories[last_dir_on_path] += size
    return directories


directories = build_tree(data)
max_size = 100_000
print("part 1:", sum([size for size in directories.values() if size <= max_size]))

disk_size = 70_000_000
needed_for_update = 30_000_000
free_space = disk_size - directories["/"]
update_space = needed_for_update - free_space
print("part 2:", min([size for size in directories.values() if size >= update_space]))

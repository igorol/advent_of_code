# https://adventofcode.com/2022/day/1

data = open("input").read().splitlines()
calorie_sum, calorie_sum_list = 0, []

for item in data:
    try:
        calorie_sum += int(item)
    except ValueError:
        calorie_sum_list.append(calorie_sum)
        calorie_sum = 0

print("part 1:", max(calorie_sum_list))
print("part 2:", sum(sorted(calorie_sum_list)[-3:]))

from itertools import product


def solve(line, possible_operators=["+", "*"]):
    test_value, numbers = line.split(":")
    test_value = int(test_value)
    numbers = [int(n) for n in numbers.split()]
    operators = list(product(possible_operators, repeat=len(numbers) - 1))

    for these_operators in operators:
        res = numbers[0]
        for n, oper in zip(range(1, len(numbers)), these_operators):
            if oper == "+":
                res += numbers[n]
            elif oper == "*":
                res *= numbers[n]
            elif oper == "||":
                res = int(f"{res}{numbers[n]}")
        if res == test_value:
            return test_value

    return 0


data = [line.strip() for line in open("input").readlines()]
print("Part 1:", sum(solve(line, possible_operators=["*", "+"]) for line in data))
print("Part 2:", sum(solve(line, possible_operators=["*", "+", "||"]) for line in data))

# Part 1: 1399219271639
# Part 2: 275791737999003

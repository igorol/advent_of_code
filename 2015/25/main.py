import re
import numpy as np

ans_row, ans_column = [int(s) for s in re.findall(r"\d+", open("input").read())]
first_code = 20151125
multiplier = 252533
divisor = 33554393

# the top code in each column has a pattern of summing 2, 3, 4, 5, ...
#    +2  +3  +4  +5  +6
# 1,  3,  6, 10, 15, 21,
top_code_in_ans_column = np.sum(np.arange(2, ans_column + 1)) + 1

# similarly, going down a column adds the column number, +1, +2 ...
code_number = top_code_in_ans_column + np.sum(
    np.arange(ans_column, ans_column + ans_row - 1)
)

code = first_code
for i in range(code_number - 1):
    code = (code * multiplier) % divisor

print("part 1:", code)

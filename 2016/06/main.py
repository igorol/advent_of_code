"""
part 1: xhnqpqql
part 2: brhailro
"""

import pandas as pd

data = pd.read_csv("input", header=None).apply(
    lambda x: [*x[0]], axis=1, result_type="expand"
)
print("part 1:", "".join(data.mode().loc[0].tolist()))
print(
    "part 2:",
    "".join(data.apply(lambda row: row.value_counts().index).iloc[-1, :].tolist()),
)

import numpy as np
import pandas as pd

df = pd.read_csv("input", header=None, delim_whitespace=True)

print(
    "part 1:",
    df.apply(np.sort, result_type="expand", axis=1)
    .apply(lambda x: x[0] + x[1] > x[2], axis=1)
    .sum(),
)

print(
    "part 2:",
    pd.DataFrame(df.values.T.flatten().reshape((-1, 3)))
    .apply(np.sort, result_type="expand", axis=1)
    .apply(lambda x: x[0] + x[1] > x[2], axis=1)
    .sum(),
)

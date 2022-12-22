import numpy as np
import matplotlib.pyplot as plt
import re


def cmd(scr, inline):
    left_num, right_num = re.findall(r'\d+', inline)
    left_num, right_num = int(left_num), int(right_num)
    if inline.startswith('rect'):
        scr[:right_num, :left_num] = 1
    elif inline.__contains__('column'):
        scr[:, left_num] = np.roll(scr[:, left_num], right_num)
    else:
        scr[left_num] = np.roll(scr[left_num], right_num)
    return scr


data = open('input').read().splitlines()

array = np.full((6, 50), fill_value=0)
screen = [cmd(array, line) for i, line in enumerate(data)][-1]
print('part 1:', np.count_nonzero(screen == 1))

print('part 2: read text in image')
plt.matshow(screen)
plt.show()

# part 1: 110
# part 2: ZJHRKCPLYJ

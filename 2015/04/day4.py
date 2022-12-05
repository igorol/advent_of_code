from hashlib import md5


def mine_adventcoins(input_string):

    counter, five_zeros_number, six_zeros_number = 0, 0, 0

    while True:
        counter += 1
        h = md5(bytes(input_string + str(counter), "utf-8")).hexdigest()

        if not five_zeros_number and h.startswith("0" * 5):
            five_zeros_number = counter

        if not six_zeros_number and h.startswith("0" * 6):
            six_zeros_number = counter

        if five_zeros_number and six_zeros_number:
            break

    return five_zeros_number, six_zeros_number


assert mine_adventcoins("abcdef")[0] == 609043
assert mine_adventcoins("pqrstuv")[0] == 1048970

five_zeros_number, six_zeros_number = mine_adventcoins("iwrupvqb")
print("Part1", five_zeros_number)
print("Part2", six_zeros_number)


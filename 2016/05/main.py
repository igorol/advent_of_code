from hashlib import md5

puzzle_input = 'cxdnnyjw'


def part1():
    password = ''
    n = 0
    while 1:
        hexdigest = md5(f'{puzzle_input}{n}'.encode('utf-8')).hexdigest()
        if str(hexdigest)[:5] == '00000':
            password += str(hexdigest)[5]
        if len(password) == 8:
            return password
        n += 1


def part2():
    password = 8 * ['']
    n = 0
    while 1:
        s = str(md5(f'{puzzle_input}{n}'.encode('utf-8')).hexdigest())
        if s[:5] == '00000' and s[5].isdigit() and int(s[5]) < len(password):
            password[int(s[5])] = s[6] if password[int(s[5])] == '' else password[int(s[5])]
        if '' not in password:
            return ''.join(password)
        n += 1


print('part 1:', part1())
print('part 2:', part2())

# part 1: f77a0e6e
# part 2: 999828ec

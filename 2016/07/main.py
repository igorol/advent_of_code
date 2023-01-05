import re


def find_brackets(string):
    brackets = re.findall(r"\[(.*?)]", string)
    for b in brackets:
        string = string.replace(f"[{b}]", ",")
    return brackets, string.split(",")


def get_abbas(words):
    abbas = [word[i : i + 4] for word in words for i in range(len(word) - 3)]
    return [a for a in abbas if a[0:2] == a[3:1:-1] and len(set(a)) == 2]


def supports_tls(line):
    brackets, non_brackets = find_brackets(line)
    non_bracket_abbas = get_abbas(non_brackets)
    bracket_abbas = get_abbas(brackets)

    if len(non_bracket_abbas) > len(bracket_abbas) == 0:
        return True
    return False


def supports_ssl(line):
    brackets, non_brackets = find_brackets(line)
    abas = [word[i : i + 3] for word in non_brackets for i in range(len(word) - 2)]
    abas = [a for a in abas if a[0] == a[2] != a[1]]

    if len(abas) > 0 and any(
        [aba[1] + aba[0] + aba[1] in b for aba in abas for b in brackets]
    ):
        return True

    return False


data = open("input").read().splitlines()
print("part 1:", sum([supports_tls(line) for line in data]))
print("part 2:", sum([supports_ssl(line) for line in data]))

# part 1: 105
# part 2: 258

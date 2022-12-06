import copy
import operator
from dataclasses import dataclass
from typing import Any, Callable, Dict, Union

operators = {
    "AND": operator.and_,
    "OR": operator.or_,
    "LSHIFT": operator.lshift,
    "RSHIFT": operator.rshift,
    "NOT": operator.invert,
    "ID": lambda x: x,
}


@dataclass
class Command:
    line: str
    arg1: Union[int, str]
    arg2: Union[int, str]
    output: str
    operator: Callable[[Any], Any]
    arity: int
    done: bool


def parse_line(line: str):
    left, right = line.split(" -> ")
    left = left.split(" ")
    if len(left) == 3:  # Ex: "kk RSHIFT 3"
        arg1, op_name, arg2 = left
        arg1 = int(arg1) if arg1.isdigit() else arg1
        arg2 = int(arg2) if arg2.isdigit() else arg2
        return Command(line, arg1, arg2, right, operators[op_name], 2, False)
    if len(left) == 2:  # Ex: "NOT gs"
        op_name, arg1 = left
        arg1 = int(arg1) if arg1.isdigit() else arg1
        return Command(line, arg1, None, right, operators[op_name], 1, False)
    if len(left) == 1:  # Ex: "44430"
        arg1 = int(left[0]) if left[0].isdigit() else left[0]
        return Command(line, arg1, None, right, operators["ID"], 1, False)
    return None


def check(wires, arg1):
    if isinstance(arg1, int):
        return arg1
    elif arg1 in wires.keys():
        return wires[arg1]
    else:
        return None


def solve(commands, new_initial_state=None):
    wires = {}
    commands = copy.deepcopy(commands)
    while len(commands) > 0:
        for command in commands:
            if command.done:
                continue
            if new_initial_state is not None: # circuit starts at `b`
                wires["b"] = new_initial_state
            if command.arity == 2:
                arg1 = check(wires, command.arg1)
                arg2 = check(wires, command.arg2)
                if arg1 is not None and arg2 is not None:
                    wires[command.output] = command.operator(arg1, arg2) & 0xFFFF
                    command.done = True
                    commands.remove(command)
            elif command.arity == 1:
                arg1 = check(wires, command.arg1)
                if arg1 is not None:
                    wires[command.output] = command.operator(arg1) & 0xFFFF
                    command.done = True
                    commands.remove(command)
    return wires


data = open("input").read().splitlines()
commands = [parse_line(line) for line in data]

part1 = solve(commands)["a"]
part2 = solve(commands, new_initial_state=part1)["a"]
print("part 1:", part1)
print("part 2:", part2)

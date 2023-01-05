import re
from dataclasses import dataclass
from functools import reduce
from operator import mul
from typing import List


@dataclass()
class Monkey:
    id: int
    worry_levels: List[int]
    num_inspections: int
    test_division: int
    if_true: int
    if_false: int
    operation: str


class KeepAway:
    INPUT = "test_input"

    def __init__(self, num_monkeys=8, num_rounds=20, worry_divisor=3):
        self.num_monkeys = num_monkeys
        self.num_rounds = num_rounds
        self.worry_divisor = worry_divisor
        self.monkeys = self.initialize_monkeys()
        self.common_divisor = reduce(mul, (m.test_division for m in self.monkeys))

    def initialize_monkeys(self):
        notes = open(self.INPUT).read().split("\n\n")
        return [
            self._parse_note(monkey_id, note) for monkey_id, note in enumerate(notes)
        ]

    def monkey_business(self):
        self.play_game()
        insp = sorted([monkey.num_inspections for monkey in self.monkeys], reverse=True)
        return insp[0] * insp[1]

    def play_game(self):
        for _ in range(self.num_rounds):
            self.play_round()

    def play_round(self):
        for monkey_id in range(self.num_monkeys):
            self.play_monkey(monkey_id)

    def play_monkey(self, monkey_id):
        worry_levels = list(self.monkeys[monkey_id].worry_levels)
        self.monkeys[monkey_id].num_inspections += len(worry_levels)
        for old_worry in worry_levels:
            if self.worry_divisor == 1:
                new_worry = (
                    eval(f"{old_worry} {self.monkeys[monkey_id].operation}")
                    % self.common_divisor
                )
            else:
                new_worry = int(
                    eval(f"{old_worry} {self.monkeys[monkey_id].operation}")
                    / self.worry_divisor
                )
            if new_worry % self.monkeys[monkey_id].test_division == 0:
                if_true = self.monkeys[monkey_id].if_true
                self.monkeys[if_true].worry_levels.append(new_worry)
            else:
                if_false = self.monkeys[monkey_id].if_false
                self.monkeys[if_false].worry_levels.append(new_worry)

        _ = [
            self.monkeys[monkey_id].worry_levels.remove(level) for level in worry_levels
        ]

    @staticmethod
    def _parse_note(monkey_id, note):
        lines = note.split("\n")
        operation = re.search(r"([*+]) (\w+)", lines[2]).group()

        return Monkey(
            id=monkey_id,
            worry_levels=[int(item) for item in re.findall(r"\d+", lines[1])],
            num_inspections=0,
            test_division=int(re.search(r"(\d+)", lines[3]).group()),
            if_true=int(re.search(r"(\d+)", lines[4]).group()),
            if_false=int(re.search(r"(\d+)", lines[5]).group()),
            operation="** 2" if operation == "* old" else operation,
        )


game1 = KeepAway(num_rounds=20, worry_divisor=3)
monkey_business = game1.monkey_business()
print("part 1:", monkey_business)

game2 = KeepAway(num_rounds=10_000, worry_divisor=1)
monkey_business = game2.monkey_business()
print("part 2:", monkey_business)

# # part 1: 50172
# # part 2: 11614682178

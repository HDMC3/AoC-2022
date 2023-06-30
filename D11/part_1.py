from typing import Callable, List
from math import floor

class Monkey:
    def __init__(self, items: List[int], operation: Callable[[int], int], test: Callable[[int], int]) -> None:
        self.items = items
        self.operation = operation
        self.test = test

    def play_turn(self, monkey_list: List):
        if len(self.items) == 0:
            return

        for item in self.items:
            new_worry = self.operation(item)
            new_worry = floor(new_worry/3)
            monkey_idx_to_throw = self.test(new_worry)
            monkey_list[monkey_idx_to_throw].items.append(new_worry)

        self.items.clear()


monkeys: List[Monkey] = [
    Monkey([75, 75, 98, 97, 79, 97, 64], 
        lambda old: old * 13, 
        lambda item: 2 if item % 19 == 0 else 7
    ),
    Monkey([50, 99, 80, 84, 65, 95], 
        lambda old: old + 2, 
        lambda item: 4 if item % 3 == 0 else 5
    ),
    Monkey([96, 74, 68, 96, 56, 71, 75, 53], 
        lambda old: old + 1, 
        lambda item: 7 if item % 11 == 0 else 3
    ),
    Monkey([83, 96, 86, 58, 92], 
        lambda old: old + 8, 
        lambda item: 6 if item % 17 == 0 else 1
    ),
    Monkey([99], 
        lambda old: old * old, 
        lambda item: 0 if item % 5 == 0 else 5
    ),
    Monkey([60, 54, 83], 
        lambda old: old + 4, 
        lambda item: 2 if item % 2 == 0 else 0
    ),
    Monkey([77, 67], 
        lambda old: old * 17, 
        lambda item: 4 if item % 13 == 0 else 1
    ),
    Monkey([95, 65, 58, 76], 
        lambda old: old + 5, 
        lambda item: 3 if item % 7 == 0 else 6
    )
]

monkey_sums = [0, 0, 0, 0, 0, 0, 0, 0]

for game_round in range(0, 20):
    for i, monkey in enumerate(monkeys):
        monkey_sums[i] += len(monkey.items)
        monkey.play_turn(monkeys)

monkey_sums.sort(reverse=True)

# Solution: 66124
print(monkey_sums[0] * monkey_sums[1])

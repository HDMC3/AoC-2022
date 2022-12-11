input_file = open("input.txt")

stacks = [
    ['N','B','D','T','V','G','Z','J'],
    ['S','R','M','D','W','P','F'],
    ['V','C','R','S','Z'],
    ['R','T','J','Z','P','H','G'],
    ['T','C','J','N','D','Z','Q','F'],
    ['N','V','P','W','G','S','F','M'],
    ['G','C','V','B','P','Q'],
    ['Z','B','P','N'],
    ['W','P','J']
]

import re

moves = []
for i, line in enumerate(input_file):
    if i > 9:
        match = re.findall("[0-9]+", line)
        move = list(map(lambda x: int(x), match))
        move[1] -= 1
        move[2] -= 1
        moves.append(move)


for move in moves:
    boxes = move[0]
    s_from = move[1]
    s_to = move[2]
    moved_elements = stacks[s_from][-boxes:]
    for _ in range(boxes):
        if len(stacks[s_from]) > 0:
            stacks[s_from].pop()

    stacks[s_to].extend(moved_elements)


message = ""
for s in stacks:
    message += s[-1]

# Solution: VRQWPDSGP
print(message)

import math

class Move:
    def __init__(self, direction: str, steps: int) -> None:
        self.direction = direction
        self.steps = steps


class Position:
    def __init__(self, x, y, parent) -> None:
        self.x = x
        self.y = y
        self.parent = parent


def get_move(move: str):
    move = move.strip()
    direction = move.split(' ')[0]
    steps = int(move.split(' ')[1])
    return Move(direction, steps)


def is_touching(h_position: Position, t_position: Position):
    valid_positions = [
        (h_position.x - 1, h_position.y + 1),
        (h_position.x, h_position.y + 1),
        (h_position.x + 1, h_position.y + 1),

        (h_position.x - 1, h_position.y),
        (h_position.x, h_position.y),
        (h_position.x + 1, h_position.y),
        
        (h_position.x - 1, h_position.y - 1),
        (h_position.x, h_position.y - 1),
        (h_position.x + 1, h_position.y - 1)
    ]

    return (t_position.x, t_position.y) in valid_positions


input_file = open('input.txt')
moves = list(map(get_move, input_file))

positions = [(0, 0)]

H = Position(0, 0, None)
_1 = Position(0, 0, H)
_2 = Position(0, 0, _1)
_3 = Position(0, 0, _2)
_4 = Position(0, 0, _3)
_5 = Position(0, 0, _4)
_6 = Position(0, 0, _5)
_7 = Position(0, 0, _6)
_8 = Position(0, 0, _7)
T = Position(0, 0, _8)

rope = [
    _1, _2, _3, _4, _5, _6, _7, _8, T
]

directions = {
    'U': (0,  1),
    'R': (1,  0),
    'D': (0, -1),
    'L': (-1, 0)
}

for move in moves:
    for i in range(0, move.steps):
        H.x += directions[move.direction][0]
        H.y += directions[move.direction][1]

        for node in rope:
            if is_touching(node.parent, node):
                continue

            if node.parent.y == node.y:
                node.x += int(math.copysign(1, node.parent.x - node.x))
            
            elif node.parent.x == node.x:
                node.y += int(math.copysign(1, node.parent.y - node.y))

            else:
                node.y += int(math.copysign(1, node.parent.y - node.y))
                node.x += int(math.copysign(1, node.parent.x - node.x))

            if node == T and (node.x, node.y) not in positions:
                positions.append((node.x, node.y))


# Solution: 2541
print(len(positions))

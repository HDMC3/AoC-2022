import math

class Move:
    def __init__(self, direction: str, steps: int) -> None:
        self.direction = direction
        self.steps = steps


class Position:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


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
H = Position(0, 0)
T = Position(0, 0)

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

        if is_touching(H, T):
            continue

        if H.y == T.y:
            T.x += int(math.copysign(1, H.x - T.x))
        
        elif H.x == T.x:
            T.y += int(math.copysign(1, H.y - T.y))

        else:
            T.y += int(math.copysign(1, H.y - T.y))
            T.x += int(math.copysign(1, H.x - T.x))

        if (T.x, T.y) not in positions:
            positions.append((T.x, T.y))


# Solution: 6339
print(len(positions))

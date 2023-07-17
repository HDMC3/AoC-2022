from __future__ import annotations
from typing import Dict, List, Tuple


class Coordinate:
    def __init__(self, x: int, y: int, symbol: str = ".") -> None:
        self.x = x
        self.y = y
        self.symbol = symbol

    def __str__(self) -> str:
        return self.symbol

    def __eq__(self, coord: (Tuple[int, int] | Coordinate)) -> bool:
        if type(coord) == tuple:
            return self.x == coord[0] and self.y == coord[1]

        return self.x == coord.x and self.y == coord.y


def get_coords_to_line(init_coord: Tuple[int, int], end_coord: Tuple[int, int]):
    coords: List[Tuple[int, int]] = []
    init_x = init_coord[0]
    init_y = init_coord[1]
    end_x = end_coord[0]
    end_y = end_coord[1]

    if init_x > end_x:
        for x in range(end_x + 1, init_x):
            coords.append((x, end_y))

    if end_x > init_x:
        for x in range(init_x + 1, end_x):
            coords.append((x, end_y))

    if init_y > end_y:
        for y in range(end_y + 1, init_y):
            coords.append((end_x, y))

    if end_y > init_y:
        for y in range(init_y + 1, end_y):
            coords.append((end_x, y))

    return coords


def get_new_sand_position(unit: Coordinate, invalid_coords: Dict[Tuple[int, int]]):
    moves = [
        (unit.x, unit.y + 1),  # DOWN
        (unit.x - 1, unit.y + 1),  # DIAGONAL LEFT
        (unit.x + 1, unit.y + 1)  # DIAGONAL RIGHT
    ]

    for move in moves:
        if invalid_coords.get(move) != None or move[1] == MAX_Y + 2:
            continue

        return (move[0], move[1])

    return None


ROCKS_AND_SAND: Dict[Tuple[int, int], str] = {}
x_list = []
y_list = []

input_file = open('input.txt')
for line in input_file:
    path_str = line.strip().split(" -> ")
    path: List[Tuple[int, int]] = []

    for coord_str in path_str:
        x = int(coord_str.split(",")[0])
        y = int(coord_str.split(",")[1])
        x_list.append(x)
        y_list.append(y)
        coord = (x, y)

        if len(path) == 0:
            path.append(coord)
            continue

        last_rock = path[-1]
        line_rocks = get_coords_to_line(last_rock, coord)

        path.extend(line_rocks)
        path.append(coord)

    for c in path:
        ROCKS_AND_SAND[c] = "#"

MAX_Y = max(y_list)
SAND_ENTRY_X = 500
SAND_ENTRY_Y = 0

current_sand = Coordinate(SAND_ENTRY_X, SAND_ENTRY_Y, "o")
sand_count = 0

while (True):
    next_move = get_new_sand_position(current_sand, ROCKS_AND_SAND)

    if current_sand == (SAND_ENTRY_X, SAND_ENTRY_Y) and next_move == None:
        sand_count += 1
        break

    if next_move != None:
        current_sand.x = next_move[0]
        current_sand.y = next_move[1]
    else:
        sand_count += 1
        ROCKS_AND_SAND[(current_sand.x, current_sand.y)] = "o"
        current_sand.x = SAND_ENTRY_X
        current_sand.y = SAND_ENTRY_Y


# Solution: 27623
print(sand_count)

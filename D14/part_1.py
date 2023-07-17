from __future__ import annotations
import os
from typing import List


class Coordinate:
    def __init__(self, x: int, y: int, symbol: str = ".") -> None:
        self.x = x
        self.y = y
        self.symbol = symbol

    def __str__(self) -> str:
        return self.symbol


class Path:
    def __init__(self) -> None:
        self.coords: List[Coordinate] = []

    def add_coordinate(self, coord: Coordinate):
        if len(self.coords) == 0:
            self.coords.append(coord)
            return

        last_coord: Coordinate = self.coords[-1]
        if last_coord.x > coord.x:
            for x in range(coord.x + 1, last_coord.x):
                self.coords.append(Coordinate(x, coord.y))

        if coord.x > last_coord.x:
            for x in range(last_coord.x + 1, coord.x):
                self.coords.append(Coordinate(x, coord.y))

        if last_coord.y > coord.y:
            for y in range(coord.y + 1, last_coord.y):
                self.coords.append(Coordinate(coord.x, y))

        if coord.y > last_coord.y:
            for y in range(last_coord.y + 1, coord.y):
                self.coords.append(Coordinate(coord.x, y))

        self.coords.append(coord)


PATHS: List[Path] = []
x_list = []
y_list = []


input_file = open('input.txt')
for line in input_file:
    path_str = line.strip().split(" -> ")
    path = Path()

    for coord in path_str:
        x = int(coord.split(",")[0])
        y = int(coord.split(",")[1])
        x_list.append(x)
        y_list.append(y)
        path.add_coordinate(Coordinate(x, y, "#"))

    PATHS.append(path)

MIN_X = min(x_list)
MAX_X = max(x_list)
MIN_Y = 0
MAX_Y = max(y_list)


def trace_rocks(cave_map: List[List[Coordinate]], paths: List[Path]):
    x_offset = MIN_X - 1
    for path in paths:
        for coord in path.coords:
            cave_map[coord.y][coord.x - x_offset].symbol = "#"


def create_cave_map():
    empty_map: List[List[Coordinate]] = []
    x_offset = MIN_X - 1
    for y in range(MIN_Y, MAX_Y + 2):
        empty_map.append([])
        for x in range(0, MAX_X - x_offset + 2):
            empty_map[-1].append(Coordinate(x, y))

    trace_rocks(empty_map, PATHS)

    return empty_map


def verify_move(x: int, y: int, cave_map: List[List[Coordinate]]):
    is_valid_x = x > 0 and x < len(cave_map[0])
    is_valid_y = y > 0 and y < len(cave_map)
    if is_valid_x and is_valid_y:
        return cave_map[y][x].symbol == "."

    return False


def get_new_sand_position(unit: Coordinate, cave_map: List[List[Coordinate]]):
    moves = [
        (unit.x, unit.y + 1),  # DOWN
        (unit.x - 1, unit.y + 1),  # DIAGONAL LEFT
        (unit.x + 1, unit.y + 1)  # DIAGONAL RIGHT
    ]

    for move in moves:
        x = move[0]
        y = move[1]
        can_move = verify_move(x, y, cave_map)
        if can_move:
            return (x, y)

    return None


def print_map(current: Coordinate):
    out = ''
    for row in cave_map:
        for coord in row:
            if coord.x == current.x and coord.y == current.y:
                out += "\033[;32m" + '@' + "\033[0;m"
            elif coord.symbol == 'o':
                out += "\033[;32m" + str(coord) + "\033[0;m"
            else:
                out += str(coord)
        out += '\n'

    print(out)


cave_map = create_cave_map()
SAND_ENTRY_X = 500 - (MIN_X - 1)
SAND_ENTRY_Y = 0

current_sand = Coordinate(SAND_ENTRY_X, SAND_ENTRY_Y, "o")
sand_count = 0

while (True):
    if current_sand.y == MAX_Y:
        os.system('clear')
        print_map(current_sand)
        break

    new_position = get_new_sand_position(current_sand, cave_map)
    if new_position != None:
        current_sand.x = new_position[0]
        current_sand.y = new_position[1]
    else:
        sand_count += 1
        cave_map[current_sand.y][current_sand.x].symbol = "o"
        current_sand.x = SAND_ENTRY_X
        current_sand.y = SAND_ENTRY_Y


# Solution: 728
print(sand_count)

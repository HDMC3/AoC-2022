from __future__ import annotations
from enum import Enum
from typing import List


class NodeState(Enum):
    NOT_VISITED = 0
    CLOSED = 1
    OPEN = 2


class Node:
    def __init__(self, row: int, col: int, height: int, height_key: str, state=NodeState.NOT_VISITED) -> None:
        self.row = row
        self.col = col
        self.state = state
        self.height = height
        self.height_key = height_key
        self.G = 0
        self.parent = None

    def open(self, current: Node):
        self.G = current.G + COST_TO_MOVE
        self.parent = current
        self.state = NodeState.OPEN

    def update(self, current: Node):
        self.G = current.G + COST_TO_MOVE
        self.parent = current


HEIGHT_BY_KEY = {
    'S': 0, 'E': 25, 'a': 0, 'b': 1, 'c': 2, 'd': 3,
    'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
    'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15,
    'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21,
    'w': 22, 'x': 23, 'y': 24, 'z': 25,
}


def verify_coord(row, col, nodes_map: List[List[Node]]):
    is_valid_row = row >= 0 and row < len(nodes_map)
    is_valid_col = col >= 0 and col < len(nodes_map[0])
    return is_valid_row and is_valid_col


def create_height_map():
    input_file = open('input.txt')

    nodes_map: List[List[Node]] = []

    for row, line in enumerate(input_file):

        nodes_map.append([])
        for col, height_key in enumerate(line.strip()):
            if height_key == 'S':
                nodes_map[row].append(
                    Node(row, col, HEIGHT_BY_KEY[height_key], height_key, state=NodeState.CLOSED))
            else:
                nodes_map[row].append(
                    Node(row, col, HEIGHT_BY_KEY[height_key], height_key))

    input_file.close()

    return nodes_map


def get_start_nodes(nodes_map: List[List[Node]]):
    nodes: List[Node] = []
    for row in nodes_map:
        for node in row:
            if node.height != 0:
                continue

            offsets = [
                (-1,  0),  # UP
                (0,  1),  # RIGHT
                (1,  0),  # DOWN
                (0, -1),  # LEFT
            ]

            for direction in offsets:
                is_coord_valid = verify_coord(
                    node.row + direction[0],
                    node.col + direction[1],
                    nodes_map
                )

                if not is_coord_valid:
                    continue

                next_node: Node = nodes_map[node.row +
                                            direction[0]][node.col + direction[1]]

                if next_node.height == node.height + 1:
                    nodes.append(node)
                    break

    return nodes


def open_nodes(current: Node, nodes_map: List[List[Node]]):
    nodes = []
    offsets = [
        (0,  1),  # RIGHT
        (1,  0),  # DOWN
        (0, -1),  # LEFT
        (-1,  0),  # UP
    ]

    for direction in offsets:
        is_coord_valid = verify_coord(
            current.row + direction[0],
            current.col + direction[1],
            nodes_map
        )

        if not is_coord_valid:
            continue

        row = current.row + direction[0]
        col = current.col + direction[1]
        possible_node: Node = nodes_map[row][col]

        if possible_node.state == NodeState.CLOSED:
            continue

        if possible_node.state == NodeState.OPEN:
            if current.G + COST_TO_MOVE < possible_node.G:
                possible_node.update(current)
            nodes.append(possible_node)
            continue

        is_valid_node = possible_node.height <= current.height + 1

        if not is_valid_node:
            continue

        possible_node.open(current)
        nodes.append(possible_node)

    return nodes


def select_next(current: Node, possible_nodes: List[Node], target: Node):
    sorted_possible_nodes = sorted(possible_nodes, key=lambda n: n.G)

    if len(possible_nodes) == 0:
        current.state = NodeState.CLOSED
        return None

    if target in possible_nodes:
        current.state = NodeState.CLOSED
        target.parent = current
        return target

    next_node = sorted_possible_nodes[0]
    next_node.state = NodeState.CLOSED

    possible_nodes.remove(next_node)
    return next_node


def get_path(current: Node):
    ref_node = current
    path = [ref_node]
    completed = False
    while (not completed):
        if ref_node.parent == None:
            completed = True
            continue
        path.insert(0, ref_node.parent)
        ref_node = ref_node.parent

    return path[1:]


def resolve(S_NODE):
    opened_nodes: List[Node] = []
    current_node = S_NODE

    solved = False
    while (not solved):
        if current_node == END_NODE:
            solved = True
            break

        possible_nodes = open_nodes(current_node, heightmap)
        for n in possible_nodes:
            if n not in opened_nodes:
                opened_nodes.append(n)

        current_node = select_next(current_node, opened_nodes, END_NODE)

        if current_node == None:
            break

    solution_path = get_path(current_node)
    return solution_path


def clear_heights_map(nodes_map: List[List[Node]], start_node: Node):
    for row in nodes_map:
        for node in row:
            node.G = 0
            node.parent = None
            if node == start_node:
                node.state = NodeState.CLOSED
            else:
                node.state = NodeState.NOT_VISITED


S_ROW = 20
S_COL = 0
E_ROW = 20
E_COL = 36
COST_TO_MOVE = 10
heightmap: List[List[Node]] = create_height_map()
END_NODE = heightmap[E_ROW][E_COL]

START_NODES: List[Node] = get_start_nodes(heightmap)
solution: int = 1000000

for s_node in START_NODES:
    clear_heights_map(heightmap, s_node)
    solution_path = resolve(s_node)
    temp_solution = len(solution_path)

    if temp_solution < solution:
        solution = temp_solution

# Solution: 321
print(solution)

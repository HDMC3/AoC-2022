input_file = open('input.txt')

def to_numbers(str_numbers: str):
    numbers = map(lambda char: int(char), list(str_numbers))
    return list(numbers)

tree_grid = list( map(lambda line: to_numbers(line.strip()), input_file) )

visible_coords = []

rows_count = len(tree_grid)
cols_count = len(tree_grid[0])

def tree(row, col):
    return tree_grid[row][col]

for row_idx in range(1, len(tree_grid)-1):
    for col_idx in range(1, len(tree_grid[0])-1):
        coord = (row_idx, col_idx)

        current_value = tree_grid[row_idx][col_idx]
        up = [tree(x, col_idx) for x in range(0, row_idx) if tree(x, col_idx) >= current_value]
        right = [tree(row_idx, x) for x in range(col_idx+1, cols_count) if tree(row_idx, x) >= current_value]
        down = [tree(x, col_idx) for x in range(row_idx+1, rows_count) if tree(x, col_idx) >= current_value]
        left = [tree(row_idx, x) for x in range(0, col_idx) if tree(row_idx, x) >= current_value]

        if len(up) == 0 or len(right) == 0 or len(down) == 0 or len(left) == 0:
            visible_coords.append(coord)

border_trees = (len(tree_grid[0]) * 2) + (len(tree_grid)*2-4)


# Solution: 1676
print(len(visible_coords) + border_trees)
input_file = open('input.txt')

def to_numbers(str_numbers: str):
    numbers = map(lambda char: int(char), list(str_numbers))
    return list(numbers)

tree_grid = list( map(lambda line: to_numbers(line.strip()), input_file) )

scenic_scores = []

rows_count = len(tree_grid)
cols_count = len(tree_grid[0])

def tree(row, col):
    return tree_grid[row][col]

for row_idx in range(1, rows_count-1):
    for col_idx in range(1, cols_count-1):
        current_value = tree_grid[row_idx][col_idx]

        up_distance = 0
        for x in range(row_idx-1, -1, -1):
            up_distance += 1
            if tree(x, col_idx) >= current_value:
                break

        right_distance = 0
        for x in range(col_idx+1, cols_count):
            right_distance += 1
            if tree(row_idx, x) >= current_value:
                break

        down_distance = 0
        for x in range(row_idx+1, rows_count):
            down_distance += 1
            if tree(x, col_idx) >= current_value:
                break

        left_distance = 0
        for x in range(col_idx-1, -1, -1):
            left_distance += 1
            if tree(row_idx, x) >= current_value:
                break

        scenic_score = up_distance * right_distance * down_distance * left_distance

        scenic_scores.append(scenic_score)


# Solution: 313200
print(max(scenic_scores))
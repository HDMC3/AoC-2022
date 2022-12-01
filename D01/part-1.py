def first_puzzle():
    input_file = open('input.txt')

    max_calories = 0
    current_sum = 0
    for line in input_file:
        if line.strip() != "":
            current_sum += int(line)
        else:
            max_calories = current_sum if current_sum > max_calories else max_calories
            current_sum = 0

    return max_calories
        
# Solution: 67633 
print(first_puzzle())
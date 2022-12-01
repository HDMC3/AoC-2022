def second_puzzle():
    input_file = open('input.txt')

    current_sum, top_one, top_two, top_three = [0] * 4
    
    for line in input_file:
        if line.strip() != "":
            current_sum += int(line)
        else:
            current_sum = 0

        if current_sum > top_one:
            top_one = current_sum
        elif current_sum > top_two:
            top_two = current_sum
        elif current_sum > top_three:
            top_three = current_sum

    return top_one + top_two + top_three

# Solution: 199628
print(second_puzzle())
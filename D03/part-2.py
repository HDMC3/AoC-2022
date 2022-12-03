import re

input_file = open('input.txt')

priority_sum = 0
current_group = []

for i,line in enumerate(input_file):

    if i%3 == 2:
        first_pattern = "|".join(current_group[0])
        first_match = re.findall(first_pattern, current_group[1])
        
        second_pattern = "|".join(first_match)
        second_match = re.findall(second_pattern, line)
        
        ord_shared_item = ord(second_match[0])

        if ord_shared_item < 97:
            priority_sum += ord_shared_item - 65 + 27
        else:
            priority_sum += ord_shared_item - 96
        
        current_group = []
        continue
    
    current_group.append(line.strip())

# Solution: 2548
print(priority_sum)

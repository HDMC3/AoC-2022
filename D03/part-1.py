import re

input_file = open('input.txt')

rucksacks = map(lambda line: line.strip(), input_file)

priority_sum = 0
for rucksack in rucksacks:
    compartment_1 = rucksack[0:int(len(rucksack)/2)]
    compartment_2 = rucksack[int(len(rucksack)/2):]
    
    pattern = "|".join(compartment_1)
    shared_item = re.findall(pattern, compartment_2)

    ord_shared_item = ord(shared_item[0])

    if ord_shared_item < 97:
        priority_sum += ord_shared_item - 65 + 27
    else:
        priority_sum += ord_shared_item - 96

# Solution: 7903
print(priority_sum)

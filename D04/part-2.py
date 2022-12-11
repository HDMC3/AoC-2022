input_file = open("input.txt")

count = 0
for line in input_file:
    pairs = line.strip().split(',')
    range_1 = list(map(lambda n: int(n), pairs[0].split('-')))
    range_2 = list(map(lambda n: int(n), pairs[1].split('-')))

    if range_1[0] <= range_2[0] and range_1[1] >= range_2[0]:
        count+=1
        continue

    if range_2[0] <= range_1[0] and range_2[1] >= range_1[0]:
        count+=1
        continue

# Solution: 852
print(count)

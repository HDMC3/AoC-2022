input_file = open("input.txt")

stream = input_file.readline()

end = 0
marker = []

for i, char in enumerate(stream):
    if char not in marker:
        marker.append(char)
        if len(marker) == 4:
            end = i+1
            break
    else:
        repeat_idx = marker.index(char)
        marker = marker[repeat_idx+1:]
        marker.append(char)
    
# Solution: 1623
print(end)

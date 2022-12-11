input_file = open("input.txt")

stream = input_file.readline()

end = 0
message_marker = []

for i, char in enumerate(stream):
    if char not in message_marker:
        message_marker.append(char)
        if len(message_marker) == 14:
            end = i+1
            break
    else:
        repeat_idx = message_marker.index(char)
        message_marker = message_marker[repeat_idx+1:]
        message_marker.append(char)
    
# Solution: 3774
print(end)

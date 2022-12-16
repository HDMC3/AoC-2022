import re
from typing import List


class Directory:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.files = {}
        self.directories: List[Directory] = []

    def get_directory(self, name_dir):
        for dir in self.directories:
            if dir.name == name_dir:
                return dir

        return None


def check_dirs(directory: Directory, name_dir):
    searched_dir = None

    for dir in directory.directories:
        if dir.name == name_dir:
            searched_dir = dir
            break

        searched_dir = check_dirs(dir, name_dir)

    return searched_dir


root = Directory('/', None)
cd = root


input_file = open('input.txt')

for line in input_file:
    commands = line.strip().split(' ')
    if commands[1] == 'cd' and commands[2] != '..':
        name_dir= commands[2]
        searched_local_dir = cd.get_directory(name_dir)
        if searched_local_dir != None:
            cd = searched_local_dir

    if commands[1] == 'cd' and commands[2] == '..':
        parent = cd.parent
        if parent != None:
            cd = parent

    if commands[0] == 'dir':
        new_dir = Directory(commands[1], cd)
        cd.directories.append(new_dir)

    if re.sub(r'[0-9]+', '', commands[0]) == '':
        cd.files[commands[1]] = int(commands[0])


from functools import reduce

dir_sizes = []

def get_sums(directory: Directory):
    files = directory.files
    size = reduce(lambda acc, curr: acc + files[curr], files, 0)

    for dir in directory.directories:
        size_subdir = get_sums(dir)
        size += size_subdir

    dir_sizes.append((directory.name, size))
    return size


get_sums(root)

used_disc = 0
for dir in dir_sizes:
    if dir[0] == '/':
        used_disc = dir[1]
        break

require_disc = 30000000
total_disc = 70000000
available_disc = total_disc - used_disc

posible_sizes = []

for dir in dir_sizes:
    if dir[1] + available_disc >= 30000000:
        posible_sizes.append(dir[1])

min_dir_size = min(posible_sizes)

# Solution: 5756764
print(min_dir_size)

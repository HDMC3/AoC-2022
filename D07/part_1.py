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

dirs_under_100000 = list(filter(lambda dir: dir[1] <= 100000, dir_sizes))

total = reduce(lambda acc, curr: acc + curr[1], dirs_under_100000, 0)

# Solution: 1297683
print(total)

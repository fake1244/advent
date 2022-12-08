
import math


class Dir:
    def __init__(self, name):
      self.dirs = []
      self.files = []
      self.size = 0
      self.name = name
      self.parent = None
    
    def add_dir(self, name):
        dir = Dir(name)
        dir.parent = self
        self.dirs.append(dir)
    
    def add_file(self, name, size):
        self.files.append(name)
        self.update_size(size)
    
    def update_size(self, size):
        self.size += size
        if self.parent:
            self.parent.update_size(size)
    
    def go_to_dir(self, name):
        for dir in self.dirs:
            if dir.name == name:
                return dir
        return None
    
    def print(self):
        print(self.name)
        print(self.size)
        dir_names = [dir.name for dir in self.dirs]
        print(dir_names)
        print(self.files)


def make_dir(file):
    root = Dir('root')
    for line in file.splitlines():
        # command
        if line.startswith('$'):
            parts = line.split(' ')
            if parts[1] == 'cd':
                if parts[2] == '..':
                    root = root.parent
                    continue
                dir = root.go_to_dir(parts[2])
                if dir == None:
                    root.add_dir(parts[2])
                    root = root.go_to_dir(parts[2])
        else:
            parts = line.split(' ')
            if parts[0] == 'dir':
                continue
            
            root.add_file(parts[1], int(parts[0]))
    while root.parent != None:
        root = root.parent
    return root


def part1(directory):
    def count_dirs(current, dirs, MAX_SIZE):
        if current.size < MAX_SIZE:
            dirs.append(current)
        for dir in current.dirs:
            count_dirs(dir, dirs, MAX_SIZE)
        return dirs


    MAX_SIZE = 100_000
    dirs = count_dirs(directory, [], MAX_SIZE)
    res = 0
    for d in dirs:
        res += d.size
    print(f"Part 1: {res}")


def part2(directory):
    def find_dir_to_delete(current, space, arr):
        if current.size > space:
            arr.append(current)
        for dir in current.dirs:
            find_dir_to_delete(dir, space, arr)
        return arr

    TOTAL_MEM = 70000000
    NEEDED_MEM = 30000000

    AVAILABLE = TOTAL_MEM - directory.size
    need_to_delete = NEEDED_MEM - AVAILABLE
    dirs = find_dir_to_delete(directory, need_to_delete, [])

    res = math.inf
    for size in [d.size for d in dirs]:
        res = min(res, size)
    print(f"Part 2: {res}")


if __name__ == '__main__':
    test = open('test.txt', 'r').read()
    input = open('input.txt', 'r').read()
    directory_test = make_dir(test)
    directory_input = make_dir(input)
    print("Test")
    part1(directory_test)
    part2(directory_test)
    print("Real puzzle")
    part1(directory_input)
    part2(directory_input)

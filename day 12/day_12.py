import math

def part1(input, begin=None, toPrint = False):
    puzzle = []
    start = None
    end = None
    for i, line in enumerate(input.splitlines()):
        row = []
        for j, char in enumerate(line):
            if char == 'S':
                start = (i, j)
                row.append(ord('a'))
                continue
            if char == 'E':
                end = (i, j)
                row.append(ord('z'))
                continue
            row.append(ord(char))
        puzzle.append(row)
    if begin:
        start = begin
    visited = set()
    queue = [(start, 0)]
    while queue:
        move, cost = queue.pop(0)
        if move in visited:
            continue
        visited.add(move)

        if move == end:
            if toPrint:
                print("Part 1: ", cost)
            return cost
        add_moves(move, queue, puzzle, cost)
        queue.sort(key=lambda x: x[1])

    return math.inf


def is_valid(move, max_x, max_y):
    if 0 <= move[0] < max_x and 0 <= move[1] < max_y:
        return True
    return False


def add_moves(move, queue, puzzle, cost):
    moves = [(move[0] + 1, move[1]), (move[0], move[1] + 1), (move[0] - 1, move[1]), (move[0], move[1] - 1)]
    max_x = len(puzzle)
    max_y = len(puzzle[move[0]])
    for test in moves:
        if not is_valid(test, max_x, max_y):
            continue
        
        if puzzle[test[0]][test[1]] - puzzle[move[0]][move[1]] <= 1:
            queue.append((test, cost + 1))


def part2(input):
    posibilities = []
    for i, line in enumerate(input.splitlines()):
        for j, c in enumerate(line):
            if c == 'a':
                posibilities.append((i, j))
    res = [part1(input, toPrint=False)]
    for pos in posibilities:
        res.append(part1(input, begin=pos, toPrint=False))

    print("Part 2: ", min(res))
    pass


if __name__ == '__main__':
    test = open('./day 12/test.txt', 'r').read()
    input = open('./day 12/input.txt', 'r').read()
    print("Test")
    part1(test, toPrint=True)
    part2(test)
    print("Real puzzle")
    part1(input, toPrint=True)
    part2(input)
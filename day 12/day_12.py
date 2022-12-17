
def find_start_end(puzzle):
    start = None
    end = None
    for r in range(len(puzzle)):
        for c in range(len(puzzle[r])):
            if puzzle[r][c] == 'S':
                start = (r, c)
                # puzzle[r][c] = 'a'
            if puzzle[r][c] == 'E':
                end = (r, c)
                # puzzle[r][c] = 'z'
    return start, end

def heuristic(curr, end):
    return abs(curr[0] - end[0]) + abs(curr[1] - end[1])

def add_move(curr, test, cost, end, queue, MAX, puzzle):
    if test[0] < 0 or test[1] < 0 or test[0] >= MAX or test[1] >= MAX:
        return
    now = puzzle[curr[0]][curr[1]]
    print(test, MAX)
    next = puzzle[test[0]][test[1]]
    if now == 'S':
        now = 'a'
    if now == 'E':
        now = 'z'

    print(f"ord now {ord(now)} ord next {ord(next)}")
    if ord(now) + 1 >= ord(next): 
        queue.append((test, cost, heuristic(test, end)))
    return

def part1(input):
    puzzle = input.splitlines()
    # print(puzzle[1][1])
    visited = set()
    start, end = find_start_end(puzzle)
    queue = [(start, 0, heuristic(start, end))]
    print(start, end)
    print(queue)
    MAX = len(puzzle)
    while queue:
        move, cost, _  = queue.pop(0) # start of q
        if (move[0], move[1]) in visited:
            continue
        print(move in visited)
        visited.add((move[0],move[1]))
        if move == end:
            print("Part 1: ", cost)
            return
        add_move(move ,(move[0] - 1, move[1]), cost + 1, end, queue, MAX, puzzle)
        add_move(move ,(move[0] + 1, move[1]), cost + 1, end, queue, MAX, puzzle)
        add_move(move ,(move[0], move[1] - 1), cost + 1, end, queue, MAX, puzzle)
        add_move(move ,(move[0], move[1] + 1), cost + 1, end, queue, MAX, puzzle)
        queue.sort(key= lambda x: x[1] + x[2])
        print(queue)
    # print(ord('a'))
    print("error")

def part2(input):
    pass


if __name__ == '__main__':
    test = open('./day 12/test.txt', 'r').read()
    input = open('./day 12/input.txt', 'r').read()
    print("Test")
    part1(test)
    part2(test)
    # print("Real puzzle")
    # part1(input)
    # part2(input)
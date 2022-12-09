
def move_head(head, dir):
    if dir == 'R':
        head[1] += 1
    elif dir == 'L':
        head[1] -= 1
    elif dir == 'U':
        head[0] += 1
    elif dir == 'D':
        head[0] -= 1
    return head

def move_tail(head, tail, dir):
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        return tail

    if head[0] != tail[0] and head[1] != tail[1]:
        if dir == 'R':
            move = 0
            if head[0] - tail[0] > 0:
                move = 1
            else:
                move = -1
            tail[0] += move
            tail[1] += 1
        elif dir == 'L':
            move = 0
            if head[0] - tail[0] > 0:
                move = 1
            else:
                move = -1
            tail[0] += move
            tail[1] -= 1
        elif dir == 'U':
            move = 0
            if head[1] - tail[1] > 0:
                move = 1
            else:
                move = -1
            tail[0] += 1
            tail[1] += move
        elif dir == 'D':
            move = 0
            if head[1] - tail[1] > 0:
                move = 1
            else:
                move = -1
            tail[0] -= 1
            tail[1] += move
    else:
        if dir == 'R':
            tail[1] += 1
        elif dir == 'L':
            tail[1] -= 1
        elif dir == 'U':
            tail[0] += 1
        elif dir == 'D':
            tail[0] -= 1

    return tail


def part1(moves):
    N = 1000
    res_grid = [[False for i in range(0, N)]  for _ in range(0, N)]
    head = [0, 0]
    tail = [0, 0]
    res_grid[0][0] = True
    for move in moves.splitlines():
        dir, count = move.split(' ')
        count = int(count)
        for i in range(0, count):
            head = move_head(head, dir)
            tail = move_tail(head, tail, dir)
            res_grid[tail[0]][tail[1]] = True
            # for line in reversed(res_grid):
            #     print(line)
    
    # for line in reversed(res_grid):
    #     print(line)
    res_sum = sum([sum(line) for line in res_grid])
    print(f"Part 1: {res_sum}")



def part2(moves):
    rope = [(0,0) for _ in range(10)]
    visited = set()
    for move in moves.splitlines():
        dir, count = move.split(' ')
        for step in range(int(count)):
            if dir == 'R':
                rope[0] = (rope[0][0], rope[0][1] + 1)
            if dir == 'L':
                rope[0] = (rope[0][0], rope[0][1] - 1)
            if dir == 'U':
                rope[0] = (rope[0][0] + 1, rope[0][1])
            if dir == 'D':
               rope[0] = (rope[0][0] - 1, rope[0][1])
        
            for i in range(1, len(rope)):
                if rope[i - 1][0] - rope[i][0] > 1:
                    if rope[i - 1][1] - rope[i][1] > 1:
                        rope[i] = (rope[i - 1][0] - 1, rope[i - 1][1] - 1)
                    elif rope[i - 1][1] - rope[i][1] < -1:
                        rope[i] = (rope[i - 1][0] - 1, rope[i - 1][1] + 1)
                    else:
                        rope[i] = (rope[i - 1][0] - 1, rope[i - 1][1])
                elif rope[i - 1][0] - rope[i][0] < -1:
                    if rope[i - 1][1] - rope[i][1] > 1:
                        rope[i] = (rope[i - 1][0] + 1, rope[i - 1][1] - 1)
                    elif rope[i - 1][1] - rope[i][1] < -1:
                        rope[i] = (rope[i - 1][0] + 1, rope[i - 1][1] + 1)
                    else:
                        rope[i] = (rope[i - 1][0] + 1, rope[i - 1][1])
                elif rope[i - 1][1] - rope[i][1] > 1:
                    rope[i] = (rope[i - 1][0], rope[i - 1][1] - 1)
                elif rope[i - 1][1] - rope[i][1] < -1:
                    rope[i] = (rope[i - 1][0], rope[i - 1][1] + 1)
            visited.add(rope[-1])
            


    # print(sorted(list(visited)))
    print(f"Part 2: {len(visited)}")




if __name__ == '__main__':
    test = open('./day 9/test.txt', 'r').read()
    test2 = open('./day 9/test2.txt', 'r').read()
    input = open('./day 9/input.txt', 'r').read()
    # directory_test = make_dir(test)
    # directory_input = make_dir(input)
    print("Test")
    part1(test)
    part2(test2)
    print("Real puzzle")
    part1(input)
    part2(input)




def part1(commands):
    cycles_to_value = {0:1,1:1}
    x = 1
    c = 1
    for command in commands.splitlines():
        if command == "noop":
            c += 1
            cycles_to_value[c] = x
        else:
            task, v = command.split(" ")
            c += 2
            cycles_to_value[c - 1] = x
            x += int(v)
            cycles_to_value[c] = x
    res = sum([20 *cycles_to_value[20], 60 *cycles_to_value[60], 100 *cycles_to_value[100], 140 *cycles_to_value[140], 180 *cycles_to_value[180], 220 *cycles_to_value[220] ])
    print(f"Part 1: {res}")
    return cycles_to_value

def part2(commands, m):
    screen = ""
    # c = 1
    pos = 1
    for i in range(0, 6):
        for j in range(1, 41):
            pos = m[i * 40 + j] 
            # print(pos)
            if j == pos or j == pos + 1 or j == pos + 2:
                screen += '#'
            else:
                screen += ' '
        screen += '\n'
    print(screen)


if __name__ == '__main__':
    test = open('./day 10/test.txt', 'r').read()
    # test2 = open('./day 9/test2.txt', 'r').read()
    input = open('./day 10/input.txt', 'r').read()
    print("Test")
    m = part1(test)
    part2(test, m)
    print("Real puzzle")
    m = part1(input)
    part2(input, m)
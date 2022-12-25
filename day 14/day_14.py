import math

def add_rocks(rock1, rock2, rocks):
    x1, y1 = rock1.split(',')
    x2, y2 = rock2.split(',')
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    for i in range(min(x1, x2), max(x1, x2) + 1):
        rocks.add((i, y1))
    
    for i in range(min(y1, y2), max(y1, y2) + 1):
        rocks.add((x1, i)) 

    pass

def print_map(minx, maxx, miny, maxy, rocks):
    print(minx, maxx, miny, maxy)
    puzzle = []
    for y in range(miny, maxy + 1):
        line = ''
        for x in range(minx, maxx + 1):
            # print((x, y))
            if (x, y) in rocks:
                line += '#'
            else:
                line += '.'
        puzzle.append(line)
        print(line)

def drop_sand(minx, maxx, miny, maxy, rocks):
    startx, starty = (500, 0)
    settled = False
    while not settled:
        if (startx, starty + 1) in rocks:
            if (startx - 1, starty + 1) in rocks:
                if (startx + 1, starty + 1) in rocks:
                    rocks.add((startx, starty))
                    settled = True
                    return True
                else:
                    startx += 1
                    starty += 1
            else:
                startx -= 1
                starty += 1
        else:
            starty += 1
        # print_map(minx, maxx, miny, maxy, rocks)

        if starty > maxy:
            settled = True
            return False





def part1(input):
    minx = math.inf
    maxx = -1
    miny = 0
    maxy = -1

    rocks = set()

    for line in input.splitlines():
        rocks_edges = line.split(' -> ')
        last_rock = rocks_edges[0]
        minx = min(minx, int(last_rock.split(',')[0]))
        maxx = max(maxx, int(last_rock.split(',')[0]))
        maxy = max(maxy, int(last_rock.split(',')[1]))
        for rock in rocks_edges[1:]:
            add_rocks(last_rock, rock, rocks)
            last_rock = rock
            minx = min(minx, int(last_rock.split(',')[0]))
            maxx = max(maxx, int(last_rock.split(',')[0]))
            maxy = max(maxy, int(last_rock.split(',')[1]))

    # print(rocks)
    print_map(minx, maxx, miny, maxy, rocks)
    possible = True
    res = -1
    while possible:
        possible = drop_sand(minx, maxx, miny, maxy, rocks)
        res += 1
    print(f"Part 1: {res}")
        



def part2(input):
    minx = math.inf
    maxx = -1
    miny = 0
    maxy = -1

    rocks = set()

    for line in input.splitlines():
        rocks_edges = line.split(' -> ')
        last_rock = rocks_edges[0]
        minx = min(minx, int(last_rock.split(',')[0]))
        maxx = max(maxx, int(last_rock.split(',')[0]))
        maxy = max(maxy, int(last_rock.split(',')[1]))
        for rock in rocks_edges[1:]:
            add_rocks(last_rock, rock, rocks)
            last_rock = rock
            minx = min(minx, int(last_rock.split(',')[0]))
            maxx = max(maxx, int(last_rock.split(',')[0]))
            maxy = max(maxy, int(last_rock.split(',')[1]))

    # add_rocks(f'{minx},{maxy + 2}', f'{maxx},{maxy + 2}', rocks)
    print_map(minx, maxx, miny, maxy, rocks)
    possible = True
    res = 0
    while possible:
        possible = drop_sand2(minx, maxx, miny, maxy, rocks)
        res += 1
        # if res == 91:
        #     break
    print_map(minx, maxx, miny, maxy, rocks)
    print(f"Part 2: {res}")


def drop_sand2(minx, maxx, miny, maxy, rocks):
    startx, starty = (500, 0)
    settled = False
    while not settled:
        if starty == maxy + 1:
            rocks.add((startx, starty))
            settled = True
            return True
        if (startx, starty + 1) in rocks:
            if (startx - 1, starty + 1) in rocks:
                if (startx + 1, starty + 1) in rocks:
                    if startx == 500 and starty == 0:
                        return False
                    rocks.add((startx, starty))
                    settled = True
                    return True
                else:
                    startx += 1
                    starty += 1
            else:
                startx -= 1
                starty += 1
        else:
            starty += 1
    


if __name__ == '__main__':
    test = open('./day 14/test.txt', 'r').read()
    input = open('./day 14/input.txt', 'r').read()
    print("Test")
    part1(test) # 24
    part2(test) # 
    print("Real puzzle")
    part1(input)
    part2(input)
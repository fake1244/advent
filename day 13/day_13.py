
import itertools
import json

def check_pair(p1, p2):
    # print(f'{p1}; {p2}')
    for e1, e2 in zip(p1, p2):
        if isinstance(e1, int) and isinstance(e2, int):
            if e1 > e2:
                return False, False
            if e1 < e2:
                return True, False
            
        elif isinstance(e1, list) and isinstance(e2, int):
            res, equal = check_pair(e1, [e2])
            if equal:
                continue
            return res, False
        elif isinstance(e1, int) and isinstance(e2, list):
            res, equal = check_pair([e1], e2)
            if equal:
                continue
            return res, False
        else:
            res, equal = check_pair(e1, e2)
            if equal:
                continue
            return res, False
    
    if len(p1) < len(p2):
        return True, False
    if len(p1) > len(p2):
        return False, False
    if len(p1) == len(p2):
        return False, True
    
    print("error")


def part1(input):
    res = []
    for i, pair in enumerate(input.split('\n\n')):
        l1, l2 = pair.splitlines()
        l1 = json.loads(l1)
        l2 = json.loads(l2)
        if check_pair(l1, l2)[0]:
            res.append(i + 1)
        # break
    print(f"Part 1: {sum(res)}")

def part2(input):
    packets = []
    for i, pair in enumerate(input.split('\n\n')):
        l1, l2 = pair.splitlines()
        l1 = json.loads(l1)
        l2 = json.loads(l2)
        packets.append(l1)
        packets.append(l2)
    packets.append([[2]])
    packets.append([[6]])

    # sort
    for i in range(len(packets)):
        for j in range(len(packets) - i - 1):
            if not check_pair(packets[j], packets[j + 1])[0]:
                packets[j], packets[j + 1] = packets[j + 1], packets[j] 

    index2 = packets.index([[2]]) + 1
    index6 = packets.index([[6]]) + 1

    print(f'Part 2: {index2 * index6}')

if __name__ == '__main__':
    test = open('./day 13/test.txt', 'r').read()
    input = open('./day 13/input.txt', 'r').read()
    print("Test")
    part1(test) # 13
    part2(test) # 140
    print("Real puzzle")
    part1(input)
    part2(input)
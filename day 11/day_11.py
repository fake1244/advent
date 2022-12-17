# class Monkey:
#     def __init__(self, name, items, operation):
#         self.inspected = 0
#         self.items = items
#         self.operant = operant
#         self.name = name
    
#     def inspect(self):
#         for item in self.items:
#             parts = self.operation.split(' ')
import math

def monkey0(items, monkey_items, part2, lcm):
    for item in items:
        new = item * 5
        if not part2:
            new //= 3
        else:
            new %= lcm
        if new % 11 == 0:
            monkey_items[3].append(new)
        else:
            monkey_items[4].append(new)
    monkey_items[0] = []

def monkey1(items, monkey_items, part2, lcm):
    for item in items:
        new = item * item
        if not part2:
            new //= 3
        else:
            new %= lcm
        if new % 2 == 0:
            monkey_items[6].append(new)
        else:
            monkey_items[7].append(new)
    monkey_items[1] = []
def monkey2(items, monkey_items, part2, lcm):
    for item in items:
        new = item * 7
        if not part2:
            new //= 3
        else:
            new %= lcm
        if new % 5 == 0:
            monkey_items[1].append(new)
        else:
            monkey_items[5].append(new)
    monkey_items[2] = []
def monkey3(items, monkey_items, part2, lcm):
    for item in items:
        new = item + 1
        if not part2:
            new //= 3
        else:
            new %= lcm
        if new % 17 == 0:
            monkey_items[2].append(new)
        else:
            monkey_items[5].append(new)
    monkey_items[3] = []
def monkey4(items, monkey_items, part2, lcm):
    for item in items:
        new = item + 3
        if not part2:
            new //= 3
        else:
            new %= lcm
        if new % 19 == 0:
            monkey_items[2].append(new)
        else:
            monkey_items[3].append(new)
    monkey_items[4] = []
def monkey5(items, monkey_items, part2, lcm):
    for item in items:
        new = item + 5
        if not part2:
            new //= 3
        else:
            new %= lcm
        if new % 7 == 0:
            monkey_items[1].append(new)
        else:
            monkey_items[6].append(new)
    monkey_items[5] = []
def monkey6(items, monkey_items, part2, lcm):
    for item in items:
        new = item + 8
        if not part2:
            new //= 3
        else:
            new %= lcm
        if new % 3 == 0:
            monkey_items[0].append(new)
        else:
            monkey_items[7].append(new)
    monkey_items[6] = []
def monkey7(items, monkey_items, part2, lcm):
    for item in items:
        new = item + 2
        if not part2:
            new //= 3
        else:
            new %= lcm
        if new % 13 == 0:
            monkey_items[4].append(new)
        else:
            monkey_items[0].append(new)
    monkey_items[7] = []


def part1(commands):
    monkey_items = {
        0 : [92, 73, 86, 83, 65, 51, 55, 93],
        1 : [99, 67, 62, 61, 59, 98],
        2 : [81, 89, 56, 61, 99],
        3 : [97, 74, 68],
        4 : [78, 73],
        5 : [50],
        6 : [95, 88, 53, 75],
        7 : [50, 77, 98, 85, 94, 56, 89],
    }
    bussiness = [0 for i in range(8)]
    for j in range(20):
        for i, monkey in enumerate([monkey0,monkey1,monkey2,monkey3,monkey4,monkey5,monkey6,monkey7]):
            bussiness[i] += len(monkey_items[i])
            monkey(monkey_items[i], monkey_items, False, 0)
    bussiness.sort()
    print(f"Part 1: {bussiness[-1] * bussiness[-2]}")

def part2(commands):
    monkey_items = {
        0 : [92, 73, 86, 83, 65, 51, 55, 93],
        1 : [99, 67, 62, 61, 59, 98],
        2 : [81, 89, 56, 61, 99],
        3 : [97, 74, 68],
        4 : [78, 73],
        5 : [50],
        6 : [95, 88, 53, 75],
        7 : [50, 77, 98, 85, 94, 56, 89],
    }
    bussiness = [0 for i in range(8)]
    lcm = math.lcm(11,2,5,17,19,7,3,13)
    for j in range(10_000):
        for i, monkey in enumerate([monkey0,monkey1,monkey2,monkey3,monkey4,monkey5,monkey6,monkey7]):
            bussiness[i] += len(monkey_items[i])
            monkey(monkey_items[i], monkey_items, True, lcm)
            # print(j)
    bussiness.sort()
    print(f"Part 2: {bussiness[-1] * bussiness[-2]}")
    pass


if __name__ == '__main__':
    print("Real puzzle")
    part1(input)
    part2(input)
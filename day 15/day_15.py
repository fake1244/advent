

def part1(input):
    valves = {}
    tunnels = {}

    for line in input.splitlines():
        parts = line.split(" ")
        valve = parts[0]
        flow_rate = int(parts[3].strip(";"))
        valves[valve] = flow_rate
        tunnels[valve] = []
        for v in parts[4:]:
            tunnels[valve].append(v.strip(","))

    start = "AA"
    max_minutes = 30

    pressure = bfs(valves, tunnels, start, max_minutes)
    print(pressure)

    pass

def bfs(valves, tunnels, start, max_minutes):
  queue = [start]
  explored = set()
  pressure = 0
  minutes = 0
  while queue and minutes < max_minutes:
    valve = queue.pop(0)
    explored.add(valve)
    pressure += valves[valve] * (max_minutes - minutes)
    minutes += 1
    for v in tunnels[valve]:
      if v not in explored:
        queue.append(v)
  return pressure




def part2(input):
    pass


if __name__ == '__main__':
    test = open('./day 15/test.txt', 'r').read()
    input = open('./day 15/input.txt', 'r').read()
    print("Test")
    part1(test) # 26 ;y = 10
    # part2(test) # 
    # print("Real puzzle")
    # part1(input)
    # part2(input)
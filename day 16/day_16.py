

def part1(input):
    valves = {}
    tunnels = {}

    for line in input.splitlines():
        parts = line.split(" ")
        
        valve = parts[1]
        flow_rate = int(parts[4].strip(";")[5:])
        valves[valve] = flow_rate
        tunnels[valve] = []
        for v in parts[9:]:
            tunnels[valve].append(v.strip(","))

    start = "AA"
    max_minutes = 30

    pressure = bfs(valves, tunnels, start, max_minutes)
    print(pressure)



def bfs(valves, tunnels, start, max_minutes):
  queue = [(start, 0)]
  explored = set()
  pressure = 0
  while queue:
    valve, time = queue.pop(0)
    if time > max_minutes:
      continue
    explored.add(valve)
    minutes_remaining = max_minutes - time
    pressure += valves[valve] * minutes_remaining
    print(f'{pressure} at min {time}')
    for v in tunnels[valve]:
      if v not in explored:
        queue.append((v, time+2))
  return pressure




def part2(input):
    pass


if __name__ == '__main__':
    test = open('./day 16/test.txt', 'r').read()
    input = open('./day 16/input.txt', 'r').read()
    print("Test")
    part1(test) # 26 ;y = 10
    # part2(test) # 
    # print("Real puzzle")
    # part1(input)
    # part2(input)
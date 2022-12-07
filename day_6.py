f = open("input.txt", 'r').read()

def part1():
  res = 0
  j = 0
  i = 4
  while True:
    window = f[j:i]
    # print(window)
    if len(set(window)) == 14:
      print(i)
      break
    i += 1
    j += 1

def part2():
  res = 0
  j = 0
  i = 14
  while True:
    window = f[j:i]
    # print(window)
    if len(set(window)) == 14:
      print(i)
      break
    i += 1
    j += 1

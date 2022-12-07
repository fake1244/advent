f = open("input.txt", 'r').read()

drawing = {
    1:['Z','T','F','R','W','J','G'],
    2:['G','W','M'],
    3:['J','N','H','G'],
    4:['J','R','C','N','W'],
    5:['W','F','S','B','G','Q','V','M'],
    6:['S','R','T','D','V','W','C'],
    7:['H','B','N','C','D','Z','G','V'],
    8:['S','J','N','M','G','C'],
    9:['G','P','N','W','C','J','D','L']
}


def part1():
  for line in f.split("\n")[10:-1]:
    move = int(line.split(" ")[1])
    col = int(line.split(" ")[3])
    dest = int(line.split(" ")[5])
    for i in range(move, move):
      # print(i)
      crate = drawing[col].pop(-1)
      drawing[dest].append(crate)
    # print(drawing)

  res = ""
  for (_,col) in drawing.items():
    res += col[-1]
  print(res)


def part2():
  for line in f.split("\n")[10:-1]:
    move = int(line.split(" ")[1])
    col = int(line.split(" ")[3])
    dest = int(line.split(" ")[5])
    for i in range(move, 0, -1):
      # print(i)
      crate = drawing[col].pop(0 - i)
      drawing[dest].append(crate)
    # print(drawing)

  res = ""
  for (_,col) in drawing.items():
    res += col[-1]
  print(res)


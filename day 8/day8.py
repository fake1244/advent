import numpy as np
f = open("input.txt", 'r').read()

def check(r, c, m, t):
  tree = m[r, c]

  
  if r == 0 or c == 0 or r == 99 - 1 or c == 99 - 1:
    # print(tree)
    return True

  left = -1
  for col in range(0, c):
    left = max(left, m[r, col])
  right = -1
  for col in range(m[r].size - 1, c, -1):
    right = max(right, m[r, col])
  up = -1
  for row in range(0, r):
    up = max(up, t[c, row])
  down = -1
  for row in range(t[c].size - 1, r, -1):
    down = max(down, t[c, row])
  visible =  tree > left or tree > right or tree > up or tree > down
  return visible


def score(r, c, m, t):
  tree = m[r, c]
  # print(tree)
  total = 1
  left = 0
  for col in range(c - 1, -1, -1):
    left += 1
    if m[r, col] >= tree:
      break
  right = 0
  for col in range(c + 1, m[r].size):
    right += 1
    if m[r, col] >= tree:
      break
  up = 0
  for row in range(r - 1, -1, -1):
    up += 1
    if m[row, c] >= tree:
      break
  down = 0
  for row in range(r + 1, t[c].size):
    down += 1
    if m[row, c] >= tree:
      break
  total = left * right * up * down
  # print(r, c, left, right, up, down)
  return total

matrix = []

for line in f.splitlines():
  row = []
  for c in line:
    row.append(int(c))
  matrix.append(row)

np_matrix = np.matrix(matrix)

np_transposed = np_matrix.transpose()

# print(np_matrix[0,0] < np_matrix[0,4])
row_end, col_end = np_matrix.shape

part1 = 0
part2 = 0
for r in range(0, row_end):
  for c in range(0, col_end):
    if check(r, c, np_matrix, np_transposed):
      part1 += 1
    score_tree = score(r,c,np_matrix, np_transposed)
    part2 = max(part2, score_tree)
    # print(score_tree)

# Part 1:  1851
# Part 2:  574080



print(f"Part1: {part1}")
print(f"Part2: {part2}")

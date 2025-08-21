def retrace_steps(dst, parents):
  if dst not in parents:
    return None

  path = []
  curr = dst
  while curr:
    path.append(curr)
    curr = parents[curr]
  path.reverse()
  return path


def is_valid(loc, grid):
  r, c = loc
  return r >= 0 and c >= 0 and \
      r < len(grid) and c < len(grid[0])


def get_neighbors(grid, loc):
  r, c = loc
  val = grid[r][c]
  neighbors = [
    n for n in [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
    if is_valid(n, grid)
  ]
  return [n for n in neighbors if grid[n[0]][n[1]] > val]


def longest_path_from_loc(grid, loc):
  length = 1

  for n in get_neighbors(grid, loc):
    length = max(length, 1 + longest_path_from_loc(grid, n))

  return length


def longest_path(grid):
  length = 1

  for r in range(len(grid)):
    for c in range(len(grid[0])):
      longest_from_here = longest_path_from_loc(grid, (r, c))
      length = max(length, longest_from_here)

  return length


print('\nLongest Increasing Path\n')

grid = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]

print(longest_path(grid))

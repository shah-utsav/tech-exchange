from collections import deque

# def is_valid(grid, loc):
#   r, c = loc
#   return r >= 0 and c >= 0 and \
#       r < len(grid) and c < len(grid[0])

# def get_neighbors(grid, loc):
#   r, c = loc
#   val = grid[r][c]

#   candidates = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
#   return [
#     n for n in candidates
#     if is_valid(grid, (n[0], n[1])) and grid[n[0]][n[1]] >= val
#   ]


def water_flow(grid):

  def inbounds(grid, r, c):
    return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r])

  def dfs(grid, stack):
    explored = set()
    while stack:
      v = stack.pop()
      if v not in explored:
        explored.add(v)
        r, c = v
        for dr, dc in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
          new_r = r + dr
          new_c = c + dc
          if inbounds(grid, new_r, new_c) and grid[new_r][new_c] >= grid[r][c]:
            stack.append((new_r, new_c))
    return explored

  atlantic_stack, pacific_stack = deque(), deque()

  last_r, last_c = len(grid) - 1, len(grid[0]) - 1
  for r in range(len(grid)):
    pacific_stack.append((r, 0))
    atlantic_stack.append((r, last_c))
  for c in range(len(grid[0])):
    pacific_stack.append((0, c))
    atlantic_stack.append((last_r, c))
  print('pacific stack is', pacific_stack)
  print('atlantic ocean is', atlantic_stack)
  atlantic = dfs(grid, atlantic_stack)
  # print(atlantic)
  pacific = dfs(grid, pacific_stack)

  return list(atlantic & pacific)


print('\nWater Flow\n')

g = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5],
     [5, 1, 1, 2, 4]]

print(water_flow(g))

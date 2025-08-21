from collections import deque


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


def is_valid(loc, maze):
  r, c = loc
  return r >= 0 and c >= 0 and \
      r < len(maze) and c < len(maze[0]) and \
      maze[r][c] == 0


def get_neighbors_1(loc, maze):
  r, c = loc
  neighbors = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
  return [neighbor for neighbor in neighbors if is_valid(neighbor, maze)]


def get_neighbors_2(loc, maze):
  neighbors = []

  # There's probably a way to handle this in a loop! Sue me.

  # go right
  curr, prev = loc, None
  while is_valid(curr, maze):
    prev = curr
    curr = (curr[0], curr[1] + 1)
  neighbors.append(prev)

  # go left
  curr, prev = loc, None
  while is_valid(curr, maze):
    prev = curr
    curr = (curr[0], curr[1] - 1)
  neighbors.append(prev)

  # go down
  curr, prev = loc, None
  while is_valid(curr, maze):
    prev = curr
    curr = (curr[0] + 1, curr[1])
  neighbors.append(prev)

  # go up
  curr, prev = loc, None
  while is_valid(curr, maze):
    prev = curr
    curr = (curr[0] - 1, curr[1])
  neighbors.append(prev)

  return neighbors


def solve_maze(maze, start, destination):
  q = deque()
  parents = dict()

  q.append(start)
  parents[start] = None

  while q:
    v = q.popleft()
    if v == destination:
      return retrace_steps(v, parents)

    for n in get_neighbors_2(v, maze):
      if n not in parents:
        parents[n] = v
        q.append(n)
   
  return []


print('\nBall Maze\n')

maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]

print(solve_maze(maze, (0, 4), (4, 4)))

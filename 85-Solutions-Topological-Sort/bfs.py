from collections import defaultdict
from collections import deque


def invert(g):
  invert = defaultdict(list)
  for node, neighbors in g.items():
    for neighbor in neighbors:
      invert[neighbor].append(node)
  return invert


def indegree(g):
  id = defaultdict(int)
  for v in g:
    for n in g[v]:
      id[n] += 1
  return id


def topological_sort(g):
  solution = []
  q = deque()
  indegrees = indegree(g)

  for v in indegrees:
    if indegrees[v] == 0:
      q.append(v)

  while q:
    v = q.popleft()
    solution.append(v)

    for n in g[v]:
      indegrees[n] -= 1
      if indegrees[n] == 0:
        q.append(n)

  for v in indegrees:
    if indegrees[v] != 0:
      raise Exception('Cycle found!')

  return solution
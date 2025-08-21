from collections import defaultdict
from collections import deque


def invert(g):
  invert = defaultdict(list)
  for node, neighbors in g.items():
    if node not in invert:
      invert[node] = []
    for neighbor in neighbors:
      invert[neighbor].append(node)
  return invert


def has_cycle(g):
  status = {}
  for v in g:
    status[v] = 'NEW'
  for v in g:
    if status[v] == 'NEW':
      if has_cycle_dfs(v, g, status):
        return True
  return False


# The recursive helper method for has_cycle
def has_cycle_dfs(v, g, status):
  status[v] = 'PRE'
  for w in g[v]:
    if status[w] == 'PRE':
      return True
    if status[w] == 'NEW':
      if has_cycle_dfs(w, g, status):
        return True
  status[v] = 'POST'
  return False


def topological_sort(g):
  status = {}
  result = deque()
  for v in g:
    status[v] = 'NEW'
  for v in g:
    if status[v] == 'NEW':
      topological_sort_helper(v, g, status, result)
  return list(result)


def topological_sort_helper(v, g, status, result):
  status[v] = 'PRE'
  for w in g[v]:
    if status[w] == 'PRE':
      raise Exception('Cycle found!')
    if status[w] == 'NEW':
      topological_sort_helper(w, g, status, result)
  status[v] = 'POST'
  result.appendleft(v)


prerequisites = {
  "Economics": ["Algebra"],
  "Calculus": ["Algebra"],
  "Algebra": [],
  "Chemistry": ["Algebra"],
  "Biology": [],
  "Differential Equations": ["Calculus"],
  "Physics": ["Algebra"],
  "Electronics": ["Physics", "Computer Science"],
  "Quantum Physics": ["Differential Equations", "Physics"],
  "Computer Science": [],
  "Bioinformatics": ["Computer Science", "Biology"]
}

ig = invert(prerequisites)
print(ig)
print(topological_sort(ig))

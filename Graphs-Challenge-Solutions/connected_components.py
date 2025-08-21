from collections import deque


def dfs_iterative(graph, src):
  discovered = set()
  s = deque()
  s.append(src)

  while s:
    v = s.pop()
    discovered.add(v)
    for w in graph[v]:
      if w not in discovered:
        s.append(w)
  return discovered


# Takes an undirected graph and returns a list of sets.
# Each set is a connected component
def connected_components(graph):
  components = []
  explored = set()
  for v in graph:
    if v not in explored:
      component = dfs_iterative(graph, v)
      components.append(component)
      explored.update(component)
  return components


print('\nConnected Components\n')

graph = {0: [2], 1: [4], 2: [0, 3, 5], 3: [2, 5], 4: [1], 5: [2, 3]}

print(connected_components(graph))

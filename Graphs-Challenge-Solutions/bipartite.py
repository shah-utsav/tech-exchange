from collections import deque


def is_bipartite(g):
  q = deque()
  a, b = set(), set()

  start = list(g.keys())[0]

  q.append(start)
  a.add(start)

  while q:
    v = q.popleft()

    for neighbor in g[v]:
      if v in a and neighbor in a:
        return False
      elif v in b and neighbor in b:
        return False
      elif neighbor in a or neighbor in b:
        continue
      else:
        q.append(neighbor)
        if v in a:
          b.add(neighbor)
        else:
          a.add(neighbor)

  return True


print('\nBipartite\n')

# This graph is bipartite, but you'll also need to test your code on a non-bipartite graph. You can make this graph non-bipartite by, for example, adding an edge between 3 and 6, or 2 and 9. Or, better yet, come up with your own examples!
g = {
  1: [2],
  2: [1, 3, 8],
  3: [2, 4],
  4: [3, 6],
  5: [7, 9],
  6: [4],
  7: [5],
  8: [2, 9],
  9: [5, 8]
}

print(is_bipartite(g))

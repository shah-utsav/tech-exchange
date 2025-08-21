from collections import deque


def is_valid(node):
  chicken_0, fox_0 = node[0], node[1]
  chicken_1, fox_1 = 3 - node[0], 3 - node[1]
  return (chicken_0 >= fox_0 or chicken_0 == 0) and (chicken_1 >= fox_1 or chicken_1 == 0) and \
      chicken_0 >= 0 and chicken_1 >= 0 and fox_0 >= 0 and fox_1 >= 0


def get_neighbors(node):
  neighbors = []
  chicken_0, fox_0, boat = node
  if boat == 0:
    neighbors.append((chicken_0 - 2, fox_0, 1))
    neighbors.append((chicken_0 - 1, fox_0, 1))
    neighbors.append((chicken_0 - 1, fox_0 - 1, 1))
    neighbors.append((chicken_0, fox_0 - 1, 1))
    neighbors.append((chicken_0, fox_0 - 2, 1))
  else:
    neighbors.append((chicken_0 + 2, fox_0, 0))
    neighbors.append((chicken_0 + 1, fox_0, 0))
    neighbors.append((chicken_0 + 1, fox_0 + 1, 0))
    neighbors.append((chicken_0, fox_0 + 1, 0))
    neighbors.append((chicken_0, fox_0 + 2, 0))
  return [neighbor for neighbor in neighbors if is_valid(neighbor)]


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


def chicken_fox():
  q = deque()
  parent = {}

  src, dst = (3, 3, 0), (0, 0, 1)
  parent[src] = None
  q.append(src)
  while q:
    v = q.popleft()
    if v == dst:
      return retrace_steps(dst, parent)
      break
    for w in get_neighbors(v):
      if w not in parent:
        parent[w] = v
        q.append(w)

  return retrace_steps(dst, parent)


print('\nChicken Fox\n')

print(chicken_fox())

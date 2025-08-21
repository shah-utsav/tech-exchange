from collections import defaultdict
from collections import deque


def build_graph(flights):
  g = defaultdict(list)
  for src, dst in flights:
    g[src].append(dst)
  return g


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


def shortest_path(graph, src, dst):
  q = deque()
  parent = {}
  parent[src] = None
  q.append(src)
  while q:
    v = q.popleft()
    if v == dst:
      break
    for w in graph[v]:
      if w not in parent:
        parent[w] = v
        q.append(w)

  return retrace_steps(dst, parent)


def ideal_flight_path(flights, home, vacation):
  g = build_graph(flights)

  return shortest_path(g, home, vacation)


print('\nFlight Itinerary\n')

flights = [('Detroit', 'Seattle'), ('Seattle', 'Portland'),
           ('Seattle', 'Vancouver'), ('Portland', 'Los Angeles'),
           ('Los Angeles', 'Los Vegas'), ('Los Angeles', 'San Francisco'),
           ('Vancouver', 'Las Vegas'), ('Vancouver', 'Toronto')]

print(ideal_flight_path(flights, 'Detroit', 'Las Vegas'))

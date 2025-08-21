from collections import defaultdict
from collections import deque


def get_actor_movie_pairs():
  file = open("files/imdb-top250.txt", 'r')
  contents = file.readlines()
  file.close()

  actor_movie_pairs = []
  for line in contents:
    split = line.split('|')
    actor_movie_pairs.append((split[0], split[1].strip()))

  return actor_movie_pairs


def retrace_steps(dst, parents):
  if dst not in parents:
    return None

  path = []
  curr = dst
  while True:
    path.append(curr)
    if parents[curr][0] == None:
      break

    path.append(parents[curr][1])
    curr = parents[curr][0]
  path.reverse()
  return path


def shortest_path(graph, src, dst):
  q = deque()
  parent = {}

  parent[src] = (None, None)
  q.append(src)

  while q:
    current_actor = q.popleft()
    if current_actor == dst:
      return retrace_steps(dst, parent)
    for w in graph[current_actor]:
      neighbor_actor, movie = w
      if neighbor_actor not in parent:
        parent[neighbor_actor] = (current_actor, movie)
        q.append(neighbor_actor)

  return []


def bacon_game(actor_1, actor_2):
  actor_movie_pairs = get_actor_movie_pairs()

  movies_to_actors = defaultdict(list)
  for actor, movie in actor_movie_pairs:
    movies_to_actors[movie].append(actor)

  g = defaultdict(list)
  for movie in movies_to_actors:
    actors = movies_to_actors[movie]
    for i in range(len(actors)):
      for j in range(i + 1, len(actors)):
        a, b = actors[i], actors[j]
        g[a].append((b, movie))
        g[b].append((a, movie))

  return shortest_path(g, actor_1, actor_2)


print('\nBacon Game\n')

print(bacon_game('Samuel L. Jackson', 'Meryl Streep'))

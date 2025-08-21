def get_actor_movie_pairs():
  file = open("files/imdb-small.txt", 'r')
  contents = file.readlines()
  file.close()

  actor_movie_pairs = []
  for line in contents:
    split = line.split('|')
    actor_movie_pairs.append((split[0], split[1].strip()))

  return actor_movie_pairs


def bacon_game(actor_1, actor_2):
  actor_movie_pairs = get_actor_movie_pairs()

  pass


print('\nBacon Game\n')

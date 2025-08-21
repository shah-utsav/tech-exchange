# Takes an undirected graph and returns a list of sets.
# Each set is a connected component
def connected_components(graph):
  components = []

  # YOUR CODE HERE
  # feel free to copy an old DFS function if you have one

  return components


print('\nConnected Components\n')

graph = {0: [2], 1: [4], 2: [0, 3, 5], 3: [2, 5], 4: [1], 5: [2, 3]}

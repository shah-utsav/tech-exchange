def is_bipartite(g):
  pass


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

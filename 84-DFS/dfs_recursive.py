from collections import deque


def dfs_recursive(graph, src, dst):
  pass


def dfs_helper(graph, src, dst, discovered):
  pass


print('DFS Implementation - Recursive\n')

graph = {
  'A': ['B'],
  'B': ['C'],
  'C': ['E'],
  'D': ['B'],
  'E': ['D', 'F'],
  'F': []
}

assert dfs_recursive(graph, 'A', 'E') == True
assert dfs_recursive(graph, 'E', 'A') == False

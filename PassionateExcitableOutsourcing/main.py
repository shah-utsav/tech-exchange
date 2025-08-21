'''Write a function that computes the length of the longest path of consecutive integers in a tree. 

2.right = 3

  1
 / \
4   3			Output: 1

  1
 / \
2   3			Output: 2


  1		- 1
   \
    3		- 1
     \
      4	- 2	Output: 2

Output: 2  '''

from TreeNode import *

# return max(curr_length,left_child,right_child)


#
def longest_consecutive_path(root):

  def helper(root, curr_length, root_value):
    if not root:
      return
    if root.val - 1 == root_value:
      curr_length += 1
    else:
      curr_length = 1
    nonlocal longest_path
    longest_path = max(longest_path, curr_length)  # 2
    helper(root.left, curr_length, root.val)
    helper(root.right, curr_length, root.val)

  longest_path = 0
  helper(root, 0, root.val)
  return longest_path


root = root_from_list([
  1,
  None,
  3,
  None,
  None,
  None,
  4,
  None,
  None,
])
pretty_print(root)
print(longest_consecutive_path(root))

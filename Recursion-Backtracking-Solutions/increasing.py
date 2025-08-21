def longest_increasing_subsequence(nums):

  def helper(nums, current):
    # BASE CASE
    if not nums:
      return current

    # RECURSIVE CASE
    # include case
    cur_num = nums[0]
    include = []
    if not current or cur_num > current[-1]:
      include = helper(nums[1:], current + [cur_num])

    # don't include
    dont_include = helper(nums[1:], current)

    if len(dont_include) > len(include):
      return dont_include
    return include

  return helper(nums, [])
print(longest_increasing_subsequence([6, 37, 2, 4, 18, 7]))
nums = [10,9,2,5,3,7,101,18]
print(longest_increasing_subsequence(nums))
def sublist_sum(nums, target):

  def helper(nums, target, lst_so_far):
    # [14, 9], 36, [18, 6, 12]
    if sum(lst_so_far) == target:
      return lst_so_far
    if not nums:
      return []

    # nums = [12, 14, 9]
    # target = 36
    # lst_so_far = [18, 6]
    
    dont_take = helper(nums[1:], target, lst_so_far)
    take = helper(nums[1:], target, lst_so_far + [nums[0]])

    if dont_take:
      return dont_take
    return take

  seed = []
  result = helper(nums, target, seed)
  return result


# Here's how to do it with an i index, not copying/slicing
def sublist_sum_2(nums, target):

  def helper(nums, target, lst_so_far, i):
    if sum(lst_so_far) == target:
      return lst_so_far
    if i == len(nums):
      return []

    dont_take = helper(nums, target, lst_so_far, i + 1)
    take = helper(nums, target, lst_so_far + [nums[i]], i + 1)

    if dont_take:
      return dont_take
    return take

  seed = []
  result = helper(nums, target, seed, 0)
  return result

# Here's how to do it with appending/popping
def sublist_sum_3(nums, target):

  def helper(nums, target, lst_so_far, i):
    if sum(lst_so_far) == target:
      return lst_so_far
    if i == len(nums):
      return []

    dont_take = helper(nums, target, lst_so_far, i + 1)
    if dont_take:
      return dont_take

    lst_so_far.append(nums[i])
    take = helper(nums, target, lst_so_far, i + 1)
    if take:
      return take
    lst_so_far.pop()

    if dont_take:
      return dont_take
    return take

  seed = []
  result = helper(nums, target, seed, 0)
  return result

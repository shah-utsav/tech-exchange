def cheat_codes(n):

  def helper(n, code_so_far):
    if len(code_so_far) == n:
      print(code_so_far)
      return

    if not code_so_far or code_so_far[-1] != 'L':
      helper(n, code_so_far + 'L')
    if len(code_so_far) <= 1 or code_so_far[-2:] != 'RR':
      helper(n, code_so_far + 'R')

  helper(n, '')
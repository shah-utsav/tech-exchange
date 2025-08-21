def hacker(n):
  def hacker_helper(n, s):
    if len(s) == n:
      print(s)
      return

    chars = '01234abc'
    for c in chars:
      hacker_helper(n, s + c)

  hacker_helper(n, "")
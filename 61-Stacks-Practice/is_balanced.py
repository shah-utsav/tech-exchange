from collections import deque
''''{{([][])}()}
'''


def is_balanced(s):
  stack = deque()
  brackets = {'(': ')', '{': '}', '[': ']', '<': '>'}
  print(stack)
  for paren in s:
    print(stack)
    if paren in brackets:  # { ,
      stack.append(paren)
    else:
      if stack:
        brack = stack.pop()
        if paren != brackets[brack]:
          return False

  if stack:
    return False
  else:
    return True


s = '{{([][])}(}'
print(is_balanced(s))

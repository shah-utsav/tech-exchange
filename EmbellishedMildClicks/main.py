codes = {
  "1": [""],
  "2": ["a", "b", "c"],
  "3": ["d", "e", "f"],
  "4": ["g", "h", "i"],
  "5": ["j", "k", "l"],
  "6": ["m", "n", "o"],
  "7": ["p", "q", "r", "s"],
  "8": ["t", "u", "v"],
  "9": ["w", "x", "y", "z"],
  "0": [""],
}

# number -> 7 digits
# return a list of words
# 2345678
def find_words(number):
  # number is valid
  str_number = str(number)
  if (len(str_number) != 7):
    return []

  for chr in str_number:
    if chr not in "0123456789":
      return []

  find_word_helper(str_number)



# 2345678
# a, d 
# a, e
# a, f
# b
# c
def find_word_helper(number):
  # basecase
  if len(number) == 1:
    return codes[number]

  #recursion
  result = []

  # ["a", "b", "c"]
  first_digit_list = codes[number[0]]

  for partial_result in find_word_helper(number[1:]):
    for char in first_digit_list:
      result.append(char + partial_result)

  return result
  

# special characters? --> only numbers with alphabetical values
# large string or number? --> integer --> 1111111 (7 digits)
# invalid/ empty input? -> return []
# not: 123-456-8898
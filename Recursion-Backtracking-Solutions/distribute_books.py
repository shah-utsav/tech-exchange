def distribute_books(books, k):

  def helper(books, pages_per_student, goal_per_student, i):

    goals = 0
    for student in range(len(pages_per_student)):
      # If any student has read too much, False
      if pages_per_student[student] > goal_per_student:
        return False
      # Count the number of students who have read the perfect amount
      elif pages_per_student[student] == goal_per_student:
        goals += 1

    # If all students have read the perfect amount, True
    if goals == len(pages_per_student):
      return True

    # If no more books, False
    if i == len(books):
      return False

    # Recurse with each student trying to read book i
    for student in range(len(pages_per_student)):
      # student tries to read book i
      pages_copy = pages_per_student[:]
      pages_copy[student] += books[i]

      if (helper(books, pages_copy, goal_per_student, i + 1)):
        return True

    return False

  # each student must read an equal number of pages (total / k)
  total_pages = sum(books)
  goal_per_student = total_pages / k

  # represent pages read by students as elements in a k-length list
  # each student starts by having read 0 pages
  pages_per_student = [0] * k
  return helper(books, pages_per_student, goal_per_student, 0)

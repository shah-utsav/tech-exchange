# Instructions

## Hacker
You need to deactivate the doomsday machine! The combination to deactivate it has `n` characters in it, made up of the digits 0-4 and letters a-c (they can repeat). Print all possible passwords of length `n`.

For example, if `n = 3`, you should print  `04a` and `3bc` and a bunch more.

## Sublist sum to target
You are given a list of non-negative integers. Determine if there is a sub-list (not necessarily consecutive) that sum to a given value.

```python
sublist_sum([6, 37, 2, 4, 18, 7], 15) -> True
```

Explanation: Because sum of [6, 2, 7] = 15

```python
sublist_sum([6, 37, 2, 4, 18, 7], 21) -> False
```

Explanation: No sublist sums to 21

```python
sublist_sum([5, 3, 2, 3], 11) -> True
```

Explanation: Because sum of [5, 3, 3] = 11

## Sublist sum to target extension

If you finish the above implementation of sublist_sum, instead of returning True, return a list of the numbers that added up to the target. Instead of returning False, return an empty list.

## Cheat Codes

Write a function cheat_codes that prints all possible strings of length `n` made up of only the characters L and R. This is just a simpler version of the hacker problem, *but* when you're done, try to extend it:
- What if you can't have two L's in a row?
- What if you can't have three R's in a row?

Try to make your recursive calls in a way that doesn't wait until the full length-n string has been created to determine if it's valid or not.

## Longest Increasing Subsequence

Given a list `nums`, return a list of the longest increasing subsequence found in the list. For example:

```
[6, 37, 2, 4, 18, 7] -> [2, 4, 7]
```

This is because the numbers 2, 4, and 7 are increasing and appear in that order in the list (though not necessarily immediately consecutively). Other increasing subsequences present in the list are [6, 37], [6, 18], [7], and so on.

## Distributing Books
Your group, made up of `k` students, has to read all of the books in the list `books`, where each element `books[i]` is a positive integer representing the number of pages in book `i` (don't worry, this is purely hypothetical).

You want to distribute the books fairly among students in your group, so that no one person has to read too much. You decide that it's only fair if every student reads exactly the same number of pages.

A book can't be split up among multiple students, and each book must be read - each element of `books` needs to be assigned to exactly one student.

Return True if it is possible to distribte the books evenly, false if not.

Examples:

```[8,15,11,20,8], k = 2 -> True```

One student reads 8 + 15 + 8 = 31 and the other reads 11 + 20 = 31.

```[6,1,3,2,2,4,1,2], k = 3 -> True```

The students read [6, 1], [3, 2, 2], and [4, 1, 2] pages each in the fairest distribution.

**Hint:** Before you even start recursing, you can figure out how many pages each student needs to read. You know how many pages there are total, and how many students need to take their equal share.
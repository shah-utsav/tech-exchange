# Instructions

## Balanced Parentheses
Write a function `balanced` that takes a sequence of parentheses and returns `True` if they are balanced; `False`, otherwise. Remember that a string of parentheses is balanced or *well-formed* if each open paren is closed before each open paren that comes before it.

You may have solved this problem with recursion way back in unit 3, but you won't need it this time!

Examples:
```python
'(()(()))()' → True
'(()()' → False
')(' → False
```

## Extension
Can you make your program handle other types of paired characters, like [], {}, and <> without duplicating a bunch of logic?

For example, these are balanced:
```
'{{([][])}()}'
'[[{{(())}}]]'
'[][][](){}'
```

but these are not:
```
'([)]'
'((()]))'
'[{()]'

```

## Extension 2

What about "" and '' in addition to the previous? These ones aren't allowed to nest, and the openers are the same as the matching closers!

**Note**: In order to type a single quote character inside a String defined by single quotes, you can 'escape' it with the \ character. To use a double quote character, you don't need to escape it. Like this:

```python
single_quote = '\''
double_quote = '"'
```

Example of a balanced String (note that the first and last single quotes are **defining** the String, not part of the String):
```
s = '((\'["{}"]\'))'
```

Example of an unbalanced String (note that the first and last single quotes are **defining** the String, not part of the String):

```
s = '(")"'
```
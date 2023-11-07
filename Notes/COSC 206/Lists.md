A list stores a sequence of values.
# Operators
```python
# + operator
>>> [1, 2, 3] + [4, 5, 6]
[1, 2, 3, 4, 5, 6]

# * operator
>>> [1, 2, 3] * 2
[1, 2, 3, 1, 2, 3]

# in/not in operator
>>> 'one' in ['one', 'two', 'three']
True

# length function
>>> len(['one', 'two', 'three'])
3

# sum, add up the integers in a list
>>> sum(1, 2, 3)
6
```
# Methods
## Adding Items
```python
# append method, add a value to the end of the list
[1, 2, 3].append(4)
>>> [1, 2, 3, 4]

# extend, similar to append, but works with multiple values
[1, 2, 3].extend([4, 5, 6])
>>> [1, 2, 3, 4, 5, 6]

# insert method, insert an item at a specified index
[1, 2, 3].insert(3, 4)
>>> [1, 2, 3, 4]

# sort, sorts items in a list
[2, 1, 3].sort()
>>> [1, 2, 3]
# also can be put in reverse
[2, 1, 3].sort(reverse=True)
>>> [3, 2, 1]
```
## Removing Items
```python
# pop, removes value at an index and returns it, if no index is given, it removes the rightmost one
[1, 2, 3].pop()
>>> 3
[1, 2, 3].pop(0)
>>> 1

# remove, remove an item by it's value rather than index. Does not return the value
[1, 2, 3].remove(2)
>>> [1, 3]
```
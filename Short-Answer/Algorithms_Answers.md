#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

O(n) because it loops as many times as n.

n a

- -
  1 0
  1

2 0
4
8

3 0
9
18
27

b)

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

O(n^2) because of the nested loop. The outer loop is O(n) and the inner loop seems close to O(n) => O(n^2)

Calculating the sum is O(1), which is insignificant, compared to O(n^2).

c)

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

O(n) because it is called recursively n times before reaching the base case. Another way of

calculating the complexity with recursion is

complexity = length of tree \* number of leaf nodes.

In this case, n \* 1 = n

## Exercise II

Problem given:

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

Solution:

n = number of stories in building

f - 1 = the highest floor of the building in which an egg thrown doesn't break

n[0:f] --> unbroken eggs
n[f:] --> broken eggs

This problem reminds me of binary search, so I would approach it in a similar way to minimize the amount of tests

(eggs dropped and thus, egg broken).

```

# Initialize a pointer that begins as the bottom floor -> low

# Initialize a pointer that begins as the top floor -> high

# Initialize a variable to hold the current winning floor. -> winner

# Set the base case that when low > high, return winner.

# While low < high:

# Drop an egg at the floor half-way between low and high, to see if it breaks.

# If it doesn't break, set the winner to the value of pointer.

    # Move low to be half-way between current floor and the top floor.

    # Drop an egg from the new floor that is half-way between low and high.

    # If it doesn't break, set the winner to be this floor. And move the low to be half-way
    between current floor and the top floor. Continue.

# If the egg did break, follow similar steps to above, except move the high to be the current floor.


```

The runtime complexity would be O(log n), because the search is divided in half each loop (similar to binary search).

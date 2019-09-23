# Week 3 Exercises

Week 3: Structured Types / Finger Exercises

## Exercise: odd tuples

Write a procedure called `oddTuples`, which takes a tuple as input, and returns a new tuple as output, where every other element of the input tuple is copied, starting with the first one. So if test is the tuple `('I', 'am', 'a', 'test', 'tuple')`, then evaluating `oddTuples` on this input would return the tuple `('I', 'a', 'tuple')`.

``` python
def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''

```

---

**My solution:** [odd_tuples.py](odd_tuples.py)

## Exercise: apply to each

Here is the code for a function `applyToEach`:

``` python
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
```

Assume that

``` markdown
testList = [1, -4, 8, -9]
```

For each of the following questions (which you may assume is evaluated independently of the previous questions, so that testList has the value indicated above), provide an expression using `applyToEach`, so that after evaluation `testList` has the indicated value. You may need to write a simple procedure in each question to help with this process.

Example Question:

``` markdown
>>> print(testList)
[5, -20, 40, -45]
```

Solution to Example Question:

``` python
def timesFive(a):
    return a * 5

applyToEach(testList, timesFive)
```

---

### apply to each 1

``` markdown
>>> print(testList)
[1, 4, 8, 9]
```

**My solution:**
[apply_to_each_1.py](apply_to_each_1.py)

---

### apply to each 2

``` markdown
>>> print(testList)
[2, -3, 9, -8]
```

**My solution:**
[apply_to_each_2.py](apply_to_each_2.py)

---

### apply to each 3

``` markdown
>>> print(testList)
[1, 16, 64, 81]
```

**My solution:**
[apply_to_each_3.py](apply_to_each_3.py)

---

## Exercise: how many

Consider the following sequence of expressions:

``` markdown
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
```

We want to write some simple procedures that work on dictionaries to return information.

First, write a procedure, called `how_many`, which returns the sum of the number of values associated with a dictionary. For example:

``` markdown
>>> print(how_many(animals))
6
```

``` python
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your code here
```

---

**My solution:** [how_many.py](how_many.py)

## Exercise: biggest

Consider the following sequence of expressions:

``` markdown
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
```

We want to write some simple procedures that work on dictionaries to return information.

This time, write a procedure, called `biggest`, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.

Example usage:

``` markdown
>>> biggest(animals)
'd'
```

If there are no values in the dictionary, `biggest` should return `None`.

``` python
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your code here
```

---

**My solution:** [biggest.py](biggest.py)

# Week 2 Exercises

Week 2: Simple Programs / Finger Exercises

## Exercise: guess my number

In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

Here is a transcript of an example session:

``` markdown
Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 87?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 81?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 84?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 82?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 83?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 83
```

**Note:** your program should use `input` to obtain the user's input! Be sure to handle the case when the user's input is not one of `h`, `l`, or `c`.

When the user enters something invalid, you should print out a message to the user explaining you did not understand their input. Then, you should re-ask the question, and prompt again for input. For example:

``` markdown
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. y
Sorry, I did not understand your input.
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
```

---

**My solution:** [guess_my_number.py](guess_my_number.py)

## Exercise: square

Write a Python function, `square`, that takes in one number and returns the square of that number.

This function takes in one number and returns one number.

``` python
def square(x):
    '''
    x: int or float.
    '''
    # Your code here

```

---

**My solution:** [square.py](square.py)

## Exercise: eval quadratic

Write a Python function, `evalQuadratic(a, b, c, x)`, that returns the value of the quadratic ![$a\cdot x^2 + b\cdot x + c$](https://render.githubusercontent.com/render/math?math=a%5Ccdot%20x%5E2%20%2B%20b%5Ccdot%20x%20%2B%20c&mode=inline).

This function takes in four numbers and returns a single number.

``` python
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # Your code here

```

---

**My solution:** [eval_quadratic.py](eval_quadratic.py)

## Exercise: fourth power

Write a Python function, `fourthPower`, that takes in one number and returns that value raised to the fourth power.

You should use the `square` procedure that you defined in an earlier exercise (you don't need to redefine `square` in this box; when you call `square`, the grader will use our definition).

This function takes in one number and returns one number.

``` python
def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here

```

---

**My solution:** [fourth_power.py](fourth_power.py)

## Exercise: odd

Write a Python function, `odd`, that takes in one number and returns `True` when the number is odd and `False` otherwise.

You should use the `%` (mod) operator, not `if`.

This function takes in one number and returns a boolean.

``` python
def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    # Your code here

```

---

**My solution:** [odd.py](odd.py)

## Exercise: power iter

Write an iterative function `iterPower(base, exp)` that calculates the exponential  ![equation](https://latex.codecogs.com/svg.latex?\inline&space;\mathrm{base}^{\mathrm{exp}})  by simply using successive multiplication. For example, `iterPower(base, exp)` should compute  ![equation](https://latex.codecogs.com/svg.latex?\inline&space;\mathrm{base}^{\mathrm{exp}}), by multiplying `base` times itself `exp` times. Write such a function below.

This function should take in two values - `base` can be a float or an integer; `exp` will be an integer  ≥ 0 . It should return one numerical value. Your code must be iterative - use of the `**` operator is not allowed.

``` python
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here

```

---

**My solution:** [power_iter.py](power_iter.py)

## Exercise: power recur

In Problem 1, we computed an exponential by iteratively executing successive multiplications. We can use the same idea, but in a recursive function.

Write a function `recurPower(base, exp)` which computes  [equation](https://latex.codecogs.com/svg.latex?\inline&space;\mathrm{base}^{\mathrm{exp}})  by recursively calling itself to solve a smaller version of the same problem, and then multiplying the result by `base` to solve the initial problem.

This function should take in two values - `base` can be a float or an integer; `exp` will be an integer  ≥ 0 . It should return one numerical value. Your code must be recursive - use of the `**` operator or looping constructs is not allowed.

``` python
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here

```

---

**My solution:** [power_recur.py](power_recur.py)

## Exercise: gcd iter

The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

- gcd(2, 12) = 2
- gcd(6, 12) = 6
- gcd(9, 12) = 3
- gcd(17, 12) = 1

Write an iterative function, `gcdIter(a, b)`, that implements this idea. One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either reach a case where the test divides both `a` and `b` without remainder, or you reach 1.

``` python
def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here

```

---

**My solution:** [gcd_iter.py](gcd_iter.py)

## Exercise: gcd recur

The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

- gcd(2, 12) = 2
- gcd(6, 12) = 6
- gcd(9, 12) = 3
- gcd(17, 12) = 1

A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that `a` and `b` are two positive integers:

If b = 0, then the answer is a

Otherwise, gcd(a, b) is the same as gcd(b, a % b)

[See this website for an example of Euclid's algorithm being used to find the gcd.](https://en.wikipedia.org/wiki/Euclidean_algorithm#Worked_example)

Write a function `gcdRecur(a, b)` that implements this idea recursively. This function takes in two positive integers and returns one integer.

``` python
def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here

```

---

**My solution:** [gcd_recur.py](gcd_recur.py)

## Exercise: is in

We can use the idea of **bisection search** to determine if a character is in a string, so long as the string is sorted in alphabetical order.

First, test the middle character of a string against the character you're looking for (the "test character"). If they are the same, we are done - we've found the character we're looking for!

If they're not the same, check if the test character is "smaller" than the middle character. If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string. (Note that you can compare characters using Python's `<` function.)

Implement the function `isIn(char, aStr)` which implements the above idea recursively to test if `char` is in `aStr`. `char` will be a single character and `aStr` will be a string that is in alphabetical order. The function should return a boolean value.

As you design the function, think very carefully about what the base cases should be.

``` python
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here

```

---

**My solution:** [is_in.py](is_in.py)

## Complete Programming Experience: polysum

A regular polygon has `n` number of sides. Each side has length `s`.

- The area of a regular polygon is: ![$\frac{0.25*n*s^2}{tan(\pi/n)}$](https://render.githubusercontent.com/render/math?math=%5Cfrac%7B0.25%2An%2As%5E2%7D%7Btan%28%5Cpi%2Fn%29%7D&mode=inline)
- The perimeter of a polygon is: length of the boundary of the polygon

Write a function called `polysum` that takes 2 arguments, `n` and `s`. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.

This is an optional exercise, but great for extra practice!

---

**My solution:** [polysum.py](polysum.py)

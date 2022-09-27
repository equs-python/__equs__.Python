# 3. Functions

## 3.1. Functions
At this point some of the code you have written will begin to seem somewhat unwieldy; large and long chunks of code, some repetition of code, and the start of the long descent into the general mess of spaghetti code.

In an effort to help clean this up, Python has functions, which are callable chunks of code that you have likely been using for a while now (if in other languages, then the `type` `help` and `abs` functions you used before). 

Functions syntax requires a `def` statement, a function name, some number of arguments (zero is a number) and a colon followed by an indented block for the code that the function runs when called.

```python
def function_name(arguments):
    arguments = arguments + 1
    return arguments
```    

We can also return multiple values using the tuple packing syntax we saw earlier

```python
def some_function():
    ''' Things happen '''
    return value_a, value_b
```

This will return a tuple of the values, which can be unpacked in the manner described earlier.

```python
a, b = some_function()
```


## *[Problem 3.1 : 5 Minutes]*

Write a modulus power function. The function takes three arguments in order, the base, the exponent and the modulus and calculates: 

```python
base ** exponent % modulus
```

Your function definition should something look like
```python
def modpow(base, exponent, modulus):
```

### 3.1.1 Keyword Arguments

Sometimes you want a function to have a 'default' argument, that is assumed to always the case until specified otherwise. This generally makes for neater function arguments when the function in question may have a large number of potential arguments that you don't want to explicitly specify each time.

Keyword arguments should always be placed after regular arguments.

```python
def function_name(arguments, keyword_arguments=default_value):
    '''Something happens'''
```


## **** Problem [5 minutes] ****

Modify your modpow function such that it has a default modulus of `None`. If no modulus is specified it should act like a regular power function.

```python
def modpow(base, exponent, modulus=None):
```


### 3.1.2 Arbitrary arguments
You may wonder at this point, that if you can simply pass a list to a function, then what's the point of ever having more than one argument? Just group all your arguments into a single list and throw that in. 

You would be right (ignoring keyword arguments), but it would look a little ugly, so there's a slightly neater inbuilt approach `*args`.  

Args takes any number of positional (i.e. non keyword arguments) that aren't specified by the function call and wraps them into a list. 

```python
def arged_function(some_argument, some_other_argument, *args, keyword='killer rabbit'):
    """ Something """

arged_function(1,2,3,4,5,6,6,7,8,9, keyword='holy hand grenade')
```

And of course continuing this, what's to stop you from handing key word arguments just using a dictionary? Again, spot on and again Python has a slightly neater syntax in the form of `**kwargs`:

```python
def arged_function(some_argument, some_other_argument, *args, keyword='killer rabbit', **kwargs):
    """ Something """

arged_function(1,2, keyword='holy hand grenade', print='True')
```

This is of course how the format method was working earlier, the position arguments were passed using `*args` and became a tuple while `**kwargs` was used for the keywords. You will notice that if you attempt to access a position that doesn't exist or a keyword that doesn't exist then the format function will throw an error.

```python
>>> "{1}".format('5')
IndexError: tuple index out of range
``` 

## *[Problem 3.2 : 10 Minutes]*

Implement a very basic version of the format function. Your function should take a string to format along with the args and kwargs. You should try to replicate the format method as closely as possible.

```python
def format(format_string, *args, **kwargs):
    ''' Things happen '''
    return formatted_string
```

## 3.2 Iterators and Generators

This section covers some more advanced looping techniques. 

An iterator in Python is any object with the `__iter__` and `__next__` methods. All the collections we saw before have associated iterators that we used when looping over them. 

A generator object creates iterators which we can then loop over. The zip function can be considered a generator; it takes a set of iterables and builds an iterator that aggregates these into an iterator of tuples:

```python
a = [1,2,3]
b = [4,5,6]

for i in zip(a,b):
    print(i)
```

We can of course unpack the tuple and have a loop over multiple collections.

```python
for a_element, b_element in zip(a,b):
   print(a_element)
   print(b_element)
```

Another useful generator is the `enumerate` function. This one returns both the element of an iterable and the index as a tuple.

```python
for index, value in enumerate(a):
    print(index)
```

We can also use the iterators for list comprehension as a bit of a cheat to build lists. Simply wrap a for loop in square braces and it becomes a list.

```python
>>> squares = [i ** 2 for i in range(10)]
>>> print(squares)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
``` 

We will discuss how to construct our own iterators and generators in the next session.


## *[Problem - Homework]*
Using whatever approach you want, use list comprehension to construct a list of the first 50 Fibonacci numbers.

If you're stuck, you might want to write a function that calculates the nth Fibonacci number first.


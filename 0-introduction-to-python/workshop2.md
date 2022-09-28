# 2. Workshop 1 - Lists and Loops

## 2.1 Collections

So far we've dealt with single variables. However say we're particularly greedy and want to store a thousand numbers without assigning each to its own individual variable. 

The solutions to this tedium are collections; data structures that have some logical method of storing and accessing variables in a consistent manner. Python by default comes with Lists, Tuples and Dictionaries (it's a hashmap).

As collections can be collections of any object, you can also have collections of collections; dictionaries of lists of complex numbers are perfectly acceptable. 


### 2.1.1 Lists
Lists can be thought of to some extent as 'vectors'. They're a collection of objects of any type with a particular numerical ordering. Lists are created by grouping a set of objects separated by commas in square brackets.

```python
a_list = [1,2,3]
```

These can be any objects, they don't need to be of the same type:

```python
b_list = [1, 'some string', -3j]
```

Elements in a list can be accessed by their position in the list *counting from 0*. This position is termed the 'index'.

```python
>>> print(b_list[0]) 
1
>>> print(a_list[1])
2
```

Lists can be appended to with the `.append()` method

```python
>>> a_list.append(4)
>>> print(a_list)
[1,2,3,4]
```

You can check the length of a list with the `len` method.

```python
>>> len(a_list)
4
```

And you can take slices of lists using colons to indicate the range of the slice

```python
>>> a_list[1:3]
[2, 3]
```
Note that the slices take the range from the lower value, up to, but not including the higher value.

Leaving the either side of the colon blank takes the range from the start or end of the list.

```python
>>> a_list[:2]
[1, 2]
>>> a_list[2:]
[3, 4]
```

Elements of lists can be modified in a reasonably straightforward manner:

```python
>>> a_list[2] = 5
>>> a_list
[1, 2, 5, 4]

```

And lastly, negative numbers in the index of a list indicate counting backwards. 

```python
>>> a_list[-1]
4
>>> a_list[-2]
5
```

Lists have an addition method defined such that adding two lists returns a new list formed by concatenation:
```python
>>> [1,2,3] + [4,5,6]
[1,2,3,4,5,6]
```

And by the same logic, multiplication duplicates a list.

```python
>>> [1,2,3] * 2
[1,2,3,1,2,3]
```
 
There are a few other properties of lists, such as sorting, removing elements and reversing them, that you can see by checking the help function for the `list`.

It's also quite easy to loop over the elements of a list in Python:

```python
>>> for i in a_list:
>>>     print(i)

1
2
5
4
```

There's quite a lot going on in here already, but there's an `in` keyword in Python for seeing whether an object exists in a collection:

```python
>>> if 5 in a_list:
>>>     print(True)
True
```

It's pertinent to also briefly discuss the range generator; while this isn't quite a list or a collection we will wave our hands and treat it as such:

```python
>>> for i in range(5)
>>>    print(i)
0
1
2
3
4
```
We can also forcibly convert this generator to a list.
```python
>>> list(range(5)
[0, 1, 2, 3, 4]
```

## *[Problem 2.1 : 5 minutes] Array Search*

At this point you should be familiar with looping and lists,
now we want to perform searchs on arrays. Unfortunately we can't
deduce everything down to an integer and we may want to find
elements that exist in a list.

In this problem we are going to have a list of names and we want to
search and find the first instance of a name.

Example, using this list of names

```
names = [
	"Jeff",
	"Alice",
	"Denise",
	"Paula",
	"Braben"
]
```

Lets try and find the user `Denise` in this list.

## *[Problem 2.3 : 5 Minutes] - Jagged Sum*
    Given a list of lists of uneven length, find the sum of the elements. Here are some example test cases:

```python
[[1], [1], [1]]
[[1, 2], [1], [1, 2, 3]]
[[1, 2, 3], [], [1, 2, 3]]
```

## 2.1.2 Tuples and Strings
Tuples are very similar to lists and almost everything from the previous section that worked with lists will work with tuples with the exception that they're immutable - once assigned they can't be changed. You can copy sections of a tuple or elements out of a tuple and modify those, but you can't change the ones inside a tuple.

Tuples are normally declared as a series of objects separated by commas and encapsulated in a pair of round brackets.

```python
>>> a_tuple = (1,2,3)

>>> a_tuple[1]
>>> 2

>>> a_tuple[1] = 3
-----------------------------------------------------------------------
TypeError                             Traceback (most recent call last)
<ipython-input-3-23f2cf2bdf70> in <module>()
----> 1 a_tuple[1] = 3

TypeError: 'tuple' object does not support item assignment

```

Tuples can also be declared by just a set of objects followed by commas. However this is less explicit and should be considered bad practice. Putting the parentheses around the objects is much friendlier for other people who read your code.
```python
>>> a_tuple = 1,2,3,
>>> print(a_tuple)
(1, 2, 3)
```

As we can build tuples using these separated commas, we can also unpack tuples in the same way. 

```python
>>> a, b = 1, 2
>>> print(a)
1
>>> print(b)
2
```
This is a handy trick that will come up again later.

It's worth noting that in Python strings are tuples of characters, not lists of characters. Hence all strings are immutable. This poses a bit of a problem as we generally want to be able to modify what we're printing. Luckily there are a few workarounds.

The first is the addition method we saw with lists. Simply add two strings to concatenate them

```python
>>> print("Hello" + "World")
HelloWorld
```
A neater solution is the old C-style string syntax followed by the % operator and then a tuple containing the values to be inserted into the string. 

```python
>>> x = 42
>>> print("A pair of numbers: %d %s" % (42, "42"))
A pair of numbers: 42 42
```

The downside to this method is that the type of the object must be included in the string, it's not a particularly general solution. The format method for a string solves this problem, and comes with a few different syntactic approaches.

Format searches for and replaces instances of `{}` within strings with the arguments in the format function. It will automatically convert other types to strings if possible.

```python
>>> print("The number of the counting shall be {}".format("three"))
```

Multiple inputs can be specified by considering the ordering of the arguments to the format function as if it were a tuple itself. So `{0}` refers to the first argument passed to the format method, `{1}` to the second and so on. 
```python
>>> print("{0} shalt thou not count, nor either shall thou count {1}".format('four', 2))
```

However this isn't particularly descriptive, so instead we can allocate names to the positional arguments, and specify this by name in the argument to the format function.
```python
>>> print("Excepting that thou then proceed to {number}".format(number=3))
```

There's quite a bit more to Python strings such as bytes formatting, the format strings of 3.6 and unicode, but these are more specialist topics so we'll leave it there for now.


### 2.1.3 Dictionaries

Dictionaries are a bit different. Whereas Lists and Tuples use an index as a key to the elements stored in the collection, dictionaries use a string. This is termed a 'key value pair'.

In keeping with the different brackets convention, dictionaries use the curly brackets `{}`.

```python
>>> a_dictionary = {'key_a':'value_a', 'key_b':12}
>>> a_dictionary['key_b']
12
``` 

Dictionaries are mutable, so you can add or change elements without any issues. 

```python
>>> a_dictionary['key_c'] = 15
>>> a_dictionary['key_b'] = a_dictionary['key_c'] / 3
```
Looping over a dictionary loops over the keys, not the values, the values can be accessed using the key as the index for the dictionary. 

```python
>>> for i in a_dictionary:
>>>    print('key: {}'.format(i))
>>>    print('value: {}'.format(a_dictionary[i]))
```

Removal is somewhat fiddlier and is best left alone unless there is a particularly good reason.

## *[Problem 2.1.5 : 5 Minutes] - Counting the occurrence*

Your task is to construct a program that will count the occurrence of numbers 0-9 that are present
in an array. Use a dictionary to solve this problem.

* Consider what the dictionary keys and values will be.
* Could you do it without using a dictionary?


### 2.1.5 Where are the arrays?

While we're here, I'll briefly emphasise that lists are **not** vectors.

For example, scalar multiplication is not element-wise.
```
>>> [1, 2, 3] * 2
>>> [1, 2, 3, 1, 2, 3]
``` 

You could do it yourself with a simple loop, or we can wait until we get the proper objects with these properties already included.

Arrays and other mathematically minded objects are in numpy, we'll get there later.

## *[Problem 2.4 : 5 Minutes] - Matrix Multiplication*
    With two nested loops and two two dimensional arrays write a python script that multiplies them together and prints the output.

```python
eye = [[1, 0], [0, 1]]
x = [[0, 1], [1, 0]]

# TODO Multiply

print(result)
```

Consider how you would scale this up for matrices of arbitrary dimensions.

## 2.1.6 Getting into the weeds

There are a few tricks with lists that I'd normally like to avoid, but are somewhat important. 

The main point is that a list object is actually an address pointing to where the list is stored. As a result we can get some odd behaviour when copying lists or modifying a tuple containing a list.

```python
>>> a_tuple = ([1,2,3],4,5)
>>> a_tuple[0][2] = 7
>>> print(a_tuple)
([1, 2, 7], 2, 3)
```
As we can see, even though the elements of the tuple cannot be modified, because the list is just a pointer to the elements of the list, they are mutable. 

Another time this pops up is when making shallow copies of a list.

```python
>>> a_list = [1,2,3]
>>> b_list = [a_list] * 3
>>> print(b_list)
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
```

As we can see, the 'b_list' is a list of lists, each is a copy of 'a_list'. So it stands to reason that I should be able to modify these.

```python
>>> b_list[0][0] = 2
```
 

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


## *[Problem 3.1.1 : 5 Minutes]*

Construct a function that will compute the average of a list.

```
def average(lst):
	#Your implementation here	
	pass

a = [15, 2, 3, 50, 9]
avg = average(a)

print(avg) #15.8

```


## *[Problem 3.1.2 : 5 Minutes] - Constructing your own list multiplication*

Construct a function that will accept a list and an integer, it should multiply the contents of the list 
with the integer given, and return a new list.

```
a = [1, 2, 3, 4]
b = list_mult(a, 2) #[1, 2, 3, 4, 1, 2, 3, 4]

```

## *[Problem 3.1.3 : 5 Minutes] - Counting the occurrence (with Strings)*

Construct a program that will count the occurence of a letter within a string.


```python

print(count_occurence("Hello", "e")) #1
print(count_occurence("lololololol", "l")) #6
print(count_occurence("Ring Ring Telegram", "i")) #2
print(count_occurence("Fabulous", "z")) #0

```


### 3.1.3 Keyword Arguments

Sometimes you want a function to have a 'default' argument, that is assumed to always the case until specified otherwise. This generally makes for neater function arguments when the function in question may have a large number of potential arguments that you don't want to explicitly specify each time.

Keyword arguments should always be placed after regular arguments.

```python
def function_name(arguments, keyword_arguments=default_value):
    '''Something happens'''
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


## *[Problem 3.2.1 : 5 Minutes] - Merging lists*

Construct your own zip function that will accept two lists as arguments and create a list with the amalgamated
lists. You will need to loop through each list and add it to a newly created one.

```
a = [1, 2, 3]
b = [4, 5, 6]

c = my_zip(a, b);

print(str(c)) #[1, 2, 3, 4, 5, 6]

```



# 2. Basic Python programming

# 2.1 Collections

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

## *[Problem 2.1 : 5 minutes] Prime Listing*

Modify your Prime finder code such that given a list, it checks each element of the list to see if it's prime.

Here are some sample lists:

- `[13, 99, 11, 97]`
- `[911, 1024, 2048]`
- `[829921]`
- `[]`

Yes, the last one is intentionally empty.

## *[Problem 2.2 : 5 Minutes] - Jagged Sum*
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

## *[Problem 2.3 : 5 Minutes] - Format*
Modify the print statement in your prime finder code to use the format method when printing which numbers are prime. 


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


### 2.1.4 Where are the arrays?

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

## 2.1.5 Getting into the weeds

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

##  *[Problem 2.5 : 5 Minutes] - List Incomprehension*
Try running the above code and satisfy for yourself that what is happening is both perfectly logical given what a list is, and is also very silly.

There is a solution to this problem, but we'll get to it later in the workshop.


## 2.2 Python files

It's a bit hard to reproduce code if it's always in the CLI, so we can instead put the code in a file and get the Python interpreter to read the file line by line and execute the code. These Python files normally have the `.py` extension, and can be run from the command line using 

```bash
python my_file.py
```

## *[Problem 2.6 : 5 Minutes] - Prime Mover*

Try moving your Prime finder code to a file and run it from the command line.

### 2.2.1 Command Line Input

Occasionally it's useful for a program to not just be a hard coded blob that needs to be opened and modified before. One way this can be achieved is by passing command line arguments. 

```python
python file.py 123 abc
```

These are passed to the file as a list, where element 0 of the list is the name of the file. You can access this list by importing the `sys` module and reading from `sys.argv`

```python
import sys
print(sys.argv[1])
print(sys.argv[2])
```

Should print

```python
123
abc
```

As you may have noticed, the list is separated by white space, with each space demarking a different element of the list.

There's a potential for error here as the argument may not have been passed, and so you're attempting to access an element of the list that does not exist. To get around this you can simply check the length of the list before accessing the elements.

```python
if len(sys.argv) >= 2:
    print(sys.argv[1])
```

This input will always be in string format, so you'll need to convert it to whatever type you need. Here are a few common functions that swap between types.

| Current Type       | Destination Type | Function |
| ------------- |:-------------:| -----:|
| String |  Int | `int`  |
| String | Float | `float` |
| Int  |  String | `str` |
| Int | Float | `float` |
| Int | Ascii Character | `chr` |
| Float | Int | `int` |
| Float | String | `str` |
| Ascii Character | Int | `ord` | 


## *[Problem 2.7 : 10 minutes] - Collatz*
The [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture) has a reasonably straight forward implementation as the 'hailstone problem'. 

Implement the hailstone problem in a Python file, your program will take a single integer as a command line argument for a starting value, you should print each intermediary value.  
- If the number is negative or zero then the program stops
- If the number is 1 then the program stops
- If the number is even divide it by 2
- If the number is odd multiply is by 3 and add one


## 2.2.2 Standard Input
Just as you can read and write to files, you can read and write to processes. This includes your running Python program. You should be used to reading things out using the print command, but writing requires all of one more command; `input`. (Note that in Python 2 it was called `raw_input` and this code won't be backwards compatible).

```python
>>> x = input()
5
>>> print(x)
5
```
As with the command line arguments, the input is in the form of a string. Unlike the command line arguments, the string is not delimited by white-space, but by a new line character (the enter button, or `\n`).

## *[Problem 2.8 : 5 minutes] - Collatz Again*

Modify your hailstone problem file to read from standard input instead of taking a command line argument.

## 2.3 Basic File I/O

Files can be read from or written to with the `'r'` and `'w'` arguments respectively. You can't do both at once. All files you open must be closed to avoid dirty edits.

```python
file_read = open('filename', 'r')
file_read.close()

file_write = open('filename', 'w')
file_write.close()
```

Reading comes with the `read`, `readline` and `readlines` commands, read takes the file buffer while readlines splits the input by the newline character. 

```
file_read.readlines()
```
Similarly we have the `write` and `writelines` commands that  take strings or lists of strings respectively and write them to the file.

```
file_write.write('Lumberjack')
file.write.write_lines(['abc', '123'])
```

When writing, you will need to insert your own newline characters for line breaks. This character is `\n`.

We can also control the scope of the file object, and automatically close it using the `with` keyword. When the indented block ends the associated file is automatically closed. 

```python
with open('filename', 'r') as f:
	''' do things '''
```

Generally this is a good idea to avoid forgetting to close the file. 

## *[Problem 2.9 : 5 Minutes] - Hello World!*
- Write `hello world` to a text file.
- Use Python to open the file, and read the contents
- Close the file, open it again in write mode and change the contents
- Confirm that this has happened in your text editor


## *[Problem 2.10 : Homework] - Primality*

- Modify your prime finder to write its output to a file
- Modify it again to read a file of integers and filter that file for prime numbers


## *[Problem - Homework] - Iterative implies Recursive*
Write a program that takes a list of lists of lists... of non-collection objects of arbitrary and non-uniform depth and prints all the non-collections. As we don't have functions on hand yet you will not be able to do this recursively. Your first problem should be finding how to distinguish between a list type and a non-collection type.

```python
    target = [[1, 2], [3, [4]], [[[5]]], 6, 7, [8, 9, 10]]
```
Where the expected output would then be the numbers from 1 through to 10.

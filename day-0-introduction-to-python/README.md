# GOOD MORNING EVERYONE!

Grab a coffee, find yourself a computer and log in with user name **equsp** and password **3QU5P**.

To prepare your workstation for this workshop, please install a code editor of your choice. We recommend using either

- [Visual Studio Code](https://code.visualstudio.com/docs/?dv=win) (this is what we are using), or
- [Atom](https://atom.io/)

Installation instructions are provided as print-outs on the desks. Then, download the workshop tutorials from GitHub: Open Git Bash, and type the following:

```bash
$ git clone https://github.com/equs-python/__equs__.Python
$ cd __equs__.Python
$ code .
```

Type the last line only if you are using Visual Studio Code. If not, open the tutorial content in your browser: [https://github.com/equs-python/__equs__.Python](https://github.com/equs-python/__equs__.Python)




# OPENING REMARKS


- a
- b
- c





# Day 0 - Basic introduction to Python

Here we introduce you to the basic usage of the Python language. We start with basic syntax, including types, control flow, and functions. We then introduce object-oriented programming, a common paradigm in code development. With these concepts under our belt, we are ready to introduce the core package for numerical programming in Python: [NumPy](http://www.numpy.org/). We conclude with an introduction to two other important packages for scientific use: [matplotlib](https://www.matplotlib.org/) for plotting and [SciPy](https://www.scipy.org/) for advanced numerical functionality.

Here's the detailed plan for the day:


1. Basic command line usage
2. First contact with Python
3. Using Python in the command line and in files
4. Simple variables and control statements
5. Functions in Python
6. Object-oriented aspects: classes and inheritance
7. Common scientific libraries for Python **!! include jupyter here !!**
8. If time permits: Advanced topics such as exceptions

# 1. Basic command line usage

Opening a terminal. Navigating through directories. Basic actions: executing files, creating and deleting files and directories, copying and moving.

An operating system is a series of excuses and abstractions that allow us to use text fields to control hardware operations. These text fields can be directly entered using a terminal emulator. (the real terminal is likely being used by your operating system to render the graphical environment that you're using and provies all the modern nicities of mouse support, windowed environments and anything that isn't strictly text based).

| Operating System        | Getting to your terminal emulator  |
| ------------- |-------------:|
| Windows      | Window + r gives you a "run" window. Into this enter either cmd.exe or powershell.exe |
| Linux      | Depends on your choice of window manager, common short cuts (mostly found in Gnome derived WMs) are Ctrl + Alt + T, but it could be just about anything. If you don't have one set, bind one. |
| Mac | Alt + Spacebar and type in "terminal" |

You can replace the windows terminal emulator with Bash if you want, this can either be done by installing Git Bash, or by running Windows Subsystem for Linux (WSL). Whatever you do, it's highly reccommended to set a key binding to open your terminal emulator.

These terminals take commands in the form of text and return responses in the form of text (generally ASCII encoded). This common format allows us to pass text not only to commands, but take the output of one command as the input to another. 

| Command        | Unix | Windows |
| ------------- |:-------------:| -----:|
| List Directory Contents |  `ls` | `dir` (ls will work on powershell) |
| Change Directory   |  `cd <path>` | `cd <path>` |
| Copy a file | `cp <source> <destination>` | `cp <source> <destination>` |
| Move a file | `mv <source> <destination>` | `mv <source> <destination>` |
| List processes and pids| `ps au` (or `top` or `htop`)| `tasklist` |
| Killing a process| `kill <pid>` | `taskkill /F /PID <pid>` |
| Shutdown | `shutdown now` | `poweroff -s -t 0` |
| Restart | `restart now` | `poweroff -r -t 0` |
| Execute a file | `<command to run file> <path to file>` | `{I've forgotten the windows one}` |
| Executing a Python file | `python <path to file>` | `python <path to file>` |

It's worth noting that the tab key will auto complete paths (and some commands), making this quite a bit faster than typing everything out manually. Depending on your terminal, pressing tab twice may also list possible completions if you aren't sure what you were looking for.

The terminal is an incredibly useful tool that we will be using throughout the workshop.


## 1.1 [Problem (5-10 minutes)]

Get used to the command line:
- Open up a terminal and try to navigate from your current position to the topmost (root) directory and then back to your own Documents folder.
- Once you've managed this, try to find the process ID of your terminal emulator and get it to terminate its own process. 
- If you don't have a keybinding to open your terminal, set one up.

As ever, if you are stuck or unsure about what to do, ask sooner rather than later. 

# 2. Hello Python!

Python is a high-level scripting language. It's quite flexible and has a well supported package library that allows it to do everything from scientific computing to running a twitter bot. The ease of use of Python does come at something of a tradeoff in performance, however in most cases the faster code development will more than offset the extra time required to run the code.

For historical reasons currently Python 2 and 3 exist as slightly different languages, Python 2 support will end later this year and so it's not particularly worth going into the differences between the two except to suggest using Python 3. 

Another key point is that Python is named after 'Monty Python', hence it is somewhat obligatory that any tutorial in the language include slightly too many references to 1970s British comedy. It is noted in advance that including jokes is a generally poor design choice for any real code.

## 2.1 Command line Interpreter
Open up the python command line interpreter (CLI) with the `python` command from your terminal emulator. As Python is an interpreted language, each line is read and executed in order. Thanks to this feature, we can use a Python terminal and simply give it Python code to execute 

Obviously, the first thing we do in any language is print the string "Hello World", I have it on good authority that the exclamation mark at the end of this string is strictly optional.

```
>>> print("Hello World")
```

We can also treat it as a basic calculator:

```
>>> 1 + 2
3
```

The regular maths operations are present (`+-/*`), as are powers: `**` and modulus `%`.

The up arrow key will iterate through previous commands, which is faster than typing them out.

We can also assign values to variables. Unlike some other languages, Python is untyped, it decides what the best type for the variable based on the data provided.

```
an_int = 2
a_float = 2.2
a_string = 'abc'
another_string = "def"
more_strings = """hijk"""
and_the_other_way = '''lm"no'''
a_complex_number = 1j
a_boolean = True
a_none_type_object = None
``` 
You can check the type of a variable using the `type()` function, for example:

```
>>> type(an_int)
int
```

If you don't know what a function does you can use the `help()` function to read the documentation for the function, so for instance, you should be able to call

```
help(type)
```

## 2.2 [Problem (5 minutes)]

Some very basic Python:
- Initialise a variable to some negative or complex number.
- Figure out how to take the absolute value of your variable. The `help` function will be useful here. There may be more than one way to do this.
- What is the type of the help function?
- What is the type of the type function?



# 3. Control flow

It would be useful for Python to be more than a glorified if somewhat introspective calculator, so we need something to control the program flow. Typically these are switches (if statements) and loops (for and while). Unlike other languages blocks of code within these control statements are de-marked by indentation. Perhaps the biggest hurdle of learning to use Python is inconsistent use of tabs and spaces. To save time and effort, the correct approach according to Python is four spaces for an indent. 

The start of an indented block is also indicated by a colon on the preceding line.


## 3.1 Switches
A switch is a common programming language feature where if a certain condition is met then the following code of block is executed. It consists of an `if` statement followed by the condition and the block to execute and then some number of optional `elif` statements with their own conditions before an optional `else` statement with its own block to be executed if none of the other conditions were met. 


```
if spanish_inquisition is True:
    print("Unexpected")
elif spanish_inquisition is None: #elif is short for else if
    print("Probably also unexpected")
else:
    print("No spanish inquisition here")
```
At this point it's probably a good idea to introduce some more Python syntax. Unlike most languages, Python tends to use words rather than symbols for its logical operations. For instance `and` and `or` are keywords:

```
if True or False:
	print("This will always return True!")

if True and False:
    print("This will never execute!")
```

Equality testing can be done using either the more traditional `==` or the `is` keyword.

```
if 5 == 5:
```
or 
```
if 5 is 5
```

There are also the usual greater than and less than operations.
```
> : Greater than
< : Less than
>= : Greater then or equal to
<= : Less than or equal to

```

Logical statements can also be nested or grouped using brackets

```
if (x > 5) and (x < 7):
 	print("x might be 6")
```

## 3.2 Problem - 5 minutes   
Write a simple chunk of Python code that determines if a number is a multiple of 13 and a multiple of 3 but not a multiple of 9. 


## 3.3 Loops

Loops are a construct that repeat some section of code until a condition is fulfilled. If the condition cannot be fulfilled in a timely manner, they will persevere despite your efforts and you will probably need to intervene.

There are two types of loops in Python, the `for` loop and the `while` loop.

The for loop iterates over some collection or range of objects (more on this later) while the while loop simply waits for a condition to be fulfilled.

Try running the following code to get an idea of each of them:

``` 
i = 0
while i < 10:
    i = i + 1
    print(i)
```

```
for i in range(10):
    print(i)
```

Both of these loops have their uses, try to use one of each in the next problem.

## 3.4 Problem (10 minutes)

Getting used to Loops and Switches:
- Write a loop to print each number from 2 to 100
- Modify your previous code to print each even number from 2 to 100
- (Extension) Modify your previous code to print each prime number from 2 to 100
- (Extension) If you have time left over increase this to primes up to 10000 and `import time` to use the time.time() function to test the speed of your code. If you don't know what this function does, don't forget to use `help()`.
- Again, if you have spare time, try to improve the performance of your code


# 4. Collections

So far we've dealt with single variables. However say we're particularly greedy and want to store a thousand numbers without assigning each to its own individual variable. 

The solutions to this tedium are collections; data structures that have some logical method of storing and accessing variables in a consistent manner. Python by default comes with Lists, Tuples and Dictionaries (it's a hashmap).

As collections can be collections of any object, you can also have collections of collections; dictionaries of lists of complex numbers are perfectly acceptable. 


## 4.1 Lists
Lists can be thought of to some extent as 'vectors'. They're a collection of objects of any type with a particular numerical ordering. Lists are created by grouping a set of objects separated by commas in square brackets.

```
a_list = [1,2,3]
```

These can be any objects, they don't need to be of the same type:

```
b_list = [1, 'some string', -3j]
```

Elements in a list can be accessed by their position in the list *counting from 0*. This position is termed the 'index'.

```
>>> print(b_list[0]) 
1
>>> print(a_list[1])
2
```

Lists can be appended to with the `.append()` method

```
>>> a_list.append(4)
>>> print(a_list)
[1,2,3,4]
```

You can check the length of a list with the `len` method.

```
>>> len(a_list)
4
```

And you can take slices of lists using colons to indicate the range of the slice

```
>>> a_list[1:3]
[2, 3]
```
Note that the slices take the range from the lower value, up to, but not including the higher value.

Leaving the either side of the colon blank takes the range from the start or end of the list.

```
>>> a_list[:2]
[1, 2]
>>> a_list[2:]
[3, 4]
```

Elements of lists can be modified in a reasonably straightforward manner:

```
>>> a_list[2] = 5
>>> a_list
[1, 2, 5, 4]

```

And lastly, negative numbers in the index of a list indicate counting backwards. 

```
>>> a_list[-1]
4
>>> a_list[-2]
5
```

There are a few other properties of lists, such as sorting, removing elements and reversing them, that you can see by checking the help function for the `list`.

It's also quite easy to loop over the elements of a list in Python:

```
>>> for i in a_list:
>>>     print(i)

1
2
5
4
```

There's quite a lot going on in here already, but there's an `in` keyword in Python for seeing whether an object exists in a collection:

```
>>> if 5 in a_list:
>>>     print(True)
True
```


## 4.2 Problem

Modify your Prime finder code such that given a list, it checks each element of the list to see if it's prime.

Here are some sample lists:

- `[13, 99, 11, 97]`
- `[911, 1024, 2048]`
- `[829921]`
- `[]`

Yes, the last one is intentionally empty.

## 4.3 Tuples and Strings
Tuples are very similar to lists and almost everything from the previous section that worked with lists will work with tuples with the exception that they're immutable - once assigned they can't be changed. You can copy sections of a tuple or elements out of a tuple and modify those, but you can't change the ones inside a tuple.

Tuples are normally declared as a series of objects separated by commas and encapsulated in a pair of round brackets.

```
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
```
>>> a_tuple = 1,2,3,
>>> print(a_tuple)
(1, 2, 3)
```

It's worth noting that in Python strings are tuples of characters, not lists of characters. Hence all strings are immutable. 


## 4.5 Dictionaries

Dictionaries are a bit different. Whereas Lists and Tuples use an index as a key to the elements stored in the collection, dictionaries use a string. This is termed a 'key value pair'.

In keeping with the different brackets convention, dictionaries use the curly brackets `{}`.

```
>>> a_dictionary = {'key_a':'value_a', 'key_b':12}
>>> a_dictionary['key_a']
12
``` 

Dictionaries are mutable, so you can add, remove or change elements without any issues. 

```
>>> a_dictionary['key_c'] = 15
>>> a_dictionary['key_b'] = a_dictionary['key_c'] / 3
```
Looping over a dictionary loops over the keys, not the values:

```
>>> for i in a_dictionary:
>>>    print('key: {}'.format(i))
>>>    print('value: {}'.format(a_dictionary[i]))
```

## 4.6 Problem



## 4.7 Where are the arrays?
In numpy, we'll get there later.


## 4.8 Getting into the weeds

There are a few tricks with lists that I'd normally like to avoid, but are somewhat important. 

The main point is that a list object is actually a pointer in memory to where the list is stored. As a result we can get some odd behaviour when copying lists or modifying a tuple containing a list.

```
>>> a_tuple = ([1,2,3],4,5)
>>> a_tuple[0][2] = 7
>>> print(a_tuple)
([1, 2, 7], 2, 3)
```
As we can see, even though the elements of the tuple cannot be modified, because the list is just a pointer to the elements of the list, they are mutable. 

Another time this pops up is when making shallow copies of a list.

```
>>> a_list = [1,2,3]
>>> b_list = [a_list] * 3
>>> print(b_list)
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
```

As we can see, the 'b_list' is a list of lists, each is a copy of 'a_list'. So it stands to reason that I should be able to modify these.

```
>>> b_list[0][0] = 2
```

## 4.9 Problem
Try running the above code and satisfy for yourself that what is happening is both perfectly logical given what a list is, and is also very silly.

There is a solution to this problem, but we'll get to it later.


## 5 Python files

It's a bit hard to reproduce code if it's always in the CLI, so we can instead put the code in a file and get the Python interpreter to read the file line by line and execute the code. These Python files normally have the `.py` extension, and can be run from the command line using 

```
python my_file.py
```


## 5.1 Command Line Input

Occasionally it's useful for a program to not just be a hard coded blob that needs to be opened and modified before. One way this can be achieved is by passing command line arguments. 

```
python file.py 123 abc
```

These are passed to the file as a list, where element 0 of the list is the name of the file. You can access this list by importing the `sys` module and reading from `sys.argv`

```
import sys
print(sys.argv[1])
print(sys.argv[2])
```

Should print

```
123
abc
```

As you may have noticed, the list is separated by whitespace, with each space demarking a different element of the list.

There's a potential for error here as the argument may not have been passed, and so you're attempting to access an element of the list that does not exist. To get around this you can simply check the length of the list before accessing the elements.

```
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


## 5.2 [Problem (10 minutes)]

Implement the hailstone problem in a Python file, your program will take a single integer as a command line argument as a starting value, you should print each intermediary value.  
- If the number is negative or zero then the program stops
- If the number is 1 then the program stops
- If the number is even divide it by 2
- If the number is odd multiply is by 3 and add one


## 5.3 Standard Input
Just as you can read and write to files, you can read and write to processes. This includes your running Python program. You should be used to reading things out using the print command, but writing requires all of one more command; `input`. (Note that in Python 2 it was called `raw_input` and this code won't be backwards compatible).

```
>>> x = input()
5
>>> print(x)
5
```
As with the command line arguments, the input is in the form of a string. Unlike the command line arguments, the string is not delimited by whitespace, but by a new line character (the enter button, or `\n`).

## 4.4 [Problem (5 minutes)]

Modify your hailstone problem file to read from standard input instead of taking a command line argument.


# 6. Functions
At this point some of the code you have written will begin to seem somewhat unwieldy; large and long chunks of code, some repetition of code, and the start of the long descent into the general mess of spaghetti code.

In an effort to help clean this up, Python has functions, which are callable chunks of code that you have likely been using for a while now (if in other languages, then the `type` `help` and `abs` functions you used before). 

Functions syntax requires a `def` statement, a function name, some number of arguments (zero is a number) and a colon followed by an indented block for the code that the function runs when called.

```
def function_name(arguments):
    arguments = arguments + 1
    return arguments
```    


## 6.1 [Problem (5 minutes)]


## 6.2 Keyword Arguments

Sometimes you want a function to have a 'default' argument, that is assumed to always the case until specified otherwise. 

```

```

TODO: FINISH THIS SECTION

## 6.3 [Problem (5 minutes)]

## 6.4 Arbitrary arguments
You may wonder at this point, that if you can simply pass a list to a function, then what's the point of ever having more than one argument? Just group all your arguments into a single list and throw that in. 

You would be right (ignoring keyword arguments), but it would look a little ugly, so there's a slightly neater inbuilt approach `*args`.  

Args takes any number of positional (i.e. non keyword arguments) that aren't specified by the function call and wraps them into a list. 

```
def arged_function(some_argument, some_other_argument, *args, keyword='killer rabbit'):
	""" Something """

arged_function(1,2,3,4,5,6,6,7,8,9, keyword='holy hand grenade')
```

And of course continuing this, what's to stop you from handing key word arguments just using a dictionary? Again, spot on and again Python has a slightly neater syntax in the form of `**kwargs`:

```
def arged_function(some_argument, some_other_argument, *args, keyword='killer rabbit', **kwargs):
	""" Something """

arged_function(1,2, keyword='holy hand grenade', print='True')
```

## 6.4 [Problem (10 minutes)]

# Iterators and Generators

This section covers some more advanced looping techniques. And we will only briefly cover these 

An iterator in Python is any object with the `__iter__` and `__next__` methods. All the collections we saw before have associated iterators that we used when looping over them. 

A generator object creates iterators.  


If you want to cheat your list building, you can use a technique called list comprehension. 

We won't cover how to build generators from functions (using the `yield` keyword), but this is something you may want to look into at some point.

TODO: FINISH THIS SECTION

# 7. Object-oriented programming

At this point you may begin to wonder what Python is really up to and how it distinguishes between and manages all these objects. Given that just about anything can be assigned to a variable, isn't an integer just a collection of function objects that act on a bit of data.

Again, you would be right, and we can see this quite clearly using the `dir()` function.

```
dir()
```

It also should be of note that I can save all my current variables as a dictionary with the names of the variables as the key, and the value as whatever the value is. And we can see these dictionaries as `globals()` and `locals()` depending on the namespace.

```
globals()
locals()
```

Now that we've noticed that everything is really a dictionary, it stands to reason that we can insert, modify or remove elements from these dictionaries (assuming we have write permissions). Given that the first time we open something up, it's somewhat obligatory that we break it trying to put it back together,  

Let's cheat at making a new variable.

```
>>> globals()['silly_walk'] = 5
>>> print(silly_walk)
5
```

As a point of pedantry, we're going to disambiguate between functions that live by themselves in whatever the current namespace is, and functions that live within another object by calling the latter a method. If someone trips up on this don't worry too much.

Let's start by 'borrowing' the abs method from a complex number object.

```
>>> our_imag = -5j
>>> help(our_imag.__abs__)
>>> abs_function = our_imag.__abs__
>>> help(abs_function)
```

Notice that the abs function takes an argument 'self'. Now try running the following commands 

```
>>> our_imag.__abs__()
>>> abs(our_imag)
>>> abs_function()
>>> abs_function(-5j)
```

The third one fails. As you may have seen from the previous help statements, the self argument is required and hence throws an error. This `self` argument is what ties our dictionary of functions together into an object or a `class`. It allows an object to reference elements of itself and hence modify or call functions that it is associated with.

## 7.1 Classes

Classes in python requires a constructor, sometimes termed an initialiser. This is a function that is called when a new instance of the object is created, for instance 

```
>>> my_int = int(5)
```

Calls the initialiser method `__init__` and returns a new instance of the integer class with the value 5.

So obviously if we want our own class we need to have some object with an `__init__` method. The syntax for creating classes is very similar to that of functions, the keyword is `class` is followed by the name of the class (Which is in CamelCase by convention) followed by two brackets (empty for now) and then a colon to start an indented block. Everything that lies within the block is a class attribute or method. Generally it's a good idea to put this in a file somewhere rather than trying to run this though the CLI.

As `__init__` is a function, we can make regular use of the usual keyword arguments along with `*args` and `**kwargs`.

We can use the self property to store things within a particular instantiation of the class. So let's start by making a Parrot class. Parrots are either alive or dead, and if they're alive they have a distinctive squawk. We will assume that all parrots are alive until proven otherwise.

```
class Parrot():

	def __init__(self, squawk, is_alive=True):
		self.squawk = squawk
		self.is_alive = is_alive
```
I can now make new parrots.

```
african_grey = Parrot('Polly want a Cracker?')
norwegian_blue = Parrot('', is_alive=False) 
```

Having an initialiser is good, but what does this parrot do? Let's give it a `squawk` function to make it talk.  

```
    def squawk(self):
        if self.is_alive:
            return self.squawk
        else:
        	return None
```

We should now be able to call this function.
```
african_grey.squawk()
norwegian_blue.squawk()
```

These sorts of trivial methods that just return an element of a class is commonly called a 'getter'. Similarly a small method that sets a class property is a 'setter'. Let's set up a setter to update whether our Parrot is still alive.

```
    def set_alive(self, is_alive):
    	self.is_alive = is_alive
```

## 7.2 Problem
Extend the Parrot class 
- Write a setter to set a new 'squawk' for the parrot
- Write a `__call__` function that makes the parrot squawk
- Give the parrot a new property 'colours' and write getters and setters for this property

If you didn't already, your `__call__` method should call the getter for squawk, if you've made a mistake in squawk or need to change it in the future you will now only have to modify one section of code, rather than every section that references `self.squawk`.


## 7.3 Inheritance
So far classes are just a neat way to organise functions and the data that the functions act on. And while that will remain to be true, we can take this a little further and neatly organise our classes.

Part of this is inheritance, we can specify that classes 'inherit' the properties of some parent class, which saves us from having to re-write them each time. These parent classes We can also specify 'abstract' classes or functions that only the child classes implement, this allows us to have multiple classes with common function calls that invoke different behaviour. 

For instance if I have an quantum gate class, it might be inherited by the Pauli X class and the CNOT class. These classes will 'overload' the methods in the quantum gate class such that when called the methods in the child classes will be used instead. 

This is all very high level, so let's go back to dealing with parrots. We're going to create a Bird class that Parrots will inherit and this parent class will manage the `is_alive` property, while only parrots get to squawk. Birds will also have air speed velocities (for the purposes of this example, emus, cassowaries and kiwis are not birds).

```
class Bird():
    def __init__(self, is_alive, air_speed_velocity):
    	self.air_speed_velocity
    	self.is_alive = is_alive
```

An in Parrot we now inherit from Bird and call the bird constructor.

```
class Parrot(Bird):
    def __init__(self, squawk, is_alive=True):
        self.squawk = squawk
        super(self).__init__(is_alive) # Calls the constructor of the super class

```
[TODO CHECK SYNTAX]

There also exists multiple inheritance, polymorphism and several books and philosophies on the matter of Object Orientation and class hierarchies, but the general rule of thumb is do what works best for whatever it is that you're doing. 


## 7.4 Problem
Finish off the bird class
- Write getters and setters for air_speed_velocity
- Check that your Parrots can now call the air speed velocity getters and setters 

Implement a Swallow class that inherits from Bird. 
- Swallows have the additional properties of being laden or unladen. Implement this and write the appropriate getters and setters
- A laden swallow moves at half the speed of an unladen swallow. You should overload the getter for the swallow to reflect this property. 


# 8. Python libraries

Here are a few useful (non-scientific) general libraries. 

- ipython - A better python CLI, strict upgrade from the regular one, no reason not to use it really.

- sys - A few good system level Python features, such as command line arguments, Python versions and other utilities.

- os - Operating system features, make directories, move files and delete files, check what OS is being run or find the user's name.

- time - All things to do with time and timing.

- rand - Random numbers and their uses, may not be suitable for cryptographic randomness

- sockets - For when you need a network socket (more on this in future days).

- pickle - Good for compacting Python object data to reload it later.

- copy - Contains the deepcopy function that gets around problems like list copying.

- matplotlib - Basic plotting library, basically the same as the matlab one there are others out there but most are just fancy wrappers for this 

These libraries can be included using the `import` keyword, as you've probably seen further up. You can also import libraries as a separate keyword in case you're too lazy to type out the full library name each time. For instance the numpy library is regularly imported as np.

```
import numpy as np
``` 

Each library also contains multiple Python files and functions, you can explicitly import one of those if you need, without including the entire library in your namespace. This is helpful when different libraries share keywords. 

``` 
import rand.random
```
or
```
from rand import random 
```

You can also be incredibly lazy and just import everything to the global namespace:

```
from rand import *
```
This may result in fiddly behaviour when two elements of the global namespace have the same name. Remembering that globals() is a dictionary, one of them will be overwritten, hence it's often much better to be more verbose. To be honest we're only really showing you this last one as an example of what not to do.

A final Python library of incredible importance is the `this` library. 


## 8.1 Problem [Over the Break]
Run and try to debug the following code:

```

```

## 9.1 NumPy
	# Arrays

## 9.2 Matplotlib

## 9.3 SciPy

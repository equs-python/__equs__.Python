# FIRST THINGS FIRST

Open Git Bash

```bash
$ git clone https://github.com/equs-python/__equs__.Python
$ cd __equs__.Python
$ git checkout -b my_branch
$ code .
```

# Day 0 - Basic introduction to Python

Here we introduce you to the basic usage of the Python language. We start with basic syntax, including types, control flow, and functions. We then introduce object-oriented programming, a common paradigm in code development. With these concepts under our belt, we are ready to introduce the core package for numerical programming in Python: [NumPy](http://www.numpy.org/). We conclude with an introduction to two other important packages for scientific use: [matplotlib](https://www.matplotlib.org/) for plotting and [SciPy](https://www.scipy.org/) for advanced numerical functionality.

Here's the detailed plan for the day:

0. **Clone this repository onto your local machine**

1. (Basic command line usage (if required))
2. First contact with Python (optional: installation)
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
| Shutdown | shutdown now | poweroff -s -t 0 |
| Restart | restart now | poweroff -r -t 0 |
| Execute a file | `<command to run file> <path to file>` | `{I've forgotten the windows one}` |
| Executing a Python file | `python <path to file>` | `python ./<path to file>` |

It's worth noting that the tab key will auto complete paths (and some commands), making this quite a bit faster than typing everything out manually. Depending on your terminal, pressing tab twice may also list possible completions if you aren't sure what you were looking for.

The terminal is an incredibly useful tool that we will be using throughout the workshop.


## 1.1 [Problem (5-10 minutes)]

Get used to the command line:
... Open up a terminal and try to navigate from your current position to the topmost (root) directory and then back to your own Documents folder.
... Once you've managed this, try to find the process ID of your terminal emulator and get it to terminate its own process. 
... If you don't have a keybinding to open your terminal, set one up.

As ever, if you are stuck or unsure about what to do, ask sooner rather than later. 

# 2. Hello Python!

Python is a high-level scripting language. It's quite flexible and has a well supported package library that allows it to do everything from scientific computing to running a twitter bot. The ease of use of Python does come at something of a tradeoff in performance, however in most cases the faster code development will more than offset the extra time required to run the code.

For historical reasons currently Python 2 and 3 exist as slightly different languages, Python 2 support will end later this year and so it's not particularly worth going into the differences between the two except to suggest using Python 3.

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
... Initialise a variable to some negative or complex number.
... Figure out how to take the absolute value of your variable. The `help` function will be useful here. There may be more than one way to do this.
... What is the type of the help function?
... What is the type of the type function?


```
For those who've used Matlab, Matlab is also an interpreted language and has its own Matlab terminal that is analagous to the Python terminal. This is as opposed to compiled languages that perform a series of contextual optimisations to blocks of code that may re-order or even just remove chunks of code that the compiler can optimise out. C as a compiled language may even optimise entire functions out of your code if it thinks there's a faster way to do it than creating a new stack frame.
```


# 3. Control statements

` `

` `

` `

## 3.3 [Problem (10 minutes)]

Getting used to Loops and Switches:
... Write a loop to print each number from 2 to 100
... Modify your previous code to print each even number from 2 to 100
... Modify your previous code to print each prime number from 2 to 100
... If you have time left over increase this to primes up to 10000 and `import time` to use the time.time() function to test the speed of your code. If you don't know what this function does, don't forget to use `help()`.
... Again, if you have spare time, try to improve the performance of your code


## 4 Python files

It's a bit hard to reproduce code if it's always in the CLI, so we can instead put the code in a file and get the Python interpreter to read the file line by line and execute the code. These Python files normally have the `.py` extension, and can be run from the command line using 

```
python my_file.py
```


## 4.1 Command Line Input

Occasionally it's useful for programs to take 


## 4.2 [Problem (10 minutes)]

Implement the hailstone problem in a Python file, your program will take a single integer as a command line argument as a starting value, you should print each intermediary value.  
... If the number is negative or zero then the program stops
... If the number is 1 then the program stops
... If the number is even divide it by 2
... If the number is odd multiply is by 3 and add one


## 4.3 Standard Input
Just as you can read and write to files, you can read and write to processes. This includes your running Python program. You should be used to reading things out using the print command, but writing requires all of one more command; `input`. (Note that in Python 2 it was called `raw_input` and this code won't be backwards compatible).



## 4.4 [Problem (5 minutes)]

Modify your hailstone problem file to read from standard input instead of taking a command line argument.


# 5. Iterators and Generators


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
```

```

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

## 7.1

Classes in python require an initialiser. This is a function that is called when a new instance of the object is created, for instance 

```
>>> int
```



## 7.2

## 7.3



# 8. Python libraries

Here are a few useful (non-scientific) general libraries. 

... sys - A few good system level Python features, such as command line arguments, Python versions and other utilities

... os - Operating system features, make directories, move files and delete files, check what OS is being run or find the user's name

... time - All things to do with timing

... rand - Random numbers and their uses, may not be suitable for cryptographic randomness

... sockets - For when you need a network socket (more on this in future days).

... pickle - Good for compacting Python object data to reload it later



## 7.1 NumPy

## 7.2 Matplotlib

## 7.3 SciPy

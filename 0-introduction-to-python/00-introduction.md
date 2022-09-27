# Day 0 - Basic introduction to Python

Here we introduce you to the basic usage of the Python language. We starting with basic syntax, including types, control flow, and functions. We then introduce object-oriented programming, a common paradigm in code development. With these concepts under our belt, we are ready to introduce the core package for numerical programming in Python: [NumPy](http://www.numpy.org/). We conclude with an introduction to two other important packages for scientific use: [matplotlib](https://www.matplotlib.org/) for plotting and [SciPy](https://www.scipy.org/) for advanced numerical functionality.

Here's the detailed plan for this week:

 1. Getting started
  - Basic command line usage
  - Hello Python!
  - Control flow in Python
 2. Basic Python programming
  - Collections
  - Pyobjects
  - Python files
  - Basic I/O in Python


# 1. Getting started

## 1.1 Basic command line usage

Opening a terminal. Navigating through directories. Basic actions: executing files, creating and deleting files and directories, copying and moving.

An operating system is a series of excuses and abstractions that allow us to use text fields to control hardware operations. These text fields can be directly entered using a terminal emulator. (the real terminal is likely being used by your operating system to render the graphical environment that you're using and provides all the modern niceties of mouse support, windowed environments and anything that isn't strictly text based).

| Operating System        | Getting to your terminal emulator  |
| ------------- |-------------:|
| Windows      | Window + r gives you a "run" window. Into this enter either cmd.exe or powershell.exe |
| Linux      | Depends on your choice of window manager, common short cuts are Ctrl + Alt + T, but it could be just about anything. |
| Mac | Command + Spacebar and type in "terminal" |

You can replace the windows terminal emulator with Bash if you want, this can either be done by installing Git Bash, or by running Windows Subsystem for Linux (WSL). Whatever you do, it's highly recommended to set a key binding to open your terminal emulator.

These terminals take commands in the form of text and return responses in the form of text (generally ASCII encoded). This common format allows us to pass text not only to commands, but take the output of one command as the input to another. 

| Command        | Unix (Linux or Mac) | Windows |
| ------------- |:-------------:| -----:|
| List Directory Contents |  `ls` | `dir` (ls will work on powershell) |
| Change Directory   |  `cd <path>` | `cd <path>` |
| Copy a file | `cp <source> <destination>` | `cp <source> <destination>` |
| Move a file | `mv <source> <destination>` | `mv <source> <destination>` |
| Make a directory | `mkdir <path to new directory>` | `mkdir <path to new directory>` | 
| List processes and pids| `ps au` (or `top` or `htop`)| `tasklist` |
| Killing a process| `kill <pid>` | `taskkill /F /PID <pid>` |
| Shutdown | `shutdown now` | `poweroff -s -t 0` |
| Restart | `restart now` | `poweroff -r -t 0` |
| Execute a file | `<command to run file> <path to file>` | `<command to run file> <path to file>` |
| Executing a Python file | `python <path to file>` | `python <path to file>` |

When you need to specify a path as an argument this is a relative path from the current directory. Unix paths must use the forward-slash key (as backslash is reserved to escape certain characters) while windows originally used backslashed paths and now uses both.

There are a few useful short-cuts that are almost essential 

| Command        |  Character | Example
| ------------- |:-------------:| -----:|
| Auto complete | tab | Just about anything really |
| Previous command | Up arrow key | |
| Absolute Path |  `/` or `C:\` | `cd /home/` or `cd C:\` |
| Up a directory   |  `..` | `cd ..` |
| Home Directory | `~` | `cd ~/Documents` |
| Previous command | `!!`| `sudo !!` |
| Interrupt a process | Ctrl + C| |
| EOF | Ctrl + D | |

It's worth noting that the tab key will auto complete paths (and some commands), making this quite a bit faster than typing everything out manually. Depending on how your shell is configured, pressing tab twice may also list possible completions if you aren't sure what you were looking for.

It's worth noting that the tab key will auto complete paths (and some commands), making this quite a bit faster than typing everything out manually. Depending on your terminal, pressing tab twice may also list possible completions if you aren't sure what you were looking for.

The terminal is an incredibly useful tool that we will be using throughout the workshop.

## *[Problem 5-10 minutes] - Command Line Blues*

Get used to the command line:

- Open up a terminal and try to navigate from your current position to the topmost (root) directory and then back to your own Documents folder.
- Once you've managed this, try to find the process ID of your terminal emulator and get it to terminate its own process. 
- Re-open your terminal and navigate to `__equs__.python`, in here make a new directory titled 'problems'. Keep your code from today in here. (in later weeks we'll be converting this to a git repository).

As ever, if you are stuck or unsure about what to do, ask sooner rather than later. 


## [Theory] What is a program?

A computer is broadly defined as a device that carries out a sequence of operations with some specified timing (a programme or schedule). The core novelty that enabled modern computation was the design of a computer of sufficient complexity where a program could specify and simulate another computer. 

This was achieved (though there are many ways of doing it) by storing the program being executed by the computer in the same region of memory that the computer was acting on. It was then possible for the computer to modify its own behaviour.

A program is then a series of instructions that specify operations that may simulate another computer with some overhead. The memory address of the currently executing instruction is associated with an 'instruction pointer' register. Programming is providing those instructions.

Given that a program may simulate another program we can also assert that given two different languages with which to execute programs that we may implement one programming language in the other. And from here we derive Python as written in C, as compiled to assembly and as executed on your computer.

## 1.2 Hello Python!

Python is a high-level scripting language. It's quite flexible and has a well supported package library that allows it to do everything from scientific computing to running a twitter bot. The ease of use of Python does come at something of a trade-off in performance, however in most cases the faster code development will more than offset the extra time required to run the code

For historical reasons currently Python 2 and 3 exist as slightly different languages, Python 2 support will end in less than a year and so it's not particularly worth going into the differences between the two except to suggest using Python 3. 

Another key point is that Python is named after 'Monty Python', hence it is somewhat obligatory that any tutorial in the language include slightly too many references to 1970s British comedy. It is noted in advance that including jokes is a generally poor design choice for any real code.


### 1.2.1 Command line Interpreter

Open up the python command line interpreter (CLI) with the `python` command from your terminal emulator. As Python is an interpreted language, each line is read and executed in order. Thanks to this feature, we can use a Python terminal and simply give it Python code to execute.

Obviously, the first thing we do in any language is print the string "Hello World", I have it on good authority that the exclamation mark at the end of this string is strictly optional.

```python
>>> print("Hello World")
```

We can also treat it as a basic calculator

```python
>>> 1 + 2
3
```

The up arrow key will iterate through previous commands, which is faster than typing them out.

The regular maths operations are present (`+-/*`), as are powers: `**` and modulus `%`.

The up arrow key will iterate through previous commands, which is faster than typing them out.

### 1.2.2 Literals and Variables

In the above examples `1` is a literal value, in theory I cannot change what `1` is, for example the following operation is illegal: 
```python
1 = 2
```
The operations are baked into the instructions that are part of the program and for the most part cannot be modified.
Conversely I can define regions of memory that may hold a variable value. These regions of memory are labelled with some name and are termed variables. Variables may be assigned a value using the assignment operator `=`.

```python
variable = 2
```

Unlike some other languages, variables in Python are untyped, the interpreter decides what the best type for the variable based on the data provided. This also implies that literals carry their own type which is then assumed by the variable.

```python
an_int = 2
a_float = 2.2
a_string = 'abc'
another_string = "def"
more_strings = """hijk"""
and_the_other_way = '''lm"no'''
a_complex_number = 1j
a_boolean = True
a_none_type_object = None
a_bytes_object = b"001010"
``` 

The assignment operator may also be used to assign the value of one variable to another:

```python
x = 5
y = x
```

We now have two different regions of memory labelled `x` and `y` each containing the same data.

You can check the type of a variable using the `type()` function, for example:

```python
>>> type(an_int)
int
```

If you don't know what a function does you can use the `help()` function to read the documentation for the function, so for instance, you should be able to call

```python
help(type)
```

## *[Problem - 5 minutes] - Operational* 

Some very basic Python:

 - Initialise a variable to some negative or complex number.
 - Figure out how to take the absolute value of your variable. The `help` function will be useful here. There may be more than one way to do this.
 - What is the type of the help function?
 - What is the type of the type function?

We've implicitly started using a number of operators here. What is the behaviour of each of the following operators and what types are they defined over? Some of these operators may exhibit different behaviour for different types. The `bin` function is defined over some types and may assist in decyphering some of these operators.

 - `=`
 - `+`
 - `-`
 - `%`
 - `/`
 - `*`
 - `|`
 - `&`
 - `^`
 - `~`

 Or some digraphs:

 - `==`
 - `//`
 - `<<`
 - `>>`
 - `**`

Lastly some compound operators:

 - `+=`
 - `**=`
 - `%=`
 - `<<=`

Some operators are also more verbose than those above:

 - `and`
 - `or`

This list is not exhaustive, especially the compound operators. Pay special attention to the division operators, what implicit type conversion occurs in each case?

## *[Problem - 5 minutes] - Binary Logic*
Distinguish between the `and` and `&` operator and the `or` and `|` operator. Consider the following cases:

 - `5 and 2` vs `5 & 2`
 - `5 or 2` vs `5 | 2`

### 1.2.3 Casting

We can cast between different types using the appropriate functions.

```python
print(int(5.1))
print(float(7))
print(chr(42)) # Have a look at the ascii table for this one - `man ascii`
print(ord('a'))
print(str(5))
print(str(5.0))
print(bin(5))
```

## *[Problem - 5 minutes] - Casting Logic*

 - Demonstrate that `ord` and `chr` are each other's inverse
 - Distinguish between the str and chr casts.
 - Consider the following casts:

 ```python
 int("5.0")
 int("50", 12)
 int("101010110", 2)
 ```
  - The `hex` function also contains an implicit cast, how would you invert the `hex` function?

### 1.2.4 Truth and Falsehood

Python has an interesting relationship with the notions of binary truth. Consider the following comparisons

 - `1 == True`
 - `0 == False`
 - `0.0 == False`
 - `1.0 == True`

 Initially we might consider that 0 is false and 1 is true and that is the end of it, but:

 - `2 == True`
 - `2 == False`
 - `'a' == True`
 - `'a' == False`
 - `'' == True`
 - `'' == False`

We're now posed with an object that is neither true nor false. At this point we adopt a model of "truthyness" and "falseyness", for the purposes of binary logic non-zero integers are considered to be "truthy" and hence will, when forced, evaluate to True, this is also true for non-empty strings. Conversely empty strings and the None type are considered to be "falsey" and will evaluate to false.


## [Theory] Python's Memory Model

Computers (ignoring any particularly fun architectures) are constructed with a linear memory. Entries in this memory are addressed, typically such that each byte in memory is uniquely associated with an address. Data is stored and retrieved by writing to and from these addresses and this process is conceptually encapsulated as a variable. 

This model of memory, while sufficient for a programming language lacks a notion of typing; how do I determine the difference between four bytes storing floating point data, four bytes storing a string, or four bytes storing an integer? The answer is to associate with each variable some additional metadata indicating the type of the variable and containing the address of a table of instructions that resolves operations on it. We can access this metadata to observe the properties and methods of a given object using the `dir` function. This metadata also contains methods for interpreting the data in a variable in a human readable and hence printable form, which is why the `print` function acts over all types implicitly.

Variable assignment in python with this meta-data entry gets somewhat more involved than other languages. Every assignment operation allocates a new region of memory and binds the name of that variable to the address of this newly allocated region. You can observe the address of each variable with the `id` function. This can be made somewhat more readable if we first `hex` the address.


### 1.2.4 IPython

At this point we're going to swap to an extended python CLI: `ipython`. Exit your python CLI using the `exit()` command and start up `ipython` instead. 

If the ipython command throws an error, you may not have it installed, give a shout and someone will try to help you with the setup. If not this is a graphical and feature upgrade but does not constitute a change in how python itself performs.


## 1.3 Control flow in Python

With our model of programs as a series of instructions in memory accessed by a particular address it follows that we can increment or set this address at will. If we increment by a variable we now have runtime programmatic control over the next sequence of instructions to execute. This is the basis of switches, loops, functions and more generally control flow.

It would be useful for Python to be more than a glorified if somewhat introspective calculator, so we need something to control the program flow. Typically these are switches (if statements) and loops (for and while). Unlike other languages blocks of code within these control statements are de-marked by indentation. Perhaps the biggest hurdle of learning to use Python is inconsistent use of tabs and spaces. To save time and effort, the correct approach according to Python is four spaces for an indent. 

The start of an indented block is also indicated by a colon on the preceding line.


### 1.3.1 Switches
A switch is a common programming language feature where if a certain condition is met then the following code of block is executed. It consists of an `if` statement followed by the condition and the block to execute and then some number of optional `elif` statements with their own conditions before an optional `else` statement with its own block to be executed if none of the other conditions were met. 

```python
if spanish_inquisition is True:
    print("Unexpected")
elif spanish_inquisition is None:  # elif is short for else if
    print("Probably also unexpected")
else:
    print("No spanish inquisition here")
```
At this point it's probably a good idea to introduce some more Python syntax. Unlike most languages, Python tends to use words rather than symbols for its logical operations (as opposed to the binary operations seen earlier). For instance `and` and `or` are keywords:

```python
if True or False:
    print("This will always return True!")

if True and False:
    print("This will never execute!")
```

Equality testing can be done using either the more traditional `==` or the `is` keyword. `is` really compares the addresses of the two objects, and hence: `x is y` is equivalent to `id(x) == id(y)`. Conversely the regular comparison operation compares the values stored at both of those addresses (with some interesting conversions between floating point and integer types).

```python
if 5 == 5:
```
or 
```python
if 5 is 5
```
However
```python
5.0 == 5
True
```
and
```python
5.0 is 5
False
```

There are also the usual greater than and less than comparison operations.
```
> : Greater than
< : Less than
>= : Greater then or equal to
<= : Less than or equal to

```

Logical statements can also be nested or grouped using brackets

```python
if (x > 5) and (x < 7):
    print("x might be 6")
```

## *[Problem 5 minutes] Multiplicative*   
Write a simple chunk of Python code that determines if a number is a multiple of 13 and a multiple of 3 but not a multiple of 9. 

## 1.3.2 Introduction to Loops

Loops are a construct that repeat some section of code until a condition is fulfilled. If the condition cannot be fulfilled in a timely manner, they will persevere despite your efforts and you will probably need to intervene.

There are two types of loops in Python, the `for` loop and the `while` loop.

The for loop iterates over some collection or range of objects (more on this later) while the while loop simply waits for a condition to be fulfilled.

Try running the following code to get an idea of each of them:

```python
i = 0
while i < 10:
    i = i + 1
    print(i)
```

```python
for i in range(10):
    print(i)
```

Both of these loops have their uses, try to use one of each in the next problem.

## *[Problem - 10 minutes] - In the Loop*

Getting used to Loops and Switches:

- Write a loop to print each number from 2 to 100
- Modify your previous code to print each even number from 2 to 100
- Modify your previous code to print each prime number from 2 to 100
- (Extension) If you have time left over increase this to primes up to 10000 and `import time` to use the time.time() function to test the speed of your code. If you don't know what this function does, don't forget to use `help()`.
- Again, if you have spare time, try to improve the performance of your code!


## 1.3.3 Scope

Unlike many other languages Python scope is at the function level not the block level, as a result the following is legal (but dangerous) Python code:

```python
if x:
  y = 6 # New variable y instantiated
print(y)
```

This code will function correctly if `x` evaluates to `True` but will throw an error regarding `y` being undefined if `x` evaluates to `False`.


### *[Problem - Homework] - No Ifs*
Write a program that takes three integer inputs:

 - If all inputs are equal print their sum
 - If one input differs, print the input that differs
 - If all inputs are different, print their product

You may *not* use the if keyword or any other control flow. The following relations may be helpful:

```python
int(False)
int(not not(x ^ 5))
5 ^ 6 ^ 5
```

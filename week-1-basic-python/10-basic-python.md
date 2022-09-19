# Basic Python

## Hello World

As with most introductory programming courses, we need to ensure we have
an understanding of basic IO functionality. We will be outputting text
and integers to the terminal.

For the first case, we will be outputting `Hello World` to the
terminal. You will use the `print` function that will accept
a string.

- What is: string? 

A string is a data type in python (and all programming language) which
represents a sequence of characters. Typically use this type to represent
names, labels and tags.

A string *literal* is encapsulated within a pair of`'` or `"` (not mixed).

- What is: print?

`print` is an inbuilt function that allows you to output data to `stdout`.
You pass a string argument to the function and it will *print* it to
the terminal.

Example:

```python
print("Hello World")
```

## Processing the average

We will be introduced to an integer and floating point data types. Your
task now is to write a program that will calculate the average of 3
numbers that habe been provided as input.

- What is: input?

Input is a term that generally refers to the program that takes data. This
is also coupled with the `input` function within python. This function will
allow the use to create an input prompt, to then accept data within the
program.

```python
line = input()
```

The above example accepts a string line as input. The data type for line
is a string as with all data returned by `input`.

- How: Storing data?

As demonstrated in the previous example, we can store a string within
the variable `line`. We can also construct and set variables of
different types within python.

```
x = 1 #integer
y = 1.0 #floating point
b = False #boolean, True is the other literal
```

The above example shows the variables `x`, `y` and `b` storing different
data types.

Given nthe task of constructing a program that will store numerical data
into three variables. Your program should be used like so:

```
1.0
2.0
3.0
Average: 2.0
```
## Submitting your answers to github

In the first topic, we introduced git and github. However, it isn't enough
to simply fork and clone repositories, we need to be able to contribute
and make changes them.

After writing your above solutions, construct an `answers` folder
within `week-1-basic-python` using `mkdir`. You can place your
solutions within this folder.

Check the status of the repository using `git status`, your repository
should have `untracked` files. These files should belong to your 
`answer` folder for the respective week.

You can `add` the files to staging, this is effectively setting up
certain files to be saved by a `commit`.

Example:
```
git add average.py`
```

The above example would have added `average.py` to staging.

Afterwards, you can construct a commit for currently staged files, these
encapsulate all the files as a set of changes between the previous
state of the repository and now. It is also required to encorporate 
a message as part of your commit.

```
git commit -m 'adding average.py answer'
``

Afterwards, your local repository has the current changes however the
remote repository has not received your changes. You can send these
changes with `git push`.

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
| List processes and pids| `ps au` (or `top` or `htop`)| `tasklist` |
| Killing a process| `kill <pid>` | `taskkill /F /PID <pid>` |
| Shutdown | shutdown now | poweroff -s -t 0 |
| Restart | restart now | poweroff -r -t 0 |
| Execute a file | `<command to run file> <path to file>` | `{I've forgotten the windows one}` |
| Executing a Python file | `python <path to file>` | `python ./<path to file>` |

The terminal is an incredibly useful tool that we will be using throughout the workshop.


## 1.1 [Problem (5 minutes)]

Get used to the command line:
... Open up a terminal and try to navigate from your current position to the topmost (root) directory and then back to your own Documents folder.
... Once you've managed this, try to find the process ID of your terminal emulator and get it to terminate its own process. 
... If you don't have a keybinding to open your terminal, set one up.

As ever, if you are stuck or unsure about what to do, ask sooner rather than later. 

# 2. Hello Python!

General intro. What is Python. What's it for. Who's behind it. How is it different from other languages. etc.

A few words on Python 2 vs 3.

# 3. Python in the command line and in files

## 3.1 Command line interpreter

## 3.2 Python files

# 4. Variables and control statements

# 5. Functions

# 6. Object-oriented programming

# 7. Python libraries

## 7.1 NumPy

## 7.2 Matplotlib

## 7.3 SciPy

# 8. Advanced topics
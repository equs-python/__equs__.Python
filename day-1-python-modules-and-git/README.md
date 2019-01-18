# Day 1 - Python modules and git

Today we will teach you how to properly package your Python code. For this, we will collaboratively build a Python package. You will learn how to document your code, spread it over multiple files, and how to write automated unit tests. To keep track of revision history, we will create a repository on GitHub. We will show you how to use git) and GitHub to develop and maintain code projects, especially when there are multiple contributors.


Here are the specific topics of the day:

1. Python packages part 1: using multiple files
2. Python packages part 2: Package installation with `setup.py`'s
3. Documenting your code
4. Unit tests
5. Maintaining coding hygiene: Linting
6. Controlling revision history with git
7. Using GitHub to share and collaborate
8. Code project


# 1. Python packages - using multiple files

When your code project becomes large, it is useful to spread your code over individual files, ideally sorted by functionality. In this section we demonstrate how this can be done in Python. We start by having a closer look at what the `import` statement, which we've seen before, actually does.

- the `import` statement
- example with two Python files
- useful file operations - find module path etc.
- using folders - introduce `__init__.py`


## 1.1 The `import` statement

Previously, when we wanted to execute code in a Python file, we used the command line to run:

```
$ python my_file.py
```

This executes the entire code within the file `my_file.py`. However, we can also *import* certain parts of our Python script, and use them in e.g. the interactive terminal. Let's suppose our `my_file.py` script contains the following code:

```python
# my_file.py
foo = 3
def add_two(number):
    return number + 2
print(add_two(foo))
```

So this file contains a variable and a function declaration, as well as a function call whose result is printed to the standard output. When we execute this file in the command line, we get the following output:

```
$ python my_file.py
5
```

### 1.1.1 Importing a Python script

Now let's have a look at how we can import the contents of the file into an interactive terminal session. We could also use a `jupyter` notebook here and the code would be the same, but let's keep it simple and stick with the terminal for now. We use the `import` statement just as we've seen before:

```python
>>> import my_file
5
```

This command *imports* the content of `my_file.py` into our Python session. We've got two important things to note here: first, note that we do not need to add the `.py` file ending to this statement - it is implicit. Only `.py` files can be imported in this way.
Second, you can see that running this command also produces as output the number `5`, which comes from our printed function call in our script.

Once we've imported the file, we have access to all the Python objects that were defined in that file using the dot-notation:

```python
>>> my_file.foo
3
>>> my_file.add_two(2)
4
```

### 1.1.2 Namespaces and aliases

When we import our script using the syntax above, we implicitly create a so-called namespace for all the objects in our script. To access those variables, we use the dot-notation, which we have seen before in connection with classes, and in fact modules too (recall `numpy` and `matplotlib`). We can use the same notation here because *everything is an object* in Python, including individual scripts, and more general modules.

It is up to us how we call our namespace for imported scripts. We have seen the syntax `import numpy as np` before - this does nothing but change the name with which we access objects in the `numpy` module. For our script, we could write:

```python
>>>  import my_file as mf
5
>>> mf.add_two(2)
4
```

Now we have made an alias for our script and called it `mf`. Introducing aliases that are shorter that the actual script name is often convenient because  it reduces the amount of text you have to write!

### 1.1.3 Importing only selected objects

Instead of importing all the objects in a script, you can also just import the ones you selected. The syntax for this is as follows:

```python
>>>  from my_file import foo
5
>>> foo
3
```

Note that when using this syntax, you don't need to use the `my_file.foo` syntax - and in fact you can't, because we are importing `foo` directly into the namespace of our session. Note that we haven't imported the function `add_two` here: so trying to call that will result in a `NameError`.

We can also create an alias for the individual objects we import using the `as` keyword in addition to our syntax above:

```python
>>>  from my_file import foo as f
5
>>> f
3
```

Please don't name a variable (or any other object - ever) `f` though.



### 1.1.4 For completeness: star-imports (don't do this!)

The last option to import the contents of a script are so-called star-imports (or *-imports). Here, the objects in the script are imported into the namespace of the current session, and we don't need script name or alias to access them. The syntax for that is as follows:

```python
>>>  from my_file import *
5
>>> add_two(2)
4
>>> foo
3
```

While this might look convenient, we strongly recommend that you don't do this. Ever. Please. Imagine you are trying to work with a script that has several star-imports at the top. For every object that is not defined in the script itself, it's a real pain to figure out where it is coming from. So please don't do this.



### 1.2 What if I don't want to run executable code in my script?

Often when you find yourself working across multiple files, you have some executable code in those scripts that is useful to have when you execute the scripts themselves - like for instance some code that tests that your functions are working correctly - but you do not want to the code to be executed when you're just importing stuff from your script.

In this case, you can put all executable code into an `if` block with the following syntax:

`if __name__ == "__main__":`

Here, `__name__` is an implicit attribut of each Python script whose value gets assigned at runtime. When the script is executed as top-level script (this means we're executing the script directly), the `__name__` is set to `"__main__"` and the condition in the `if` block evaluates to `True`. On the other hand, when we *import* our script into a different session, the `__name__` attribute gets assigned the file name of the script (test this for yourself!), and hence the condition evaluates to `False` and any code within this `if` block will not be executed.

Let's add that block to our example:


```python
# my_file.py
foo = 3
def add_two(number):
    return number + 2

if __name__ == "__main__":
    print(add_two(foo))
```

Now here's what happens when we import the file:

```python
>>> import my_file
```

Exactly nothing! Nothing gets printed here because we are not executing the script directly, but rather just importing it into our current interactive session. When we do want to execute it directly, we would call:

```
$ python my_file.py
5
```

And here we would get the expected output, because the script was executed as top-level script.


## 1.3 Multiple Python files and folders

As projects grow in size, it often makes sense to organise different Python scripts in different directories, i.e. folders.

As an example, let's create a folder called `more_files` and put two Python scripts in there: `another_file.py` and `yet_another_file.py`, such that our directory structure is as follows:

```
my_file.py
more_files
    - another_file.py
    - yet_another_file.py
```

And suppose we have two very simple functions in our two new files:

```python
# another_file.py

def another_function(argument):
    print('Another function call with {}'.format(argument)
```

and equivalently:

```python
# yet_another_file.py

def yet_another_function(argument):
    print('Yet another function call with {}'.formata(argument)
```

Now let's import those functions into an interactive session. As before, we will use the dot-notation to navigate between Python objects. In fact, when you use the auto-completion function in an `ipython` session, you can see that Python recognises the directory structure.

However, when we actually try to run the `import` statement, we get the following error:


```python
>>> from more_files.another_file import another_function                    
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-1-422ba4a26f03> in <module>
----> 1 from more_files.another_file import another_function

ModuleNotFoundError: No module named 'more_files'

```

Python tells us that it did not find a *module* called `more_files`. This is because the dot-notation is for Python objects only, and a folder (as opposed to a Python script) is not a Python object. We can *only* import Python modules using this `import` statement - to import all other types of file into our script we need to use different methods. What we have been calling "Python script" up until here is recognised by Python as a *module*.

So how can we import functions from modules in sub-directories then? In order for this to work, we need to create a *module* out of this folder. To do this, we create another Python script with a special name: `__init__.py`, and we place it inside the `my_files` folder, such that our directory structure looks like:

```
my_file.py
more_files
    - __init__.py
    - another_file.py
    - yet_another_file.py
```

What do we write into the `__init__.py` file? Well, nothing for now. We get back to this later. Now take a look at what happens when we try and run the same `import` statement from above:

```python
>>> from more_files.another_file import another_function
>>> another_function('now working!')
Another function call now working!
```

The import is working correctly, and Python recognises `my_file.py` as a module.

### 1.3.1 What goes into `__init__.py`?

*Recall the `__init__` method for Python classes. Creating a file like this in a (module) folder has the same effect!*

In the example above, we left the `__init__.py` file empty, because we don't need to put anything in there in order for Python to recognise our directory as a module. However, the `__init__.py` file is the file that get's executed during a module import so we can fill it with code that we would like to run on an import.

One of the most common uses for `__init__.py` files is importing objects from scripts within that module, which in turn allows us to import those from the module directly, instead of having to use the dot-notation to navigate between scripts. Using our example from above, let's create an `__init__.py` file with the following content:

```python
# __init__.py
from .another_file import another_function
from .yet_another_file import yet_another_function
```

The dots at the beginning of the module name indicate a *relative* import - meaning that those two scripts are in the same directory. We won't go into any more detail on that here, but if you want to learn more about relative (and absolute) imports, check out this really nice StackOverflow post on [relative  imports for the billionth time](https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time).

With these modifications to our `__init__.py` file, we can now import our functions as follows:

```python
>>> from more_files import another_function, yet_another_function
>>> another_function('now imported!')
Another function now imported!
>>> yet_another_function('now imported too!')
Yet another function now imported too!
```

So we can skip specifying the individual scripts which shortens our import syntax. Hurray!


## 1.4 Importing from different locations

All of the examples above worked because we were importing modules from the same directory that our top-level script was in. If we want to import module that lie in a different directory, we have two options:

1. We can provide the explicit path to the module
2. We can *install* the module - and Python will create all required references for us

We will deal with the second point in more detail later on, for now we just take a quick look at how to add an explicit path to a module. For this, we use the built-in `sys` library and add the path to the module to `sys`'s `path` variable like so:

```python
import sys
sys.path.append('path/to/my/module')
```

Let's take a look at an example. Suppose we are in the same directoy as our `more_files` folder and we want to import `yet_another_function` from `yet_another_file.py`.

```
we are here
more_files
    - another_file.py
    - yet_another_file.py
```

So here's what we can do:

```python
import sys
sys.path.append('more_files')
from yet_another_file import yet_another_function
```
And you can test for yourself that this works.

The `sys.path` variable contains all directories in which Python will look for modules when you're trying to import something. Take a look at what's in there with `print(sys.path)`!

# 2. Python packages - installation

What does it mean to install a Python package? What is a `setup.py` file? What is `pip`? These are terms that you may or may not have come across before, and now we will shed some light onto what they mean and do. Here we keep the discussion fairly short, so if you want to learn more check out the following link:

[Official Python tutorial on package installation](https://packaging.python.org/tutorials/installing-packages/)

In short, installing a (pure) Python package means that the module code with all its subdirectories is copied into the `site-packages` directory in the Python installation folder.

As an example, let's find the location of an installed Python module. Open an interactive session and type the following:

```python
>>> import numpy as np
>>> np.__file__
```

The `__file__` attribute is another special attribute (just like the `__name__` attribute that we encountered above).


Why `setup.py`? What does "installation" mean exactly? How is it different from `pip`?

- `python setup.py install` vs `python setup.py develop`
- How to write the `setup.py` file
- optional: command line entry points?

# 3. Documenting your code

- Why documentation saves lifes
- Documentation styles (first reference to PEP8)
- Writing doc-strings
- (compiling doc-strings into documentation?)
  
# 4. Unit tests

- When to write tests (create a `tests/` directory in module directory)
- Python unit testing libraries
- Introduction to `pytest`

# 5. Maintaining code hygiene: Linting!

- Why lint
- PEP8
- Overview of Python linters
- Introduction to `pylint`
- Editing the `.pylintrc` file

# 6. Controlling revision history with git

# 7. Using GitHub to share code and collaborate

# 8. Code project


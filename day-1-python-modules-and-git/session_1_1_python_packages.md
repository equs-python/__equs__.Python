# \_\_equs\_\_.Python workshop 2019
## Day 1 - Python modules and Git

# 1. Python packaging (1 1/2 hours)

In this tutorial we cover the process of building packages in Python. We start from the very basics of what a Python package is and how to install it, and make our way up from there to build an installable Python package ourselves at the end of this session.

## 1.1 Organising code across multiple files

When your code project becomes large, it is useful to spread your code over individual files, ideally sorted by functionality. In this section we demonstrate how this can be done in Python. We start by having a closer look at what the `import` statement, which we've seen before, actually does.

- the `import` statement
- example with two Python files
- useful file operations - find module path etc.
- using folders - introduce `__init__.py`


### 1.1.1 The `import` statement

Previously, when we wanted to execute code in a Python file, we used the command line to run:

```
$ python my_file.py
```

This executes the entire code within the file `my_file.py`. However, we can also *import* certain parts of our Python script, and use them in e.g. the interactive terminal.

## \*\*\*\* PROBLEM: Make a file (5 minutes) \*\*\*\*

Create a file that contains

- a variable declaration
- a function definition
- a `print` statement

It could for example look like this:

```python
# my_file.py
foo = 3
def add_two(number):
    return number + 2
print(add_two(foo))
```

Then, execute this file in the command line and look at the output:

```
$ python my_file.py
5
```

We will use this file for all our examples below.

## \*\*\*\*

#### 1.1.1.1 Importing a Python script

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

#### 1.1.1.2 Namespaces and aliases

When we import our script using the syntax above, we implicitly create a so-called namespace for all the objects in our script. To access those variables, we use the dot-notation, which we have seen before in connection with classes, and in fact modules too (recall `numpy` and `matplotlib`). We can use the same notation here because *everything is an object* in Python, including individual scripts, and more general modules.

It is up to us how we call our namespace for imported scripts. We have seen the syntax `import numpy as np` before - this does nothing but change the name with which we access objects in the `numpy` module. For our script, we could write:

```python
>>>  import my_file as mf
5
>>> mf.add_two(2)
4
```

Now we have made an alias for our script and called it `mf`. Introducing aliases that are shorter than the actual script name is often convenient because  it reduces the amount of text you have to write!

#### 1.1.1.3 Importing only selected objects

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



#### 1.1.1.4 For completeness: star-imports (don't do this!)

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



#### 1.1.2 What if I don't want to run executable code in my script?

Often when you find yourself working across multiple files, you have some executable code in those scripts that is useful to have when you execute the scripts themselves - like for instance some code that tests that your functions are working correctly - but you do not want to the code to be executed when you're just importing stuff from your script.

In this case, you can put all executable code into an `if` block with the following syntax:

```python
if __name__ == "__main__":
```

Here, `__name__` is an implicit attribute of each Python script whose value gets assigned at runtime. When the script is executed as top-level script (this means we're executing the script directly), the `__name__` is set to `"__main__"` and the condition in the `if` block evaluates to `True`. On the other hand, when we *import* our script into a different session, the `__name__` attribute will be different, and hence the condition evaluates to `False` and any code within this `if` block will not be executed.

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

## \*\*\*\* PROBLEM: What's my `__name__`? (5-10 minutes) \*\*\*\*

Find out what the value of the `__name__` attribute is if a file is not executed as top-level script.

- Create two Python files, e.g. `foo.py` and `bar.py`. 
- In `bar.py` import `foo`, and vice versa.
- In both scripts, add an `if __name__ == "__main__"` block, and in that bloch print out the name of the imported script
- Execute both files using the terminal


## \*\*\*\*


### 1.1.3 Multiple Python files and folders

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
    print('Another function call with {}'.format(argument))
```

and equivalently:

```python
# yet_another_file.py
def yet_another_function(argument):
    print('Yet another function call with {}'.format(argument))
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

#### 1.1.3.1 What goes into `__init__.py`?

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


### 1.1.4 Importing from different locations

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

## \*\*\*\* PROBLEM: What is `sys.path`? (5 minutes) \*\*\*\*

- Open a Python session and print out `sys.path`
- Add a new path to it, and print it out again
- Close and reopen the session, and again print out `sys.path`
- **Optional:** How can you make permanent changes to that variable?

## \*\*\*\*

## 1.2 Python package installation

What does it mean to install a Python package? What is a `setup.py` file? What is `pip`? These are terms that you may or may not have come across before, and now we will shed some light onto what they mean and do. Here we keep the discussion fairly short, so if you want to learn more check out the following link:

[Official Python tutorial on package installation](https://packaging.python.org/tutorials/installing-packages/)

In short, installing a (pure) Python package means that the package code with all its modules in subdirectories is copied into the `site-packages` directory in the Python installation folder. This is the default directory for all Python packages. Every package that lives in there can be imported from every other project or (i)python prompts.

As a first example, let's find the location of an installed Python package. Open an interactive session and type the following:

```python
>>> import numpy as np
>>> np.__file__
/home/virginia/.miniconda3/lib/python3.7/site-packages/numpy/__init__.py
```

The `__file__` attribute is another special attribute (just like the `__name__` attribute that we encountered above). It contains the path to the top-level module that is imported. Now note that the actual path will look different on every computer/operating system.

## \*\*\*\* PROBLEM: Find your `site-packages` directory (5 minutes) \*\*\*\*

Where are all your modules coming from? Find the path to Python's `site-packages` directory.

## \*\*\*\*

So does that mean that if we want a package to be available everywhere that we just need to copy it into the `site-packages` folder? For simple Python packages that do not require additional compilation the answer is yes - and, more general, every package that can be found under any of the paths listed in `sys.path` can be imported from everywhere.

However, the actual installation of a Python package does a few more things than simply just copying the code...

### 1.2.1 Installing a Python package

There are two main options for installing Python packages, and while they might look very different at first, they actually have a lot in common and down at their core do the same thing.

#### 1.2.1.1 Installing from source

The first option to install a new Python package is called "installation from source". This means that you have the source code of the package available locally on your machine, after e.g. cloning it from a GitHub repository. The package contains a special file called `setup.py`, that has all the installation instructions in it.

For example, consider the following directory structure:

```shell
example_package/
    - __init__.py
    - example_module.py
setup.py
```

The `example_module.py` is a short script that contains a single function:

```python
# example_module.py
def my_module_function():
    print('This is a function in example_module!')
```

The `setup.py` file lives outside of the package directory. In order to install this package, we run the following command in the terminal:

```shell
$ python setup.py install
```
We will have a look at what `setup.py` looks like in a moment, but first let's have a look at what it *does*:

Navigate into the `example_module` directory and run this command. Python will now create a bunch of files and references to your package - those store distribution and build information which we won't go into any detail here. At the end of all the output that you get from running this command you should see something like:

```shell
Installed /home/virginia/.miniconda3/lib/python3.7/site-packages/example_package-0.0-py3.7.egg
Processing dependencies for example-package==0.0
Finished processing dependencies for example-package==0.0
```

Now let's see if it worked! Open your favourite interactive console and try to import the package:

```python
>>> from example_package import my_module_function
>>> my_module_function()
'This is a function in example_module!'
```
And if you can see the output above then you've installed the package successfully! You can also check the `site-packages` directory now to see that it's there!

#### 1.2.1.2 Installing via pip

The example above - *installation from source* - requires us to have our own, local copy of the source code. Alternatively, if you want to install a package whose source code you do not have, you can use a package manager like `pip` or `conda`. They both access online servers that store Python packages. `pip` accesses the PyPI (Python package index) that currently has more than 150k packages available.

(*Note that `pip` can also install from source - and in fact what `pip` does is actually running `python setup.py install` after it downloaded the package files.*)

Check out PyPI [https://pypi.org/](https://pypi.org/) right now! To see a list of all the packages on PyPI, you can add the word "simple" at the end of the URL - such that it reads [https://pypi.org/simple](https://pypi.org/simple).

`pip` is a command line tool - that means that it is used from the command line. Have a look at your pip right now! Open a terminal and type:

```shell
$ pip
```

This will print out a reference guide for how to use `pip`. To install a package, we call it like this:

```shell
$ pip install <package_name>
```

Where we replace `<package name>` with the actual name of the package. We can also uninstall packages with pip:

```shell
$ pip uninstall <package_name>
```

And if you need more information on how to use a specific command with `pip`, you can add `--help` at the end of each command. For example, take a look at the output from

```shell
$ pip install --help
```

## \*\*\*\* PROBLEM: List all modules with `pip` (5 minutes) \*\*\*\*

To view all the packages we have installed, type:

```shell
$ pip list
```
Who has got the most modules installed?

## \*\*\*\*



## \*\*\*\* PROBLEM: Install the `funniest-joke` (20 minutes) \*\*\*\*

Your task is to to install a Python package called `funniest-joke` using `pip`. This is a very light-weight package that contains the [funniest joke in the world](https://www.youtube.com/watch?v=ienp4J3pW7U).

This package has a problem though: it was written for Python 2, so you will have to make it Python 3 compatible. Python 2/3 compability is one of the everyday hurdles of Python programmers, so this is an illustrative example of the real struggle in the life of a Python developer.

- Watch the [sketch on youtube](https://www.youtube.com/watch?v=ienp4J3pW7U)
- Install the package via `pip`:
```shell
$ pip install funniest-joke
```
- Execute the joke like this:

```python
>>> import funniest_joke
>>> funniest_joke.joke()
```

- Find and fix the **three** bugs
- **Optional:** fix the unicode display in the `print` function

If you're a newbie to Python and this isn't obvious to you, scroll down and follow the instructions below.

\*\*\*\*


Installing a Python module and not being able to use it properly because of version incompabilities is something that will happen to you a lot, so we want to use this example to show you some basic techniques on how to deal with those errors. The errors in this example aren't obvious for Python newbies, so if they don't make any sense to you right now don't be discouraged but instead try to *focus on the process of finding* those errors.

First of all, the error message that you should see looks like this:

```python
>>> import funniest_joke
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-3-6230e76666e1> in <module>
----> 1 import funniest_joke

~/.miniconda3/lib/python3.7/site-packages/funniest_joke/__init__.py in <module>
      3 '''
      4 
----> 5 from text import joke
      6 del text
      7 

ModuleNotFoundError: No module named 'text'
'''
```
We have seen this type of error before! And it links to the `__init__.py` file of the `funniest_joke` package. The reason for this error is quite subtle: the script is missing a dot in the import statement. Instead of 

```python
from text import joke
```

it should be

```python
from .text import joke
```

The dot infront of `.text` indicates a relative import and that's a requirement for packages in Python 3. This module was written for Python 2 only. But since we know how to fix this problem, and we know where Python keeps its packages, let's fix it!

After this, the import should work as expected. However, there are still two more problems to fix. The first one relates to how Python 2 and 3 handle strings - and without going into too much detail here - what you need to do to fix it is to remove the `.decode('utf-8')` in the `text.py` file. Have a look at [how strings are different in Python 2 and 3](http://python3porting.com/problems.html).

And the last error message that we expect relates to the syntax of the `print` function. In Python 2, `print` is a statement and you can call it without brackets. In Python 3, you need brackets around the arguments because `print` is now a function.

Once you've fixed all three errors, you should be able to print out the joke! It should look like this:

```python
>>> import funniest_joke
>>> funniest_joke.joke()
'<p>Wenn ist das Nunst\\u00fcck git und Slotermeyer? Ja! ... Beiherhund das Oder die Flipperwaldt gersput.</p>'
```

Those symbols that you see in the text are unicode symbols that are not rendered properly in the terminal.


## \*\*\*\* PROBLEM: Uninstall the `funniest-joke` (5 minutes) \*\*\*\*

Once you're done with this, let's uninstall this package again:

```shell
$ pip uninstall funniest-joke
```
And check that the source files have disappeared!

## \*\*\*\*

#### Package development

Once you've installed a package, in order to make any changes to it you need to edit the files in `site-packages`, as we've done in the problem above. This is quite inconvenient for when you are still actively developing a package and would like to keep the code somehwere more accessible.

In this case, you can ask Python to make an installation that *links* to your actual package directory. In order to do that, you should install it using the `develop` keyword instead of the `install` keyword like so:

```shell
$ python setup.py develop
```


This way, Python will create a symbolic link to the actual directory in which the source code lives, and it will access this directory when the package is imported - instead of making its own copy in `site-packages` at the time of installation.

Try it out with the `example_package`!

By the way, it is possible to achieve the same thing with `pip`. The syntax for this is

```shell
$ pip install -e <package_name>
```

Where the `-e` flag stands for editable and `<package_name>` here would be `example_package`. You would have to execute this command in the package directory.

Now take another look at the output of

```shell
$ pip list
```

The module should now come up with its path next to it.


## 1.2.2 What goes into a `setup.py` file?

Here is the content of the `setup.py` file in our `example_package`:

```python
"""
Setup file for the example_module
"""
from setuptools import setup

setup(
    name='example_package',
    version='0.0',
    description='An example Python module',
    author='Mr. Neutron',
    author_email='python@equs.org',
    packages=['example_package']
)
```

We import the `setup` function from Python's built-in `setuptools` package and call it with a series of arguments that describe the package. Most importantly, note the `packages` keyword: here we list the name of the module that actually gets installed. We can have several module names here if we want - and they would all get installed under the name specified in the `name` keyword at the top.

Let's have a look at a few more add-ons that you can put into a `setup.py` file to make life more exciting. For a full and comprehensive description, check out the [setuptools documentation](https://setuptools.readthedocs.io/en/latest/setuptools.html).

### 1.2.2.1 Adding installation requirements to `setup.py`

Often you will find yourself using other modules in your Python package - for instance when you're writing a numerical package you will most likely use `numpy` or `scipy`. You can (and should!) add this information to your `setup.py` file:

```python
from setuptools import setup
setup(
    [...] # Truncated for readability
    install_requires=['numpy', 'scipy']
)
```

Where we omitted the rest of the code from above for simplicity.

You can also specify versions for those modules, by using:

```python
install_requires=['numpy>=1.13', 'scipy>=1.1']
```

## \*\*\*\* PROBLEM: Add installation requirements (5-10 minutes) \*\*\*\*

Edit the `setup.py` file from this example and re-run the installation command to see how adding requirements changes the behavior.

- Add `numpy` and `scipy` to requirements
- Add a module that you do not have installed (e.g. `qinfer`)

## \*\*\*\*

### 1.2.2.2 Command-line entry points

As a nifty little feature of your package installation, you can create a command-line entry point - that is a command that you run in the command line which executes a certain piece of Python code associated with your package.

## \*\*\*\* PROBLEM: Create a command-line entry point (20 minutes) \*\*\*\*

We want to add a command line entry for a command that we call `call_my_module`, and which executes the `my_module_function` function in the `example_package` from above.

- First add a module called `command_line.py` to our example_package:

```
example_package/
    - __init__.py
    - example_module.py
    - command_line.py
setup.py
```

- Import our function from `example_module.py` and define a new function called `main` which executes that function:

```python
# command_line.py
from .example_module import my_module_function

def main():
    my_module_function()
```

- Now, to the `setup.py` script you need to add:

```python
from setuptools import setup
setup(
    [...] # Truncated for readability
    entry_points={
        'console_scripts':
            ['call_my_module=example_package.command_line:main'],
    }
)
```

Here we are assigning the desired function call to the command `call_my_module`.

- Run the installation again:

```shell
$ python setup.py develop
```

- Open a terminal and type:

```shell
$ call_my_module
```
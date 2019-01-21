# FIRST THINGS FIRST

Open Git Bash

```bash
$ git clone https://github.com/equs-python/__equs__.Python
$ cd __equs__.Python
$ git checkout -b my_branch
$ code .
```

# Day 1 - Python modules and git

Today we teach you how to properly package your Python code. For this, we collaboratively build a Python package. You learn how to document your code, spread it over multiple files, and how to write automated unit tests. To keep track of revision history, we create a repository on GitHub and show you how to use git and GitHub to develop and maintain code projects, especially when there are multiple contributors.


Here are the specific topics of the day:

1. Python packages part 1: using multiple files
2. Python packages part 2: Package installation with `setup.py`'s
3. Python packages part 3: Documenting, testing and linting code
4. Controlling revision history with git
5. Using GitHub to share and collaborate
6. Code project


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
    print('Yet another function call with {}'.format(argument)
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

In short, installing a (pure) Python package means that the package code with all its modules in subdirectories is copied into the `site-packages` directory in the Python installation folder. This is the default directory for all Python packages. Every package that lives in there can be imported from every other project or (i)python prompts.

As a first example, let's find the location of an installed Python package. Open an interactive session and type the following:

```python
>>> import numpy as np
>>> np.__file__
/home/virginia/.miniconda3/lib/python3.7/site-packages/numpy/__init__.py
```

The `__file__` attribute is another special attribute (just like the `__name__` attribute that we encountered above). It contains the path to the top-level module that is imported. Now note that the actual path will look different on every computer/operating system.

So does that mean that if we want a package to be available everywhere that we just need to copy it into the `site-packages` folder? For simple Python packages that do not require additional compilation the answer is yes - and, more general, every package that can be found under any of the paths listed in `sys.path` can be imported from everywhere.

However, the actual installation of a Python package does a few more things than simply just copying the code...

### 2.1 Installing a Python package

There are two main options for installing Python packages, and while they might look very different at first, they actually have a lot in common and down at their core do the same thing.

#### 2.1.1 Installing from source

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

#### 2.1.2 Installing via pip

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

To view all the packages we have installed, type:

```shell
$ pip list
```

And if you need more information on how to use a specific command with `pip`, you can add `--help` at the end of each command. For example, take a look at the output from

```shell
$ pip install --help
```

#### Pip installation example: the funniest joke

Let's take a look at an example: We want to install a Python package called `funniest-joke`. This is a very light-weight package that contains the [funniest joke in the world](https://www.youtube.com/watch?v=ienp4J3pW7U).

To install it, open a terminal and type the following:

```shell
$ pip install funniest-joke
```

Now let's have a look at this joke! Open a Python terminal and type:

```python
>>> import funniest_joke
>>> funniest_joke.joke()
```
Now if you are running this in Python 3 (which is what we're using on all workshop computers) this code won't execute and you will see an error message. The reason for this is that this project was developed for Python 2 only.

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

After this, the import should work as expected. However, there are still two more problems to fix. The first one relates to how Python 2 and 3 handle strings - and without going into too much detail here - what you need to do to fix it is to remove the `.decode('utf-8')` in the `text.py` file.

And the last error message that we expect relates to the syntax of the `print` function. In Python 2, `print` is a statement and you can call it without brackets. In Python 3, you need brackets around the arguments because `print` is now a function.

Once you've fixed all three errors, you should be able to print out the joke! It should look like this:

```python
>>> import funniest_joke
>>> funniest_joke.joke()
'<p>Wenn ist das Nunst\\u00fcck git und Slotermeyer? Ja! ... Beiherhund das Oder die Flipperwaldt gersput.</p>'
```

Those symbols that you see in the text are unicode symbols that are not rendered properly in the terminal.

Once you're done with this, let's uninstall this package of - indeed very questionable - humor:

```shell
$ pip uninstall funniest-joke
```

And check that the source files have disappeared!

#### Package development

Once you've installed a package, in order to make any changes to it you need to edit the files in `site-packages`, as we've done in the example above. This is quite inconvenient for when you are still actively developing a package and would like to keep the code somehwere more accessible.

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


## 2.2 What goes into a `setup.py` file?

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
    author='Mr. X',
    author_email='python@equs.org',
    packages=['example_package']
)
```

We import the `setup` function from Python's built-in `setuptools` package and call it with a series of arguments that describe the package. Most importantly, note the `packages` keyword: here we list the name of the module that actually gets installed. We can have several module names here if we want - and they would all get installed under the name specified in the `name` keyword at the top.

Let's have a look at a few more add-ons that you can put into a `setup.py` file to make life more exciting. For a full and comprehensive description, check out the [setuptools documentation](https://setuptools.readthedocs.io/en/latest/setuptools.html).

### 2.2.1 Adding installation requirements to `setup.py`

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

Edit the `setup.py` file in this example and re-run the installation command to see how addind requirements changes the behavior.

### 2.2.2 Command-line entry points

As a nifty little feature of your package installation, you can create a command-line entry point - that is a command that you run in the command line which executes a certain piece of Python code associated with your package.

For example, let's suppose we want to add a command line entry for a command that we call `call_my_module`, and which executes the `my_module_function` function in the `example_package` from above.

Do do that, we add a module called `command_line.py` to our example_package:

```
example_package/
    - __init__.py
    - example_module.py
    - command_line.py
setup.py
```

We let this script import our function from `example_module.py` and define a new function called `main` which executes that function:

```python
# command_line.py
from .example_module import my_module_function

def main():
    my_module_function()
```

Now, to our `setup.py` script we add:

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

Try it out! Rerun

```shell
$ python setup.py develop
```

And then:

```shell
$ call_my_module
```



# 3. Python packages - documentation, unit testing and linting

    “Code is more often read than written.”

    — Guido van Rossum

Guido van Rossum, the creator of the Python programming language made this very simple, yet incredibly meaningful statement above.

What we take from this is that it is immensly important *how* you write your code - be it for yourself or for other people. Have you ever found yourself in a situation where you had to use a piece of code that you've written many months ago (without documentation), and puzzled over what the code does? Or even worse, have you perhaps changed an auxilirary file, or upgraded your compiler/interpreter since then and now the old code doesn't run anymore? Or have you ever worked on a project collaboratively and found it extremely difficult to make out what other people's code is doing?

For all of those reasons, there exist coding standards - these are a collection of good practices which - when taken to heart - make each and every one of us a better person. Here we want to give you an overview of the three main components of those standards: documentation, testing and linting. And because this is a Python workshop, we use the official [PEP8 Python style guide](https://www.python.org/dev/peps/pep-0008/).


## 3.1 Let there be documentation

We assume that we can skip the argument on whether or not one should write documentation for code, and instead start with an illustrative example. We have an intentionally (arguably) badly written, undocumented and uncommented piece of code below. Can you figure out what it does?

```python
import numpy as np

def M(rho, n=1):
    m = rho.shape[0]//2
    prjs =[np.kron(s[:, np.newaxis],s[:, np.newaxis].T)
        for s in np.eye(m * 2)]
    pr =[np.abs(np.trace(prj.dot(rho))) for prj in prjs]
    res= np.random.choice(
        [i for i in range(m*2)], n, p=pr)
    return [np.eye(m*2)[r,:] for r in res]
```

The function `M` performs a measurement on a quantum state by projecting into the z-eigenbasis. The input state needs to be a density matrix. It's used in the following fashion:

```python
>>> import numpy as np
>>> rho = np.array([[0.5, 0.5], [0.5, 0.5]])
>>> M(rho, 3)
[array([0., 1.]), array([0., 1.]), array([1., 0.])]
```

Where we have prepared the maximally mixed state of a single qubit system and performed three measurements on it.

Now let's improve the readability of this piece of code to make it easier to use, understand and potentially modify. We will do this in three steps:

- Improve readability
- Add in-line comments
- Add documentation

### 3.1.1 Code should be readable on its own

Of course we are advocating for commenting and documentation here, but the first thing you should consider when writing code for yourself or others is that the code should be readable on its own. You can achieve this by e.g. using self-explanatory variable names, spaces and indents, as well as spreading long lines of code over multiple lines.

Here is a revised version of the function above where we changed all variable names and modified the formatting of the code:

```python
import numpy as np

def measure_state(state, number_of_samples=1):
    num_qubits = state.shape[0] // 2
    projectors = [
        np.kron(
            pure_state_vector[:, np.newaxis],
            pure_state_vector[:, np.newaxis].T
        )
        for pure_state_vector in np.eye(num_qubits * 2)
    ]
    outcome_probabilities = [
        np.abs(np.trace(projector.dot(state))) for projector in projectors
    ]
    results = np.random.choice(
        [i for i in range(num_qubits * 2)],
        number_of_samples,
        p=outcome_probabilities)
    return [
        np.eye(num_qubits*2)[result, :] for result in results
    ]
```

This is the exact same code as the one above, but with more descriptive variable names and cleaner code formatting. The overall amount of code gets longer when you do this, but we believe the gain in readability is worth it. And because it's still the same code, there are no losses in terms of performance.

### 3.1.2 Comments explain why, code explains how

Now that the code is more or less readable on its own, we continue with inserting comments to offer some additional explanations on what the code is doing. The general guide lines for in-line comments are that they should be consise (you can get more verbose in the documentation), at the appropriate position in the code, and describing what and why the code is doing what it's doing. The *how* should be self-explanatory if you made your code readable following the advise from the previous section.

See below for our revised example:

```python
import numpy as np

def measure_state(state, number_of_samples=1):
    num_qubits = state.shape[0] // 2
    # Prepare basis projectors in form of density matrices
    # Note: to calculate the tensor product we require column
    # vectors; we use the np.newaxis command for that
    projectors = [
        np.kron(
            pure_state_vector[:, np.newaxis],
            pure_state_vector[:, np.newaxis].T
        )
        for pure_state_vector in np.eye(num_qubits * 2)
    ]
    # Calculate the outcome probabilities using Born's rule
    outcome_probabilities = [
        np.abs(np.trace(projector.dot(state))) for projector in projectors
    ]
    # Randomly draw results from a uniform distribution
    # weighted by the outcome probabilities
    results = np.random.choice(
        [i for i in range(num_qubits * 2)],
        number_of_samples,
        p=outcome_probabilities)
    return [
        np.eye(num_qubits*2)[result, :] for result in results
    ]
```

### 3.1.3 Write documentation

Many people, especially those new to programming, or those working mainly on their own, stop after adding in-line comments to their code. However, as soon as a project becomes bigger or has multiple people working on or using it, writing proper documentation is crucial.

In Python (and other programming languages), it is common practice to write so-called *doc-strings*. A doc-string, as the name suggests, is a string that contains documentation. These are typically spread over multiple lines and every function, class and module in Python should have one - and in fact already *has* one, implicitly. This can be exposed using a special attribute called `__doc__`, that every Python object has.

Let's have a look! Open a console and type:

```python
>>> print(len.__doc__)
Return the number of items in a container.

```

This is the doc-string of the built-in `len` function in Python. When you write your own function, you can give it a doc-string by inserting a (optionally) multi-line string right below the `def` statement:

```python
>>> def foo():
    """
    This is my function foo.
    It prints the word 'bar' to the console.
    """
    print('bar')
>>> print(foo.__doc__)
    This is my function foo.
    It prints the word 'bar' to the console.
```
And we can do the same for classes and modules.

#### 3.1.3.1 What goes into a doc-string?

A doc-string should explain what the function/class/module is used for, and how it is used. In very simple cases, it is sufficient to provide a single line doc-string, like for example in the `len` function.

Broadly speaking, for more complex Python functions (or classes), doc-strings should contain the following:

-  Brief explanation of the object and its purpose
-  Enumerated description of inputs and outputs
-  Any exceptions that are raised
-  Examples
-  Further notes and comments

Under these considerations, this is how we would write a doc-string for our `measure_state` function:

```python
def measure_state(state, number_of_samples=1):
    """Performs a projective measurement of a quantum state in the Z-basis

    Parameters
    ----------
    state : numpy array
        The state in density matrix representation
    number_of_samples : int, optional
        How often to perform a measurement. Defaults to 1.

    Returns
    -------
    list
        A list of state vectors for each measurement

    Examples
    -------
    Single-qubit pure state measurement:
        >>> import numpy as np
        >>> state = np.array([[0, 0], [0, 1]])
        >>> measure_state(state, 2)
        [array([0., 1.]), array([0., 1.])]
    """
    # source code here
```

There are several different style guides for doc-strings. Among the most commonly used styles are:

- [Google doc-strings](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings)
- [NumPy doc-strings](https://numpydoc.readthedocs.io/en/latest/format.html)
- [reStructured Text doc-strings](http://docutils.sourceforge.net/rst.html)


#### 3.1.3.2 New feature in Python 3.5+: type hinting

In Python version 3.5, the [typing](https://docs.python.org/3/library/typing.html) module was introduced which provides syntactic means to display input and output types - as is common practice in many other (typed) languages.

Here is an example from the module documentation:

```python
def greeting(name: str) -> str:
    return 'Hello ' + name
```

Here, the function expects a string as input, and returns a string. Note that this is merely an annotation, you can still call the function with a different input type or change the return type of the function without getting into trouble. However, it definitely is quite neat and useful for documentation purposes.

  
## 3.2. Let there be tests

It goes without saying that every code that you plan to put to use needs to be tested. Chances are you are already doing this - even if perhaps not in an automated fashion. Here we take a look at how to write automated tests, structure them, and what modules we have got available in Python to run those tests.

### 3.2.1 Testing basics: the `assert` statement

The core idea behind writing tests is that we know what the expected output of the function (or more general, object) that we want to test is. So what we need to do is to *assert* that the actual output matches the expected one.

For problems like this, Python has got the built-in `assert` statement which takes to inputs: `True` or `False`. If provided with a condition that evaluates to `True`, nothing happens and the code execution continues. If provided with `False`, it raises an `AssertionError` exception and the execution flow is interrupted.

Try it for yourself:

```python
>>> assert True # This works
>>> assert False # This will raise an error
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-1-a871fdc9ebee> in <module>
----> 1 assert False

AssertionError: 
```

Now let's have a look at how to use this `assert` statement to write an actual test. Suppose we have the following function:

```python
def add_two(number: float) -> float:
    """ Adds  the number 2 to a given input float. """
    return number + 2
```

In order to test this function, we would use the assert statement as follows:

```python
>>> assert add_two(2) == 4
>>> assert add_two(0) == 2
```

We know what the expected outcome is, so here we assert that that's the case. Now imagine someone meddled with that function, and changed its behavior such that it no longer adds 2 to a given input. Then the `assert` statements would catch that.

This was a very simple example of how to use the `assert` statement. Now let's have a look at how we can build test cases from there.

### 3.2.2 Building unit tests

The general layout for tests within a package is to have a separate folder for tests within your project directory.

Take for example our `example_packages` directory:

```shell
example_packages/
    - example_package/
        - __init__.py
        - example_module.py
    - setup.py
    - tests/
        - tests.py # And more
```

Within the `tests` folder, we have one or more Python scripts that contain tests for each aspect of the package.

**NEED better examples!**

EXAMPLE: need to rework example_module a bit ... fill in a bit more code ... maybe this can be a simple numeric module? add two numbers, subtract? Ideally something more exciting than this.

This is what the `test_example_module.py` looks like:

```python
def test_add_two():
    assert condition_1
    assert condition_2

def test_subtract_two():
    assert condition_3
    assert condition_4()

def test_ ...?
```

Now that we have written a bunch of tests, perhaps the most straight-forward thing to do is to call all those functions in a row and make sure they all run smoothly. For exactly this purpose, there exist a series of Python modules which do exactly that for us - but automated and with lots of other nifty features.


#### 3.2.3 Running your tests - Python test suites

Among the most popular test runners for Python are:

- [unittest](https://docs.python.org/3/library/unittest.html)
- [nose or nose2](https://nose2.readthedocs.io/en/latest/getting_started.html)
- [pytest](https://docs.pytest.org/en/latest/)


`unittest` is part of Python's standard library, while the other two modules are add-ons that you can install via `pip`. Both `unittest` and `nose` require you to build classes for every test that inherit from `unittest` baseclasses and have their own implementation of the `assert` statement. `pytest` on the other hand can use the `assert` statement directly (while also being able to work with the `unittest` and `nose` syntax). This is why in this tutorial we concentrate on `pytest` only. You can check out this [comprehensive unit test tutorial](https://realpython.com/python-testing/) to learn more about the other two test runners.

#### 3.2.4 Using `pytest` to test your code

`pytest` ships with most Python distributions, but should you not already have it you can install it via

```shell
$ pip install pytest
```

Once installed, you can take a look at how it's used by typing:

```shell
$ pytest --help
usage: pytest [options] [file_or_dir] [file_or_dir] [...]
...
```

This will print out a comprehensive list of possible arguments and expressions for `pytest`. In the simplest case, you just need to navigate to the directory where the `tests/` folder lives and simply run

```shell
$ pytest
```

`pytest` will automatically enter the `tests/` folder and execute every function whose name matches the pattern `def test_*()`, and it will check every file that whose name matches the pattern `test*.py`.

Let's have a look at what `pytest` does in our example module. Recall our package structure:

```shell
** execute pytest here **
example_package/
    - __init__.py
    - example_module.py
setup.py
tests/
    -tests.py
```

TODO

```shell
$ pytest
... output
```

And this is what it looks like if a test is failing:

TODO

```shell
$ pytest
... output
```


## 3.3. Let there be linters

The term linting refers to the process of analysing source code in any language to flag possible programming errors, bugs and undesired stylistic constructions. A linter is a program or tool that does exactly  that.

You have probably already come across linters without even noticing it. They are built into many IDEs (Integrated Development Enviroment) and flag things like unequal numbers of brackets at the beginning or end of an instruction, or when you're trying to call a function with the wrong number of arguments. As such, they are incredibly useful in letting you know that your code won't run properly - even before you first tested it.

In addition to syntax testing, a linter can also provide feedback on stylistic elements: it can, for instance, detect duplicated code and recommend that you do some refactoring there. Or it can help you enforce certain style guide lines across a project, to manage, for example, naming conventions of functions and variables, or how doc-strings should be formatted. Therefore, *using a linter can help you enforce and maintain proper code quality.*

### 3.3.1 Choice of linter: the `pylint` module

Just as we had various choices for test runners, we also have several choices for linters in Python. Check out [this comprehensive tutorial]() for an overview and some background on linting in Python.

Here, we concentrate on `pylint`, a light-weight yet powerful package that integrates easily with many Python IDEs and ships with many Python distributions. If you haven't got it already you can install it via:

```shell
$ pip install pylint
```

To get an overview of how it works, simply type `pylint` into a terminal:

```shell
$ pylint
Usage:  pylint [options] modules_or_packages

  Check that module(s) satisfy a coding standard (and more !).

    pylint --help

  Display this help message and exit.
...
```

Let's have a look at an example. Consider our first example of the `quantum_measurement.py` function:

```python
import numpy as np

def M(rho, n=1):
    m = rho.shape[0]//2
    prjs =[np.kron(s[:, np.newaxis],s[:, np.newaxis].T)
        for s in np.eye(m * 2)]
    pr =[np.abs(np.trace(prj.dot(rho))) for prj in prjs]
    res= np.random.choice(
        [i for i in range(m*2)], n, p=pr)
    return [np.eye(m*2)[r,:] for r in res]
```

Here's how `pylint` rates our code:

```shell
$ pylint quantum_measurement_1.py
************* Module quantum_measurement_1
quantum_measurement_1.py:5:9: C0326: Exactly one space required after assignment
    prjs =[np.kron(s[:, np.newaxis],s[:, np.newaxis].T)
         ^ (bad-whitespace)
quantum_measurement_1.py:5:35: C0326: Exactly one space required after comma
    prjs =[np.kron(s[:, np.newaxis],s[:, np.newaxis].T)
                                   ^ (bad-whitespace)
quantum_measurement_1.py:6:0: C0330: Wrong continued indentation (add 3 spaces).
        for s in np.eye(m * 2)]
        ^  | (bad-continuation)
quantum_measurement_1.py:7:7: C0326: Exactly one space required after assignment
    pr =[np.abs(np.trace(prj.dot(rho))) for prj in prjs]
       ^ (bad-whitespace)
quantum_measurement_1.py:8:7: C0326: Exactly one space required before assignment
    res= np.random.choice(
       ^ (bad-whitespace)
quantum_measurement_1.py:10:0: C0304: Final newline missing (missing-final-newline)
quantum_measurement_1.py:10:25: C0326: Exactly one space required after comma
    return [np.eye(m*2)[r,:] for r in res]
                         ^ (bad-whitespace)
quantum_measurement_1.py:1:0: C0111: Missing module docstring (missing-docstring)
quantum_measurement_1.py:3:0: C0103: Function name "M" doesn't conform to snake_case naming style (invalid-name)
quantum_measurement_1.py:3:0: C0103: Argument name "n" doesn't conform to snake_case naming style (invalid-name)
quantum_measurement_1.py:3:0: C0111: Missing function docstring (missing-docstring)
quantum_measurement_1.py:4:4: C0103: Variable name "m" doesn't conform to snake_case naming style (invalid-name)
quantum_measurement_1.py:7:4: C0103: Variable name "pr" doesn't conform to snake_case naming style (invalid-name)

--------------------------------------------------------------------
Your code has been rated at -8.57/10
```

So overall you can tell that `pylint` isn't very  happy with our code. It even gave us a negative overall score. Note that point ratings just get added up and we could in principle disable negative scores by capping it at zero. Let's leave it at that for now though. The goal is, unsurprisingly, to reach 10/10.

Let's have a look at what those messages mean. We can get some information on each category of `pylint` messages by using the `--help-message` argument in the terminal:

**Missing docstring**

```shell
$ pylint --help-message=missing-docstring
:missing-docstring (C0111): *Missing %s docstring*
  Used when a module, function, class or method has no docstring.Some special
  methods like __init__ doesn't necessary require a docstring. This message
  belongs to the basic checker.
```

`pylint` requires you to add doc-strings to modules, classes and functions, and flags an error if it can't find them.

**Bad whitespace**

```shell
$ pylint --help-message=bad-whitespace
:bad-whitespace (C0326): *%s space %s %s %s*
  Used when a wrong number of spaces is used around an operator, bracket or
  block opener. This message belongs to the format checker.
```

Whitespaces are a notorious issue of discussion in Python, in particular because the entire programming syntax relies on indentation. However, what `pylint` is telling us here is that it expects whitespaces after assignments and commas, which is in fact quite reasonable - in Latex or just normal written texts you also use spaces between words and punctuation to improve readability.

**Invalid name**

```shell
$ pylint --help-message=invalid-name
:invalid-name (C0103): *%s name "%s" doesn't conform to %s*
  Used when the name doesn't conform to naming rules associated to its type
  (constant, variable, class...). This message belongs to the basic checker.
```

Per default, `pylint` abides to fairly well defined naming conventions for constants, variable, function and class names. To figure out `pylint` is expecting exactly we can re-run the linter with the additional argument `--include-naming-hint=y`, to find that function and variable names are being matched to the following regular expression:

`(([a-z_][a-z0-9_]{2,})|(_[a-z0-9_]*)|(__[a-z][a-z0-9_]+__))$'`

If you haven't come across regular expressions before, all this means is that function and variable names should have only have lower case letters, numbers and underscores and consist of at least 2 letters. 

TODO: Alan can you check this.


### 3.3.2 Don't agree with `pylint`? Make your own rules

If you find some of the stylistic requirements of the default `pylint` configuration unreasonable or too cumbersome, or you would like to enforce additional, custom style codes then you can do so by editing the `.pylintrc` file. This file contains the default configuration for the linter and it is generated automatically when installing `pylint`.

At any point, you can ask `pylint` to generate a copy of this file for you that you can customise as desired.

## \*\*\*\* PROBLEM: DIY linting (5-10 minutes) \*\*\*\*

Create and edit a `.pylintrc` file. Open a terminal and type:

```shell
$ pylint --generate-rcfile > .pylintrc
```

This will create a file called `.pylintrc` in the current directory. Open the file in your favourite editor and take a look.

Find the the list of disabled messages under the `[MESSAGES CONTROL]` section, and add `bad-whitespace` to this list. Then re-run the linter using this file as follows:

```shell
$ pylint quantum_measurement.py --rcfile=<path-to-your-.pylintrc>
```

**Optional:** Can you find the expression that `pylint` uses to calculate the score and cap it at zero?

## \*\*\*\*


# 6. Controlling revision history with git

When you develop a piece of code, be it in Python, Matlab, Latex, or whatever else, over time you will find yourself making changes to that code, to improve, expand or simply just change the behavior of it.

How do you keep track of different versions of your code there?

If you're a newbie to programming, chances are you might have used different files, e.g. `my_awesome_code_v0.py`, `my_awesome_code_v1.py` and so on. While this may work in a small capacity, it certainly doesn't scale well for larger projects or when multiple people are working on the same project together and you want to keep track of who did what and when.

For this reason, there exist so-called version control managers. These are programs that keep track of revision history of text-based files, allow you to store comments alongside of every revision iteration,and enable you to easily compare or switch back to older versions if required.

By far the most popular choice for this is Git, which is an incredibly powerful, well-maintained, open-source project originially started by Linus Torvalds (creator of the Linux operating kernel).

Git is cross-platform compatible and can be used with or without GitHub, which is an online platform that integrates Git into an online host for code projects. In order to use GitHub, you need a GitHub account. To use Git, you merely need to provide Git with some user information (like name and email) for it to keep track of what changes were made by your identity.

## 6.1 Using Git in the command line

For this tutorial, we have installed [Git for Windows](https://git-scm.com/download/win) on the lab computers, which ships with its own Bash console.

Open the Git Bash console and type `git` to get an overview of how to use it:

```bash
$ git
usage: git [--version] [--help] [-C <path>] [-c name=value]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index
```

At any point in time, you can call `git --help` to get more information, and, in particular, you can also call `--help` on a specific command to see how it works.

Let's walk through an example of how to initialise a Git project, or, to be more specific, a *repository* as Git-speak would have us call it.

### Step 1: Create an empty repository

Open a Git Bash console, create a new folder and initialise an empty repository:

```bash
$ mkdir my_git_repo
$ cd my_git_repo
$ git init
```

This should print something like `Initialized empty Git repository in ../../my_git_repo/.git/`. And if you have a look into the folder, you will find that Git created a new folder called `.git` (you might have to enable the viewing of hidden files in your explorer). In this folder, Git stores information about all the files in the repository.

At any point in time, you can call `git status` in that repository to see what's going on in the repository.

### Step 2: Add a new file for tracking

Now that we have the repository set up, let's create a file and add it to the file tracking index.

Create a simple file called `my_file.txt` or similar, and add a few lines of text to it:

```shell
# my_file.txt
This is a text file.
We will track its revision history with git.
```
Now go back to Git Bash and type:

```bash
$ git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	my_file.txt

nothing added to commit but untracked files present (use "git add" to track)
```

You can see that Git recognised that a new file was added to the repository, but it's telling us that the file is currently "untracked". Let's add this file to tracking via:

```bash
$ git add my_file.txt
```

Now if we print out `git status` again we should see the following:

```bash
$ git status
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   my_file.txt
```

Git has now added the file to its tracking system and expects us to *commit* the file. Committing a file means that we are saving its current status as a checkpoint in the version history. To commit our file, we run:

```bash
$ git commit -m "My first version of my_file.txt"
[master (root-commit) eb42456] My first version of my_file.txt
 1 file changed, 2 insertions(+)
 create mode 100644 my_file.txt
```

If you haven't set up a Git identiy yet, Git will at this stage ask you who you are. Follow the command prompts to provide a name and email address, and then run the command above again.

Now if we run `git status` again, we should see the following:

```bash
$ git status
On branch master
nothing to commit, working directory clean
```


### \*\*\*\* PROBLEM: Change the file, add and commit (5 minutes)\*\*\*\*

Now let's make a change to our file, and then add and commit the new version. Check the output of `git status` between the different stages.

Then have a look at the output of `git log`.

### \*\*\*\*

There are a variety of options to compare different versions of a file, the most convenient ones are when using code editors that integrate with Git, like VSCode for example. GitHub too allows for a user-friendly comparison. Git also allows us to go back in time to specific versions of the code, but we won't go into much more detail on this at this stage.


# 7. Using GitHub to share code and collaborate

GitHub allows us to host our repositories online, which is a great way of collaborating or publishing code projects. To get started on an online repository you can:

- Upload an existing repository from your local machine
- Download an existing repository from GitHub

Here we will walk through an example of downloading an existing repository, making a change to it (add and commit that change), and then uploading this change to the online repository.

**TODO** Example with two_qubit_simulator. Make a new branch. Make a change to that branch. Push to remote. Make a Pull Request (Use protected branch)!

# 8. Code project

**Note: to participate in this project you will need a GitHub account.**

Now that we have covered how to build Python packagaes and how to work on Python projects on GitHub, let's all collaborate together and build a Python package that can simulate one and two qubit quantum circuits.

We build a skeleton for this package and your task is to write the content and tests for it.

The package is structured as followed:

```shell
two_qubit_simulator/
    - __init__.py
    - quantum_register.py
    - quantum_circuit.py
    - quantum_gates/
        - __init__.py
        - quantum_gate.py
        - hadamard.py
        - cnot.py
        - ...
tests/
    - test_quantum_register.py
    - test_quantum_circuit.py
    - test_quantum_gates.py
setup.py
README.md
.pylintrc
```

The project is hosted here:

[link to github repo]

Start by making a local clone of the repository and create your own branch. Depending on what part of the project you decide to work on, give your branch a descripitve name.

The plan is to divide the project into the following parts:

- Write the `quantum_register.py` module + tests
- Write the `quantum_circuit.py` module + tests
- Write the `quantum_gates` module + tests
- Write documentation and usage examples

The `README.md` file contains information of how the individual modules are expected to work. Once you finished writing (and testing!) a piece of your code, make a pull request to the `development` branch. Any PR made to this branch will have to pass the automated tests and linting before it can be merged. We encourage all of you to review each others PRs.


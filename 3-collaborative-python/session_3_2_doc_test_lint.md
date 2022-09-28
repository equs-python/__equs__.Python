# \_\_equs\_\_.Python workshop 2019
## Day 1 - Python modules and Git


# 2. Documentation, unit testing and linting (1 hour)

    “Code is more often read than written.”

    — Guido van Rossum

Guido van Rossum, the creator of the Python programming language made this very simple, yet incredibly meaningful statement above.

What we take from this is that it is immensely important *how* you write your code - be it for yourself or for other people. Have you ever found yourself in a situation where you had to use a piece of code that you've written many months ago (without documentation), and puzzled over what the code does? Or even worse, have you perhaps changed an auxiliary file, or upgraded your compiler/interpreter since then and now the old code doesn't run anymore? Or have you ever worked on a project collaboratively and found it extremely difficult to make out what other people's code is doing?

For all of those reasons, there exist coding standards - these are a collection of good practices which - when taken to heart - make each and every one of us a better person. Here we want to give you an overview of the three main components of those standards: documentation, testing and linting. And because this is a Python workshop, we use the official [PEP8 Python style guide](https://www.python.org/dev/peps/pep-0008/).


## 2.1 Let there be documentation (15 minutes)

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

*(You can find this file under examples/doc_test_lint/)*

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

### 2.1.1 Code should be readable on its own

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

### 2.1.2 Comments explain why, code explains how

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

### 2.1.3 Write documentation

Many people, especially those new to programming, or those working mainly on their own, stop after adding in-line comments to their code. However, as soon as a project becomes bigger or has multiple people working on or using it, writing proper documentation is crucial.

In Python (and other programming languages), it is common practice to write so-called *docstrings*. A docstring, as the name suggests, is a string that contains documentation. These are typically spread over multiple lines and every function, class and module in Python should have one - and in fact already *has* one, implicitly. This can be exposed using a special attribute called `__doc__`, that every Python object has.

Let's have a look! Open a console and type:

```python
>>> print(len.__doc__)
Return the number of items in a container.

```

This is the docstring of the built-in `len` function in Python. When you write your own function, you can give it a docstring by inserting a (optionally) multi-line string right below the `def` statement:

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

#### 2.1.3.1 What goes into a docstring?

A docstring should explain what the function/class/module is used for, and how it is used. In very simple cases, it is sufficient to provide a single line docstring, like for example in the `len` function.

Broadly speaking, for more complex Python functions (or classes), docstrings should contain the following:

-  Brief explanation of the object and its purpose
-  Enumerated description of inputs and outputs
-  Any exceptions that are raised
-  Examples
-  Further notes and comments

Under these considerations, this is how we would write a docstring for our `measure_state` function:

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

There are several different style guides for docstrings. Among the most commonly used styles are:

- [Google docstrings](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings)
- [NumPy docstrings](https://numpydoc.readthedocs.io/en/latest/format.html)
- [reStructured Text docstrings](http://docutils.sourceforge.net/rst.html)


#### 2.1.3.2 New feature in Python 3.5+: type hinting

In Python version 3.5, the [typing](https://docs.python.org/3/library/typing.html) module was introduced which provides syntactic means to display input and output types - as is common practice in many other (typed) languages.

Here is an example from the module documentation:

```python
def greeting(name: str) -> str:
    return 'Hello ' + name
```

Here, the function expects a string as input, and returns a string. Note that this is merely an annotation, you can still call the function with a different input type or change the return type of the function without getting into trouble. However, it definitely is quite neat and useful for documentation purposes.

  
## 2.2. Let there be tests (25 minutes)

It goes without saying that every code that you plan to put to use needs to be tested. Chances are you are already doing this - even if perhaps not in an automated fashion. Here we take a look at how to write automated tests, structure them, and what modules we have got available in Python to run those tests.

### 2.2.1 Testing basics: the `assert` statement

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

### 2.2.2 Building unit tests

The general layout for tests within a package is to have a separate folder for tests within your project directory.

For example:

```shell
top_level_direcory/
    - my_package/
        - __init__.py
        - my_module_1.py
        - my_module_2.py
        - ...
    - setup.py
    - tests/
        - test_my_module_1.py
        - test_my_module_2.py
        - ... # You can never have too many tests!
```

Within the `tests` folder, we have one or more Python scripts that contain tests for each aspect of the package. A common way to organise tests is to create separate test files for the separate modules in your package.


### Example: bulding tests for `measure_state`

As an example, let's build some tests for the `measure_state` function from the documentation section. Before writing a test, you should think about:

- What is the simplest example for how my function should work?
- What are the edge cases?

In our example, perhaps the simplest case would be the measurement of a pure state in the z-basis - this should always return the input state because that's the basis we're measuring in. So a test for this could look like this:

```python
# test_measurement.py
def test_pure_state_measurement():
    """ Testing the measurement of a pure state in Z """
    # Test 1: State |0>, one measurement
    state = np.array([[1, 0], [0, 0]])
    expected_result = np.array([1, 0])
    actual_result = measure_state(state, number_of_samples=1)

    # Numpy's version of the assert statement for arrays
    assert np.allclose(expected_result, actual_result)

    # Test 2: State |1>, one measurement
    state = np.array([[0, 0], [0, 1]])
    expected_result = np.array([0, 1])
    actual_result = measure_state(state, number_of_samples=1)

    assert np.allclose(expected_result, actual_result)
```

Where we have used the `np.allclose` function that takes two `numpy` arrays as input and returns `True` when all elements are equal (that is, up to numeric precision), and `False` if that's not the case.

Now the next thing we might do is to test that this outcome is reliable under our random sampling. So let's write another test that tests the statistics of a pure state measurement in z:

```python
# test_measurement.py
def test_pure_state_measurement_stats():
    """ Testing the measurement of a pure state in Z """
    # Test 1: State |0>, 100 measurements
    state = np.array([[1, 0], [0, 0]])
    expected_result = np.array([1, 0])
    actual_results = measure_state(state, number_of_samples=100)

    for actual_result in actual_results:
        assert np.allclose(expected_result, actual_result)
```

Now let's think about edge cases. If we measure a maximally mixed state in the z-basis, then we should get either outcome 50% of the time. So let's write a test for that too:

```python
# test_measurement.py

def test_mixed_state_measurement_stats():
    """ Testing the statistics of a maximally mixed state
        measurement in Z
    """
    # State (|0> + |1>)/sqrt(2), 5000 measurements
    state = np.array([[0.5, 0.5], [0.5, 0.5]])
    number_of_samples = 5000
    actual_results = measure_state(
        state, number_of_samples=number_of_samples
    )
    # Count how often the |0> and |1> state were measured
    _, counts = np.unique(
        actual_results, return_counts=True, axis=0
    )
    tolerance = 0.05
    assert abs(counts[0] / number_of_samples - 0.5) < tolerance
```

Here we're applying a common trick to test whether two numbers are close: we specified an acceptable tolerance and check that our outcome is close to the target value (here 0.5).

Now that we have written a bunch of tests, perhaps the most straight-forward thing to do is to call all those functions in a row and make sure they all run smoothly. But this is a bit cumbersome and we don't want to do this everytime we change our code. For exactly this purpose, there exist a series of Python modules which do exactly that for us - but automated and with lots of other nifty features.


#### 2.2.3 Running your tests - Python test suites

Among the most popular test runners for Python are:

- [unittest](https://docs.python.org/3/library/unittest.html)
- [nose or nose2](https://nose2.readthedocs.io/en/latest/getting_started.html)
- [pytest](https://docs.pytest.org/en/latest/)


`unittest` is part of Python's standard library, while the other two modules are add-ons that you can install via `pip`. Both `unittest` and `nose` require you to build classes for every test that inherit from `unittest` baseclasses and have their own implementation of the `assert` statement. `pytest` on the other hand can use the `assert` statement directly (while also being able to work with the `unittest` and `nose` syntax). This is why in this tutorial we concentrate on `pytest` only. You can check out this [comprehensive unit test tutorial](https://realpython.com/python-testing/) to learn more about the other two test runners.

#### 2.2.4 Using `pytest` to test your code

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

`pytest` will automatically enter `tests/` folders, look through every modules whose name matches the pattern `test*.py`, and execute every function whose name matches the pattern `def test_*()`.



## \*\*\*\* PROBLEM: Run `pytest` (5 minutes) \*\*\*\*

Open a terminal, navigate to the `examples/doc_test_lint/` directory and run:

```shell
$ pytest
============================= test session starts ==============================
platform linux -- Python 3.7.1, pytest-4.0.2, py-1.7.0, pluggy-0.8.0
rootdir: /home/virginia/Documents/python_workshop_19/general-content/day-1-python-modules-and-git/examples/doc_test_lint, inifile:
collected 3 items                                                              

test_measurement.py ...                                                  [100%]

=========================== 3 passed in 0.10 seconds ===========================
```

The output should look something like the above. Now modify one or more tests such that they fail, and rerun `pytest` on that.


## \*\*\*\*

## 2.3. Let there be linters (15 minutes)

The term linting refers to the process of analysing source code in any language to flag possible programming errors, bugs and undesired stylistic constructions. A linter is a program or tool that does exactly  that.

You have probably already come across linters without even noticing it. They are built into many IDEs (Integrated Development Enviroment) and flag things like unequal numbers of brackets at the beginning or end of an instruction, or when you're trying to call a function with the wrong number of arguments. As such, they are incredibly useful in letting you know that your code won't run properly - even before you first tested it.

In addition to syntax testing, a linter can also provide feedback on stylistic elements: it can, for instance, detect duplicated code and recommend that you do some refactoring there. Or it can help you enforce certain style guide lines across a project, to manage, for example, naming conventions of functions and variables, or how docstrings should be formatted. Therefore, *using a linter can help you enforce and maintain proper code quality.*

### 2.3.1 Choice of linter: the `pylint` module

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
$ pylint measurement_1.py
************* Module measurement_1
measurement_1.py:13:9: C0326: Exactly one space required after assignment
    prjs =[np.kron(s[:, np.newaxis],s[:, np.newaxis].T)
         ^ (bad-whitespace)
measurement_1.py:13:35: C0326: Exactly one space required after comma
    prjs =[np.kron(s[:, np.newaxis],s[:, np.newaxis].T)
                                   ^ (bad-whitespace)
measurement_1.py:14:0: C0330: Wrong continued indentation (add 3 spaces).
        for s in np.eye(m * 2)]
        ^  | (bad-continuation)
measurement_1.py:15:7: C0326: Exactly one space required after assignment
    pr =[np.abs(np.trace(prj.dot(rho))) for prj in prjs]
       ^ (bad-whitespace)
measurement_1.py:16:7: C0326: Exactly one space required before assignment
    res= np.random.choice(
       ^ (bad-whitespace)
measurement_1.py:18:0: C0304: Final newline missing (missing-final-newline)
measurement_1.py:18:25: C0326: Exactly one space required after comma
    return [np.eye(m*2)[r,:] for r in res]
                         ^ (bad-whitespace)
measurement_1.py:11:0: C0103: Function name "M" doesn't conform to snake_case naming style (invalid-name)
measurement_1.py:11:0: C0103: Argument name "n" doesn't conform to snake_case naming style (invalid-name)
measurement_1.py:11:0: C0111: Missing function docstring (missing-docstring)
measurement_1.py:12:4: C0103: Variable name "m" doesn't conform to snake_case naming style (invalid-name)
measurement_1.py:15:4: C0103: Variable name "pr" doesn't conform to snake_case naming style (invalid-name)

--------------------------------------------------------------------
Your code has been rated at -7.14/10
```

So overall you can tell that `pylint` isn't very  happy with our code. It even gave us a negative overall score. Note that point ratings just get added up and we could in principle disable negative scores by capping it at zero. Let's leave it at that for now though, but note that the goal -unsurprisingly- is to reach 10/10.

Let's have a look at what those messages mean. We can get some information on each category of `pylint` messages by using the `--help-message` argument in the terminal:

**Missing docstring**

```shell
$ pylint --help-message=missing-docstring
:missing-docstring (C0111): *Missing %s docstring*
  Used when a module, function, class or method has no docstring.Some special
  methods like __init__ doesn't necessary require a docstring. This message
  belongs to the basic checker.
```

`pylint` requires you to add docstrings to modules, classes and functions, and flags an error if it can't find them.

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


### 2.3.2 Don't agree with `pylint`? Make your own rules

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

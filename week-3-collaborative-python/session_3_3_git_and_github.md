# \_\_equs\_\_.Python workshop 2019
## Day 1 - Python modules and Git


# 3. Controlling revision history with git (30 minutes)

When you develop a piece of code, be it in Python, Matlab, Latex, or whatever else, over time you will find yourself making changes to that code, to improve, expand or simply just change the behavior of it.

How do you keep track of different versions of your code there?

If you're a newbie to programming, chances are you might have used different files, e.g. `my_awesome_code_v0.py`, `my_awesome_code_v1.py` and so on. While this may work in a small capacity, it certainly doesn't scale well for larger projects or when multiple people are working on the same project together and you want to keep track of who did what and when.

For this reason, there exist so-called version control managers. These are programs that keep track of revision history of text-based files, allow you to store comments alongside of every revision iteration,and enable you to easily compare or switch back to older versions if required.

By far the most popular choice for this is Git, which is an incredibly powerful, well-maintained, open-source project originially started by Linus Torvalds (creator of the Linux operating kernel).

Git is cross-platform compatible and can be used with or without GitHub, which is an online platform that integrates Git into an online host for code projects. In order to use GitHub, you need a GitHub account. To use Git, you merely need to provide Git with some user information (like name and email) for it to keep track of what changes were made by your identity.

## 2.1 Using Git in the command line

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


### \*\*\*\* PROBLEM: Change the file, add and commit (10 minutes)\*\*\*\*

Now let's make a change to our file, and then add and commit the new version. Check the output of `git status` between the different stages.

Then have a look at the output of `git log`.

### \*\*\*\*

There are a variety of options to compare different versions of a file, the most convenient ones are when using code editors that integrate with Git, like VSCode for example. GitHub too allows for a user-friendly comparison. Git also allows us to go back in time to specific versions of the code, but we won't go into much more detail on this at this stage.


## 2.2 Using GitHub to share code and collaborate

GitHub allows us to host our repositories online, which is a great way of collaborating or publishing code projects. To get started on an online repository you can:

- Upload an existing repository from your local machine
- Download an existing repository from GitHub

## **** Problem: Upload your project to GitHub (15 minutes) ***

Upload the repository that you've made in the previous problem to GitHub.

- Make a GitHub account
- Follow the instructions on GitHub to upload your local repository
 
## ****

Now we will walk through an example of downloading an existing repository, making a change to it (add and commit that change), and then uploading this change to the online repository.

For this demonstration, we will use the remote repository hosted here:

[https://github.com/equs-python/two-qubit-simulator](https://github.com/equs-python/two-qubit-simulator)

Note that this will also form our coding project for the afternoon.

## **** Problem: Fork the two-qubit-simulator repository (5 minutes) ***

Make your own fork of the repository linked above.
 
## ****

And now we begin by making a local copy of this repository. In Git-speak this is called *cloning*.

```bash
$ git clone https://github.com/<your-user-name>/two-qubit-simulator
Cloning into 'two-qubit-simulator'...
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 385 (delta 0), reused 5 (delta 0), pack-reused 378
Receiving objects: 100% (385/385), 49.42 KiB | 0 bytes/s, done.
Resolving deltas: 100% (223/223), done.
Checking connectivity... done.
```

This will create a local folder on our computer into which the entire repository content is copied. Now we navigate into the repository, and ask for a `git status`:

```bash
$ git status
On branch master
nothing to commit, working directory clean
```

## **** Problem: Add a new feature (25 minutes) ***

Now we have the project code locally. Before we start developing any code, let's install the package using:

```bash
$ python setup.py develop
```

And this should install the package for us. To start making modifications, the first thing we do is to create a separate branch for our work, like so:

```bash
$ git checkout -b new_feature
Switched to a new branch 'new_feature'
```

A branch in Git is like a separate code-base - at the time the branch is created it has the exact same files and code as the base branch (`master`) but when we make changes to those files they won't be reflected in `master`. This is very useful for when you'd like to incorporate a new feature into an existing project without compromising the working code base.

Now let's make change to the code in our `new_feature` branch. We want to add a file called `utilities.py` in which we can store some useful functions for our project. The first function we want to add is a conjugate transpose method.

```python
"""
# utilities.py
Contains utility functions for the two_qubit_simulator module
"""
import numpy as np

def conjugate_transpose(array):
    """ Calculates the conjugate transpose of an array

        Parameters
        -------
        array : numpy ndarray
            The array to be transposed
        
        Returns
        -------
        numpy ndarray
            The conjugate transpose of the input array
    """
    return np.conjugate(
        np.transpose(array)
    )
```

Now let's add and commit this file to our branch.

```bash
$ git add .
$ git commit -m "Added utilities module with conjugate transpose"
```

At this point, let's quickly check back into the master branch to see that the change we made here has not taken place in master:

```bash
$ git checkout master
```

And then we switch back to our branch using the same command.

```bash
$ git checkout new_feature
```

Now before we are finished with our new feature, we need to make two more changes: 1. we need to add our function to the `__init__.py` file, and we need to write a test for it.

```python
"""
# __init__.py
Initialise the two_qubit_simulator module.
Add import statements from auxilirary modules here.
"""
from .utilities import conjugate_transpose
```

And to add a test for our function, we create a new file called `test_utilities.py` in the `tests/` folder, into which we write a simple test:

```python
"""
# test_utilities.py
Test the functions in the utilities module
"""
from two_qubit_simulator import conjugate_transpose

def test_conjugate_transpose():
    # Test with real-valued array
    test_array_1 = np.array([[1, 2], [3, 4]])
    assert np.allclose(
        conjugate_transpose(test_array_1),
        np.array([[1, 3], [2, 4]])
    )
    # Test with complex-valued array
    test_array_1 = np.array([[1j, 2], [1j, 4]])
    assert np.allclose(
        conjugate_transpose(test_array_1),
        np.array([[-1j, -1j], [2, 4]])
    )
```

Once that's done, let's run `pylint` and `pytest` and when those two things pass, we are ready to publish our changes!

```bash
$ pylint two_qubit_simulator --rcfile=.pylintrc
-------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

If nothing went wrong, this is what we should see for the linting. And for the testing:

```bash
$ pytest
============================= test session starts ==============================
platform linux -- Python 3.7.1, pytest-4.0.2, py-1.7.0, pluggy-0.8.0
rootdir: /home/virginia/Desktop/two-qubit-simulator, inifile:
collected 4 items                                                              

tests/test_circuits.py .                                                 [ 25%]
tests/test_gates.py .                                                    [ 50%]
tests/test_qubit_register.py .                                           [ 75%]
tests/test_utilities.py .                                                [100%]

=========================== 4 passed in 0.08 seconds ===========================
```

As soon as both tests and linting passed, we are ready to add our feature to the project. For this, we're first going to upload our changes to the remote repository. In Git-speak, this is called `pushing`.

```bash
$ git push --set-upstream-origin new_feature
```

Here we push our changes to a new branch online. We only need to do this once. For any further changes we want to upload we just use `git push`.

Now let's have a look on the project page!

[https://github.com/equs-python/two-qubit-simulator](https://github.com/equs-python/two-qubit-simulator)

In order to merge our changes into the `master` branch, we open a *Pull Request*, or PR for short. This will run `pytest` and `pylint` for us, and only if those tests pass will we be allowed to merge the PR. Moreover, the `master` branch also requires PRs to be reviewd and accepted by one of the repository administrators. We will go through this procedure online.
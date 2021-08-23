# Intro

These are some very general instructions that may or may not work for your own particular machine. If you're having problems feel free to ask and someone will try to give you a hand. 

# Linux

## Python Setup

### Option 1: Default Python
For python on debian derived distros:

```
sudo apt-get install python
```

And to get pip:

```
sudo apt-get install python-pip
```

This may fail to get the correct Python version on some older distro releases. In this case using a python environment manager like anaconda or pyenv is suggested.

### Option 2: Anaconda/Miniconda
You can download an installation script for either anaconda or the lighter weight miniconda from (here)[https://www.anaconda.com/download/]. When prompted at the end of your installation, let anaconda modify your .bashrc file.

Re-load your bashrc file using 

```
source ~/.bashrc
```

And you should be up and running.

### Option 3: Pyenv
Pyenv manages a separate Python environment on a per-subdirectory basis. This makes development and maintaining different versions of Python across different directories much easier than swapping between environments using conda.

## Git setup

For ubuntu based distros:

```
sudo apt-get install git
```
Other distros should have a similar package in their package manager.


## Python Packages

We're going to need a few Python packages for today, they are:

```
ipython
numpy
matplotlib
seaborn
jupyter
qiskit
```

### Option 1: pip
pip is the default Python package manager. We'll be installing to the local user's Python environment in order to avoid any permissions issues.

```
pip install --user ipython matplotlib numpy jupyter
```

This is generally a good idea to avoid conflicts with any other package managers you might have.

### Option 2: conda
If you've used an anaconda or miniconda install you can also use the conda package manager. This shouldn't conflict with pip but sometimes has more recent releases (which may include essential bugfixes).

```
conda install ipython matplotlib numpy jupyter
```

# Mac

## Brew Setup (Optional)
[Homebrew](https://brew.sh) is a package manager for Mac. Using this will likely make the installation process much easier, but you can still do it manually if you want. 

## Python Setup

Obviously Python is important for a Python workshop, you can check if you already have Python by opening a terminal using 'spotlight' (Command + Spacebar and type in `terminal`) and entering the command:

```
python --version
``` 
If the version is 3.6 or above then you're all set. If nothing comes up then you need to install Python. If you've already installed Python and nothing is coming up then you likely need to add it to your system path.

If you instead see Python 2 then you can check if Python 3 is installed using:
```
python3 --version
```

If this is the case then we can alias `pip` and `python` to Python 3 in your `.bashrc` file or equivalent.

```
alias python='python3'
alias pip='python3 -m pip'
```

### Option 1: Brew Python

Open a terminal (Cmd+Space, type 'terminal', hit Return) and then run:

```
brew install python
```

### Option 2: Anaconda

Go to the [Anaconda download page](https://www.anaconda.com/download/#macos) and download the installer for Python 3.7. Run the installer.

### Option 3: Python

Go to the [Python.org download page](https://www.python.org/downloads/) and download the latest installer. Run the installer.

## Git Setup

You should already have git installed. If not, please ask for help!

## Python Packages
We're going to need a few Python packages for today, they are:

```
ipython
numpy
matplotlib
jupyter
seaborn
```

### Option 1: pip
pip is the default Python package manager. We'll be installing to the local user's Python environment in order to avoid any permissions issues.

```
pip install --user ipython matplotlib numpy jupyter
```

This is generally a good idea to avoid conflicts with any other package managers you might have.

If pip works but the packages do not appear when you invoke python then you may have a separate Python 2 and Python 3 installation. There are a few different fixes for this:

To directly invoke Python 3's pip you can:
```
pip3 install --user <packages>
```

Or use a particular python to invoke pip you can:

```
python -m pip install --user <packages>
```

Lastly you can alias the first command in your bashrc file (or equivalent depending on what shell you are using):

```
alias pip='python -m pip'
```


### Option 2: conda
If you've used an anaconda or miniconda install you can also use the conda package manager. This shouldn't conflict with pip but sometimes has more recent releases (which may include essential bugfixes).

```
conda install ipython matplotlib numpy jupyter
```


# Windows

## Chocolatey Setup [Optional]
Chocolatey is a package manager for Windows, using this will likely make the installation process much easier, but you can still do it manually if you want. 

You can setup chocolatey using the instructions from (here)[https://chocolatey.org/install].

## Python Setup
Obviously Python is important for a Python workshop, you can check if you already have Python by opening a terminal (Window + R then type in cmd.exe) and entering

```
python --version
``` 
If the version is 3.6 or above then you're all set. If nothing comes up then you need to install Python. If you've already installed Python and nothing is coming up then you likely need to add it to your system path.

### Python Option 1: Chocolatey
If you have chocolatey then this is pretty easy. 

```
choco install python
```

Once the installation has finished, close and re-open your terminal and see if Python is working.
If it's not then you might need to add it to your system path. This can be done using the `SETX` command.

```
SETX PATH "%PATH%;C:\<path to Anaconda>\scripts;C:\<path to anaconda>"
```

You will need to close and re-open your terminal for the changes to be loaded.

### Python Option 2: Chocolatey Anaconda / Miniconda

Anaconda is a Python package manager and environment manager all in one. If you have Chocolatey you can install it instead of the default Python with:
```
choco install anaconda3 
```

If you want the minimalist version with fewer default packages, then you can use miniconda instead.

```
choco install miniconda3 
```

Once the installation has finished, close and re-open your terminal and see if Python is working.
If it's not then you might need to add it to your system path. This can be done using the `SETX` command.

```
SETX PATH "%PATH%;C:\<path to Anaconda>\scripts;C:\<path to anaconda>"
```

You will need to close and re-open your terminal for the changes to be loaded.

You may want to later set up some proper conda environments, but for now we will simplify matters by using the default environment.

### Python Option 3: Direct install 
If you're not going down the Chocolatey route, you can instead pick install Python directly from (here)[https://www.python.org/downloads/]. When prompted, make sure that you add anaconda to your PATH environment variable.
This can be done using the `SETX` command.

```
SETX PATH "%PATH%;C:\<path to python>\scripts;C:\<path to python>"
```

You will need to close and re-open your terminal for the changes to be loaded.


### Python Option 4: Anaconda / Miniconda
And if you prefer the direct download of anaconda or miniconda you can get it from (here)[https://www.anaconda.com/download/]. You may need to manually add this to your PATH environment variable. 

This can be done using the `SETX` command.

```
SETX PATH "%PATH%;C:\<path to Anaconda>\scripts;C:\<path to anaconda>"
```
You will need to close and re-open your terminal for the changes to be loaded.

You may want to later set up some proper conda environments, but for now we will simplify matters by using the default environment.

## Python package setup

We're going to need a few Python packages for today, they are:

```
ipython
numpy
matplotlib
jupyter
seaborn
qiskit
```

### Option 1: pip
pip is the default Python package manager. We'll be installing to the local user's Python environment in order to avoid any permissions issues.

```
pip install --user ipython matplotlib numpy jupyter
```

This is generally a good idea to avoid conflicts with any other package managers you might have.


### Option 2: conda
If you've used an anaconda or miniconda install you can also use the conda package manager. This shouldn't conflict with pip but sometimes has more recent releases (which may include essential bugfixes).

```
conda install ipython matplotlib numpy jupyter
```

### Option 3: Build from source
If you've having a particularly bad day you may need to build from source. This will almost never happen and is merely mentionned for completeness. 

## Git setup

We're going to need a git client, the easiest way to do this is git bash for windows. 

### Git Option 1: Chocolatey
As before we can use chocolatey to install git for windows. 

```
choco install git 
```

### Git Option 2: Direct installation
Alternatively, you can manually install it from (here)[https://gitforwindows.org/].


## Python Packages

We're going to need a few Python packages for today, they are:

```
ipython
numpy
matplotlib
seaborn
jupyter
qiskit
```

### Option 1: pip
pip is the default Python package manager. We'll be installing to the local user's Python environment in order to avoid any permissions issues.

```
pip install --user ipython matplotlib numpy jupyter
```

This is generally a good idea to avoid conflicts with any other package managers you might have.
If this is failing with pip not being detected then you've got another system path issue. One quick fix is to instead run:

```
python -m pip install --user <packages>
```
In the longer term you will want to add pip to your system path.

### Option 2: conda
If you've used an anaconda or miniconda install you can also use the conda package manager. This shouldn't conflict with pip but sometimes has more recent releases (which may include essential bugfixes).

```
conda install ipython matplotlib numpy jupyter
```




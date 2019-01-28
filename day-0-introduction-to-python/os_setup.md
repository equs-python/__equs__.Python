# Intro

These are some very general instructions that may or may not work for your own particular machine. If you're having problems feel free to ask and someone will try to give you a hand. 

# Windows
These instructions are for if you have brought your own windows machine. If you're using the lab computer and want to use Windows then you should already be set.

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
If it's not then you might need to add it to your system path.

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
If it's not then you might need to add it to your system path.

### Python Option 3: Direct install 

(here)[https://www.python.org/downloads/]


### Python Option 4: Anaconda / Miniconda
(here)[https://www.anaconda.com/download/]

## Python package setup

### Option 1: pip
pip is the default Python package manager 

### Option 2: conda
If you've used an anaconda or miniconda install you can also use the conda package manager. This shouldn't conflict with pip but sometimes has more recent releases (which may include essential bugfixes).

### Option 3: Build from source
If you've having a particularly bad day you may need to build from source. This will almost never happen 

## Git setup

We're going to need a git client, the easiest way to do this is git bash for windows. 

### Git Option 1: Chocolatey

```
choco install git 
```

### Git Option 2: Direct installation

(here)[https://gitforwindows.org/]


# Mac

## Brew Setup (Optional)
[Homebrew](https://brew.sh) is a package manager for Mac. Using this will likely make the installation process much easier, but you can still do it manually if you want. 

## Python Setup

Obviously Python is important for a Python workshop, you can check if you already have Python by opening a terminal using 'spotlight' (Command + Spacebar and type in `terminal`) and entering the command:

```
python --version
``` 
If the version is 3.6 or above then you're all set. If nothing comes up then you need to install Python. If you've already installed Python and nothing is coming up then you likely need to add it to your system path.

### Option 1: Brew Python

### Option 2: Anaconda

### Option 3: Python


## Git Setup


# Linux

##

##

##

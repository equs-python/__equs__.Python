
# VSCode

A quasi open source text editor written in the electron framework and developed by Microsoft.

Once installed, you can launch it from your terminal with the `code` command. 

## Installation

### Windows


### Mac

### Linux

## Git Integration

## Linting


# Atom

An open source text editor written in the electron framework and developed by Git.

Once installed, you can launch it from your terminal with the `atom` command. 

## Installation

### Windows
An installer can be found (here)[https://atom.io/]. 
Alternatively you can install atom using chocolatey.

```
choco install atom
```

For more details on using chocolatey, see the end of the page.

### Mac
A .rpm file can be found (here)[https://atom.io/].
Alternatively, you can install atom using brew.

```
brew cask install atom
```

For more details on using brew, see the end of the page.

### Linux
A .deb file can be found (here)[https://atom.io/] or if you're more comfortable building from source (or you aren't running a debian derived distro) you can build from source from (here)[https://github.com/atom/atom/blob/master/docs/build-instructions/linux.md].

## Git Integration


## Linting


# Sublime Text

A non open source text editor. Unlike the other two it isn't written in the electron framework and is somewhat less resource intensive for it.

Once installed, you can launch it from your terminal with the `subl` command. 

## Installation

### Windows
If you're using a lab machine, you can try to use the portable version found (here)[https://www.sublimetext.com/3].
If you're using your own machine, you can either do an install via chocolatey or use the regular installer from (here)[https://www.sublimetext.com/3].
For more details on chocolatey, see the bottom of this page.

If you are using chocolatey, the following should install sublime.
```
choco install sublimetext3
```

### Mac
You have the choice of installing sublime either using brew, or downloading the dmg file found (here)[https://www.sublimetext.com/3].
The instructions for the brew installation are given below, if you want to know more about brew, see the bottom of this page. 

```
brew install caskroom/cask/brew-cask
brew tap caskroom/versions
brew cask install sublime-text
```

### Linux
Installation instructions for a range of Linux distros can be found (here)[https://www.sublimetext.com/docs/3/linux_repositories.html].
A tarball installation can be found (here)[https://www.sublimetext.com/3].

The short version can be found below.
```
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -

sudo apt-get install apt-transport-https

echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

sudo apt-get update
sudo apt-get install sublime-text
```
## Package Management
Sublime text has an optional package manager that can install plugins. We're going to want a few of these.
The instructions to install the package manager can be found (here)[https://packagecontrol.io/installation].

You can access the command palette to use package control with control + shift + p or command + shift + p.

## Git Integration
Open the command palette and go to `Package Control: Install Package` (typing will search and auto-complete). A second list will appear, this time displaying available packages. Find and select the `Git` package. 


## Linting
Open the command palette and go to `Package Control: Install Package` (typing will search and auto-complete). A second list will appear, this time displaying available packages. Find and select the `Pylinter` package. 

# (Chocolatey)[https://chocolatey.org/]
A package manager for the Windows operating system. This allows you to install software packages from your terminal. 
Installation instructions can be found (here)[https://chocolatey.org/install]. You will need administrator privileges to do this installation, and as a result cannot install it to the lab machines.

# (Brew)[https://brew.sh/]
A package manager for the OSX operating system. This allows you to install software packages from your terminal. 
Installation instructions can be found (here)[https://brew.sh/].
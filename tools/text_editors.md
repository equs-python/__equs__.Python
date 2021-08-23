# Vim, Vi and Emacs

 Text editors with no mouse support, it is incredibly useful to know how to use at least one of these. The primary reason these editors have no mouse support is that they nearly predate the mouse. The arguments about the merits of Vi and Emacs pre-date the internet and have their own wikipedia page that may be considered suggested reading. In short emacs is considered more featured (having its own web browser, e-mail client and games and is often joked as being an operating system), while vim is more lightweight and is more ubiquitous. If learning vim, there is a dedicated `vimtutor` command that provides an in-vim, vim tutorial. 

The utility of learning an in-terminal text editor is that it makes editing code remotely much easier; simply `ssh` into the machine, crack open your text editor and get going! Both of these editors are fully scripted and are extendable with plugins in much the same way as anything else on this list. They also have three to four decades worth of support, documentation and guidance when compared to the other options. 


To launch any of these from your terminal simply invoke 
```bash
vim
emacs
```

If they're not installed then 

# Atom

An open source "hackable" IDE written in the electron framework and developed by Github. As github is now owned by Microsoft this text editor is in competition with their other quasi-open source electron based IDE VScode. As a result Atom support seems to be in the process of quietly winding down. As it runs in electron it uses an entire chromium browser instance to run a text editor and may be quite heavy on the RAM consumption.


That said it's still a usable text editor and doesn't have the same strings attached as some of the others listed here.

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

If you're not using ubuntu Atom may already exist in your distro's package manager, otherwise we can add the atom ppa and install it from there.

```
sudo apt update
sudo apt install software-properties-common apt-transport-https wget
wget -q https://packagecloud.io/AtomEditor/atom/gpgkey -O- | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main"
sudo apt install atom
``` 

If you prefer a .deb file can be found (here)[https://atom.io/] or if you're more comfortable building from source (or you aren't running a debian derived distro) you can build from source from (here)[https://github.com/atom/atom/blob/master/docs/build-instructions/linux.md].

## Git Integration

Go to settings and install packages. From there search for "git-plus" and install it.

## Linting

Go to settings and install packages. From there search for "linter-pylint" and install it.

# Sublime Text

A non open source text editor. Unlike the other two it isn't written in the electron framework and is somewhat less resource intensive for it.

Once installed, you can launch it from your terminal with the `subl` command. 

## Installation

### Windows
Install via chocolatey or use the regular installer from (here)[https://www.sublimetext.com/3].
For more details on chocolatey, see the primer on package managers.

If you are using chocolatey, the following should install sublime.
```
choco install sublimetext3
```

### Mac
You have the choice of installing sublime either using brew, or downloading the .dmg file found (here)[https://www.sublimetext.com/3].
The instructions for the brew installation are given below, if you want to know more about brew, see the primer on package managers. 

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

 
# VSCode
A quasi open source text editor written in the electron framework and developed by Microsoft. It's currently somewhat popular but that may be due to a much larger marketing budget rather than any strict novelty. There are concerns that features of this text editor may be paywalled (and indeed there are already annoucments for subscription only features). As it runs in electron it uses an entire chromium browser instance to run a text editor and may be quite heavy on the RAM consumption.

Once installed, you can launch it from your terminal with the `code` command. 

## Installation

Go to [https://code.visualstudio.com/download](https://code.visualstudio.com/download) and download the appropriate installer for your operating system.

### Windows


(https://code.visualstudio.com/docs/setup/windows#_installation)[https://code.visualstudio.com/docs/setup/windows#_installation]

Download and execute the appropriate `.exe` file, and simply follow the installation instructions.

### Mac

[https://code.visualstudio.com/docs/setup/mac](https://code.visualstudio.com/docs/setup/mac)

1. Download Visual Studio Code for macOS.
2. Double-click on the downloaded archive to expand the contents.
3. Drag Visual Studio Code.app to the Applications folder, making it available in the Launchpad.
4. Add VS Code to your Dock by right-clicking on the icon and choosing Options, Keep in Dock.


### Linux

[https://code.visualstudio.com/docs/setup/linux](https://code.visualstudio.com/docs/setup/linux)

Download the appropriate installer. For debian based system, navigate to the Downloads directory and run:

```bash
$ sudo dpkg -i <vscode_installer>.deb
```

And replace the name in the angled brackets by the actual name of the installer.

## Git Integration

VS Code should take care of this automatically. Let us know if you need a hand.

## Linting

Install the Python extention for this. In the sidebar on the left, click on the `Extensions` symbol and install the `ms-python.python` extension. Note that in order for this to work you need to have a working Python environment set up with a linting module. We recomment `pylint` for that, which is shipped per default with the Anaconda distribution.





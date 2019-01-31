#!/bin/bash
#################
# Set up some aliases
#################

BASHRC=$HOME/.bashrc
echo "# <<<< EQUS CHANGES BEGIN HERE >>>>" >> $BASHRC
echo "alias pip='python3 -m pip'" >> $BASHRC
echo "alias python='python3'" >> $BASHRC
echo "alias ipython='ipython3'" >> $BASHRC
source $BASHRC

#################
# Linux core utils
#################
echo "Installing required packages..."
sudo apt-get -y update
sudo apt-get -y install vim
sudo apt-get -y install git
sudo apt-get -y install docker.io
sudo apt-get -y install apt-transport-https
sudo apt-get -y install gcc
sudo apt-get -y install libxml2-dev
sudo apt-get -y install libxsl1-dev
sudo apt-get -y install zlib1g-dev
sudo apt-get -y install g++

# Add the user to the docker group
# This won't work until the user has logged
sudo usermod -aG docker $USER

# Disable the lock screen
dconf write /org/cinnamon/desktop/lockdown/disable-lock-screen true
dconf write /org/cinnamon/desktop/lockdown/disable-log-out true

#################
# Text Editors
#################
echo "Installing text editors..."
# VSCode
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
rm microsoft.gpg

# Sublime Text
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

# Atom Text Editor
wget -qO - https://packagecloud.io/AtomEditor/atom/gpgkey | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" > /etc/apt/sources.list.d/atom.list'

# Updating
sudo apt-get update

# Installing them all
sudo apt-get -y install code
sudo apt-get -y install sublime-text
sudo apt-get -y install atom

# #################
# # Python core utils
# #################
echo "Setting up Python..."
sudo apt-get -y install python3
sudo apt-get -y install python3-dev
sudo apt-get -y install python3-distutils
sudo apt-get -y install python3-pip
sudo apt-get -y install ipython3

# #################
# # jupyter 
# #################
python3 -m pip install jupyter
sudo apt-get -y install jupyter-core
sudo apt-get -y install jupyter-notebook

# #################
# # Pip stuff
# #################
python3 -m pip install setuptools
python3 -m pip install cython
python3 -m pip install numpy
python3 -m pip install scipy
python3 -m pip install matplotlib


#################
# Environment setup
#################
AUR=$HOME/aur
mkdir $AUR

# #################
# # Miniconda setup
# #################
echo "Installing Conda..."
MINICONDA=$AUR/miniconda3
MINICONDA_INST=$MINICONDA/src
MINICONDA_BIN=$MINICONDA/src/bin
mkdir $MINICONDA
cd $MINICONDA

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh -b -p $MINICONDA_INST

CONDA=$MINICONDA_BIN/conda
ACTIVATE="source $MINICONDA_BIN/activate"
DEACTIVATE=$MINICONDA_BIN/deactivate

# Update
$CONDA update -n base -c defaults conda -y
$CONDA init
$CONDA init bash
source $BASHRC

#########
# pyQuil
#########
echo "Installing pyquil..."
PYQUIL=$AUR/pyquil
PYQUIL_GIT=https://github.com/rigetti/pyquil.git
PYQUIL_REQUIREMENTS=$PYQUIL/requirements.txt

# # Clone repo
git -C $AUR clone $PYQUIL_GIT

# Setup environment
CONDA create -n pyquil -y
$ACTIVATE pyquil

# Install dependencies
python3 -m pip install -r $PYQUIL_REQUIREMENTS

# Install pyquil
python3 -m pip install $PYQUIL

$CONDA deactivate


#########
# pyGSTi
#########
echo "Installing pyGSTi..."
PYGSTI=$AUR/pyGSTi
PYGSTI_GIT=https://github.com/pyGSTio/pyGSTi.git

# # Clone Repo
git -C $AUR clone $PYGSTI_GIT

# # Setup Environment
$CONDA create -n pygsti -y
$ACTIVATE pygsti

# # Setup dependencies
$CONDA install numpy -y
$CONDA install matplotlib -y

# # Install pygsti
python3 -m pip install $PYGSTI

# # And clear
$CONDA deactivate

# Get rid of the error message
echo "export PYGSTI_BACKCOMPAT_WARNING=0" >> $BASHRC

#########
# QCoDes
#########
echo "Installing QCoDeS..."
QCODES=$AUR/Qcodes
QCODES_GIT=https://github.com/QCoDeS/Qcodes.git
QCODES_YML=$QCODES/environment.yml

# Clone Repo
# git -C $AUR clone $QCODES_GIT

# Create environment
$CONDA env create -f $QCODES_YML

# Activate the environment 
$CONDA activate qcodes

# Install 
python3 -m pip install $QCODES

# And clear
$CONDA deactivate

#########
# Qiskit
#########
echo "Installing Qiskit..."

QISKIT=$AUR/qiskit-tutorials
QISKIT_GIT=https://github.com/Qiskit/qiskit-tutorials.git
QISKIT_YML=$QISKIT/environment.yml

# Clone Repo
git -C $AUR clone $QISKIT_GIT

# Create environment
$CONDA env create -f $QISKIT_YML

# Activate the environment 
$ACTIVATE qiskit

# Install some helpful things
python3 -m pip install matplotlib
python3 -m pip install pyplot

# And clear
$CONDA deactivate


# #########
# # qinfer
# #########
echo "Installing qinfer..."
QINFER=$AUR/python-qinfer
QINFER_GIT=https://github.com/QInfer/python-qinfer.git
QINFER_REQUIREMENTS=$QINFER/requirements

# Clone repo
git -C $AUR clone $QINFER_GIT

# Create environment
$CONDA create -n qinfer -y
$ACTIVATE qinfer

# Install requirements
python3 -m pip install -r $QINFER_REQUIREMENTS

# Additional requirements
python3 -m pip install matplotlib
python3 -m pip install pyplot

# Install qinfer
python3 -m pip install $QINFER

# And clear
$CONDA deactivate


#################
# Qutip
#################
echo "Installing qutip..."
QUTIP=$AUR/qutip
QUTIP_GIT=https://github.com/qutip/qutip.git
QUTIP_REQUIREMENTS=$QUTIP/requirements.txt

# Clone repo
git -C $AUR clone $QUTIP_GIT

# Create environment
$CONDA create -n qutip -y
$ACTIVATE qutip

# Install requirements
python3 -m pip install -r $QUTIP_REQUIREMENTS

# Additional requirements
python3 -m pip install matplotlib
python3 -m pip install pyplot

# Install qinfer
# Build from source wasn't working
python3 -m pip install qutip

# And clear
$CONDA deactivate

#################
# OpenFermion
#################
echo "Installing OpenFermion..."

OPENFERMION=$AUR/openfermion
OPENFERMION_GIT=https://github.com/quantumlib/openfermion.git
OPENFERMION_DOCKER=$OPENFERMION/docker
OPENFERMION_REQUIREMENTS=$OPENFERMION/requirements.txt

git -C $AUR clone $OPENFERMION_GIT


# In case the docker install fails, here's an environment too
$CONDA create -n openfermion -y
$ACTIVATE openfermion

python3 -m pip install -r OPENFERMION_REQUIREMENTS

python3 -m pip install $OPENFERMION

$CONDA deactivate

# And the docker install at the end
sudo docker build -t openfermion_docker $OPENFERMION_DOCKER

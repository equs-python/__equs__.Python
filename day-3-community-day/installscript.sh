#!/bin/bash
#################
# Set up some aliases
#################


# set colors
f7=$'\e[37m'
f1=$'\e[31m'

BASHRC=$HOME/.bashrc

# Handle inputs
INST_BASE=false
INST_TEXT=false
INST_PYTHON=false
INST_CONDA=false

INST_PYQUIL=false
INST_PYGSTI=false
INST_QCODES=false
INST_QISKIT=false
INST_QINFER=false
INST_QUTIP=false
INST_OPEN_FERMION=false
INST_OPEN_FERMION_DOCKER=false

# Base case, just install all
if test $# -eq 0; then
    NST_BASE=true
    INST_TEXT=true
    INST_PYTHON=true
    INST_CONDA=true
    INST_PYQUIL=true
    INST_PYGSTI=true
    INST_QCODES=true
    INST_QISKIT=true
    INST_QINFER=true
    INST_QUTIP=true
    INST_OPEN_FERMION=true
    INST_OPEN_FERMION_DOCKER=true
fi


while test $# -gt 0
do
    arg=$1
    case $arg in 
        --base) INST_BASE=true
    ;;
        --text) INST_TEXT=true
    ;;
        --python) INST_PYTHON=true
    ;;
        --conda) INST_CONDA=true
    ;;
        --pyquil) INST_PYQUIL=true
    ;; 
        --qcodes) INST_QCODES=true
    ;;
        --pygsti) INST_PYGSTI=true
    ;;
        --qiskit) INST_QISKIT=true
    ;;
        --qutip) INST_QUTIP=true
    ;; 
        --qinfer) INST_QINFER=true
    ;;
        --openfermion) INST_OPEN_FERMION=true
    ;;
        --openfermion-docker) INST_OPEN_FERMION_DOCKER=true
    esac
    shift
done

#################
# Linux core utils
#################
if $INST_BASE; then
    echo "${f1}Installing required packages...${f7}"
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
fi

#################
# Text Editors
#################
if $INST_TEXT; then
    echo "${f1}Installing text editors...${f7}"
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
fi

# #################
# # Python core utils
# #################
if $INST_PYTHON; then
    echo "${f1}Setting up Python...${f7}"
    sudo apt-get -y install python3
    sudo apt-get -y install python3-dev
    sudo apt-get -y install python3-distutils
    sudo apt-get -y install python3-pip
    sudo apt-get -y install ipython3


    echo "# <<<< EQUS CHANGES BEGIN HERE >>>>" >> $BASHRC
    echo "alias pip='python3 -m pip'" >> $BASHRC
    echo "alias python='python3'" >> $BASHRC
    echo "alias ipython='ipython3'" >> $BASHRC
    source $BASHRC


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

fi

#################
# Environment setup
#################
AUR=$HOME/aur
mkdir $AUR

# #################
# # Miniconda setup
# #################
if $INST_CONDA; then
    echo "${f1}Installing Conda...${f7}"

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
fi

#########
# pyQuil
#########
if $INST_PYQUIL; then
echo "${f1}Installing pyquil...${f7}"
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
fi

#########
# pyGSTi
#########
if $INST_PYGSTI; then
    echo "${f1}Installing pyGSTi...${f7}"
    PYGSTI=$AUR/pyGSTi
    PYGSTI_GIT=https://github.com/pyGSTio/pyGSTi.git

    # # Clone Repo
    git -C $AUR clone $PYGSTI_GIT

    # Setup Environment
    $CONDA create -n pygsti -y
    $ACTIVATE pygsti

    # Setup dependencies
    $CONDA install numpy -y
    $CONDA install matplotlib -y

    # Install pygsti
    python3 -m pip install $PYGSTI

    # Notebook Kernels
    python3 -m install ipykernel
    $CONDA install nb_conda_kernels

    # # And clear
    $CONDA deactivate

    # Get rid of the error message
    echo "export PYGSTI_BACKCOMPAT_WARNING=0" >> $BASHRC
fi

#########
# QCoDes
#########
if INST_QCODES; then
    echo "${f1}Installing QCoDeS...${f7}"

    QCODES=$AUR/Qcodes
    QCODES_GIT=https://github.com/QCoDeS/Qcodes.git
    QCODES_YML=$QCODES/environment.yml

    # Clone Repo
    git -C $AUR clone $QCODES_GIT

    # Create environment
    $CONDA env create -f $QCODES_YML

    # Activate the environment 
    $CONDA activate qcodes

    # Install 
    python3 -m pip install $QCODES

    # Notebook Kernels
    python3 -m install ipykernel
    $CONDA install nb_conda_kernels

    # And clear
    $CONDA deactivate
fi

#########
# Qiskit
#########
if INST_QISKIT; then
    echo "${f1}Installing Qiskit...${f7}"

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

    # Notebook Kernels
    python3 -m install ipykernel
    $CONDA install nb_conda_kernels

    # And clear
    $CONDA deactivate

fi

# #########
# # qinfer
# #########
echo "${f1}Installing qinfer...${f7}"
QINFER=$AUR/python-qinfer
QINFER_GIT=https://github.com/QInfer/python-qinfer.git
QINFER_REQUIREMENTS=$QINFER/requirements.txt

# Clone repo
git -C $AUR clone $QINFER_GIT

# Create environment
$CONDA create -n qinfer -y
$ACTIVATE qinfer

# Install requirements
python3 -m pip install -r $QINFER_REQUIREMENTS

# The above seems to not actually work

# Additional requirements
python3 -m pip install numpy
python3 -m pip install matplotlib
python3 -m pip install pyplot

# Install qinfer
python3 -m pip install $QINFER

# Notebook Kernels
python3 -m install ipykernel
$CONDA install nb_conda_kernels

# And clear
$CONDA deactivate


#################
# Qutip
#################
echo "${f1}Installing qutip...${f7}"
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
python3 -m pip install cython
python3 -m pip install numpy
python3 -m pip install scipy
python3 -m pip install matplotlib
python3 -m pip install pyplot

# Install qinfer
# Build from source wasn't working
python3 -m pip install qutip

# Notebook Kernels
python3 -m install ipykernel
$CONDA install nb_conda_kernels

# And clear
$CONDA deactivate

#################
# OpenFermion
#################
echo "${f1}Installing OpenFermion...${f7}"

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

# Notebook Kernels
python3 -m install ipykernel
$CONDA install nb_conda_kernels

$CONDA deactivate

# And the docker install at the end
sudo docker build -t openfermion_docker $OPENFERMION_DOCKER
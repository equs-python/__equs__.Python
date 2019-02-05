# GOOD MORNING!

## And welcome to day 3 of the Python workshop!

For today's sessions, we have set up your computers with Virtual Boxes running Linux Mint, with all the software we need today pre-installed. Below you can find specific setup instructions for the different sessions. If you want to reproduce this setup on your own machine, we're providing our bash script (`installscript.sh`) that installs all required dependencies and sets up individual conda environments for each session.

## pyQuil setup instructions

The following instructions are only valid if you're using your own machine, on our workshop computers we already have `qvm` and `quilc` installed.

To set up a pyQuil environment with local simulators on your own machine, first head to the [Rigetti Forest web page](http://rigetti.com/forest) and request a token to download both the Quantum Virtual Machine (`qvm`) and the Rigetti Quil compiler (`quilc`). Download both packages and install them following the instructions on the website.

Next you need to start the two servers in two separate terminals like so:

```bash
$ qvm -S
```

and

```bash
$ quilc -S
```

The `pyquil` package should already be installed on your computers (if not, get it via `pip`!), so you can head straight to the example notebooks and get started (and remember to activate the appropriate conda environment):

```bash
$ conda activate pyquil
$ cd ~/aur/pyQuil
$ jupyter notebook
```





## pyGSTi setup instructions

To set you up for our pyGSTi session, open a terminal (Ctrl+Alt+T) and type:

```bash
$ cd ~/aur/pyGSTi/
$ git pull
$ cd jupyter_notebooks
$ conda activate pygsti
$ jupyter notebook START_HERE.ipynb
```

## Qcodes setup instructions

To set up your qcodes environment, run the following commands

```bash
$ conda activate qcodes
$ pip install ~/aur/Qcodes
```

## Qinfer Setup Instructions

If you haven't cloned the equs-python repository onto your Virtual Box yet, please run the following command in the terminal:

```bash
$ git clone https://github.com/equs-python/__equs__.Python
```



Then, to set up your qinfer environment, run the following commands

```bash
$ conda activate qinfer
$ pip install matplotlib
$ pip install pyplot
$ pip install ~/aur/python-qinfer
```

And finally, open the notebook for this tutorial (and remember that you can tab to autocomplete paths):

```bash
$ cd __equs__.Python/day-3-community-day/qinfer
$ jupyter notebook equs-python-qinfer.ipynb
```


## Qutip Setup Instructions

To set up your qutip environment run the following commands

```bash
$ conda activate qutip
$ pip install cython
$ pip install numpy
$ pip install scipy
$ pip install ~/aur/qutip
```

## Openfermion Setup Instructions

To set up your Open Fermion environment run the following commands

```bash
conda activate openfermion
pip install openfermionpyscf
pip install openfermioncirq
```

And then you will find the ipython notebook in the `day-3-community-day` directory in the workshop git repository. Simply run `jupyter-notebook` to access it.

If you can't find the notebook, don't forget to `git pull` to update your local copy of the repository.

If you want to use the docker image, you can find instructions in the `README.md` file in the `openfermion` directory
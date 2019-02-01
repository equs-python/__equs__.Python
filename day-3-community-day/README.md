# GOOD MORNING!

## and welcome to day 3 of the Python workshop!

For today's sessions, we have set up your computers with Virtual Boxes running Linux Mint, with all the software we need today pre-installed.

To get started for our first session, open a terminal (Ctrl+Alt+T) and type:

```bash
$ cd aur/pyGSTi/
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
$ conda activate openfermion
$ pip install ~/aur/openfermion
```

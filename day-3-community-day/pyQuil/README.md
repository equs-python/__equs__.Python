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


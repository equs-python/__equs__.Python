# \_\_equs\_\_.Python workshop 2019
## Day 2 - Putting python to work

# 2. Hardware control (and experiment automation) project.

Now let's have a go at writing code to control some hardware and perform an experiment. 

## 2.1 Load the device.

It's too hard to have physical experimental equipment attached to every computer here. Instead, a "virtual power supply" is ready to run!

Open a new command prompt and do the following:
  - Navigate to today's directory in the workshop repository. It should be `__equs__.Python/day-2-python-hw-applications`
  - Navigate to inside the `demo_hardware` subdirectory.
  - Start the demo hardware by running `python power_supply.py`

You should see a small graphical-user-interface (GUI) that shows the front control panel of a 2-channel power supply. Play with the controls for a minute to see if it makes sense.

**Don't worry about the strange display below Channel 2 just yet!**

## 2.2 Read The Flimsy Manual

This 

Error codes

-3 Invalid argument
-4 No arguments given
-7 Command not known

## 2.2 Read things from device

## 2.3 Remote control of the device

| Command | Arguments | Description |
| ------------- |:-------------:|:-------------:|
|`'setactive'` | channel, state | Turn the output on or off on a given channel |
|`'v_set'` | channel, voltage | Set the nominal voltage on a given channel |
|`'i_set'` | channel, current | Set the nominal current on a given channel |
|`'v_set?'` | channel | Get the nominal voltage on a given channel |
|`'i_set?'` | channel | Get the nominal current on a given channel |
|`'v_act?'` | channel | Get the actual voltage on a given channel |
|`'i_act?'` | channel | Get the actual current on a given channel |
|`'*IDN?*'` | None | Get the device identifier as a string |


## 2.4 Automating an experiment

Channel 2 has an old tungsten filament light bulb attached as a load. The experiment is to measure 
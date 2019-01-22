# \_\_equs\_\_.Python workshop 2019
## Day 2 - Putting python to work

We've covered a fair bit of _how_ to code in Python. Today the focus will shift to putting this superpower to work. For experiments we'll typically need to interact with and control hardware devices - and Python is great for this (but has limits). The nuts and bolts can get laborious and are mostly too time consuming for this workshop. We'll explore some case studies to build up a picture of the challenges, focussing on what Python can do (and where its limits are). We will write code to control a simple hardware device, and put it to work automating an experiment.

Here are the specific topics of the day:

**TODO:** *insert hyperlinks to module content pages*

1. Motivating Python in the lab with case studies
   1. Overview of goal
   2. Simple text-based communication
   3. Windows DLL control (with ctypes)
   4. Deeper levels of hell...
2. Experiment automation project
   1. Querying a hardware device
   2. Controlling a hardware device
   3. Doing physics faster (better?) through automation
3. Tips, Tricks, and Teasers
4. Installfest / Hackathon



## Getting started

To get started, download the tutorial content to your local machine (if you haven't already done so yesterday). Open the Git Bash and type:

```bash
$ git clone https://github.com/equs-python/__equs__.Python
$ cd __equs__.Python
$ code .
```

And with that, let's go!

# 1. Motivating Python in the lab (1 hour)

In this section we present a variety of case studies to highlight how useful Python can be in the lab, and also to illustrate the range of challenges that can be encountered when talking to hardware.

## 1.1 Automated experiment

Show plot of data (recently presented at AIP in Perth).

This measurement consists of:
- Go through a set of points-of-interest.
- For each one, we want fluorescence spectra to be recorded at a variety of laser powers *and* a range of temperatures (heater currents).

## 1.2 Text-based querying for logging (PCM60x charge controller)

Excellent simple example as a warm-up. The charge controller for my home-built solar-charged home battery.

```python
# Copy code here
```

The really important detail is that the code is simple but the documentation was terrible.

## 1.2 Text-based communication (Coherent Obis laser)

The basic set_power method looks fairly straight-forward:

```python
def set_power(self, power):
    """ Set laser power
    @param float power: desired laser power in watts
    """
    self._communicate('SOUR:POW:LEV:IMM:AMPL {}'.format(power))
```

What tricks are hiding in `self._communicate` I wonder?

```python


def _communicate(self, message):
    """ Send a receive messages with the laser
    @param string message: message to be delivered to the laser
    @returns string response: message received from the laser
    """
    self._send(message)
    time.sleep(0.1)
    response_len = self.obis.inWaiting()
    response = []

    while response_len > 0:
        this_response_line = self.obis.readline().decode().strip()
        if (response_len == 4) and (this_response_line == 'OK'):
            response.append('')
        else:
            response.append(this_response_line)
        response_len = self.obis.inWaiting()

    # Potentially multi-line responses - need to be joined into string
    full_response = ''.join(response)

    if full_response == 'ERR-100':
        self.log.warning(self._model_name + ' does not support the command ' + message)
        return '-1'

    return full_response
```

And here there seem to be some tricks in `self._send`

```python
def _send(self, message):
    """ Send a message to to laser
    @param string message: message to be delivered to the laser
    """
    new_message = message + self.eol
    self.obis.write(new_message.encode())
```

**TODO:** Re-write this out as a simple example, then show how it was wrapped up into general functions.




## 1.3 Thorlabs APT-motor rotational stage (Windows DLL and ctypes)

## 1.4 Deeper levels of hell 

Sometimes the only way out is to use python to send text strings of visual basic code through to a device...


# 2. Experiment control project

## 2.1 Load the device.

It's too hard to have physical experimental equipment attached to every computer here. Instead, a "virtual power supply" is ready to run!

**TODO:** Instructions to start the virtual device running

## 2.2 Read things from device

## 2.3 Remote control of the device

## 2.4 Automating an experiment
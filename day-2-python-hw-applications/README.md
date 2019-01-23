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

*Caveat*: I make no claim to be "the best" at this stuff. Many of my code examples are taken from real lab software I have worked on; it works, but it may not be optimal.



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

### Topical example

Consider the following dataset, which was presented at the AIP Congress in Perth. The distance between two peaks in a photoluminescence spectrum ("Stokes shift") is shown versus both heater current and laser power.

![Colour plot of automated data](images/20181119_stokes_shift_matrix.png)


This measurement consists recording spectra at two wavelengths, at every combination of laser power and heater current (both divided into a range of 20 values). That's 400 measurement points, and each spectrum can take as long as 20 minutes for the low laser powers!

Far too laborious even for a Masters student...

### Structuring the problem

We can think of this experiment as:
- For each heater current:
  - For each laser power:
    - Record the spectra.
    - Find the peak positions.
    - Calculate the distance between them ("shift").

This looks quite a lot like nested `for` loops!

And the image is for just one nanodiamond; in the lab this measurement was repeated for numerous nanodiamonds. We could achieve this with another layer of `for` loop.

*(Yes, the dataset shown above really did take days to measure even with round-the-clock autonomous operation)*

### Gluing multiple devices together

Doing this experiment autonomously requires Python to:
- adjust the heater current (control a power supply),
- set the laser power,
- acquire spectra,
- re-align on the fluorescent ND to counteract physical drift of optical alignment.

Clearly we need to think a bit about Python and hardware.

## 1.2 Text-based querying for logging (PCM60x charge controller)

Excellent simple example as a warm-up. The charge controller for my home-built solar-charged home battery. I wanted to produce a live online plot of the charging current and battery voltage so that I could monitor progress while not at home.

I went searching online for what might be possbile in Python, and after some time (measured in days) I found https://github.com/solarsnoop/PCM60X-Monitor/blob/master/emoncms.py
which gave me the basic idea to follow. Querying the device to log charge current is only a few lines of code:

```python
import serial
# Connect serial
ser = serial.Serial(port='/dev/ttyACM0', baudrate=2400, timeout=2)
ser.write(b"\x51\x50\x49\x47\x53\xB7\xA9\x0D")
result = ser.read(70)
ser.read()
ser.read()
```

The command is pretty cryptic, and was not in the documentation that I could initially find.

Even after getting the communication to work, there was still some effort to interpret the returned information (`'032.3 24.02 00.10 00.00 00.10 0045 +023'`).

More digging, and I found a PDF copy of the "MPPT-3000 Standard RS232 communication Protocol", which explains things a bit further.

![image of table from MPPT comm protocol](images/pcm60x_pigs_ref.png)

Aha, that crazy text string is actually listing the ascii hex codes for "QPIGS" with some end-of-line carriage return characters! I think things are making sense, but what the heck is that table showing two definitions of "F" in the notes column? And what about "M is an integer..."? Where is "M" anyway?

These docs are probably buggy.

Sadly, the docs are mostly buggy.

The really important detail is that the code is simple but the documentation was terrible.

## 1.3 Text-based communication (Coherent Obis laser)

Here is a list of code that sets the output power of this laser:

```python
import serial

eol = '\r'
com_port = 'COM1'

obis = serial.Serial(com_port, timeout=1)

new_power = 10e-3
message = 'SOUR:POW:LEV:IMM:AMPL {}'.format(new_power) + eol
obis.write(message.encode())

time.sleep(0.1)

response_len = obis.inWaiting()
response = []

while response_len > 0:
    this_response_line = obis.readline().decode().strip()
    response.append(this_response_line)
    response_len = self.obis.inWaiting()

# Potentially multi-line responses - need to be joined into string
full_response = ''.join(response)
```

Most of this is quite readable Python code. The message to send to the OBIS laser is a bit cryptic. It can be read as `SOURce:POWer:LEVel:IMMediate:AMPLitude <value>` and is described in the Operators Manual (Appendix C):

> Set/Query Laser Power Level
> 
> Sets present laser power level in watts. Setting power level does not turn the laser on.
> 
> Command: SOURce:POWer:LEVel:IMMediate:AMPLitude \<value\>
>
> Query: SOURce:POWer:LEVel:IMMediate:AMPLitude?
>
> Reply: \<x.xxxxx\>
>
> The reply string represents the present laser power level setting as an NRf value in watts.

**TODO:** Decide whether quote (above) or screenshot (below) is better.

![Snippet of Obis operators manual](images/obis_manual_set_power.png)

Of course, there are plenty more commands available in this communication vocabulary. Appendix C lists more than 3 pages in its opening Quck Reference table:

![Sample content from the OBIS Command quick reference](images/obis_manual_command_list_eg.png)

We want to use many of these commands, but do not want to have to write out the communication structure every time.

**Note:** *Code duplication is EVIL.*

**Exercise:** Can you think of some reasons why?

So let's write some methods that we can reuse multiple times.

```python
def _send(self, message):
    """ Send a message to to laser
    @param string message: message to be delivered to the laser
    """
    new_message = message + self.eol
    self.obis.write(new_message.encode())
```

That will be enough for some commands, but often we want to know how the device responds to a query. This new method takes `_send` and builds on it to process the response.

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

We don't want to remember all those cryptic commands. Let's make a method to set power in a more user-friendly way.

```python
def set_power(self, power):
    """ Set laser power
    @param float power: desired laser power in watts
    """
    self._communicate('SOUR:POW:LEV:IMM:AMPL {}'.format(power))
```


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
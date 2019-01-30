# \_\_equs\_\_.Python workshop 2019
## Day 2 - Putting python to work

We've covered a fair bit of _how_ to code in Python. Today the focus will shift to putting this superpower to work. For experiments we'll typically need to interact with and control hardware devices - and Python is great for this (but has limits). The nuts and bolts can get laborious and are mostly too time consuming for this workshop. We'll explore some case studies to build up a picture of the challenges, focussing on what Python can do (and where its limits are). We will write code to control a simple hardware device, and put it to work automating an experiment.

Here are the specific topics of the day:

1. [Motivating Python in the lab with case studies](session_2_1_python_hardware_case_studies.md)
   1. Overview of goal
   2. Simple text-based communication
   3. Windows DLL control (with ctypes)
   4. Deeper levels of hell...
2. [Experiment automation project](session_2_2_hardware_control_project.md)
   1. Querying a hardware device
   2. Controlling a hardware device
   3. Doing physics faster (better?) through automation
3. [Introduction to Qudi as a deeper case study](session_2_3_introduction_to_qudi.md)
4. Introduction to pyQuil

*Caveat*: I make no claim to be "the best" at this stuff. Many of my code examples are taken from real lab software I have worked on; it works, but it may not be optimal.



## Getting started

To get started, download the tutorial content to your local machine. If you haven't been here yet, open Git Bash and type:

```bash
$ git clone https://github.com/equs-python/__equs__.Python
$ cd __equs__.Python/day-2-python-hw-applications
$ code .
```

If you already have the repository cloned to your comptuer, then open Git Bash and navigate to the __equs__.Python directory and type:

```bash
$ git checkout master
$ git pull
$ cd __equs__.Python/day-2-python-hw-applications
$ code .
```


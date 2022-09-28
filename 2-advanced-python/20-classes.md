## 4 Classes and inheritance

### 4.1 Variables, Object functions and Scoping
At this point you may begin to wonder what Python is really up to and how it distinguishes between and manages all these objects. Given that just about anything can be assigned to a variable, isn't an integer just a collection of function objects that act on a bit of data.

Again, you would be right, and we can see this quite clearly using the `dir()` function.

```python
dir()
```

It also should be of note that I can save all my current variables as a dictionary with the names of the variables as the key, and the value as whatever the value is. And we can see these dictionaries as `globals()` and `locals()` depending on the name-space.

```python
globals()
locals()
```

Now that we've noticed that everything is really a dictionary, it stands to reason that we can insert, modify or remove elements from these dictionaries (assuming we have write permissions). Given that the first time we open something up, it's somewhat obligatory that we break it trying to put it back together,  

Let's cheat at making a new variable.

```python
>>> globals()['silly_walk'] = 5
>>> print(silly_walk)
5
```

As a point of pedantry, we're going to disambiguate between functions that live by themselves in whatever the current namespace is, and functions that live within another object by calling the latter a method. If someone trips up on this don't worry too much.

Let's start by 'borrowing' the abs method from a complex number object.

```python
>>> our_imag = -5j
>>> help(our_imag.__abs__)
>>> abs_function = our_imag.__abs__
>>> help(abs_function)
```

Notice that the abs function takes an argument 'self'. Now try running the following commands 

```python
>>> our_imag.__abs__()
>>> abs(our_imag)
>>> abs_function()
>>> abs_function(-5j)
```

The third one fails. As you may have seen from the previous help statements, the self argument is required and hence throws an error. This `self` argument is what ties our dictionary of functions together into an object or a `class`. It allows an object to reference elements of itself and hence modify or call functions that it is associated with.

### 4.2 Classes

Classes in python requires a constructor, sometimes termed an initialiser. This is a function that is called when a new instance of the object is created, for instance 

```python
>>> my_int = int(5)
```

Calls the initialiser method `__init__` and returns a new instance of the integer class with the value 5.

So obviously if we want our own class we need to have some object with an `__init__` method. The syntax for creating classes is very similar to that of functions, the keyword is `class` is followed by the name of the class (Which is in CamelCase by convention) followed by two brackets (empty for now) and then a colon to start an indented block. Everything that lies within the block is a class attribute or method. Generally it's a good idea to put this in a file somewhere rather than trying to run this though the CLI.

As `__init__` is a function, we can make regular use of the usual keyword arguments along with `*args` and `**kwargs`.

We can use the self property to store things within a particular instantiation of the class. So let's start by making a Parrot class. Parrots are either alive or dead, and if they're alive they have a distinctive squawk. We will assume that all parrots are alive until proven otherwise.

```python
class Parrot():

    def __init__(self, squawk, is_alive=True):
        self.squawk = squawk
        self.is_alive = is_alive
```
I can now make new parrots.

```python
african_grey = Parrot('Polly want a Cracker?')
norwegian_blue = Parrot('', is_alive=False) 
```

Having an initialiser is good, but what does this parrot do? Let's give it a `squawk` function to make it talk.  

```python
    def squawk(self):
        if self.is_alive:
            return self.squawk
        else:
            return None
```

We should now be able to call this function.
```python
african_grey.squawk()
norwegian_blue.squawk()
```

These sorts of trivial methods that just return an element of a class is commonly called a 'getter'. Similarly a small method that sets a class property is a 'setter'. Let's set up a setter to update whether our Parrot is still alive.

```python
    def set_alive(self, is_alive):
        self.is_alive = is_alive
```

### **** Problem [10 Minutes] ****
Extend the Parrot class 
- Write a setter to set a new 'squawk' for the parrot
- Write a `__call__` function that makes the parrot squawk
- Give the parrot a new property 'colours' and write getters and setters for this property

And lastly, because the writer was press-ganged into this. We can define a `pining_for_the_fjords` method that indicates that the parrot is no longer alive. 
- Write the `pining_for_the_fjords` function such that it calls the setter for the alive property.

If you didn't already, your `__call__` method should call the getter for squawk, if you've made a mistake in squawk or need to change it in the future you will now only have to modify one section of code, rather than every section that references `self.squawk`.


### 3.3.2 Inheritance
So far classes are just a neat way to organise functions and the data that the functions act on. And while that will remain to be true, we can take this a little further and neatly organise our classes.

Part of this is inheritance, we can specify that classes 'inherit' the properties of some parent class, which saves us from having to re-write them each time. These parent classes We can also specify 'abstract' classes or functions that only the child classes implement, this allows us to have multiple classes with common function calls that invoke different behaviour. 

For instance if I have an quantum gate class, it might be inherited by the Pauli X class and the CNOT class. These classes will 'overload' the methods in the quantum gate class such that when called the methods in the child classes will be used instead. 

This is all very high level, so let's go back to dealing with parrots. We're going to create a Bird class that Parrots will inherit and this parent class will manage the `is_alive` property, while only parrots get to squawk. Birds will also have air speed velocities (for the purposes of this example, emus, cassowaries and kiwis are not birds).

```python
class Bird():
    def __init__(self, is_alive, air_speed_velocity):
        self.air_speed_velocity
        self.is_alive = is_alive
```

An in Parrot we now inherit from Bird and call the bird constructor.

```python
class Parrot(Bird):
    def __init__(self, squawk, is_alive=True):
        self.squawk = squawk
        super(self).__init__(is_alive) # Calls the constructor of the super class

```

There also exists multiple inheritance, polymorphism and several books and philosophies on the matter of Object Orientation and class hierarchies, but the general rule of thumb is do what works best for whatever it is that you're doing. 


### **** Problem [10 Minutes] ****
Finish off the bird class
- Write getters and setters for air_speed_velocity
- Check that your Parrots can now call the air speed velocity getters and setters 

Implement a Swallow class that inherits from Bird. 
- Swallows have the additional properties of being laden or unladen. Implement this and write the appropriate getters and setters
- A laden swallow moves at half the speed of an unladen swallow. You should overload the getter for the swallow to reflect this property. 


### 4.3 Python libraries

Here are a few useful (non-scientific) general libraries. 

- ipython - A better python CLI, strict upgrade from the regular one, no reason not to use it really.

- sys - A few good system level Python features, such as command line arguments, Python versions and other utilities.

- os - Operating system features, make directories, move files and delete files, check what OS is being run or find the user's name.

- time - All things to do with time and timing.

- random - Random numbers and their uses, may not be suitable for cryptographic randomness

- sockets - For when you need a network socket (more on this in future days).

- pickle - Good for compacting Python object data to reload it later.

- copy - Contains the `deepcopy` function that gets around problems like list copying.

- matplotlib - Basic plotting library, basically the same as the matlab one there are others out there but most are just fancy wrappers for this 

- numpy - Numerical Python, more to follow

- scipy - Scientific Python, more to follow

- itertools - A bunch of very useful tools for more advanced iteration

These libraries can be included using the `import` keyword, as you've probably seen further up. You can also import libraries as a separate keyword in case you're too lazy to type out the full library name each time. For instance the numpy library is regularly imported as np.

```python
import numpy as np
``` 

Each library also contains multiple Python files and functions, you can explicitly import one of those if you need, without including the entire library in your name-space. This is helpful when different libraries share keywords. 

```python
import random.random
```
or
```python
from random import random 
```

You can also be incredibly lazy and just import everything to the global name-space:

```python
from random import *
```
This may result in fiddly behaviour when two elements of the global name-space have the same name. Remembering that `globals()` is a dictionary, one of them will be overwritten, hence it's often much better to be more verbose. To be honest we're only really showing you this last one as an example of what not to do.

A final Python library of incredible importance is the `this` library. 

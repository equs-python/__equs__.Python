
# 4.0 Python for scientific computing

While Python is a very popular programming language due to its simplicitly and expressiveness, it is also receiving increasingly more attention in the context of scientific computing. Today there is a vast amount of scientific libraries out there which help you to perform almost any numeric task you can think of - from Fourier transforms to differential equation solvers, or machine learning and clever data visualisation tools. In this section we take a look at two of the most commonly used libraries: [NumPy](https://numpy.org) and [Matplotlib](https://matplotlib.org). For completeness, we also mention [Scipy](https://scipy.org) here, which essentially implements a variety of extra functionality to extend NumPy, but in the interest of time we will skip this library here.

If in doubt when using a new package, don't forget to `dir()` the package, and `help()` on anything within the package.

## 4.1 NumPy - Numerical computing in Python

```python
import numpy as np
```

Numpy is a numerical Python library that contains huge amount of mathematical functions which come in handy for day-to-day scientism.

Most notably, Numpy defines *arrays*, which are treated like matrices and can be used in the context of linear 
algebra or whenever else array operations are desired. This is not the same as nested Python lists, as we have seen in earlier tutorials today.

To create an array, we can use the  `array`  class in Numpy to convert a Python list to an array. The lists must be regular and all elements must be of the same type. For example:

```python
x = np.array([
    [0, 1],
    [1, 0]
])
```

These arrays can be treated as tensors. Rather than lists where addition was concatenation and multiplication was duplication, these will now follow the appropriate (element-wise) mathematical operations.

```python
>>> x + x # Element-wise sum
array([
    [0, 2],
    [2, 0]
])
>>> x * 5 # Scalar product
array([
    [0, 5],
    [5, 0]
])
>>> -x
array([
    [0, -1],
    [-1, 0]
])
>>> x ** 2
array([
    [0, 1],
    [1, 0]
])

```

We can still slice these arrays in the same manner as a list:

```python
>>> x[:, 1]
array([1,0])
```

This operation is selecting all rows from the second column.

If we want to see the dimensions of these slices we can use the `.shape` property.

```python
>>> x.shape # Original array
(2, 2)
>>> x[:, 1].shape # Sliced array (second column only)
(2,)
```

The `shape` attribute is a tuple that contains the number of elements in each direction.

## **** Problem: Array slicing [5 Minutes] ****

For the array `x` as specified below,

```python
x = np.array([
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
])
```

What are the outputs of the following slicing operations? Try and have a guess first before you test it.

- `x[:, 0]`
- `x[:2, 1]`
- `x[0, 1:]`
- `x[:1]`
- `x[1::2]`

## 4.0.1 More Numpy

We can also modify the shape of an array by calling the `reshape` method:

```python
>>> x.reshape((4, 1))
array([[0],
       [1],
       [1],
       [0]])
>>> x.reshape((1,4))
array([[0, 1, 1, 0]])
```

Note that this operation needs to preserve all elements in the array, so the product of the individual dimensions along each axes needs to remain constant. Here we went from `2*2` to `4*1` and `1*4` respectively.

Arrays in Numpy can only contain a single type. This type is defined by the `dtype` property, and can be set as a keyword argument when the array is created.

```python
>>> x.dtype
dtype('int64')
```

When we created this array, this type was chosen as default. If we had created an array with floating point numbers, Numpy would have defaulted to `'float64'`, which stands for 64-bit floating point numbers.

```python
>>> y = np.array([0.5]).dtype
dtype('float64')
```

Note that this is not a built-in Python type, but instead a type that Numpy defines. This is because Numpy is largely written in C and the `dtype` of an array resembles the equivalent type in C.


## **** Problem [10 Minutes] Numpy Pauli ****

- Create the Pauli matrices using Numpy
- Verify that the matrices are unitary
- Write a function that calculates the commutation relations between two numpy arrays
- Write a function that performs a tensor product over strings of Pauli operators

**Hint:** Take a look at the `dot`, `tensordot` and/or `kron` operation in Numpy. Consider how kron and reduce can be used together.

## 4.0.2 Scipy - Scientific Computing in Python
Scipy is another set of useful libraries that contains a bunch of wrappers for optimised Fortran, C and C++ code that performs curve fitting, ODE solving and a range of other things. It compliments numpy well. As it's a grab bag the features of scipy are best demonstrated through their use. 

- `scipy.optimize` : Minimisation functions, good for fitting functions
- `scipy.linalg` : While numpy specialises in array notations scipy extends this to include sparse representations, `scipy.linalg.sparse` is practically the standard here.
- `scipy.fft` : Bindings to FFT libraries
- `scipy.interpolate` : Interpolation libraries
- `scipy.integrate` : Integration libraries (Gaussian Quadratures are generally a good starting place)

## **** Problem [10 Minutes] Gaussian Fit ****
Construct a function that generates random Gaussian functions in the range [0, 1] and that peak within this range, these Gaussians may be classes with properties or partial functions with keyword arguments.
- Using `scipy.optimize` write a fitter that calculates the parameters of the Gaussian by sampling the function. Have a look at some of the options for constrained minimisation within scipy.
- Using `scipy.integrate` Integrate over the original Gaussian and your fit. Compare this to a mathematical evaluation of the integral of your Gaussian over the range [0, 1]. You can find the error function in either `numpy.erf` or `scipy.special.erf`.
- [Extension] Extend the above to a multi-Gaussian generator and fitter for an arbitrary and unknown number of Gaussians, you may want to consider moving your generator to be at least a second order function.

## 4.0.3 Matplotlib - Visualising data in Python

Matplotlib is a matlab-like interface for plotting in Python. 

For this part of the tutorial, we'll take advantage of the `jupyter notebook` interface here, so start up jupyter from your terminal with: 

```python
jupyter notebook
``` 

Your browser should open to display your current directory tree. Once here, create a new notebook using the button on the top right.

Jupyter notebooks provide a series of 'cells' each of which can contain and execute Python code. The cells share the same global namespace and as a result variables and functions are shared between cells. This is a reasonably neat way to organise Python code and test and execute chunks of code separately. Sort of a halfway house between the CLI and code in a file, with the added benefit that the cell output is displayed directly and can be kept visible during the working session, which is particularly handy for graphical output like plots.

Cells can be executed using `shift + enter`.
New cells can be created by pressing `ctrl` followed by `a` for above or `b` for below the current cell.

With that out of the way, import matplotlib. 

```python
import matplotlib.pyplot as plt
```

It is a widely accepted standard to import the `matplotlib.pyplot` module under the `plt` alias.

And now we can start plotting. Let's create a simple list of numbers and plot them:

```python
y_vals = [i**2 for i in range(10)]
plt.plot(y_vals)
```

This is the minimal amount of information we need to provide the `plot` function with, but when we take a look at the documentation you can see that it is very customisable. For example, we can also specify the x coordinate positions:

```python
x_vals = [i**3 for i in range(10)]
plt.plot(x_vals, y_vals)
```

Of course all good plots need a title and axis labels.

```python
plt.title('Quadratic vs Cubic')
plt.xlabel('X')
plt.ylabel('Y')
```

You can use latex inline equations within these strings and matplotlib will render them appropriately. For the moment, let's wrap this up as a function.

```python
def quad_plot(title="Obligatory Title"):
    plt.plot([i**2 for i in range(10)])
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.title(title)
```

And then we can dive into styling and other tweaks. Matplotlib comes with some default styles, which we can see here:

```python
for style in plt.style.available:
    plt.figure()
    with plt.style.context(style):
        quad_plot(title=style)
```

Have a look through these and see if you can't find something that looks presentable.
These styles are all fully customisable and there is a near endless amount of aesthetic tweaking you can get up to here. If you're not happy with the options on offer, the `seaborn` package has more.

Matplotlib also does bar plots with `plt.bar` and can do images and two dimensional plots with `imshow`. There are a range of other plots that cover most applications.


## **** Problem [10 Minutes] Fitter **** 
- Plot the output of your original Gaussian and your fitted Gaussian from the prior problem
- Again momentarily pretending that the Gaussian represents a normalised control pulse, produce a two dimensional image plot of the population of qubits in the 1 state as you vary the width and amplitude of your Gaussian.

## 4.0.4 More Plotting

3D plots require the mplot3d package from `mpl_toolkits`.

```python
from mpl_toolkits import mplot3d
```

And while we're here, let's get numpy involved

```python
import numpy as np
```

The numpy linspace and meshgrid functions are quite useful for setting coordinates. The first argument is the lower bound, the second the upper and the third the number of points sampled in that range.

```python
x_vals = np.linspace(-5, 5, 50)
y_vals = np.linspace(-5, 5, 50)

def quad_3d(x, y):
    return x ** 2 + y ** 2

x_coords, y_coords = np.meshgrid(x_vals, y_vals)

z_coords = quad_3d(X_coords, Y_coords)
```

We'll also save the plot object to play around with as we need to.

```python
plot = plt.axes(projection='3d')
plot.plot_surface(x_coords, y_coords, z_coords)
```


## **** Problem ($\infty$ minutes) Make a pretty plot  **** 
- Use your hailstone function to plot the length of each sequence for all numbers in some range.
- Format your plot nicely enough that somebody else approves of it
- Nitpick someone else's plot and see if they can find a way to implement your changes

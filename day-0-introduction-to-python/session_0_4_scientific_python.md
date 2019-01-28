
# 4. Python for scientific computing

While Python is a very popular programming language due to its simplicitly and expressiveness, it is also receiving increasingly more attention in the context of scientific computing. Today there is a vast amount of scientific libraries out there which help you to perform almost any numeric task you can think of - from Fourier transforms to differential equation solvers, or machine learning and clever data visualisation tools. In this section we take a look at three of the most commonly used libraries: [NumPy](https://numpy.org), [Scipy](https://scipy.org) and [Matplotlib](https://matplotlib.org).

If in doubt when using a new package, don't forget to `dir()` the package, and `help()` on anything within the package.

## 4.1 NumPy - Numerical computing in Python

```python
import numpy as np
```

Numpy is a numerical python library and contains a few functions that come in handy.

```python
np.log
np.sqrt
np.array
```

And at last, arrays, vectors and matrices. Numpy can convert a list to an array. The lists must be regular and all elements must be of the same type.

```python
x = np.array([
    [0, 1],
    [1, 0]
])
```

These arrays can be treated as tensors. Rather than lists where addition was concatination and multiplication was duplication, these will now follow the appropriate mathematical operations.

```python
x + x
x * 5
-x
x ** 2
```

We can still slice these arrays in the same manner as a list:

```python
>>> x[:,1]
array([1,0])
```

If we want to see the dimensions of these slices we can use the `.shape` property.

```python
>>> x[:,1].shape
(2,)
```

Of course as arrays have a shape, we can also reshape them

```python
>>> x.reshape((4, 1))
array([[0],
       [1],
       [1],
       [0]])
>>> x.reshape((1,4))
array([[0, 1, 1, 0]])
```

As arrays must contain a single type, this type is defined by the dtype property, and can be set as a keyword argument when the array is created.

```python
>>> x.dtype
dtype('int64')
```

Numpy also offers the `dot` and `tensordot` functions for more general matrix and tensor multiplication, along with the `kron` operation for the kronecker product.

## 4.2 Matplotlib - Visualising data in Python

Matplotlib is a matlab like interface for plotting in Python. 

We'll take advantage of the jupyter notebook interface here, so start up jupyter from your terminal with: 

```python
jupyter notebook
``` 
Your browser should open to display your current directory tree. Once here, create a new notebook and import matplotlib. 

```python
import matplotlib.pyplot as plt
```

As we'll be displaying the plots within the notebook, we need to specify that we're using matplotlib inline.

```python
%matplotlib inline
```

And now we can start plotting.  

```python
y_vals = [i**2 for i in range(10)]
plt.plot(y_vals)
```

We can also specify the x coordinate positions

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


## **** Problem **** 
- Use your hailstone function to plot the length of each sequence for all numbers in some range.
- Format your plot nicely enough that somebody else approves of it
- Nitpick someone else's plot and see if they can find a way to implement your changes

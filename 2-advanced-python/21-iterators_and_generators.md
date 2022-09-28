## 5 Iterators and Generators


### 5.1 Try and Except
    
When an error occurs, Python will throw an exception. These exceptions can be caught and handled, preventing the code from crashing.

```python
  try:
    5 / 0
  except ZeroDivisionError: 
    print("Oops")
  finally: # If needed for any cleanup 
    pass
```

Exceptions are typed; such that different exceptions may caught and handled differently. You can see the entire list of base exceptions in Python in `__builtins__`. We will return to this object later.

From a style point of view, exceptions should be a matter of last resort, proper input formatting is always a better approach than resorting to a very crude nominally undeclared and widely scoped GOTO. This only becomes messier if functions are included within the try block.

It's a good, if not explicitly necessary idea to specify what error is being caught in each case. While you can leave this blank, it generally demonstrates that the programmer does not quite know what their code is doing or why it is crashing. 

Exceptions can be manually raised using the `raise` keyword:

```python
raise TypeError
```

### 5.2 Iterators And Generators
    
An iterable is any object in python with the `__iter__` method. Iter can be invoked using the `iter` dispatch function.
An iterator is any object in python with the `__next__` method. Next can be invoked using the `next` dispatch function.

An iterator contains an internal state and will return one element of the state at a time, when it reaches the end it will raise a `StopIteration` exception. 


```python
for i in [1, 2, 3]:
    print(i)
```

```python
iter_obj = iter([1, 2, 3])
while True:
    try:
        i = next(iter_obj)
    except StopIteration:
        break
    print(i)
```

From the above we can see that collections are already iterables, and that a for loop is simply looping over their iterator. We can also see that the `for` keyword is what we can consider to be a "generator expression" as we will see later.

A special class of iterator is the generator. A generator is a function that has been converted into an iterator using the `yield` keyword. 

```python
def my_generator():
    yield "Test"
    yield 5
    yield 1 + 1j
    return
```

Yield will temporarily halt the execution of the function, return the current value and then resume execution when the function is called again. Return will raise StopIteration.

We can demonstrate that the generator is an iterable by checking its properties using the `dir` method.

### [Problem - 5 minutes] Range
Implement your own range function a generator.

### [Problem - 15 minutes] Convex Combinations

Write a generator that produces all combinations with replacement given a list of elements and a number of elements to draw.

For example:
```python
combinations(['a', 'b', 'c'], 2)
```
Should produce:
```python
aa
ab
ac
ba
bb
bc
ca
cb
cc
```

Consider the memory overhead between using a generator as compared to storing each element in a list. Consider what features you lose when using an iterator as compared to a collection. 


### [Problem - 15 minutes] Linked List
Implement an iterator for the `LinkedList` data structure provided below. Focus on `NodeIter` first and implement `LinkedListIter` using it.

    ```python
    class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __iter__(self):
        return NodeIter(self)

class LinkedList:
    def __init__(self):
        self.head = None

    def get_last_node(self):
        if self.head is None:
            return None
            
        # Uses NodeIter to get to the last node
        for node in self.head:
            if node.next is None:
                return node

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.get_last_node()
        last_node.next = new_node

    def __iter__(self):
        return LinkedListIter(self)

class NodeIter:
    def __init__(self, node):
        self.node = node

    # TODO: Implement me
    def __iter__(self):
        pass

    # TODO: Implement me
    def __next__(self):
        pass
        
class LinkedListIter:
    # TODO: Implement me
    def __init__(self, lst):
        pass

    # TODO: Implement me
    def __iter__(self):
        pass

    # TODO: Implement me
    def __next__(self):
        pass
```





### 5.3 Map, Filter, Reduce, Partial
Each of these functions have an intutive understanding of their operation, however their implementation may at first look a little odd.

Map is a generator that applies a function to every element of a collection: `f(g, [a, b, c, ...]) -> [g(a), g(b), g(c), ...]`.

```python
def map(fn, collection):
    for i in collection:
        yield fn(i)
    return
```

Filter is a generator that removes all the elements in a collection that don't satisfy the predicate provided.
```python
def filter(pred, collection):
  for i in collection:
        if pred(i):
            yield(i)

filter(is_even, range(10))
```

Zip is a generator that takes at least two iterables of the same length and returns their elements  
```python
def zip(*iterables):
    it = [iter(i) for i in iterables]
    while True:
        yield tuple(next(i) for i in it)
```

Reduce applies a function and 'consumes' an iterable, so `reduce(f, [a, b, c]) -> f(f(a, b), c)`
```python
def reduce(fn, iterable):
    it = iter(iterable)

    value = next(it)

    for element in it:
        value = function(value, element)

    return value
```


Partial allows us to partially place arguments in a function and then 
```python
def partial(fn, *args, **kwargs):
    def p_func(*p_args, **p_kwargs):
        return fn(*args, *p_args, **kwargs, **p_kwargs)
    return p_func
```



### 5.4 List Comprehension and Generator Comprehension

Casting an iterator to a list will exhaust its elements and store them within the list, for example": `list(range(10))`. Given that a for loop is already a generator expression, we can cast those to lists as well:

```python
gen_exp = (j ** 2 for j in range(10))
for i in gen_exp:
    print(i)
```
You can also use `if` statements inside comprehensions 
```python
from math import exp, pi
gen_exp  = (exp(j, pi) for j in range(10) if j % 2 == 0)
for i in gen_exp:
  print(i)
```

Using square brackets instead of parenthesis collects generator elements into a list for you. This is a list comprehension.
```python
list_exp = [j ** 2 for j in range(10)]
print(list_exp)
```

### 5.5 Anonymous Functions

Given the ubiquity of functions as objects it would be useful to be able to quickly declare functions as python objects without assigning them to a particular namespace. From this we have un-named or anonymous functions.

```python
fn = lambda x : x + 1
fn(5)
```

By not specifying a name we can use these as shorthand:
```
map(lambda x : x + 1, [1, 2, 3])
```

These can be very helpful for reordering arguments for use with partial or other functions, for example using lambda to reorder allows us to curry the second argument rather than the first.
```python
partial(lambda a, b: f(b, a), val)
```


### [Problem - Homework]

Functional programming is just as powerful as imperative programming. Consider the following code that recusively defines the integers and then rederives addition and exponentiation.

```python
interpret_int = lambda n : n(lambda x : 1 + x)(0)

ONE = lambda f : lambda x : f(x)
PLUS = lambda x : lambda y : lambda p : lambda q : x(p)(y(p)(q))
EXP = lambda m : lambda n : n(m)

TWO = PLUS(ONE)(ONE)
print(interpret_int(EXP(TWO)(EXP(TWO)(TWO))))
```

Derive a new lambda expression that defines multiplication.

import unittest as pyunit

from example_package import example_file 

class ExampleTest(pyunit.TestCase):

    def test_example(self):
        assert(example_file.value == 5)
    

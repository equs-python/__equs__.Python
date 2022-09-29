from setuptools import setup

setup(
    name='example_pkg', # Pip will recognise this as 'example-pkg'
    version='0.0',
    description='An example Python module',
    package_dir={'' : 'src'},
    author='Mr. Neutron',
    packages=['example_package']
)

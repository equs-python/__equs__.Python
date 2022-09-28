# 4.1 Python and Quantum

While there are a range of different Python libraries out there for quantum simulation, benchmarking and execution (qutip, pyquil, cirq, pennylane etc) we'll be looking at Qiskit as a representative of a range of libraries that all map Python to some choice of instruction set.

Here are a few current Python packages and their utilities, typically simulators are free to use while executing code on devices requires an invitation.

 - Pyquil/Forest - Python frontends for the Quil ISA
 - Qiskit - Python frontend for the OpenQASM ISA
 - Cirq - Python frontend for Google's Quantum simulators and devices
 - ProjectQ - Python frontend for the OpenQASM ISA
 - Ocean - Python frontend for DWave
 - Strawberry Fields - Python frontend with multiple backends

Most of the above follow a similar set of patterns.

 - A gate class with derived classes for standard gate sets.
 - A circuit class that consists of an ordered collection of gates.
 - A simulator / backend class that executes the circuit and provides measurement results.

Typically using the backend class requires some form of account or registration. 

Additionally most of the above operate through jupyter notebooks which allow for easy visualisation. Workflow using these tools often looks as follows:

 - An ipython terminal for 'scratchpad' python code
 - A jupyter notebook for executing and visualising code against a simulator or backend
 - A text editor or IDE for saving useful constructs in a Python module for re-use
 - A terminal for using git and executing test cases or other system level tasks


## 4.1.1 Qiskit basics

We'll start with specifying a circuit
```python
from qiskit import IBMQ, QuantumCircuit, execute

n_qubits = 5
n_classical_bits = 5

# Our circuit object
circuit = QuantumCircuit(n_qubits, n_classical_bits)

# Add a gate to the circuit
circuit.x(0)

# Measure the 0th qubit
circuit.measure([0], [0]) 

# Draw our circuit
circuit.draw()
```
Circuits have a number of properties that produce standard gates, as ever we can see class methods and properties with `dir`. Of particular note are the gates on offer. Qiskit devices only calibrate `X`, `sqrt(X)` and `ZX` gates along with an in software implementation of `Z` gates, all other gates are constructed from this base set, circuits will typically be more accurate if they can be expressed more directly in these terms.

The set of builtin gates which are internally decomposed include: `x, y, z, t, s, p(theta), u3(theta, phi, gamma), r[x, y, z](theta), ucr[x, y, z](theta)`. All of these (and a few others) should be supported by the circuit class. Lastly there are a few 'meta' gates that act as higher level abstractions of common gate sequences are the MCMT (multi-control multi-target) gate 


Next we can pass the circuit object to a simulator or backend. Some of these require an API key to use remote devices, however we can also use local inbuilt simulators.

To load IBM account credentials (this may not be required for some of the simulators) we can:
```python
qiskit.IBMQ.save_account(token) # Saves an account to disk using an API token for loading later, can be done once per machine and then loaded from then on
qiskit.IBMQ.load_account() # Loads a saved account
```

Next we may be interested in what devices are available to us:

```python
provider = qiskit.IBMQ.get_provider()
print(provider.backends())
```

Typically the 'open' backends are no larger than five qubits. The simulators can handle up to 32 qubits. We can select a particular backend using:

```python
backend = provider.get_backend('ibmq_quito')
```
If we do not wish to deal with the device queue we can also execute on a simulator. To get a local simulator we can grab one of the fake backends. 

```python
from qiskit.providers.fake_provider import FakeVigo # Fake 5 qubit device
from qiskit.providers.fake_provider import FakeTokyo # Fake 20 qubit device

backend = FakeTokyo()
```

If we're in a jupyter notebook we can make use of the ability of the browser to visualise these devices

```python
import qiskit.tools.jupyter # Some helper stuff for jupyter notebooks
backend()
```

Next we should transpile our circuit for the device that we are executing it on. This allocates qubits, decomposes gates into the backend's basis set and injects swaps and bridges to ensure that all gates can be performed by the backend device's coupling map.
```python
transpiled_circuit = qiskit.transpile(circuit, backend=backend)
```
Transpile may also take arguments to fix an initial qubit mapping, seeds to ensure consistency between random transpilation methods, and different sets of basis gates. We could further decompose our 

To execute our code we create a job with a list of circuits, a backend and a number of shots.
```python
job = execute(transpiled_circuit, backend, shots=1024)
```
The job object may either be a synchronous call to a local backend, or an asynchronous call to a remote backend. If it is asynchronous then your python code will not block until you attempt to view the measurement results of the circuit.
```python
results = job.result()
print(results.get_counts())
```
Our results are stored in a dictionary where the keys are binary strings of measurement outcomes and the values are the count for that outcome. **Be aware that for mytsterious reasons qiskit count strings reverse the order of the qubits.**

Which we can plot as a histogram.

```python
qiskit.plot_histogram(results.get_counts())
```

## 4.1.2 Qiskit Backends

A quick look at the properties of the device backends reveals a small family of other qiskit objects, it is provided here as a summary.
- `name` : The name of the device
- `status` : The status of the device, useful if the device has gone offline or to check the queue length
- `options` / `set_options` : The default device options, the ability to set options. 
  - For physical backends this can modify measurement and some other properties of the device
  - For simulators backends these set the simulation options 
- `configuration()` : Device configuration
  - `n_qubits` : Number of qubits on that device
  - `gates` : The gates that the device supports (marked as TODO by some devices)
  - `coupling_map` : The device coupling map as a list of lists
  - `basis_gates` : The basis gates that the device supports
- `properties()` : Device properties
  - `t1` : T1 time of the device
  - `t2` : T2 time of the device
  - `gates` : Gates that the device supports
  - `frequency(qubit)` : The frequency of the qubit (not sure which frequency, docs don't say)
  - `readout_error(qubit)` : Scalar readout error rate
  - `readout_length(qubit)` : Readout time
  - `last_update_date` : When this device was last updated (typically anywhere up to five days for a real device, simulated backends are a snapshot)


## 4.1.3 Randomised Benchmarking, Allocation and Routing
Here we will look at the necessity of tranpilation for qubit allocation and routing. 

- Write a sample random circuit using consisting of x gates on random qubits, cnot gates between random qubits.
- Apply the same set of gates in reverse order such that the total action of the circuit is the identity.

Try transpiling both with qiskit's native transpiler and SABRE. SABRE transpilation may be performed as below
```python
transpiled_circuit = qiskit.transpile(
    circuit, backend=backend,
    layout_method='sabre', routing_method='sabre'
    ) 
```
It's recommended to use `FakeTokyo` for this, and to have enough gates that statistically all physical qubits are involved in the circuit before transpilation. Have a look at the transpiled circuit produced by native qiskit and by SABRE. In particular consider the problems that may arise from the introduction of ancillae.

Extend your circuit generation to write a function that builds randomised benchmarking circuits. You should consider how you can parameterise your basis set as a part of the function. 
- Use scipy to fit your RB curves and calculate the average gate error rate
- Compare the average gate error rates when SABRE is used for allocation, routing, routing and allocation and bare qiskit

## 4.1.5 Measurement Error Calibration [Extension]

Measurement errors on IBM devices are state dependent. The error rates associated with measuring a 1 state are often double that of measuring a 0 state.
- Construct a set of circuits that profiles the measurement error channel in the measurement basis (consider some limited tomography here)
- Write a class that wraps the `results` object such that it will execute a target circuit along with the measurement error calibration circuits
- Let your class return a modified set of counts that have applied the inverse of the measurement error channel to the bare qiskit results.
Compare the accuracy of circuits both with and without your measurement error calibrating class.
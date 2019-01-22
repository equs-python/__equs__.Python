"""
Example file for the __equs__.Python workshop 2019

https://github.com/equs-python/__equs__.Python

This file contains the measure_state function which
performs a measurement of a given quantum state.
"""
import numpy as np

def measure_state(state, number_of_samples=1):
    """Performs a projective measurement of a quantum state in the Z-basis

    Parameters
    ----------
    state : numpy ndarray
        The state in density matrix representation
    number_of_samples : int, optional
        How often to perform a measurement. Defaults to 1.

    Returns
    -------
    list
        A list of state vectors for each measurement

    Examples
    -------
    Single-qubit pure state measurement:
        >>> import numpy as np
        >>> state = np.array([[0, 0], [0, 1]])
        >>> measure_state(state, 2)
        [array([0., 1.]), array([0., 1.])]
    """
    num_qubits = state.shape[0] // 2
    projectors = [
        np.kron(
            pure_state_vector[:, np.newaxis],
            pure_state_vector[:, np.newaxis].T
        )
        for pure_state_vector in np.eye(num_qubits * 2)
    ]
    outcome_probabilities = [
        np.abs(np.trace(projector.dot(state))) for projector in projectors
    ]
    print(outcome_probabilities)
    results = np.random.choice(
        [i for i in range(num_qubits * 2)],
        number_of_samples,
        p=outcome_probabilities)
    return [
        np.eye(num_qubits*2)[result, :] for result in results
    ]

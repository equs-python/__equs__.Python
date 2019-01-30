"""
Example file for the __equs__.Python workshop 2019

https://github.com/equs-python/__equs__.Python

This file contains unit tests for the measure_state
function from the measurement_2.py module.
"""
import numpy as np

from measurement_2 import measure_state

def test_pure_state_measurement():
    """ Testing the measurement of a pure state in Z """
    # Test 1: State |0>, one measurement
    state = np.array([[1, 0], [0, 0]])
    expected_result = np.array([1, 0])
    actual_result = measure_state(state, number_of_samples=1)

    # Numpy's version of the assert statement for arrays
    assert np.allclose(expected_result, actual_result)

    # Test 2: State |1>, one measurement
    state = np.array([[0, 0], [0, 1]])
    expected_result = np.array([0, 1])
    actual_result = measure_state(state, number_of_samples=1)

    assert np.allclose(expected_result, actual_result)

def test_pure_state_measurement_stats():
    """ Testing the statistics of a pure state measurement in Z """
    # Test 1: State |0>, 100 measurements
    state = np.array([[1, 0], [0, 0]])
    expected_result = np.array([1, 0])
    actual_results = measure_state(state, number_of_samples=100)
    # Loop over the results
    for actual_result in actual_results:
        assert np.allclose(expected_result, actual_result)

def test_mixed_state_measurement_stats():
    """ Testing the statistics of a pure state measurement in Z """
    # State (|0> + |1>)/sqrt(2), 5000 measurements
    state = np.array([[0.5, 0.5], [0.5, 0.5]])
    number_of_samples = 5000
    actual_results = measure_state(
        state, number_of_samples=number_of_samples
    )
    # Count how often the |0> and |1> state were measured
    outcomes, counts = np.unique(
        actual_results, return_counts=True, axis=0
    )
    tolerance = 0.05
    assert abs(counts[0] / number_of_samples - 0.5) < tolerance


"""This module contains unit tests for the merge_sort function
from the hw2_debugging module. It tests various scenarios including
sorted arrays, reverse sorted arrays, and random arrays.
"""

import rand
from hw2_debugging import merge_sort


def test_sorted_array():
    """
    Tests the merge_sort function with an already sorted array.
    Asserts that the sorted array remains unchanged.
    """
    arr = [1, 2, 3, 4, 5]
    assert merge_sort(arr) == [1, 2, 3, 4, 5], "Sorted array should remain sorted"


def test_reverse_sorted_array():
    """
    Tests the merge_sort function with a reverse sorted array.
    Asserts that the array is sorted in ascending order.
    """
    arr = [5, 4, 3, 2, 1]
    assert merge_sort(arr) == [1, 2, 3, 4, 5], "Reverse sorted array should be sorted"


def test_random_array():
    """
    Tests the merge_sort function with 
    a randomly generated array.
    Asserts that the array is sorted correctly.
    """
    arr = rand.random_array(10)
    
    sorted_arr = merge_sort(arr)
    
    expected_arr = sorted(arr)

    assert sorted_arr == expected_arr, "Random array should be sorted"

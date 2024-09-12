"""This module imports random_array function from rand.py and uses it to
generate, sort a random array in ascending order using the
merge sort algorithm.
"""

from rand import random_array


def merge_sort(arr):
    """
    Sort an input array using the merge sort algorithm by
    recursively dividing
    and recombining the array.

    Args:
        arr (list): The input array to be sorted.

    Returns:
        list: The sorted array.
    """
    if len(arr) == 1:
        return arr

    half = len(arr) // 2
    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
    Merges two sorted arrays into a single sorted array.

    Args:
        left_arr (list): The left half of the array.
        right_arr (list): The right half of the array.

    Returns:
        list: Merged and sorted array.
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1  # Increment after placing in merge_arr
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1  # Increment after placing in merge_arr

    # Add any remaining elements from right_arr
    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]
        right_index += 1

    # Add any remaining elements from left_arr
    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]
        left_index += 1

    return merge_arr


# Generate a random array of 20 elements
test_arr = random_array(20)

# Sort the array
arr_out = merge_sort(test_arr)

# Print the sorted array
print(arr_out)

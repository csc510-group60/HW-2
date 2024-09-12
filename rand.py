"""This module utilizes the subprocess.run
function in order to generate
random arrays within a given range"""
import subprocess


def random_array(size):
    """Function accepts an integer size as a parameter,
    and uses the subprocess.run function
    in order to generate random integers between
    1 and 20."""
    arr = [0] * size
    for i in range(size):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True
        )
        arr[i] = int(shuffled_num.stdout.strip())
    return arr

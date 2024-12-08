#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Convert the list to a numpy array with 64-bit integers
    arr = np.array(arr, dtype=np.int64)
    # Calculate the sum excluding the max and min values
    print(f"{np.sum(arr) - np.max(arr)} {np.sum(arr) - np.min(arr)}")


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

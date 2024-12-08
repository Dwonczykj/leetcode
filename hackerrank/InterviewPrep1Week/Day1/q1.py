#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr, n):
    # Write your code here
    p_counter = 0
    z_counter = 0
    for i in range(n):
        if arr[i] > 0:
            p_counter += 1
        elif arr[i] == 0:
            z_counter += 1
    print("\n".join(
        [f"{(a/n):.6f}" for a in (p_counter, (n-p_counter-z_counter), z_counter)]))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)

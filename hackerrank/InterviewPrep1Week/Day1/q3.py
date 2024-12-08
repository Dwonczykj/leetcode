#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    """Convert a 12-hour time to a 24-hour time."""
    # Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
    # - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
    # Write your code here
    if s[-2:] == "AM":
        return s[:-2] if s[:2] != "12" else "00" + s[2:-2]
    else:
        return f"{int(s[:2]) + (12 if s[:2] != "12" else 0)}{s[2:-2]}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

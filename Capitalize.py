#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    stringList = s.split(" ")
    capitlaizedList = []
    for word in stringList:
        capitlaizedList.append(word.capitalize())
    
    return " ".join(capitlaizedList)

if __name__ == '__main__':
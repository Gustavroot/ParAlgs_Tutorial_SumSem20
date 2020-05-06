"""

	Main gateway to all the examples written in this repository

"""


# Local dir
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path += '/'
import sys
# adding examples-related resources
sys.path.append(dir_path + "./examples/")
from example01 import EXAMPLE01


if __name__ == '__main__':

    # options to play with 'lu-alg': {'ge_kji--naive','ge_kij--naive','ge_kji--opt','ge_kij--opt'}
    params = { 'lu-alg':'ge_kji--naive', 'mat-size':'600x600', 'mat-random':True }
    EXAMPLE01(params)

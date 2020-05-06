"""
	Basic Gaussian elimination, comparison of kij vs kji
"""

# Local dir
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path += '/'
import sys
sys.path.append(dir_path + "../base/")
# adding Matrix-related resources
from matrix import Matrix


def EXAMPLE01(params):

    print("\n****")
    print("EXAMPLE01:\n")

    # un-pack parameter for the LU decomposition
    lu_params = dict()
    for key in params:
        if key.split('-')[0] == 'lu':
            lu_params[key.split('-')[1]] = params[key]

    # un-pack params for the construction of the matrix
    mat_params = dict()
    for key in params:
        if key.split('-')[0] == 'mat':
            mat_params[key.split('-')[1]] = params[key]

    buff_mat = Matrix(mat_params)

    t1 = buff_mat.computeLU(lu_params)

    print("--matrix size : "+mat_params['size'])
    print("--execution time (seconds) : "+str(t1)+"\n")

    buff_mat.checkLUCorrectn()
    print("****\n")

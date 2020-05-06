"""
	Consists of everything related to the Matrix class
"""

import time
import numpy as np

from base import luDecomposer


class Matrix:

    def __init__(self, params):

        if 'size' not in params:
            raise Exception("Parameter mat-size is needed for matrix manipulations.")
        mat_size = [int(i) for i in params['size'].split('x')]
        if mat_size[0] != mat_size[1]:
            raise Exception("We deal only with squares matrices here.")
        self.nx = mat_size[0]
        self.ny = mat_size[1]

        if 'random' not in params:
            raise Exception('Parameter mat-random is needed for matrix initializations.')
        self.random = params['random']
        if self.random == True:
            self.mat = np.random.rand(self.nx,self.ny)
        else:
            raise Exception('The Matrix class is not able to import matrices given by you... yet.')

        self.matLU          = []
        self.measureTimings = True
        self.wasLUApplied   = 0


    # Input:
    # 	'alg':  algorithm to be chosen (e.g. gaussian_kij)
    # Returns:
    # 	the execution time, with a value of zero if self.measureTimings was set to False
    def computeLU(self, params):
        exec_time = 0

        if self.measureTimings:
            exec_time = time.time()

        # first parameter is the LU-params, second is the matrix (object of type Matrix)
        self.matLU = luDecomposer(params, self)
        self.wasLUApplied += 1

        if self.measureTimings:
            exec_time = time.time() - exec_time

        return exec_time


    def getLU(self):
        return self.matLU


    def getMat(self):
        return self.mat


    def checkLUCorrectn(self):
        print("Checking the correctness of LU disabled for now.")


    def display(self):
        print(self.mat)

"""
	Contains functions that can be generally called from anywhere
        (provided this file is added to the local Python path)
"""

import numpy as np


# Input :
#	'ijk_form' : which of the ijk forms of Gaussian-Elimination to use
#	'M' : the matrix on which to perform the factorization
# Output :
#	without overriding M, it returns a single matrix containing L and U
def luDecomposer(params, M):

    ijk_forms = ['kij--naive','kji--naive','kij--opt','kji--opt']

    alg_split = params['alg'].split('_')
    if alg_split[0] != 'ge':
        print("Only Gaussian-Elimination supported for LU decomposition.")
    ijk_form = alg_split[1]

    if ijk_form not in ijk_forms:
        raise Exception('The chosen ijk-form is not implemented')

    print("LU decomposition using the "+ijk_form.split('--')[0]+" form of (sequential) Gaussian-Elimination ("+ijk_form.split('--')[1]+")\n")

    M = M.getMat()

    if ijk_form == 'kij--naive':
        return kijLUDecomposerNaive(M)
    elif ijk_form == 'kji--naive':
        return kjiLUDecomposerNaive(M)
    elif ijk_form == 'kij--opt':
        return kijLUDecomposerOpt(M)
    elif ijk_form == 'kji--opt':
        return kjiLUDecomposerOpt(M)
    else:
        raise Exception('LU decomposer not known')


# kij form, naive (i.e. explicit accesses)
def kijLUDecomposerNaive(M):

    m = M.shape[0]
    n = M.shape[1]

    N = np.copy(M)

    for k in range(0,n):
        for i in range(k+1,n):
            N[i,k] = N[i,k] / N[k,k]
            for j in range(k+1,n):
                N[i,j] = N[i,j] - N[i,k] * N[k,j]

    return N


# kji form, naive (i.e. explicit accesses)
def kjiLUDecomposerNaive(M):

    m = M.shape[0]
    n = M.shape[1]

    N = np.copy(M)

    for k in range(0,n):

        for i in range(k+1,n):
            N[i,k] = N[i,k] / N[k,k]

        for j in range(k+1,n):
            for i in range(k+1,n):
                N[i,j] = N[i,j] - N[i,k] * N[k,j]

    return N


# kij form, optimized (i.e. NumPy's slicing)
def kijLUDecomposerOpt(M):

    m = M.shape[0]
    n = M.shape[1]

    N = np.copy(M)

    for k in range(0,n):
        for i in range(k+1,n):
            N[i,k] = N[i,k] / N[k,k]
            N[i,k+1:] -= N[i,k] * N[k,k+1:]

    return N


# kji form, optimized (i.e. NumPy's slicing)
def kjiLUDecomposerOpt(M):

    m = M.shape[0]
    n = M.shape[1]

    N = np.copy(M)

    for k in range(0,n):

        N[k+1:,k] = N[k+1:,k] / N[k,k]

        for j in range(k+1,n):
            N[k+1:,j] = N[k+1:,j] - N[k+1:,k] * N[k,j]

    return N

## Some examples illustrating how parallel algorithms work and behave

&nbsp;

#### Dependencies:

To run the examples in this repository you need:

 - to have NumPy installed
 - preferably your Python installation is BLAS-enabled

#### Running the code:

Simply run
```sh
$ python main.py
```
in the terminal. For more specific details on the input params, check the comments inside of `main.py`.

#### Examples

 - basic MPI example of sending data in a ring: avoiding deadlocks
 - fan-in, parallel, naive (Alg. 21)
 - fan-in, parallel, optimized (Alg. 27)
 - matrix-matrix multiplication, serial
 - matrix-matrix multiplication, parallel (Alg. 37)
 - matmul optimized (Cannon's algorithm)
 - Gaussian-Elimination (kij and kji forms), serial, BLAS and no-BLAS (Alg. 4 and Alg. 8) :heavy_check_mark:
 - Gaussian-Elimination, kji, parallel, column-wrapped storage (Alg. 18)
 - Gaussian-Elimination, kji, parallel, column-wrapped storage, send-ahead (Alg. 21)

## Code to add matrix by splitting it up
import numpy as np
import multiprocessing
import os
from multiprocessing import get_context
def matrix_multiply_worker(A_chunk, B_chunk, C_shape, C_chunk_start):
    C_chunk = np.add(A_chunk, B_chunk)
    return (C_chunk_start, C_chunk)

def parallel_matrix_multiply(A, B, num_processes=None):
    num_rows = A.shape[0]
    C = np.zeros((num_rows, B.shape[1]))
    chunk_size = (num_rows + num_processes - 1) // num_processes

    pool = get_context("fork").Pool(processes=num_processes)
    # with multiprocessing.Pool(processes=num_processes) as pool:
    results = [pool.apply_async(matrix_multiply_worker, 
                                args=(A[i:i + chunk_size], B[i:i + chunk_size], chunk_size, i)) 
                                for i in range(0, num_rows, chunk_size)]

    for result in results:
        C_chunk_start, C_chunk = result.get()
        C[C_chunk_start:C_chunk_start + chunk_size, :] = C_chunk

    return C

A = np.random.rand(100, 100)
B = np.random.rand(100, 100)

num_processes = 4

C = parallel_matrix_multiply(A, B, num_processes)
print(C)
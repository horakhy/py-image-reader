import numpy as np
import time


w, h = 1000, 1000
Matrix = [[0 for x in range(w)] for y in range(h)] 

for i in range(h):
    for j in range(w):
        Matrix[i][j] = i + j

start_time = time.time()
np.dot(Matrix, Matrix)

print("--- %s seconds ---" % (time.time() - start_time))


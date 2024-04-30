from threading import Thread
 
MAX = 4
MAX_THREAD = 4
 
matC = [[0 for i in range(MAX)] for j in range(MAX)]
step_i = 0
 
# Function to print matrix in readable format
def printMatrix(mat):
  for row in mat:
    print(row)
 
# Function to multiply a row of matrix A
# with entire matrix B to get a row of matrix C
def multi():
  global step_i, matC
  i = step_i
  step_i = step_i + 1
  for j in range(MAX):
    for k in range(MAX):
      matC[i][j] = matC[i][j] + matA[i][k] * matB[k][j]

def add():
  global step_i, matC
  i = step_i
  step_i = step_i + 1
  for k in range(MAX):
      matC[i][k] = matA[i][k] +matB[i][k]
def simpleMult():
  global step_i, matC
  i = step_i
  step_i = step_i + 1
  for k in range(MAX):
      matC[i][k] = matA[i][k] * matB[i][k]
 
if __name__ == "__main__":
  # matrix A used for muliplication
  matA = [[0,0,0,0],
          [9,2,0,3],
          [0,2,1,7],
          [2,2,7,9]]
   
  # matrix B used for multiplication
  matB = [[6,5,5,2],
          [1,7,9,6],
          [6,6,8,9],
          [0,3,5,2]]
  # creating list of size MAX_THREAD
  thread = list(range(MAX_THREAD))
  # creating MAX_THEAD number of threads
  for i in range(MAX_THREAD):
    thread[i] = Thread(target=multi)
    thread[i].start()
     
  # Waiting for all threads to finish
  for i in range(MAX_THREAD):
    thread[i].join()
     
  # Printing the resultant matrix C = A x B
  printMatrix(matC)




  ##### For reference to generate random matrix
  MATRIX_SIZE = 1000
MATRIX_COUNT = 16


def rnd_matrix()i:
    offset = np.random.randint(1,10)
    stretch = 2*np.random.rand()+0.1
    return offset + stretch * np.random.rand(MATRIX_SIZE, MATRIX_SIZE)


print "Creating input matrices in parent process."
# Create input in memory. Children access this input.
INPUT = [rnd_matrix(i) for i in xrange(MATRIX_COUNT)]
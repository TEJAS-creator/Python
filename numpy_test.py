import numpy as np  # Import the actual NumPy library

a = np.random.randint(1, 10, size=(3, 3))
b = np.random.randint(1, 10, size=(3, 3))

print(f"\nmatrix a = \n{a}")
print(f"\nmatrix b = \n{b}")
print(f"\nNorm= {np.linalg.norm(a)}")
print(f"\nDeterminant= {np.linalg.det(a)}")
print(f"\nInverse= {np.linalg.inv(a)}")
print(f"\nEigen Values= {np.linalg.eig(a)}")
print(f"\nMultiplication= {np.dot(a, b)}")
print(f"\nTranspose= {np.transpose(a)}")
print(f"\nRank= {np.linalg.matrix_rank(a)}")
print(f"\nTrace= {np.trace(a)}")
print(f"\nSum= {np.sum(a)}")
print(f"\nMean= {np.mean(a)}")
print(f"\nStandard Deviation= {np.std(a)}")

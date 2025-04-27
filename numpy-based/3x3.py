import numpy as np

print('Enter a 3 X 3 matrix row wise : ')
rows = []
for i in range(3):
    row = [int(x) for x in input(f'Enter row number [{i+1}] : ').split()]
    rows.append(row)

M = np.array(rows)  
print(f"Largest element is {M.max()}")
print(f"Smallest element is {M.min()}")
print(f"Sum of each row is {np.sum(M,axis=1)}")
print(f"Sum of each column is {np.sum(M,axis=0)}")
print(f"Sum is {np.sum(M,axis=None)}")

print("Sorting...")
print(f"Row wise : \n{np.sort(M,axis=1)}")
print(f"Column wise : \n{np.sort(M,axis=0)}")

print(f"All elements of the matrix in sorted order : {np.array(np.sort(M,axis=None).reshape(3,3))}")
import numpy as np

mat = np.array([
    [1,2,30,4],
    [-5,6,7,8],
    [9,10,11,12]
]
)

print(f"The matrix is \n{mat}")
print('\n')
mat = mat.T
print('Matrix after rotation by 90 degree in clockwise direction is')
print(np.flip(mat,axis=1))
print('\n')
print('Matrix after rotation by 90 degree in anti-clockwise direction is')
print(np.flip(mat,axis=0))

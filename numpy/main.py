        # library import commands: #virtualenv venv
                                # source venv/bin/activate
                                # pip install numpy



import numpy as np


n1 = np.array([10,20,30,40])
n2 = np.array([20,30,50,60])

print(np.vstack((n1,n2)))
print(np.hstack((n1,n2)))
print(np.column_stack((n1,n2)))
print(np.intersect1d(n1,n2))
print(np.setdiff1d(n1,n2))
print(np.setdiff1d(n2,n1))
print(np.sum([n1]))
print(np.sum([n1,n2]))



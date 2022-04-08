        # library import commands: #virtualenv venv
                                # source venv/bin/activate
                                # pip install numpy



import numpy as np


n1 = np.array([10,20,30,40])
n2 = np.array([20,30,50,60])

print(np.vstack((n1,n2)))
print("------------")
print(np.hstack((n1,n2)))
print("------------")
print(np.column_stack((n1,n2)))
print("------------")
print(np.intersect1d(n1,n2))
print("------------")
print(np.setdiff1d(n1,n2))
print("------------")
print(np.setdiff1d(n2,n1))
print("------------")
print(np.sum([n1]))
print("------------")
print(np.sum([n1,n2]))
print("------------")
print(np.sum([n1,n2],axis=0))
print("------------")
print(np.sum([n1,n2],axis=1))
print("------------")
print(n1+1)
print("------------")
print(n1-1)
print("------------")
print(n1+2)
print("------------")
print(n1/2)
print("------------")
print(np.mean(n1))
print("------------")
print(np.median(n1))
print("------------")
print(np.std(n1))
print("------------")



import numpy as np
n1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
n2 = np.array([[9,8,7], [6,5,4], [3,2,1]])




import numpy as np

n1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
n2 = np.array([[9,8,7], [6,5,4], [3,2,1]])

print(n1)
print("---------")
print(n1[0])
print("---------")
print(n1[-1])
print("---------")
print(n1[0:2])
print("---------")
print(n1[0:3][0:3]) 
print("---------")
n3 = n1.dot(n2)
print("---------")

np.save('numpytest1.npy', n3)

n4 = np.load('numpytest1.npy')
print(n4)
print("---------")
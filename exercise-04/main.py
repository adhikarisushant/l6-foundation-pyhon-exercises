import numpy as np

    # intro to numpy
# n1 = np.array([10, 20, 30, 40])

# print(n1)
# print(type(n1))

# n2 = np.array([[10,20,30,40],[1,3,5,7]])
# print(n2)
# n3 = np.zeros((1,2))
# print(n3)
# n4 = np.full((2,3),5)
# print(n4)

# n5 = np.arange(10,20)
# print(n5)
# n6 = np.arange(10,50,5)
# print(n6)

# n7 = np.random.randint(1,100,5)
# print(n7)
# print(n7.shape)


n1 = np.array([10,20,30,40])
n2 = np.array([20,30,50,60])
print(np.vstack(n1,n2))
print(np.hstack((n1,n2)))
print(np.column_stack((n1,n2)))
print(np.intersect1d(n1.n2))
print(np.setdiff1d(n1,n2))
print(np.setdiff1d(n2,n1))
print(np.sum([n1]))
print(np.sum([n1,n2]))
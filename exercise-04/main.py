import numpy as np

    # intro to numpy
n1 = np.array([10, 20, 30, 40])

print(n1)
print(type(n1))

n2 = np.array([[10,20,30,40],[1,3,5,7]])
print(n2)
n3 = np.zeros((1,2))
print(n3)
n4 = np.full((2,3),5)
print(n4)

n5 = np.arange(10,20)
print(n5)
n6 = np.arange(10,50,5)
print(n6)

n7 = np.random.randint(1,100,5)
print(n7)
print(n7.shape)


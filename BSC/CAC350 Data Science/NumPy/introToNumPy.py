import numpy as np

floats = np.array([1,2.5,6,8,5.25], dtype='float32')
print(floats)

np.ones(15,dtype=int)

myArray = np.arange(0,105,5)
print(myArray)

np.random.rand(10)

np.random.randint(10,50,size=10)

x1 = np.random.randint(0,10,size=8)
x1

x2 = np.random.randint(0,10,size=(5,8))
x2

x3 = np.random.randint(15, size=(3,5,8))
x3

a = np.array([1,2,3,4,5,6,7,8])
y = np.vstack([x2,a])
y

y,extra = np.split(y,[5])

x2 = x2.reshape((1,5,8))
newX3 = np.vstack([x3,x2])

h1 = np.array([5,5,5,5,5])
test = np.random.randint(10,size=(5,7))
h1 = h1.reshape((5,1))
newTest = np.hstack([test,h1])
newTest
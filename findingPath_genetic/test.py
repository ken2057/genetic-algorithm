import numpy as np

a = np.array([1,2,3])
b = np.array([7,4,8,2,1])
c = np.concatenate((a[0:1],b),axis=0)
print(c)
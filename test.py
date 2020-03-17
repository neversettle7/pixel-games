import numpy as np

x = np.arange(12).reshape((3,4))
x = np.flip(x)
print(x)
print('\n')

print(np.sort(x,axis=0))

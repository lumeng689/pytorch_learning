import numpy as np

c = np.array([
    [1, 0, 0, 0, 0, 0],
    [0.6, 0, 0.4, 0, 0, 0],
    [0, 0.6, 0, 0.4, 0, 0],
    [0, 0, 0.6, 0, 0.4, 0],
    [0, 0, 0, 0.6, 0, 0.4],
    [0, 0, 0, 0, 0, 1]
])

r = np.dot(c, c)
print(r)
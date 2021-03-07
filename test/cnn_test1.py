import numpy as np

c = np.array([
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
])

n1 = np.array([
    [1, 1, 1],
    [0, 1, 1],
    [0, 0, 1]
])

r = np.multiply(n1, c)
print(r)

n3 = np.array([
    [1, 2],
    [3, 4]
])

n4 = np.array([
    [5, 6],
    [7, 8]
])

print("n3 * n4:::  对应位置元素相乘")
# print(np.multiply(n3, n4))
print(n3 * n4)

print("n3 dot n4::: 矩阵相乘")
print(n3.dot(n4))
print("n4 dot n3::: 矩阵相乘")
print(n4.dot(n3))

r_n4 = np.linalg.inv(n4)
print("n4的逆矩阵")
print(r_n4)

print("逆矩阵相乘")
print(n4 * r_n4)
print(n4.dot(r_n4))

print('n4的转置矩阵')
print(n4.transpose())

print('n4的行列式')
print(np.linalg.det(n4))

print('求矩阵的特征值与特征向量')
'''
  求得的元组中第一个为特征值元组，
  第二个为相对应的特征向量
  此处为多行注释
  '''
print(np.linalg.eig(n4))

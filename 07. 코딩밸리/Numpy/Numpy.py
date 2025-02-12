import numpy as np

a = np.array([1,2,3])
'''print(a)
'''
b = np.array([[1,2,3],
             [4,5,6]])
'''print(b)

print(b[0,1])
print(b[0:2, 1:3])
print(a+b)
print(a*b)
'''

class_nums = np.array(
[[9, 9, 10],
[8, 8, 8],
[9, 8, 10],
[8, 7, 7]]
)
mean_students = np.array([25, 28.9, 28.1, 23.5])
senior_students = class_nums[:, 2] * mean_students
print(senior_students)
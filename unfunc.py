import numpy as np
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
# Without ufunc, we can use Python's built-in zip() method:
# z = []
# for i, j in zip(x, y):
#     z.append(i+j)
# NumPy has a ufunc for this, called add(x, y) that will produce the same result.
z = np.add(x, y)
print(z)

import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]


def addarr(x, y):
    return x+y


# numpy.frompyfunc(func, nin, nout)
# nin: [int] Number of input arguments to that function.
# nout: [int] Number of objects returned by that function.


addarr = np.frompyfunc(addarr, 2, 1)
print(addarr(x, y))

# -----------------------------------
# Check if a Function is a ufunc

print(type(np.add))

# If it is not a ufunc, it will return another type, like this built-in NumPy function for joining two or more arrays:

print(type(np.concatenate))

# If the function is not recognized at all, it will return an error:
# print(type(np.blalsajkld))

# -----------------------------------
# To test if the function is a ufunc in an if statement
if type(np.add) == np.ufunc:
    print("add is a universal function")
else:
    print("add is not a universal function")

# now checking with the concatenation
if type(np.concatenate) == np.ufunc:
    print("concatenate is a universal function")
else:
    print("concatenate is not a universal function")

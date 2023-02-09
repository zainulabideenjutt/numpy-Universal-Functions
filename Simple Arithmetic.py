# You could use arithmetic operators + - * / directly between NumPy arrays,
# but this section discusses an extension of the same where we have functions that can take any array-like objects e.g. lists, tuples etc. and perform arithmetic conditionally.
import numpy as np
# Original Arrays
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])


# Simple Arithmetic
# =================================================================
# Addition
sum = np.add(arr1, arr2)
print("Sum :", sum)

# Subtraction
sub = np.subtract(arr1, arr2)
print("Subtraction : ", sub)
print(sub.base)
# base is none that means is a copy a not changing the original arrays if i change the sub

# Multiplication
Multiply = np.multiply(arr1, arr2)
print("Multiplication :", Multiply)

# Divide
Divide = np.divide(arr2, arr1)
print("Divide : ", Divide)

# Medium Arithmetic
# ========================================================
# Power()
# -------------------------------------------
# The power() function rises the values from the first array to the power of the values of the second array
power = np.power(arr1, arr2)
print("Power : ", power)

# Remainder
# -------------------------------------------------
# Both the mod() and the remainder() functions return the remainder of the values in the first array corresponding to the values in the second array
mod = np.mod(arr1, arr2)
remainder = np.remainder(arr1, arr2)
print("Reminder : ", remainder)
print("Msdulus : ", mod)

# Quotient and Mod or Remainder
# -------------------------------------------------
# The divmod() function return both the quotient and the the mod.
Quotientmod = np.divmod(arr1, arr2)
# First one will be Quotient and the other one will be reminder
print("Quotient and Remoinder : ", Quotientmod)

# Absolute Values
# -------------------------------------------------
# using real number array
realarray = [-1, -2, 1, 2, 3, -4]
Absolutearray = np.absolute(realarray)
print("Absolute array : ", Absolutearray)

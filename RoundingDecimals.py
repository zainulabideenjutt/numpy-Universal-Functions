# There are primarily five ways of rounding off decimals in NumPy:
# truncation
# fix
# rounding
# floor
# ceil
import numpy as np
# ==============================================
# Truncation
# ==============================================
# |Remove the decimals, and return the float number closest to zero
# |Use the trunc() and fix() functions.
arr = np.trunc([-3.12532, 3.3265, -6.65546])
print("Output using trunc", arr)
# -----------------------------------------------Using fix()
arr = np.fix([-3.12532, 3.3265, -6.65546])
print("Output using fix :`", arr)


# ==============================================
# Rounding
# around(value:float,upto decimals)
# ==============================================
# |The around() function increments preceding digit by 1
# |if its Nextdigit>=5 else do nothing.
arr = np.around(3.54, 1)
print("Rounding with less than 5 : ", arr)
arr = np.around(3.56, 1)
print("Rounding with greater than 5 : ", arr)


# ==============================================
# Floor
# ==============================================
# |The floor() function rounds off decimal
# |to nearest lower integer.
arr = np.floor([-3.1666, 3.6667])
print("Using Floor : ", arr)


# ==============================================
# Ciel
# ==============================================
# |The ciel() function rounds off decimal
# |to nearest upper integer.
arr = np.floor([-3.1666, 3.6667])
print("Using Ciel : ", arr)

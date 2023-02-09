# NumPy provides functions to perform log at the base 2, e and 10.

# We will also explore how we can take log for any base by creating a custom ufunc.

# All of the log functions will place -inf or inf in the elements if the log can not be computed.

from math import log
import numpy as np
# ==============================================
# Log at base 2
# ==============================================
arr = np.arange(1, 10)
print("Log at base 2 : ", np.log2(arr))

# ==============================================
# Log at base 10
# ==============================================
print("Log at base 10 : ", np.log10(arr))

# ==============================================
# Log at base e
# ==============================================
print("Log at base 10 : ", np.log(arr))
# ==============================================
# Log at base e
# ==============================================
# |Numpy doesnot provide a builtin support for log of any base
# |but we can achive this by frompyfunc() method along with builtin methof math.log

nplog = np.frompyfunc(log, 2, 1)
# log of 100 with base 15
print("Log of 100 with base 15  : ", nplog(100, 15))

"""
TIME
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

names = ['5 AM to 10 AM', '10 AM to 3 PM', '3 PM to 8 PM', '8 PM to 10 PM', '10 PM to 5 AM']
values = [2,5,42,58,54]

plt.plot(names, values)
plt.title('Time')
plt.grid(True)
plt.show()
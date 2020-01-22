"""
PLATFORMS PREFERRED
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

names = ['PC', 'Console']
values = [110,56]

plt.bar(names, values)
plt.title('Platforms Preferred')
plt.grid(True, axis='y')
plt.show()
"""
PLATFORMS USED
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

names = ['PC', 'Console']
values = [128,38]

plt.bar(names, values)
plt.title('Platforms Used')
plt.grid(True, axis='y')
plt.show()
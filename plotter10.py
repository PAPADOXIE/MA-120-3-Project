"""
AESTHETICS
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

names = ['Minimalist', 'Gamery']
values = [62,102]

plt.bar(names, values)
plt.title('Aesthetic Preference')
plt.grid(True, axis='y')
plt.show()
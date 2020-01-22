"""
DURATION
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

values = []
for i in range(72):
    values.append(2)
for i in range(51):
    values.append(0.5)
for i in range(13):
    values.append(6.5)
for i in range(21):
    values.append(4)
for i in range(9):
    values.append(8)

values = np.array(values)
mean = values.mean()
minima = values.min()
maxima = values.max()
sigma = values.std()
x = np.linspace(0, mean + sigma*3, 100)

plt.plot(x,stats.norm.pdf(x,mean,sigma))

plt.xlabel('Duration')
plt.ylabel('Probability')
plt.title('Duration')
plt.axis([mean - sigma*3, mean + sigma*3, 0, 0.05])
plt.grid(True)
plt.show()
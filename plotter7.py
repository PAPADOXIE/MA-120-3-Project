"""
AGE
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

values = []
for i in range(105):
    values.append(22)
for i in range(55):
    values.append(15.5)
for i in range(2):
    values.append(50)
for i in range(4):
    values.append(28)

values = np.array(values)
mean = values.mean()
minima = values.min()
maxima = values.max()
sigma = values.std()
x = np.linspace(0, maxima, 100)

plt.plot(x,stats.norm.pdf(x,mean,sigma))

plt.xlabel('Age')
plt.ylabel('Probability')
plt.title('Age')
plt.axis([mean - sigma*3, mean + sigma*3, 0, 0.05])
plt.grid(True)
plt.show()
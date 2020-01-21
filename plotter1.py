"""
MONEY SPENT ON SETUP
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

values = []
for i in range(94):
    values.append(20000)
for i in range(31):
    values.append(60000)
for i in range(14):
    values.append(90000)
for i in range(19):
    values.append(100000)
    
values = np.array(values)
mean = values.mean()
minima = values.min()
maxima = values.max()
sigma = values.std()
x = np.linspace(0, maxima, 100)

plt.plot(x,stats.norm.pdf(x,mean,sigma))

plt.xlabel('Amount Spent')
plt.ylabel('Probability')
plt.title('Money Spent on Setup')
plt.axis([40000, 100000, 0, 0.05])
plt.grid(True)
plt.show()
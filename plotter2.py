"""
MONEY SPENT ON GAMES
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

values = []
for i in range(82):
    values.append(500)
for i in range(15):
    values.append(1000)
for i in range(22):
    values.append(5000)
for i in range(22):
    values.append(10000)
for i in range(8):
    values.append(20000)
for i in range(13):
    values.append(40000)
    
values = np.array(values)
mean = values.mean()
minima = values.min()
maxima = values.max()
sigma = values.std()
x = np.linspace(0, maxima, 100)

plt.plot(x,stats.norm.pdf(x,mean,sigma))

plt.xlabel('Amount Spent')
plt.ylabel('Probability')
plt.title('Money Spent on Games')
plt.axis([minima, maxima, 0, 0.05])
plt.grid(True)
plt.show()
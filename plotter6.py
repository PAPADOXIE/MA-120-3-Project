"""
PROVINCES
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

labels = ['Punjab','Gilgit Baltistan','Balochistan', 'KPK', 'Sindh', 'Federal Territory']
sizes = [154,1,1,6,2,2]
explode = (0.25,0.5,0,0.9,0.1,0.5)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)

ax1.axis('equal')  
plt.tight_layout()
plt.show()
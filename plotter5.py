"""
COMMONLY PLAYED GAMES
"""

import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import numpy as np
from scipy import stats

names = ['Competitive', 'Casual', 'Both']
set1 = []
set2 = []

for i in range(32):
    set1.append('Competitive')
for i in range(20):
    set2.append('Casual')
for i in range(57):
    set1.append('Both')
    set2.append('Both')

set1 = set(set1)
set2 = set(set2)

v2 = venn2([set1,set2],('',''))

v2.get_patch_by_id('10').set_color('blue')
v2.get_patch_by_id('01').set_color('purple')
v2.get_patch_by_id('11').set_color('green')

v2.get_patch_by_id('10').set_edgecolor('none')
v2.get_patch_by_id('01').set_edgecolor('none')
v2.get_patch_by_id('11').set_edgecolor('none')

v2.get_label_by_id('10').set_text('Competitive\n(19.28%)')
v2.get_label_by_id('01').set_text('Casual\n(12.05%)')
v2.get_label_by_id('11').set_text('Both\n(68.67%)')

plt.show()



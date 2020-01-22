import numpy as np
from scipy import stats

x1 = [] #Spent on setup
for i in range(94):
    x1.append(20000)
for i in range(31):
    x1.append(60000)
for i in range(14):
    x1.append(90000)
for i in range(19):
    x1.append(100000)

x2 = [] #Spent on games
for i in range(82):
    x2.append(500)
for i in range(15):
    x2.append(1000)
for i in range(22):
    x2.append(5000)
for i in range(22):
    x2.append(10000)
for i in range(8):
    x2.append(20000)
for i in range(13):
    x2.append(40000)


print(np.mean(x1))
print(np.mean(x2))

alpha = 0.01                                                     # significance level = 1%
n1, n2 = len(x1), len(x2)                                        # sample sizes
var1, var2 = np.var(x1, ddof = 1), np.var(x2, ddof = 1)          # sample variances
sp = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2)) # pooled standard deviation
print(sp)
df = n1 + n2 - 2                                                 # degrees of freedom
t = stats.t.ppf(1 - alpha/2, df)                                 # t-critical value for 99% CI
print(t)

lower = (np.mean(x1) - np.mean(x2)) - t * sp * np.sqrt(1 / len(x1) + 1 / len(x2)) 
upper = (np.mean(x1) - np.mean(x2)) + t  * sp * np.sqrt(1 / len(x1) + 1 / len(x2)) 
print(str(lower) +'  '+ str(upper))

lower = (np.mean(x2) - np.mean(x1)) - t * sp * np.sqrt(1 / len(x1) + 1 / len(x2)) 
upper = (np.mean(x2) - np.mean(x1)) + t * sp * np.sqrt(1 / len(x1) + 1 / len(x2)) 
print(str(lower) +'  '+ str(upper))

print(stats.ttest_ind(x1, x2, equal_var=False))
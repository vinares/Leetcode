import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

p = 0.5
n = 5
X = np.arange(0,n+1,1)
plist = stats.binom.pmf(X, n, p)
plt.bar(X,plist,width=0.1)

plt.title('Binom destribution p=0.5 n=5')
plt.xlabel('Random variable X')
plt.ylabel('Probability')
plt.xticks(X)
plt.show()
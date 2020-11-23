import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

X = np.arange(0, 2, 1)
p = 0.5
plist = stats.bernoulli.pmf(X,p)
plt.bar(X,plist,width=0.1)

plt.title('Benoulli distribution p=0.5')
plt.xlabel('Random varible X')
plt.ylabel('Probability')
plt.xticks(X)
plt.show()
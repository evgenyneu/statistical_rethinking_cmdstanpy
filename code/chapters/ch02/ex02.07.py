import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

w = 6
l = 3

x = np.linspace(0, 1, 100)
plt.plot(x, stats.beta.pdf(x, w + 1, l + 1))

# Quadratic approximation
plt.plot(x, stats.norm.pdf(x, 0.67, 0.16))

plt.show()

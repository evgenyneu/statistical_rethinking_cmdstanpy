import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# define grid
p_grid = np.linspace(0, 1, num=20)

# define prior
prior = np.repeat(1, 20)

# compute likelihood at each value in grid
likelihood = stats.binom.pmf(k=6, n=9, p=p_grid)

# compute product of likelihood and prior
unstd_posterior = likelihood * prior

# standardize the posterior, so it sums to 1
posterior = unstd_posterior / sum(unstd_posterior)

# Show plot
plt.plot(p_grid, posterior, '-o')
plt.xlabel("Probability of water")
plt.ylabel("Posterior probability")
plt.title("20 points")
plt.show()

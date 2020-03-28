import numpy as np

ways = np.array([0, 3, 8, 9, 0])  # Create a numpy array
plausabilities = ways / sum(ways)
print(plausabilities)

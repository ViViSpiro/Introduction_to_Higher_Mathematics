import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 10, 130)
k_1 = 1
k_2 = 2
plt.plot(x, np.cos(k_1 * x))
plt.plot(x, np.cos(k_2 * x))
plt.show()

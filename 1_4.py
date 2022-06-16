import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 10, 130)

plt.plot(x, np.cos(1 * x))
plt.plot(x, np.cos(2 * x))
plt.show()

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)
plt.axis([0, 3, 0, 3])
plt.plot(t, t, 'r--', t, t**2, t, t**3)
plt.show()
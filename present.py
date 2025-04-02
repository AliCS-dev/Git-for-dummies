import matplotlib.pyplot as plt
import numpy as np #numpy for numerical Ops.
# Creating an array of 200 evenly spaced values from 0 to 2π (one full sine wave cycle)
x = np.linspace(0, 2 * np.pi, 300)
# Calculating the sine of each x value to generate y values
y = np.sin(x)
# Creating a figure and axis for the plot
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
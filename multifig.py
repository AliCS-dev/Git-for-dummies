import matplotlib.pyplot as plt
# Creating the first figure (Figure 1)
plt.figure(1)

# Creating the first subplot in Figure 1 (2 rows, 1 column, first plot)
plt.subplot(211)



plt.plot([1, 2, 3])# Plotting a simple line graph
# Creating the second subplot in Figure 1 (2 rows, 1 column, second plot
plt.subplot(212)
plt.plot([4, 5, 6])
# Creating a second figure (Figure 2)
plt.figure(2)
plt.plot([7, 8, 9])
plt.show()
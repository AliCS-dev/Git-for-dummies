import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9])
plt.text(2, 4, 'This is a point')
plt.annotate('Annotated Point', xy=(2, 4), xytext=(3, 7), 
             arrowprops=dict(facecolor='black', shrink=0.05))# for annotation colour black and text and xy points
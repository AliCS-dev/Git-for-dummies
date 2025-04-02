import matplotlib.pyplot as plt
csfont = {'fontname':'Comic Sans MS'}
hfont = {'fontname':'Helvetica'}
plt.style.use('ggplot')
plt.plot([1, 2, 3], [1, 4, 9], linewidth=2.0, color='purple')
plt.xlabel('X-axis', fontsize=14, color='blue')
plt.ylabel('Y-axis', fontsize=14, color='blue')
plt.title('Advanced Graphs', fontname = 'Comic Sans MS')
plt.show()
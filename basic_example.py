#importing moduel pyplot from library
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')  #creating a scattered plot with red colour -> ro stands for colour of the plot
#first line represent x-axis and the second one represetnt y axis
plt.axis([0, 10, 0, 10])# x - axis range is form zero to six
#y asix is from 0 to twenty

#lables
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.title('Complex')



plt.show()
import matplotlib.pyplot as plt
import numpy as np  
import pandas as pd 

# Sample data

x = np.arange(0, 11)
y = np.arange(50, 61)
plt.plot(x, y) #Line plot
plt.title('Line Plot')
plt.show()

a = np.arange(0, 11)
b = np.arange(50, 61)
plt.scatter(a, b, c='g') #Scatter plot , c=color, g=green
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
plt.savefig('scatter_plot_test.png') #Save the plot as an image file

y=x*x
plt.plot(x,y, 'r--')
plt.plot(x,y, 'ro')
plt.plot(x,y, 'r*--')
plt.plot(x, y, 'r*', linestyle='dashed', linewidth = 4, markersize = 10)
plt.show()

# Creating subplots
plt.subplot(1, 2, 1) #1 row, 2 columns, 1st subplot
plt.plot(x, y, 'b--')
plt.title('Subplot 1')
plt.subplot(1, 2, 2) #1 row, 2 columns, 2nd subplot
plt.plot(x, y, 'g*-')
plt.title('Subplot 2')
plt.show()

# Sine curve
np.pi
p = np.arange(0, 4*np.pi, 0.1)
q = np.sin(p)
plt.subplot(1, 2, 1) #1 row, 2 columns, 1st subplot
plt.plot(p, q, 'm--')
plt.title('Sine Curve')

# Cosine curve
r = np.cos(p)
plt.subplot(1, 2, 2) #1 row, 2 columns, 2nd subplot
plt.plot(p, r, 'c--')
plt.title('Cosine Curve')
plt.show()

# Bar plot
x1 = ['A', 'B', 'C', 'D', 'E']
y1 = [10, 15, 7, 12, 20]

#x2 = ['A', 'B', 'C', 'D', 'E']
x2 = ['F', 'G', 'H', 'I', 'J']
y2 = [5, 10, 3, 1, 15]
plt.bar(x1, y1, color='orange')
plt.bar(x2, y2, color='purple')
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

#Histogram
a = np.array([11, 51, 21, 2, 5, 27, 55, 73, 22, 87, 44, 50])
plt.hist(a, bins=15) #bins=number of bars in histogram 
plt.title('Histogram')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

# Boxplot
plt.boxplot(a)
plt.title('Boxplot')
plt.ylabel('Values')
plt.show()

# Pie chart
labels = ['Python', 'C++', 'Java', 'Ruby', 'JavaScript']
sizes = [30, 25, 20, 15, 10]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'orange']
#explode = (0.1, 0, 0, 0, 0) #explode the first slice
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()
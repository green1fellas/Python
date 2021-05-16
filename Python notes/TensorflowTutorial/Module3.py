import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 2.5, 3, 4]
y = [1, 4, 7, 9, 15]

# No LBF

plt.plot(x, y, 'ro')
plt.axis([0, 6, 0, 20])
# plt.show()

# Linear Regression
#   -Finding a line to find a linear relation
#   -"Line of Best Fit" refers to the best fitted linear line

# W/ LBF
plt.plot(x, y, 'ro')
plt.axis([0, 6, 0, 20])
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
plt.show()
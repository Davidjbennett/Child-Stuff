import matplotlib.pyplot as plt
import numpy as np

file_data = np.loadtxt('2_record2308.dat')

plt.plot(file_data)
plt.ylabel("y label")
plt.xlabel("x label")
plt.show()
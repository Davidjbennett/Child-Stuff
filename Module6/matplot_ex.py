# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import numpy as np

file_data = np.loadtxt('2_Record2308.dat')

plt.plot(file_data)
plt.ylabel("y label")
plt.xlabel("x label")
plt.show()

# file_data1 = np.loadtxt('2_Record3388.dat')

# plt.plot(file_data2)
# plt.ylabel("y label")
# plt.xlabel("x label")
# plt.show()

# axis = plt.subplots()
# axis.plot([10,15,5,7,0,40])
# axis.set(title="A graph")
# plt.show()
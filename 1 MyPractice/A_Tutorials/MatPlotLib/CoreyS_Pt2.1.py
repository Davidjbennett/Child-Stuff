from matplotlib import pyplot as plt
import numpy as np

ages_x = [25,26,27,28,29,30,31,32,33,34,35]

x_indexes = np.arange(len(ages_x))
width = 0.25
#! create multiple bars over one x variable by decreasing bar size and moving bars over

py_dev_y = [45372,48876,53850,57287,63016,65998,
            70003,70000,71496,75370,83640]
plt.bar(x_indexes - width, py_dev_y, color = '#ff9933', width= width, label="Python Devs")
# plt.plot(ages_x, py_dev_y, color = '#ff1133', label="Python Devs")
#! .plot() will use line plot by default
#! .bar() will do bars

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 
        62316, 64928, 67317, 68748, 73752]
plt.bar(x_indexes, dev_y, color = '#33ffaa', width= width, label="All Devs")
# plt.plot(ages_x, dev_y, color = '#33ff00', label="All Devs")
#!last graph plotted will always be top most graph



js_dev_y = [37810,43515,46823,49293,53437,56373,
            62375,66674,68745,68746,74583]
plt.bar(x_indexes + width, js_dev_y, width= width, color = '#fa13af', label='JavaScript Devs')

plt.title("Median salary (USD) by age.")
plt.xlabel("Ages")
plt.ylabel("Median salary")

plt.xticks(ticks= x_indexes, labels= ages_x)
#! allows you to incrememnt according to indexes and labels with ages

plt.legend()
plt.grid(True, axis= 'y')

plt.show()
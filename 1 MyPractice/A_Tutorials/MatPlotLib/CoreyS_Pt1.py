from matplotlib import pyplot as plt

# print(plt.style.available) prints available styles
plt.style.use('bmh')
#!no need for color,marker,linestyle,linewidth, etc when using a style

# plt.xkcd() this make the graph look comic style

ages_x = [25,26,27,28,29,30,31,32,33,34,35]

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 
        62316, 64928, 67317, 68748, 73752]

plt.plot(ages_x, dev_y, label="All Devs")
# plt.plot(ages_x, dev_y, 'bo-.', label="All Devs")
#!can pass in legend arguments here. Have to call plt.legend below to see legend.

py_dev_y = [45372,48876,53850,57287,63016,65998,
            70003,70000,71496,75370,83640]

plt.plot(ages_x, py_dev_y, label="Python Devs")
# plt.plot(ages_x, py_dev_y, color='#ff7d9f', linestyle='--', marker = '^', linewidth=5, label="Python Devs")
#! Can implement line style, color arguements differently.
#! Can use hex values for color

js_dev_y = [37810,43515,46823,49293,53437,56373,
            62375,66674,68745,68746,74583]
plt.plot(ages_x, js_dev_y, label='JavaScript Devs')
# plt.plot(ages_x, js_dev_y, color='#6611ff', linewidth=.5, label='JavaScript Devs')
#! linewidth makes bigger lines

plt.title("Median salary (USD) by age.")
plt.xlabel("Ages")
plt.ylabel("Median salary")

# plt.legend(["All Devs", "Python"])
plt.legend()
#!Order matters when doing legend ^^ ex. JS_Devs is 3rd because it was plotted 3rd

plt.grid(True)

# plt.tight_layout() when the graph is squooshed together

plt.savefig('plot.png')

plt.show()
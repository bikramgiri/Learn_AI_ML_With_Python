# import matplotlib.pyplot as plt

#**Pie Charts:

# plt.style.use("Solarize_Light2")

# labels = ["JavaScript", "HTML/CSS", "SQL", "Python", "Java"]
# slices = [59219, 55466, 47544, 36433, 32917]
# explode = (0, 0, 0, 0.1, 0)  # only "explode" the 4th slice (i.e. 'Python')

# plt.pie(slices, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, startangle=165) # startangle=165 means the pie chart will start from the 165-degree angle
# plt.title("Most Popular Programming Languages")
# plt.tight_layout() # Adjusts the plot to ensure everything fits without overlapping

# plt.savefig('pie_chart.png') 

# plt.show()






#**Line Plots(or line charts): In short, it means showing trends over time.

import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")

# Ages 18 to 55
ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
            78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]

dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]

plt.plot(ages_x, py_dev_y, color='#444444', linewidth=2, label='Python Developer')
plt.plot(ages_x, js_dev_y, color='#f97300', linewidth=2, label='JavaScript Developer')
plt.plot(ages_x, dev_y, color='#008fd5', linewidth=2, label='Full Stack Developer')

plt.xlabel("Ages")
plt.ylabel("Median Salary in USD")
plt.title("Median Salary of Developers by Age in USD")

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig('plot.png') # Saves the plot as a PNG file

plt.show()

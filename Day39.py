# Day39: Pie chart vs bar chart, Bar chart, Histogram 

# Pie Charts:
# Pie charts are circular statistical graphics, which are divided into slices to illustrate numerical proportions. 
# Each slice represents a category's contribution to the whole.

# Bar Charts:
# Bar charts represent categorical data with rectangular bars. The length of each bar is proportional to the value it represents.
# They are useful for comparing different groups or tracking changes over time.

# Histograms:
# Histograms are a type of bar chart that represent the distribution of numerical data by dividing the data into bins or intervals.
# They are useful for understanding the underlying frequency distribution of the data.

# -------------code---------------

# **Bar Plots:

# import matplotlib.pyplot as plt

# plt.style.use('fivethirtyeight')

# departments = ["Computer Science", "Electrical", "Civil", "Mechanical", "Aerospace", "Computer Engineering", "AI/ML", "Physics"]

# no_of_students = [120, 60, 90, 80, 40, 50, 30, 60]

# plt.bar(departments, no_of_students,  edgecolor = "black", color="skyblue")

# plt.xlabel("Departments")
# plt.ylabel("Number of Students")
# plt.title("Number of Students in Each Department")

# for i, value in enumerate(no_of_students):
#     plt.text(i, value + 2, str(value), ha='center')
    
# plt.show()




# **Histograms:

import matplotlib.pyplot as plt

ages = [18, 19, 20, 21, 21, 22, 22, 23, 24, 24, 25, 26, 26, 27, 28, 29, 30, 30, 31, 32]

plt.hist(ages, bins=10, edgecolor='black', color='lightgreen')

plt.xlabel("Age Range")
plt.ylabel("Number of Students")
plt.title("Age Distribution of Students")

plt.show()

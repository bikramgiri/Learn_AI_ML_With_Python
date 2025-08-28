# Day36: Data Visualization

# 1. Data Collection
# 2. Data Cleaning
# 3. Data Visualization

# 3. Data Visualization: Visual representation of data
# It is the process of representing data graphically to identify patterns, trends, and insights.

# Commonly used libraries for data visualization in Python include:
# **a. Matplotlib: 
# One of the classic libraries for data visualization.
# 1. Most of it is based on ggplot.
# 2. It is difficult to write but easy to understand.

# In the function pie() which is used to plot pie charts, you can pass the data and labels to create a pie chart easily.
# Example:
# import matplotlib.pyplot as plt
# plt.pie(data, labels=labels)
# plt.show()

# One of the parameter is : autopct = "%1.1f%%"
# Example:
# plt.pie(data, labels=labels, autopct='%1.1f%%')
# plt.show()

# 3. Difficult to remember as different functions have different parameters and different parameter names for same work.
# Example:
# plt.pie(data, labels=labels, autopct='%1.1f%%')
# plt.show()
 #e.g:
 #1-> Function(color = [""....])
 #2-> Function(size = [""....])
 #3-> Function(style = [""....])


# **b. Seaborn: Extended version of matplotlib
# In short, it is a statistical data visualization library based on Matplotlib. 
# It provides a high-level interface for drawing attractive statistical graphics.

# 1. It is extended version of matplotlib.
# 2. It is easy to write and understand.
# 3. It makes the plots with difficult syntax in matplotlib easy.
# 4. Both matplotlib and seaborn cannot be directly used in web programs.
# 5. Both matplotlib and seaborn cannot create interactive visualization easily.


# **c. Plotly: 
# In short, it is a library for creating interactive plots and dashboards.

# 1. Makes the creation of interactive visualization easy.
# 2. Can be directly used in websites.
# 3. Plotly JS(Firstly it was introduced in JavaScript).
# 4. The library that we use in python is entirely based on Plotly JS and is simply called plotly.
# 5. Gives maximum output in minimum lines of codes.
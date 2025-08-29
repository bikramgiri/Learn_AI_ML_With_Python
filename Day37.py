# Day37: Pie Charts and Line Plots or line charts

# **Pie Charts: In short, it means making comparisons between few numbers of variables or data.
# When we have to make comparisons between few numbers of variables or data.
# Pie chart becomes useless when we have large number of samples or data.
# Pie chart is useful when the number of sample is <= 5

# **Slices and Labels
# Slices = [values...]
# Labels = ["Names..."]

# Example:
# labels = ["Python", "Java", "JavaScript", "C++"]
# slices = [3000, 2050, 2000, 2500]

# For styles: 
# print(plt.style.available) # Prints all available styles


#**Line Plots(or line charts): In short, it means showing trends over time.
# We use line plots when we have to see the relationship between two variables over a continuous interval.

# Examples: Suppose we take the survey of devs we want to know that how their salary changes with their age

# v1 and v2: When v1 is increases v2 decreases or vice versa  => -ve relation
# v1 and v2: When v1 is increases v2 increases or vice versa  => +ve relation

# plt.plot(ages_x, py_dev_y, color='#444444', linestyle='--', marker='o', linewidth=1, label='Python Developer')

# *linestyle='--'
# ValueError: '.-' is not a valid value for ls; supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'


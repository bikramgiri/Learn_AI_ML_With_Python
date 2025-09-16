# Day45: Point Plot, Pivot Table Heatmap

# *Point Plot: In short, it is used to visualize the distribution of a continuous variable. It displays individual data points along a single axis, allowing you to see the spread and clustering of values.*
# It is particularly useful for comparing distributions across different categories or groups.

# Confidence Interval(CI): It is a range of values that is likely to contain the true population parameter with a certain level of confidence. In point plots, CI is often represented as error bars around the mean or median of the data points.
# The width of the CI can be adjusted to reflect different levels of confidence (e.g., 95%, 99%).
# A narrower CI indicates more precision in the estimate, while a wider CI indicates less precision.
# CI is important because it provides a measure of uncertainty around the estimated value, helping to assess the reliability of the results.

# CI: Confidence Interval is the change in data when multiple experiments are done.
# CI is the range in which the true value lies.

# Less confidence interval = more bharpardo
# More confidence interval = less bharpardo



# Important Plots Recap from Day42:
# *Pivot Table Heatmap:(Important plot) In short, it is a graphical representation of data where individual values are represented as colors in a matrix format. 
# It is used to visualize the relationship between two categorical variables and a continuous variable.
# The intensity of the color indicates the magnitude of the continuous variable, making it easy to identify patterns, trends, and outliers in the data.*





# -------- code -------------


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.set_style("whitegrid") # plt.style.use()--> Matplotlib
sns.set_context("notebook", font_scale = 1.0) # plt.rcParams.update()--> Matplotlib

tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")
iris = sns.load_dataset("iris")

# *Point Plot

# , hue = 'smoker', dodge = True, markers = ['o', 's'], linestyles = ['-', '--'], ci = 95, capsize= 0.1 inch, dodge = 0.3 inch
# sns.pointplot(data = tips, x = 'day', y = 'total_bill', hue = 'sex', dodge = 0.3, markers = ['x', 's'], linestyles = ['-', '--'], capsize = 0.08) # ci = None means no confidence interval
# plt.title('Point Plot of Average Total Bill by Day')
# # plt.xlabel('Day')
# # plt.ylabel('Total Bill')
# plt.tight_layout()
# plt.show()



# *Pivot Table Heatmap

x = flights.pivot_table(index = 'year', columns = 'month', values = 'passengers')
sns.heatmap(x, annot = True, fmt = '.0f', cmap = 'coolwarm') # fmt = 'd' means integer values
plt.title('Heatmap of Passengers by Month and  Year')
# plt.xlabel('Month')
# plt.ylabel('Year')
plt.tight_layout()
plt.show()


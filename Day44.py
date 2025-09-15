# Day44: Violin Plot, Count Plot, Facet Grid


# **Violin Plot: In short, It means a combination of box plot and KDE plot.
# A violin plot is a method of plotting numeric data and can be understood as a combination of a box plot and a kernel density plot.
# It is used to visualize the distribution of the data and its probability density.
# The idea is to use the box plot to find the outliers in the data and then use the KDE to find the density of the data.
# The outliers are the points that are far away from the mean and the density is the number of points that are close to the mean.

# It is the combination of KDE(Kernel Density Estimation) and box plot.


# **Count plot: In short, It means a combination of bar plot and histogram.
# A count plot is a type of bar plot that shows the counts of observations in each categorical bin using bars.
# It is used to visualize the distribution of categorical data.   
# The height of each bar represents the number of observations in that category.
# It is similar to a histogram, but it is used for categorical data instead of continuous data.

# Count Plot vs Histogram:
# Count plot take categorical data (e.g: Customer A, Customer B, Customer C, day, week etc.) but histogram take numerical data (e.g: 1, 2, 3, 4, etc.)
# Count plot is used to visualize the distribution of categorical data while histogram is used to visualize the distribution of numerical data.
# Count plot shows the count of observations in each category while histogram shows the frequency of observations in each bin(bin means range of values).



# **Facet Grid: In short, It means a combination of multiple plots in a single figure.
# A FacetGrid is a multi-plot grid for plotting conditional relationships.

# ----------  code ............

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.0)

tips = sns.load_dataset("tips")


# **Violin plot
# plt.figure(figsize=(8, 5))
# sns.violinplot(x = "day", y = "total_bill", data = tips, hue = "sex", inner="box") # , inner="box", palette="Pastel1", split=True
# plt.title("Violin Plot of Total Bill by Day and Sex")
# plt.tight_layout()
# plt.show()


# **Count plot
# plt.figure(figsize=(8, 5))
# sns.countplot(data = tips, x = "day", hue = "sex")
# plt.title("Count Plot of records by Day and Sex")
# plt.tight_layout()
# plt.show()


# **Facet Grid
g = sns.FacetGrid(tips, col="sex", row="time", margin_titles=True)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
g.set_axis_labels("Total Bill", "Tip")
g.set_titles(col_template="{col_name}", row_template="{row_name}")
g.add_legend()
plt.subplots_adjust(top=0.9)
g.fig.suptitle('Facet Grid: Total Bill vs Tip by Sex and Time')
plt.show()




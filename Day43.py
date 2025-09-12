# Day43:


# *Numeric Variables and Categorical Variables

# *Numeric Variables --> Quantitative variables(E,g: age, height, weight, temperature, income) -->Descriptive statistics: Numeric works belong to this category
# *Categorical Variables --> Qualitative variables (E.g: gender, marital status, occupation, education level) --> Inferential statistics: Testing and other inferential Stuffs belong to this category

# **Numeric Variables(Quantitative variables): Variables that represent measurable quantities and can take on a wide range of numerical values. 
# Examples include age, height, weight, temperature, and income. 
# Numeric variables can be further classified into two types:
# 1. Continuous Variables: These can take any value within a given range (e.g., height, weight).
# 2. Discrete Variables: These can only take specific, distinct values (e.g., number of children, number of cars).

# **Descriptive statistics: Numeric works belong to this category
# Descriptive statistics involves summarizing and describing the main features of a dataset.
# Common descriptive statistics for numeric variables include:
# 1. Measures of Central Tendency: Mean, Median, Mode
# 2. Measures of Dispersion: Range, Variance, Standard Deviation 
# 3. Percentiles and Quartiles: Values that divide the dataset into specific proportions
# 4. Data Visualization: Histograms, Box Plots, Scatter Plots


# **Categorical Variables(Qualitative variables): Variables that represent distinct categories or groups. 
# Examples include gender, marital status, occupation, and education level. 
# Categorical variables can be further classified into two types:
# 1. Nominal Variables: These represent categories without any intrinsic ordering (e.g., gender, occupation).
# 2. Ordinal Variables: These represent categories with a meaningful order or ranking (e.g., education level, customer satisfaction ratings).
# Categorical variables can be encoded using techniques such as one-hot encoding or label encoding to make them suitable for analysis and modeling.

# *Inferential statistics: Testing and other inferential Stuffs belong to this category
# Inferential statistics involves making predictions or inferences about a population based on a sample of data.
# Common inferential statistics techniques for categorical variables include: 
# 1. Hypothesis Testing: Chi-Square Test, Fisher's Exact Test
# 2. Confidence Intervals: Estimating the range within which a population parameter lies
# 3. Regression Analysis: Logistic Regression for binary outcomes, Multinomial Logistic Regression for multi-class outcomes
# 4. Data Visualization: Bar Charts, Pie Charts
# In summary, numeric variables are associated with descriptive statistics that summarize and describe data, while categorical variables are linked to inferential statistics that allow for making predictions and drawing conclusions about populations based on sample data.


# *plt.figure(figsize=(8, 4)) = 8 inches wide and 4 inches tall

# Hue => value must be qualitative or categorical variable
# Size => value must be quantitative or numeric variable

# *Box Plot:
# Q1 = 25th percentile
# Q2 = 50th percentile = Median
# Q3 = 75th percentile
# IQR = Inter Quartile Range = Q3 - Q1

# Min value = Q1 - 1.5*IQR
# Max value = Q3 + 1.5*IQR

# swarmplot : ma overlap hudaina
# BSwarmplot : ma overlap hunxa

# ---------------  code ---------------

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.set_style("whitegrid") # plt.style.use()--> Matplotlib
sns.set_context("notebook", font_scale = 1.0) # plt.rcParams.update()--> Matplotlib

tips = sns.load_dataset("tips")

# *1. Histogram with KDE(Kernel Density Estimate) plot:

# plt.figure(figsize = (8, 5))
# sns.histplot(tips['total_bill'], kde = True, color = 'green', bins = 20) # bins = 20 means 20 bars will be there
# plt.title('Histogram + KDE from Tips -> Total Bill')
# # plt.xlabel('Total Bill')
# # plt.ylabel('Frequency')
# plt.tight_layout()
# plt.show()


# plt.figure(figsize=(8, 5))
# sns.histplot(tips['total_bill'], bins=20, color="skyblue", edgecolor="black")  # histogram
# sns.kdeplot(tips['total_bill'], color="green", linewidth=2)  # KDE overlay
# plt.title("Histogram + KDE from Tips -> Total Bill")
# plt.tight_layout()
# plt.show()



# **2. Scatter Plot with hue and size

# plt.figure(figsize = (8, 4))
# sns.scatterplot(data = tips, x = 'total_bill', y = 'tip', hue = 'day', size = 'size', sizes = (20, 240))
# plt.title('Scatter Plot from Tips : Total Bill vs Tip (hue = Day, size = Order Size)')
# # plt.xlabel('Total Bill')
# # plt.ylabel('Tip')
# plt.tight_layout()
# plt.show()


# **3. Box + swarm combined plot (important)

plt.figure(figsize = (10, 5))
sns.boxplot(data = tips, x = 'smoker', y = 'tip') # x = day or smoker , y = tip  or total_bill
sns.swarmplot(data = tips, x = 'smoker', y = 'tip', color = 'k', alpha = 0.4) # More the alpha value more opaque the color(opaque the color means less transparent more  ), less the alpha value more transparent the color
plt.title('Box + Swarm Plot from Tips : Tips vs Smoker')    
# plt.xlabel('Day')
# plt.ylabel('Total Bill')
plt.show()
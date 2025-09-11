# Day42: Plotting with Matplotlib

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.set_style("whitegrid") # plt.style.use()--> Matplotlib
sns.set_context("notebook", font_scale = 1.0) # plt.rcParams.update()--> Matplotlib

tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")
iris = sns.load_dataset("iris")

# print(tips)

# **1. Histogram + KDE(KDE: Kernel Density Estimate)

# plt.figure(figsize=(8, 4))
# sns.histplot(tips['total_bill'], kde=True, color='blue', bins=30)
# plt.title('Histogram + KDE from Tips -> Total Bill')
# # plt.xlabel('Total Bill')
# # plt.ylabel('Frequency')
# plt.show()


# **2. Scatter Plot with hue and size

# plt.figure(figsize = (8, 3))
# sns.scatterplot(data = tips, x = 'total_bill', y = 'tip', hue = 'day', size = 'size', sizes = (20, 200), alpha = 0.7)
# plt.title('Scatter Plot from Tips -> Total Bill vs Tip')
# # plt.xlabel('Total Bill')
# # plt.ylabel('Tip')
# plt.show()


# **3. Box + swarm combined plot (important)

# plt.figure(figsize = (10, 5))
# sns.boxplot(data = tips, x = 'day', y = 'total_bill', palette = 'Set2')
# sns.swarmplot(data = tips, x = 'day', y = 'total_bill', color = 'black', alpha = 0.5) # More the alpha value more opaque the color(opaque the color means less transparent more  ), less the alpha value more transparent the color
# plt.title('Box + Swarm Plot from Tips -> Total Bill vs Day')    
# # plt.xlabel('Day')
# # plt.ylabel('Total Bill')
# plt.show()


# **4. Regression per smoker status (lmplot)

# sns.lmplot(data = tips, x = 'total_bill', y = 'tip', hue = 'smoker', height = 4, aspect = 1.3) #  # , scatter_kws = {'color': 'blue', 'alpha': 0.5}, line_kws = {'color': 'red'}
# plt.title('Regression Plot from Tips -> Total Bill vs Tip')
# # plt.xlabel('Total Bill')
# # plt.ylabel('Tip')
# plt.show()


# **5. Correlation Heatmap (numeric columns) (important)

# cor = tips.select_dtypes(include = [np.number]).corr()
# sns.heatmap(cor, annot = True, cmap = 'coolwarm')
# plt.title('Correlation Heatmap from Tips')
# # plt.xlabel('Features')
# # plt.ylabel('Features')
# plt.show()


# **6. FacetGrid Scatter plot by time(Lunch/Dinner)

# g = sns.FacetGrid(tips, col = 'time', height = 4, aspect = 1)
# g.map(sns.scatterplot, 'total_bill', 'tip', alpha = 0.7)
# g.add_legend()
# plt.show()


# **7. Violin Plot (distribution by category) (important)

# plt.figure(figsize = (10, 5))
# sns.violinplot(data = tips, x = 'day', y = 'total_bill', hue = 'sex', split = True, palette = 'muted')
# plt.title('Violin Plot from Tips -> Total Bill vs Day')
# # plt.xlabel('Day')
# # plt.ylabel('Total Bill')
# plt.show()


# **8. Pair plot (multi-variable relationships)

# sns.pairplot(iris, hue = 'species', height = 2.5, diag_kind='auto') # diag_kind = 'hist' or 'kde' or 'auto'
# plt.suptitle('Pair Plot from Iris Dataset')
# # plt.xlabel('Features')
# # plt.ylabel('Features')
# plt.tight_layout()
# plt.show()


# **9. Strip Plot (all points with jitter(jitter: add some noise to the data to make it easier to see the distribution of points))

# plt.figure(figsize = (8, 5))
# sns.stripplot(data = tips, x = 'day', y = 'tip', hue = 'sex', dodge = True, jitter = True, alpha = 0.7)
# plt.title('Strip Plot from Tips -> Tip vs Day')
# # plt.xlabel('Day')
# # plt.ylabel('Tip')
# plt.show()


# **10. Count plot (frequiency of categories)

# plt.figure(figsize = (7, 4))
# sns.countplot(data = tips, x = 'day', hue = 'sex')
# plt.title('Count Plot from Tips -> Day')
# # plt.xlabel('Day')
# # plt.ylabel('Count')
# plt.tight_layout()
# plt.show()


# **11. Point plot (mean with confidence interval)

# plt.figure(figsize = (8, 5))
# sns.pointplot(data = tips, x = 'day', y = 'tip', hue = 'sex', dodge = True, markers=['o', 's'], capsize = 0.1, errwidth = 1, palette = 'Set2')
# plt.title('Point Plot from Tips -> Tip vs Day')
# # plt.xlabel('Day')
# # plt.ylabel('Tip')
# plt.show()



# **12. Joint plot (scatter + marginal histograms)

# sns.jointplot(data = tips, x = 'total_bill', y = 'tip', kind = 'reg', height = 6, marginal_kws = dict(bins=15, fill=True))
# plt.suptitle('Joint Plot from Tips -> Total Bill vs Tip', y = 1.02)
# # plt.xlabel('Total Bill')
# # plt.ylabel('Tip')
# plt.show()


# **13. Residual plot (residuals from linear regression)

# plt.figure(figsize = (7, 4))
# sns.residplot(data = tips, x = 'total_bill', y = 'tip', lowess = True)
# plt.title('Residual Plot from Tips -> Total Bill vs Tip')
# # plt.xlabel('Total Bill')
# # plt.ylabel('Residuals')
# plt.show()


# **14. Heatmap of pivoted data (time series like flights dataset)

# flights_pivot = flights.pivot(index = 'month', columns = 'year', values = 'passengers')
# plt.figure(figsize = (12, 6))
# sns.heatmap(flights_pivot, annot = True, fmt = 'd', cmap = 'YlGnBu')
# plt.title('Heatmap from Flights Dataset')
# # plt.xlabel('Year')
# # plt.ylabel('Month')
# plt.show()
# Day38: Line plot vs Scatter Plot

# *Line Plot: In short, it is used to visualize the trend of a continuous variable over time.
# We use line plots when any one of the two variables is continuous and the other is categorical.
# Example: Age(x-axis), Growth of Salary(y-axis) in an experiment.


# *Scatter Plot: In short, it is used to visualize the relationship between two continuous variables.
# When Both the variables are discrete than we use scatter plots
# To look at the correlation and classification/Clustering(KNN=K-Nearest Neighbors)



# For styles: 
# print(plt.style.available) # To see all the available styles

# plt.scatter(view_count, likes, c = ratio, cmap = "viridis", alpha = 0.7, edgecolors = "black", linewidth = 0.7)
# c = ratio # It means color by the ratio
# cmap = "viridis" # It means use the viridis colormap
# alpha = 0.7 # It means set the transparency level to 0.7, more the alpha value more opaque(more visible) the markers, less than alpha value more transparent
# edgecolors = "black" # It means set the edge color of the markers to black
# linewidth = 0.7 # It means set the linewidth of the edges to 0.7

# cmap = "summer"
# print(plt.colormaps()) # To view all colormaps
# cmap:
# ValueError: 'sumer' is not a valid value for cmap; supported values are 'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Grays', 'Grays_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'berlin', 'berlin_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'k', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'vanimo', 'vanimo_r', 'viridis', 'viridis_r', 'winter', 'winter_r'

# Ratio = Like / Dislike
# Dislike Increase Ratio Decrease
# Like Decrease Ratio Increase

# *Thing to understand while see plots:
# outliers : Points that are significantly different from others
# correlation : Measure of how closely two variables move in relation to each other
# clustering/overlapping : Grouping of similar data points

# plt.xscale("log") : It means to use a logarithmic scale for the x-axis
# plt.yscale("log") : It means to use a logarithmic scale for the y-axis
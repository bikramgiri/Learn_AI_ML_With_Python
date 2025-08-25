# Day34: Data Cleaning Day 3
# day3_sample_dirty_dataset.csv
# cleaned_day3_sample_dirty_dataset.csv

# Outliers affect mean and standard deviation, which can skew the results of data analysis.
# Therefore, it's important to handle them appropriately.

# Outliers doesnot affect median and mode, so they are more robust measures of central tendency in the presence of outliers.

# **Note: 
# I Have a DataSet (Numeric Values)
# 1. In that dataset, I have some missing values
# 2. I have to fill them
# 3. Before filling them, we check for outliers
# a. If there are outliers we firstly remove the outliers
# 4. We fill the missing values
# 5. Fill them with mean (Since there are no outliers now)

#**For numeric Values
# Examples of Outliers numeric values: [100, 200, 300, 400, 500, 1000]
# If there are outliers then there are two approaches to deal with them:
# 1. You can completely remove the outliers and fill up the NAN value by Mean.
# 2. You can keep the outliers and fill up the NAN value by Median.

# Mean => Mathematical Average
# Formula = Sum of all values / Number of values

# Median => Positional Average
# Formula = Middle value of sorted data


# **For String Values
# Examples of Outliers string values: ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
# If there are outliers then there are two approaches to deal with them:

# *Used in Machine Learning:
# 1. You can completely remove the outliers and fill up the NAN value by Mode. (Used in Machine Learning)

# *Used in Analysis
# 2. You can either keep the outliers, "unknown"  (Used in Analysis)

# Mode => Most repeated Value


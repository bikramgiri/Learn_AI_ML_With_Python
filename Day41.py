# Day41: Time Series

# Time Series: In short, it means data that is indexed by time.
# A sequence of data points collected at specific time intervals.
# It helps in analyzing trends, patterns, and seasonal variations over time.
# Time series data is often visualized using line charts to show how values change over time.
# Examples: Stock prices over time, daily temperatures, monthly sales figures, etc.


# ------------- code ---------------

import matplotlib.pyplot as plt
import pandas as pd

# Use a predefined style for the plot
plt.style.use('fivethirtyeight')

# D for daily, W for weekly, M for monthly, Y for yearly
dates = pd.date_range('2025-01-01', periods= 10, freq = 'D') # ("Starting date", "Number of Dates", "Common Difference")

# Sample data
no_of_product_sold = [100, 80, 40, 50, 60, 30, 90, 110, 40, 10] 

plt.figure(figsize=(8, 4)) # figsize=(8, 4) means width=8, height=4
plt.plot_date(dates, no_of_product_sold, 'r-', linestyle='solid') # 'r-' means red line
plt.plot_date(dates, no_of_product_sold, 'bo') # 'bo' means blue circle markers

plt.title('Daily Product Sales')
plt.xlabel('Date')
plt.ylabel('Number of Products Sold')
plt.tight_layout() # Adjusts plot to ensure everything fits without overlapping
plt.show()

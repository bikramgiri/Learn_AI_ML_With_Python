# Day53: House Price Prediction Project Using Linear Regression

# Numeric and Categorical Variables

# Numeric Variables(Quantitative Variables):
# It is a variable that has numeric values. 
# It can be discrete or continuous.
# Examples: Age, Height, Weight, Price, etc.

# Categorical Variables(Qualitative Variables):
# It is a variable that represents categories or groups.
# Examples: Gender, Location, Garage Type, etc.

# Types of Categorical Variables:
# 1. Nominal: 
# Categories without a specific order (e.g., Color, Type)
# It has no order or ranking among its categories.

# One-Hot Encoding:
# It is a technique used to convert nominal categorical variables into numerical values.
# Each category is represented as a binary vector.

# 2. Ordinal:
# Categories with a specific order (e.g., Size: Small, Medium, Large, good, better, best)
# It has a meaningful order or ranking among its categories.

# Ordinal Encoding:
# It is a technique used to convert ordinal categorical variables into numerical values.
# Each category is assigned a unique integer based on its order or rank.



# ......................... Code ............................
# House Price Prediction Project
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder

#Convert YearBuilt into Age of the House
df = pd.read_csv('House Price Prediction Dataset.csv')
# print(df.sample(10))

df["Age"] = 2025 - df["YearBuilt"]
df.drop("YearBuilt", axis=1, inplace=True)

# print(df.sample(3))

condition_encoder = OrdinalEncoder(categories=[['Poor', 'Fair', 'Good', 'Excellent']])
df[['Condition']] = condition_encoder.fit_transform(df[['Condition']])

# print(df.head(10))

#Garage
ohe = OneHotEncoder(drop = None, sparse_output=False)
garage_encoded = ohe.fit_transform(df[['Garage']])

garage_cols = ohe.get_feature_names_out(['Garage'])
garage_df = pd.DataFrame(garage_encoded, columns = garage_cols, index = df.index)
df.drop("Garage", axis=1, inplace=True)
df = pd.concat([df, garage_df], axis=1)

# print(df.sample(4))

# Location
ohe = OneHotEncoder(drop = None, sparse_output=False)
location_encoded = ohe.fit_transform(df[['Location']])

location_cols = ohe.get_feature_names_out(['Location'])
location_df = pd.DataFrame(location_encoded, columns = location_cols, index = df.index)
df.drop("Location", axis=1, inplace=True)
df = pd.concat([df, location_df], axis=1)

# print(df.sample(4))

df.drop("Id", axis=1, inplace=True)
print(df.sample(4))
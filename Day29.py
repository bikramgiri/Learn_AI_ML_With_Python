# Day29: Survey Result Public and schema

# loc: In short, it means location
# It is used to access a group of rows and columns by labels or a boolean array.
# Here, ending element include hunxa

# Example:
# df = pd.DataFrame({
#     "F_name": ["Sam", "John", "Doe"],
#     "L_name": ["Smith", "Doe", "Johnson"],
#     "Email": ["sam@example.com", "john@example.com", "doe@example.com"]
# })
# df.loc[0:2, "F_name"] # Output: Sam
# df.loc[0:2, "F_name":"L_name"] # Output: Sam Smith
# df.loc[0:2, "Email"] # Output: sam@example.com
# df.loc[0:1, "Email"] # Output: sam@example.com

# iloc: In short, it means integer location
# It is used to access a group of rows and columns by integer indices.
# Here, ending element include hudaina

# Example:
# df.iloc[0:2, 1:3] # Output: Smith Doe
# df.iloc[0:2, 1:4] # Output: Smith Doe john@example.com

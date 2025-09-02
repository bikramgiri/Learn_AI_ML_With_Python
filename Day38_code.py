import pandas as pd
import matplotlib.pyplot as plt
# Or
# from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv("Data.csv")
# print(data)

view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']
# print(view_count)
# print(likes)
# print(ratio)

# plt.scatter(view_count, likes) # (view_count = x-axis, likes = y-axis)
plt.scatter(view_count, likes, c = ratio, cmap = "Spectral_r", alpha = 0.7, edgecolors = "black", linewidth = 0.7)

cbar = plt.colorbar()
cbar.set_label("Like to Dislike Ratio")

plt.xscale("log") 
plt.yscale("log")

plt.xlabel("View Count")
plt.ylabel("Total Likes")
plt.title("Trending YouTube Videos")

plt.tight_layout
plt.show()
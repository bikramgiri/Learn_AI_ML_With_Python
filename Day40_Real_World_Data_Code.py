import pandas as pd
import matplotlib.pyplot as plt
# Or
# from matplotlib import pyplot as plt
from collections import Counter
# import collections as Counter

plt.style.use('fivethirtyeight')

data = pd.read_csv("Real_World_Data.csv")
ids = data['Responder_id']
lang_response = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_response:
    language_counter.update(response.split(';'))

most_repeated = language_counter.most_common(10)

languages = []
popularity = []

for item in most_repeated:
    languages.append(item[0])
    popularity.append(item[1])
    
languages.reverse()
popularity.reverse()
    
plt.barh(languages, popularity)

plt.title("Top 10 Most Popular Languages")
plt.xlabel("No of people who use")

plt.tight_layout()
plt.show()
from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter
import pandas as pd

plt.style.use('fivethirtyeight')

#!Ways to read a csv below:
#! #1
# with open('data.csv') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#! #2 
data = pd.read_csv('data.csv')

ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()
for response in lang_responses:
        language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
        languages.append(item[0])
        popularity.append(item[1])

languages.reverse()
popularity.reverse()

#! barh() is for a horizontal bar
plt.barh(languages, popularity, color = '#66bbff', height=.5)

plt.title("Most Popular Languages")
plt.xlabel("Number of Peoples Who Use It")

plt.tight_layout()

plt.show()
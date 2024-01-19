# -*- coding: utf-8 -*-
"""Copy of week1 DataMining

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wmnq8MY3PTcQfWC7uM76yJO8qVlKHKbH
"""

import pandas as pd
url = "https://raw.githubusercontent.com/shstreuber/Data-Mining/master/data/adult.data.simplified24.csv"
df2 = pd.read_csv(url)

fill_data2 = df2[df2['nativecountry'] == "Cuba"]

fill_data2

from google.colab import files
fill_data2.to_csv('./fill_data2.csv', sep = ',')
files.download('fill_data2.csv')
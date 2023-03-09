import numpy as np
import pandas as pd

url = 'https://raw.githubusercontent.com/akmand/datasets/main/baseball.csv'

dataframe = pd.read_csv(url)

#print(dataframe.head(5))
#print(dataframe.tail(5))
#print(dataframe.shape)
#print(dataframe.describe)

#print(dataframe.iloc[3:7])

da
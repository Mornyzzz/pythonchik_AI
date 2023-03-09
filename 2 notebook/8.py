import numpy as np
import pandas as pd

url = 'https://raw.githubusercontent.com/akmand/datasets/main/baseball.csv'

dataframe = pd.read_csv(url)
print(dataframe.head(5))

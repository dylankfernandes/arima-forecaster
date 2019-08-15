import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
import warnings
import pickle

# get the flight data
df = pd.read_csv('https://raw.githubusercontent.com/blue-yonder/pydse/master/pydse/data/international-airline-passengers.csv', sep=';')
df['Month'] = pd.to_datetime(df['Month'])
df.set_index('Month', inplace=True)

# create and fit the model
model = SARIMAX(
  df['Passengers'],
  order=(1, 0, 1),
  seasonal_order=(1, 1, 1, 2),
  enforce_invertibility=False,
  enforce_stationarity=False
)

results = model.fit()

# save the dataframe to a pickle file
filename = 'analysis/data'
file = open(filename, 'wb')
pickle.dump(df, file)
file.close()

# save the fitted model to a pickle file
filename = 'analysis/forecaster'
file = open(filename, 'wb')
pickle.dump(results, file)
file.close()
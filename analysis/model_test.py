import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
import pickle

# get the data and the forecaster
filename='analysis/forecaster'
file = open(filename, 'rb')
results = pickle.load(file)
file.close()

filename='analysis/data'
file = open(filename, 'rb')
df = pickle.load(file)
file.close()

# retrieve predictions with its confidence interval
prediction = results.get_prediction(start=pd.to_datetime('1959-01-01'), dynamic=False)
prediction_ci = prediction.conf_int()

# plot the predictions against the real data 
ax = df['Passengers'].plot()
prediction.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7)

ax.fill_between(prediction_ci.index,
                prediction_ci.iloc[:, 0],
                prediction_ci.iloc[:, 1], color='k', alpha=.2)

ax.set_xlabel('Date')
ax.set_ylabel('Temperatures')
plt.legend()

plt.show()

forecasted_mean = prediction.predicted_mean
true_mean = df['Passengers']['1959-01-01':]

# Compute the mean square error
mse = ((forecasted_mean - true_mean) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

### Write some python code which returns a line graph of the record high and record low temperatures by day of the year
### over the period 2005-2014.

## Load libraries
%matplotlib inline
import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd

## Load data
data = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fe827567d56c440d073c979fc5b1add34f500c5ea0c784ccf4f0ea38.csv')

## Subset
data = data[data['Date'] < '2015-01-01']

## Subset max temp and group by day of year
datamax = data[data['Element'] == 'TMAX']
datamax['Date'] = list(map(pd.to_datetime, datamax['Date']))
datamax['Fix'] = [item.dayofyear for item in datamax['Date']]
datamax = datamax.groupby(['Fix'])['Data_Value'].max()
datamax = datamax.reset_index()

## Subset min temp and group by day of year
datamin = data[data['Element'] == 'TMIN']
datamin['Date'] = list(map(pd.to_datetime, datamin['Date']))
datamin['Fix'] = [item.dayofyear for item in datamin['Date']]
datamin = datamin.groupby(['Fix'])['Data_Value'].min()
datamin = datamin.reset_index()

## Plot min and max
plt.plot(datamax['Fix'],datamax['Data_Value'], '-', c='red', label= 'Max Temp.')
plt.plot(datamin['Fix'],datamin['Data_Value'], '-', c='blue', label= 'Min Temp.')

## Make up graph
plt.gca().fill_between(range(len(datamax['Fix'])), datamin['Data_Value'], datamax['Data_Value'], facecolor='green', alpha=0.3 )
plt.legend()
plt.title('Min and Max Temp. Melbourne 2005 -2014')
plt.ylabel('Temp.')
plt.xlabel('Day of Year')

plt.savefig('temps.png')

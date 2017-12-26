### Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) 
### record high or record low was broken in 2015. (builds on MinMaxTempMelb.py)

## Subset data
data2015 = data[data['Date'] >= '2015-01-01']

## Transform Date column to day of year
data2015['Date'] = list(map(pd.to_datetime, data2015['Date']))
data2015['Fix'] = [item.dayofyear for item in data2015['Date']]

## Rename and subset frames
data2015 = data2015[['Data_Value', 'Fix']]
datamax = datamax.rename(columns={'Fix' : 'Fix', 'Data_Value' : 'MAX'})
datamin = datamin.rename(columns={'Fix' : 'Fix', 'Data_Value' : 'MIN'})

## Merge frames and add column with True/False, then plot
merge15 = pd.merge(data2015, datamax, how='inner', left_on='Fix', right_on='Fix')
mergeminmax = pd.merge(merge15, datamin, how='inner', left_on='Fix', right_on='Fix')

## Create function to check if exceeded
def checker(row):
    if row['Data_Value'] > row['MAX'] or row['Data_Value'] < row['MIN'] :
        check = True
    else : check = False   
    return check

## Apply function to df
mergeminmax['exceed'] = mergeminmax.apply(checker, axis=1)

## Plot all values that exceeded the MIN/MAX 2005-2014
plt.plot((mergeminmax[mergeminmax['exceed'] == True])['Fix'], (mergeminmax[mergeminmax['exceed'] == True])['Data_Value'], '.', c='red')
plt.ylim( (0, 500))
plt.title('Temps in 2015 that exceeded the 2004-2014 maxima')
plt.ylabel('Day of Year')
plt.xlabel('Temp.')

plt.savefig('overlay.png')
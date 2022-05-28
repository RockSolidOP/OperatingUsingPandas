import pandas as pd

daterange = pd.period_range('1/1/2022', freq='30d', periods=4)


date_data = pd.DataFrame(data=daterange, columns=['Date Range'])


date_diff = date_data['Date Range'].diff(periods=1)

dateFirstDayofMonth = pd.DataFrame()

dateFirstDayofMonth_toTimeStamped = pd.DataFrame()

dateFirstDayofMonth['First of Month'] = date_data['Date Range'].values.astype('datetime64[M]')

print(dateFirstDayofMonth.dtypes)

dateFirstDayofMonth_toTimeStamped['First of Month'] = dateFirstDayofMonth['First of Month'].dt.to_timestamp()

print(dateFirstDayofMonth.dtypes)

print(dateFirstDayofMonth_toTimeStamped['First of Month'])

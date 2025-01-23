
# 02.1 Create a Script _________________________
print("Hello World")

# 02.2 Import _________________________
import pandas as pd
data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print (data_frame)

# 03 Datasets _________________________

# 04 Series __________________________________________________
data = pd.Series([23,45,7,34,6,63,36,78,54,34])
print(data)

# 04.1 Date Range  __________________________________________________
data_dates = pd.date_range("2021-05-01", "2021-05-12")
print(data_dates)

# 04.2 Series Apply  __________________________________________________

my_series = pd.Series([2, 4, 6, 8, 10])
my_series_new = my_series.apply(my_series / 2)
print (my_series_new)
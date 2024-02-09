import csv
import pandas
import statistics

# Read the entire CSV file into a pandas DataFrame
df = pandas.read_csv('screentimeALT2.csv')
print("df to string")
print(df.to_string())

# Filter out the column, value_eur
daily_values = df['Daily average screentime (decimal)']
weekly_values = df['Screentime (Weekly)(Decimal)']
print("Daily average screentime (decimal) values",type(daily_values),daily_values)

#Find daily mean
mean_value_daily = round(statistics.mean(daily_values), 2)
print("Mean Value Daily average screentime (decimal):", mean_value_daily)

#Find weekly mean
mean_value_weekly = round(statistics.mean(weekly_values), 2)
print("Mean Value Screentime (Weekly)(Decimal):", mean_value_weekly)

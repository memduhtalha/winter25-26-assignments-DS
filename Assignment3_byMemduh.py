import pandas as pd

# Part 1
df = pd.read_csv('sales_data.csv')
print(df.head())
print(df.dtypes)

# Part 2
df['Units_Sold'] = df['Units_Sold'].fillna(df['Units_Sold'].mean())
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce').fillna(0)
df['Date'] = pd.to_datetime(df['Date'])

# Indexing
df.set_index('OrderID', inplace=True)
df.reset_index(inplace=True)
df.set_index('Date', inplace=True)

# Part 3
# Filtering Data
high_value_sales = df[(df['Sales'] > 500) & (df['Region'] == 'Europe')]
print(high_value_sales.head())

# Updating and Adding Columns
df.iloc[4, df.columns.get_loc('Units_Sold')] = 99
df['Profit'] = df['Sales'] * 0.20

# Sorting Data
df_sorted = df.sort_values(by=['Region', 'Sales'], ascending=[True, False])
print(df_sorted.head())

# Part 4
# Regional Performance
reg_perf = df.groupby('Region').agg({'Sales': 'sum', 'Units_Sold': 'mean'})
print(reg_perf)

# Product Deep Dive
prod_max = df.groupby('Product')['Profit'].max()
print(prod_max)

# Time Series Analysis
monthly_sales = df['Sales'].resample('M').sum()
print(monthly_sales)
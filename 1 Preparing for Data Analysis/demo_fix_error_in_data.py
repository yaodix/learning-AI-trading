import pandas as pd

data = {
  'Price': ['$100.00', '$200.50', '$300.75', '$400.00'],
  'Revenue': ['1,000', '2,500', '3,750', '5,000'],
  'Quantity': ['10', '15', '20', 'twenty-five']
}

df = pd.DataFrame(data)

print(df.head())


print(df.info())

df['Price'] = df['Price'].str.replace('$', '').astype(float)
df['Revenue'] = df['Revenue'].str.replace(',', '').astype(float)
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')

print('cleaned data:')
print(df.info())
print(df.head())

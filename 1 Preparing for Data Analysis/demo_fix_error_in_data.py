# 函数使用
# replace
# astype

import pandas as pd


def test1():
  data = {
    'Price': ['$100.00', '$200.50', '$300.75', '$400.00'],
    'Revenue': ['1,000', '2,500', '3,750', '5,000'],
    'Quantity': ['10', '15', '20', 'twenty-five']
  }

  df = pd.DataFrame(data)

  print(df.head())

  print(df.info())
  

  # df['Price'] = df['Price'].replace({'\$': ''}, regex=True).astype(float) #需要使用转义字符
  df['Price'] = df['Price'].str.replace('$', '').astype(float)
  df['Revenue'] = df['Revenue'].str.replace(',', '').astype(float)
  df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')

  print('cleaned data:')
  print(df.info())
  print(df.head())


def test2():
  data = {
      'Price': ['USD 10', 'USD 20', 'USD 30'],
      'Revenue': ['+100', '-10', '+500'],
      'Quantity': ['2', '4', '6']
  }
  df = pd.DataFrame(data)

  df['Price'] = df['Price'].replace({'USD ': ''}, regex=False).astype(float)
  df['Revenue'] = df['Revenue'].replace({r'\+': ''}, regex=True).astype(float)
  df['Quantity'] = df['Quantity'].astype(float)
  print(df.info())
  print(df.head())
  
  
if __name__ == '__main__':
  test1()
  # test2()
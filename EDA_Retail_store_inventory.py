import numpy as np
import pandas as pb
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')


df=pb.read_csv("C:\\Users\\Vaishnavi\\Downloads\\archive (2).zip")
print(df)

print("dataset information")
print(df.info())

print("database statistical summary")
print(df.describe())

print("missing value")
print(df.isnull().sum())

print("duplicated values")
print(df['Product ID'].duplicated().sum())

print("duplicated values")
print(df['Store ID'].duplicated().sum())

df=df.drop_duplicates(subset="Units Sold", keep=False)
print(df)

for col in df.select_dtypes(include=['object']):
    df[col].fillna(df[col].mode())

for col in df.select_dtypes(include=['number']):
    df[col].fillna(df[col].mean())

df["Date"]=df["Date"].astype('datetime64[ns]')
print(df.info())

df['actual_discount']=(df['Units Sold']/df['Discount'])
print(df['actual_discount'])

df['actual_pricing']=(df['Competitor Pricing']-df['Price'])
print(df['actual_pricing'])

df['order_weekday']=df['Date'].dt.day_name()
print(df['order_weekday'])

units_sales=df.groupby('Category')['Units Sold'].sum().sort_values(ascending=False)
print("units_sales",units_sales)

category_sales=df.groupby('Category')['Discount'].sum().sort_values(ascending=False)
print("category_sales",category_sales)

top_products=df.groupby('Product ID')['Units Sold'].sum().sort_values(ascending=False).head(3)
print(top_products)

numericalcol=["Store ID","Competitor Pricing","Discount",'Demand Forecast',
      'Price']

for col in numericalcol:
   plt.figure(figsize=(10,5))
   sns.histplot(df[col],kde=True)
   plt.title(f"Distribution of {col}")
   plt.show()

   categorialcol = ['Category', 'Region', 'Weather Condition', 'Seasonality']
   for col in categorialcol:
       plt.figure(figsize=(10, 5))
       value_count = df[col].value_counts()

       plt.bar(value_count.index, value_count.values, color="purple")
       plt.title(f"Distribution of {col}")
       plt.xlabel(col)
       plt.ylabel("count")
       plt.show()

       plt.figure(figsize=(10, 5))
       sns.barplot(x=units_sales.index, y=units_sales.values, palette="Blues")
       plt.title('sales by region')
       plt.xlabel("units_sales")
       plt.ylabel("Region")
       plt.xticks(rotation=45)
       plt.show()

       plt.figure(figsize=(10, 5))
       sns.barplot(x=category_sales.index, y=category_sales.values, palette="Paired")
       plt.title('sales by catergory')
       plt.xlabel("Category")
       plt.ylabel("Discount")
       plt.xticks(rotation=45)
       plt.show()

       #report analysis

       """print(df.info())
       print(df['actual_discount'])
       print(df['actual_pricing'])
       print(df['order_weekday'])
       print("units_sales", units_sales)
       print("category_sales", category_sales)
       print(top_products)"""

# ===============================
# Order Data Analysis Project
# ===============================

# 0️⃣ Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: adding theme to project
sns.set(style="whitegrid")

# 1️⃣ Load Data
df = pd.read_csv("../data/orders_500.csv")
# print("Data Loaded Successfully!")
print(df.head())

# 2️⃣ Data Overview
# print("=== Data Info ===")
# print(df.info())
# print("=== Statistical Summary ===")
# print(df.describe())
# print("=== Missing Values ===")
# print(df.isnull().sum())

# 3️⃣ Basic Analysis

# 3a. Total Sales
total_sales = round(df['amount'].sum(),2)
print("Total Sales:", total_sales)

# 3b. Average Order Amount
avg_amount = round( df['amount'].mean(),2)
print("Average Order Amount:", avg_amount)

# 3c. Sales by City
sales_by_city = (
    df.groupby('city', as_index=False)['amount']
    .sum()
    .rename(columns={'amount':'TotalByCity'})
    .sort_values(by='TotalByCity' , ascending=False)
)
print(sales_by_city.head(5))

# 3d. Orders by Customer
orders_by_customer = (
    df.groupby('customer' , as_index=False)
    .agg(
        OrderCount = ('customer', 'count'),
        TotalByCustomer = ('amount' , 'sum')
    )
    .sort_values(by='TotalByCustomer' , ascending=False)
)
print(orders_by_customer.head(5))

# 4️⃣ Advanced Analysis

# 4a. Monthly Sales Trend
# df['date'] = pd.to_datetime(df['date'])
# df['month'] = df['date'].dt.month
# monthly_sales = ...
# print(monthly_sales)

# 4b. Highest Sales Day
# daily_sales = ...
# max_day = ...
# print(max_day)

# 4c. Top 5 Customers
# top_customers = ...
# print(top_customers)

# 5️⃣ Visualization

# Example: Sales by City
# plt.figure(figsize=(8,5))
# sns.barplot(x=sales_by_city.index, y=sales_by_city.values)
# plt.title("Sales by City")
# plt.xlabel("City")
# plt.ylabel("Total Sales")
# plt.show()

# Example: Monthly Sales Trend
# plt.figure(figsize=(8,5))
# sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o')
# plt.title("Monthly Sales Trend")
# plt.xlabel("Month")
# plt.ylabel("Total Sales")
# plt.show()

# Example: Top 5 Customers
# plt.figure(figsize=(8,5))
# sns.barplot(x=top_customers.index, y=top_customers.values)
# plt.title("Top 5 Customers by Sales")
# plt.xlabel("Customer")
# plt.ylabel("Total Sales")
# plt.show()
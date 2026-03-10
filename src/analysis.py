# ===============================
# Order Data Analysis Project
# ===============================

# 0️⃣ Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

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
print(sales_by_city.head())

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
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period('M')
monthly_sales = (
    df.groupby('month', as_index=False)['amount']
    .sum()
    .rename(columns={'amount':'TotalAmount'})
    .sort_values(by='month', ascending=True)
)
print(monthly_sales)

# 4b. Highest Sales Day
daily_sales = (
    df.groupby('date', as_index=False)['amount']
    .sum()
    .rename(columns={'amount':'TotalAmount'})
)
max_day = daily_sales.sort_values(by='TotalAmount' , ascending=False)
print(max_day.head(1))

# 4c. Top 5 Customers
top_customers = (
    df.groupby('customer',as_index=False)['amount']
    .sum()
    .rename(columns={'amount':'TotalAmount'})
    .sort_values(by='TotalAmount', ascending=False)
    .head(5)
)
print(top_customers)

# 5️⃣ Visualization
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")


# Example: Sales by City
plt.figure(figsize=(8,5))
sns.barplot(data=sales_by_city, x='city', y='TotalByCity')
plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.savefig(f"../figures/SalesByCity{timestamp}.png")
sales_by_city.to_csv(f"../results/sales_by_city_{timestamp}.csv", index=False)
plt.show()

# Example: Monthly Sales Trend
plt.figure(figsize=(8,5))

monthly_sales['month'] = monthly_sales['month'].astype(str)
sns.lineplot(data=monthly_sales, x='month', y='TotalAmount')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.savefig(f"../figures/MonthlySalesTrend{timestamp}.png")
monthly_sales.to_csv(f"../results/MonthlySalesTrend{timestamp}.csv", index=False)
plt.show()

# Example: Top 5 Customers
plt.figure(figsize=(8,5))
sns.barplot(data=top_customers,  x='customer', y='TotalAmount')
plt.title("Top 5 Customers by Sales")
plt.xlabel("Customer")
plt.ylabel("Total Sales")
plt.savefig(f"../figures/Top5Customers{timestamp}.png")
top_customers.to_csv(f"../results/Top5Customers{timestamp}.csv", index=False)
plt.show()
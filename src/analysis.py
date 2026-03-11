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
def load_data(path):
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.to_period('M')
    # print("Data Loaded Successfully!")
    # print(df.head())
    return df

# 2️⃣ Data Overview
def check_data_quality(df):
    print("=== Data Info ===")
    df.info()
    print("=== Statistical Summary ===")
    print(df.describe())
    print("=== Missing Values ===")
    print(df.isnull().sum())

# 3️⃣ Basic Analysis
def basic_analysis(df):
    # 3a. Total Sales
    print("\n=== Basic Analysis ===")
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
    # print(sales_by_city.head())

    # 3d. Orders by Customer
    orders_by_customer = (
        df.groupby('customer' , as_index=False)
        .agg(
            OrderCount = ('customer', 'count'),
            TotalByCustomer = ('amount' , 'sum')
        )
        .sort_values(by='TotalByCustomer' , ascending=False)
    )
    # print(orders_by_customer.head(5))
    return {
        "sales_by_city" : sales_by_city,
        "orders_by_customer" : orders_by_customer
    }

# 4️⃣ Advanced Analysis
def advance_analysis(df):
    print("\n=== Advanced Analysis ===")

    # 4a. Monthly Sales Trend
    monthly_sales = (
        df.groupby('month', as_index=False)['amount']
        .sum()
        .rename(columns={'amount':'TotalAmount'})
        .sort_values(by='month', ascending=True)
    )
    # print(monthly_sales)
    
    # 4b. Highest Sales Day
    daily_sales = (
        df.groupby('date', as_index=False)['amount']
        .sum()
        .rename(columns={'amount':'TotalAmount'})
    )
    max_day = daily_sales.sort_values(by='TotalAmount' , ascending=False)
    # print(max_day.head(1))

    # 4c. Top 5 Customers
    top_customers = (
        df.groupby('customer',as_index=False)['amount']
        .sum()
        .rename(columns={'amount':'TotalAmount'})
        .sort_values(by='TotalAmount', ascending=False)
        .head(5)
    )
    # print(top_customers)
    return {
        "monthly_sales" : monthly_sales,
        "max_day" : max_day.head(1),
        "top_customers" : top_customers
    }


timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
FIGURES_PATH = "../figures/"
RESULTS_PATH = "../results/"

# 5️⃣ Visualization
def show_sales_by_city(sales_by_city):
    # Example: Sales by City
    plt.figure(figsize=(8,5))
    sns.barplot(data=sales_by_city, x='city', y='TotalByCity')
    plt.title("Sales by City")
    plt.xlabel("City")
    plt.ylabel("Total Sales")
    plt.savefig(f"{FIGURES_PATH}/sales_by_city_{timestamp}.png")
    plt.close()
    sales_by_city.to_csv(f"{RESULTS_PATH}/sales_by_city_{timestamp}.csv", index=False)
    plt.show()

def show_monthly_sales_trend(monthly_sales):
    # Example: Monthly Sales Trend
    plt.figure(figsize=(8,5))
    monthly_sales['month'] = monthly_sales['month'].astype(str)
    sns.lineplot(data=monthly_sales, x='month', y='TotalAmount')
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.savefig(f"{FIGURES_PATH}/monthly_sales_trend{timestamp}.png")
    plt.close()
    monthly_sales.to_csv(f"{RESULTS_PATH}/monthly_sales_trend{timestamp}.csv", index=False)
    plt.show()

def show_top_5_customers(top_customers):
    # Example: Top 5 Customers
    plt.figure(figsize=(8,5))
    sns.barplot(data=top_customers,  x='customer', y='TotalAmount')
    plt.title("Top 5 Customers by Sales")
    plt.xlabel("Customer")
    plt.ylabel("Total Sales")
    plt.savefig(f"{FIGURES_PATH}/top_5_customers{timestamp}.png")
    plt.close()
    top_customers.to_csv(f"{RESULTS_PATH}/top_5_customers{timestamp}.csv", index=False)
    plt.show()

def main():
    print("\n=== Order Data Analysis Started ===\n")
    
    df = load_data("../data/orders_500.csv")

    check_data_quality(df)

    results_basic = basic_analysis(df)

    results_advance = advance_analysis(df)

    show_sales_by_city(results_basic["sales_by_city"])

    show_monthly_sales_trend(results_advance["monthly_sales"])

    show_top_5_customers(results_advance["top_customers"])

    print("\n=== Analysis Completed Successfully ===")

if __name__ == "__main__":
    main()  

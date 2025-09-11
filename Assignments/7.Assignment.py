import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
from datetime import datetime, timedelta

# ---------------- Generate Sample Data ----------------
# Months: Jan to Jun 2025
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 6, 30)
categories = ["Electronics", "Clothing", "Groceries", "Home & Kitchen", "Beauty", "Books", "Toys"]

# Create random sales dataset
n = 2000  # number of transactions
dates = [start_date + timedelta(days=random.randint(0, (end_date-start_date).days)) for _ in range(n)]
category = np.random.choice(categories, size=n)
units = np.random.randint(1, 101, size=n)
price = np.random.uniform(5, 500, size=n).round(2)
sales = (units * price).round(2)

df = pd.DataFrame({
    "date": dates,
    "category": category,
    "units_sold": units,
    "price_per_unit": price,
    "total_sales": sales
})

# Extract month info
df["month"] = df["date"].dt.month_name()

# ---------------- Analysis ----------------
# Total revenue per month
monthly_revenue = df.groupby("month")["total_sales"].sum()

# Best-selling product category
best_category = df.groupby("category")["total_sales"].sum().idxmax()

# Peak sales month
peak_month = monthly_revenue.idxmax()

# Average sales per day
daily_sales = df.groupby(df["date"].dt.date)["total_sales"].sum()
avg_sales = np.mean(daily_sales)

# Day with highest sales
best_day = daily_sales.idxmax()
best_day_value = daily_sales.max()

# ---------------- Results ----------------
print("=== Data Summary ===")
print("Total revenue:", round(df["total_sales"].sum(), 2))
print("Best-selling category:", best_category)
print("Peak sales month:", peak_month)
print("Average daily sales:", round(avg_sales, 2))
print("Day with highest sales:", best_day, "with", round(best_day_value, 2))

# ---------------- Visualizations ----------------
# Line chart - monthly trend
monthly_revenue.plot(kind="line", marker="o", title="Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

# Bar chart - category sales
df.groupby("category")["total_sales"].sum().plot(kind="bar", title="Sales by Category")
plt.ylabel("Revenue")
plt.show()

# Pie chart - category distribution
df.groupby("category")["total_sales"].sum().plot(kind="pie", autopct='%1.1f%%', title="Sales Distribution")
plt.ylabel("")
plt.show()

# Histogram - transaction sales distribution
df["total_sales"].plot(kind="hist", bins=30, title="Transaction Sales Distribution")
plt.xlabel("Total Sales per Transaction")
plt.show()

# ---------------- User input for month ----------------
user_month = input("Enter a month to analyze (e.g., March): ").title()

if user_month in df["month"].unique():
    m_df = df[df["month"] == user_month]
    print(f"\nSales Report for {user_month}:")
    print("Total sales:", round(m_df["total_sales"].sum(), 2))
    print("Best-selling category:", m_df.groupby("category")["total_sales"].sum().idxmax())
    print("Transactions:", len(m_df))
else:
    print("Invalid month entered!")

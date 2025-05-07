
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# بارگذاری داده
df = pd.read_csv('data/1_18398218064.csv')

# تبدیل ستون تاریخ
df['Order Date'] = pd.to_datetime(df['Order Date'])

# -----------------------------
# تحلیل فروش ماهانه
df['Month'] = df['Order Date'].dt.month
df['Month Name'] = df['Order Date'].dt.month_name()

monthly_sales = df.groupby(['Month', 'Month Name'])['Total'].sum().sort_index()
monthly_sorted = monthly_sales.sort_values(ascending=False).reset_index()

# بیشترین و کمترین ماه از نظر فروش
max_month = (monthly_sorted.iloc[0]['Month Name'], monthly_sorted.iloc[0]['Total'])
min_month = (monthly_sorted.iloc[-1]['Month Name'], monthly_sorted.iloc[-1]['Total'])

# نمودار فروش ماهانه
sns.set_theme()
plt.figure(figsize=(10, 6))
sns.barplot(data=monthly_sorted, x='Month Name', y='Total', palette='Blues_d')
plt.title('Monthly Sales')
plt.xticks(rotation=45)
plt.ylabel('Total Sales')
plt.xlabel('Month')
plt.tight_layout()
plt.savefig('images/monthly_sales.png')
plt.close()

# -----------------------------
# pivot table فروش محصولات در مناطق مختلف
pivot_table = df.pivot_table(index='Product', columns='Region', values='Total', aggfunc='sum', fill_value=0)

# heatmap فروش
plt.figure(figsize=(12, 10))
sns.heatmap(pivot_table, cmap='YlGnBu', linewidths=0.5)
plt.title('Sales Heatmap by Product and Region')
plt.tight_layout()
plt.savefig('images/heatmap.png')
plt.close()

# -----------------------------
# تحلیل فروش هر دسته‌بندی
categories = df['Category'].unique()
category_sales = {}

for cat in categories:
    top_products = df[df['Category'] == cat].groupby('Product')['Total'].sum().sort_values(ascending=False)
    category_sales[cat] = top_products

# -----------------------------
# خروجی خلاصه
print(f"بیشترین فروش ماه: {max_month[0]} با مبلغ {max_month[1]:,.0f}")
print(f"کمترین فروش ماه: {min_month[0]} با مبلغ {min_month[1]:,.0f}")

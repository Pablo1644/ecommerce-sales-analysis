import pandas as pd
import matplotlib.pyplot as plt

# 1. Wczytanie danych - Data load
df = pd.read_csv("sales_data.csv")

# 2. Wstępna analiza danych - preliminary data analysis
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
print(f"Liczba duplikatów: {df.duplicated().sum()}")
df['order_date'] = pd.to_datetime(df['order_date'])
print(df['order_date'])
print(df.describe())

# 3.  Przekształcenie danych - Data transformations
df['total_sales'] = df['price'] * df['quantity']
df['year'] = df['order_date'].dt.year
# in old pandas - df['week'] = df['order_date'].dt.week
df['week'] = df['order_date'].dt.strftime('%W').astype(int)
df['day_of_week'] = df['order_date'].dt.day_name()


# 4. Analiza sprzedaży - Sales analyse
top_10_products =df.groupby('product_name')['total_sales'].sum().sort_values(
    ascending=False).head(10)
print(top_10_products)

sell_for_category = df.groupby('category')['total_sales'].sum().reset_index()
print(sell_for_category)

df['month'] = df['order_date'].dt.to_period('M')
df_monthly_sales = df.groupby('month')['total_sales'].sum().reset_index()
print(df_monthly_sales)

top_5_localizations = df.groupby("customer_location")['total_sales'].sum().sort_values(
    ascending=False).head(5).reset_index()
print(top_5_localizations)

average_sale_for_each_client = df.groupby("customer_id", as_index=False).agg(
    average_sale=("total_sales", "mean")
)
print(average_sale_for_each_client)

# 5. Wizualizacja danych - Data visualization
top_10_products = df.groupby("product_name")['total_sales'].sum().sort_values(
    ascending=False).head(10)
print(top_10_products)
top_10_products.plot(kind ="bar")
plt.xticks(rotation=0)
plt.ticklabel_format(style='plain', axis='y')
plt.title("Product sales value[PLN]")
plt.show()

sales_by_category = (df.groupby("category")["total_sales"].sum())

sales_by_category.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=0
)
plt.ylabel("") 
plt.title("Share of categories in total sales")
plt.show()

# 6. Dodatkowe analizy - Additional analyse
sale_by_day = df.groupby('day_of_week')['total_sales'].sum()
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
sale_by_day.index = pd.Categorical(sale_by_day.index, categories=day_order, ordered=True)
sale_by_day = sale_by_day.sort_index()
sale_by_day.plot(kind='pie', title='Percentage of sales by day of the week', autopct='%1.1f%%')
plt.ylabel('')
plt.show()

# corelation
correlation = df[['price', 'quantity']].corr()
print("Correlation between price and quantity:"+str(correlation.iloc[0,1]))
print("There is no significant correlation between price and quantity.")


# 7. Zapis przekształconych danych - Save transformed data
df.to_csv('processed_sales_data.csv', index=False)
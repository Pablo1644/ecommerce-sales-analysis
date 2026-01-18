# ecommerce-sales-analysis

Sales data analysis focused on trends, seasonality and customer insights. Data was prefabricated by AI to not use real data.

# How to launch it?
## How to run it?

- Make sure Python 3.9 or newer is installed.
- Install required dependencies:
  ```bash
  pip install pandas matplotlib
  ```
  - Place the sales_data.csv file in the project directory.
  - Run the script.
  

## Project Description

This project performs a sales data analysis for an e-commerce company based on one year of transactional data. The goal is to identify sales trends, best-selling products, seasonality patterns, and customer behavior to support business and marketing decisions.

The program loads data from a CSV file and performs data cleaning, which means removing missing values and duplicates. 
It also converts  date fields into a pandas datetime format to enable time-based analysis.



## Key Analysis Areas
- Top 10 best-selling products by total sales value
- Sales performance by product category
- Monthly sales trends to identify seasonality
- Top customer locations by total sales
- Average order value per customer
- Sales distribution by day of the week
- Correlation analysis between product price and quantity sold

## Visualizations

- Bar charts for top-selling products
- Pie charts for category and weekday sales distribution
- Results displayed in the terminal (used as an internal log rather than user-facing output)

## Output
- Processed dataset saved as `processed_sales_data.csv 
- Visual insights into sales performance and customer behavior

## Comments
- Comments were added primarily for learning purposes and to clearly separate each project requirement. They were written in both Polish and English.

## Technologies Used
- Python with pandas and matplotlib libraries
- pandas
- matplotlib


# Online Store Sales Analysis

This is a basic data analysis project aimed at showcasing an initial portfolio piece.
It explores and visualizes sales data from an online store using Python, pandas, matplotlib, and seaborn.

## Dataset

The dataset (`1_18398218064.csv`) includes information such as:
- Order Date
- Product
- Category
- Region
- Total Sales

## Main Analyses

1. **Monthly Sales Analysis**
   - Total sales aggregated by month.
   - Includes a bar chart of monthly performance.
   - Identifies the highest and lowest grossing months.

2. **Sales Heatmap**
   - A heatmap showing total sales by product and region.
   - Built using a pivot table for better visualization.

3. **Category-wise Top Products**
   - Lists top-selling products for each category based on total revenue.

## Outputs

All generated plots are saved in the `images/` folder:
- `monthly_sales.png`
- `heatmap.png`

## Requirements

- Python 3.x
- pandas
- matplotlib
- seaborn

Install dependencies via pip:

```bash
pip install pandas matplotlib seaborn
```

## Running the Analysis

Simply run:

```bash
python analysis.py
```

## License

This project is for demonstration and portfolio purposes only.

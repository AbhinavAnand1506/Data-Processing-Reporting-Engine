import numpy as np

def calculate_kpis(df):
    df['Revenue'] = df['Quantity'] * df['Price']

    total_revenue = float(np.sum(df['Revenue']))
    avg_revenue = float(np.mean(df['Revenue']))
    max_revenue = float(np.max(df['Revenue']))

    product_summary = df.groupby('Product')['Revenue'].sum().reset_index()

    return {
        "total_revenue": total_revenue,
        "average_revenue": avg_revenue,
        "max_revenue": max_revenue
    }, product_summary

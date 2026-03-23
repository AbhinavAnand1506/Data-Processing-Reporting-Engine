import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Handle missing values
    df.dropna(inplace=True)

    # Standardize column names
    df.columns = df.columns.str.strip().str.capitalize()

    # Convert datatypes
    df['Quantity'] = df['Quantity'].astype(int)
    df['Price'] = df['Price'].astype(float)

    return df

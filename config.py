import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(BASE_DIR, 'data', 'sales_data.csv')
OUTPUT_FILE = os.path.join(BASE_DIR, 'output', 'report.xlsx')
LOG_FILE = os.path.join(BASE_DIR, 'logs', 'app.log')

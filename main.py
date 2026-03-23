from config import DATA_FILE, OUTPUT_FILE
from utils.data_cleaner import clean_data
from utils.kpi_calculator import calculate_kpis
from utils.report_generator import generate_report

def run_pipeline():
    print("Starting Data Processing Engine...")

    # Step 1: Load & Clean Data
    df = clean_data(DATA_FILE)
    print("Data cleaned successfully")

    # Step 2: Calculate KPIs
    summary, product_summary = calculate_kpis(df)
    print("KPIs calculated")

    # Step 3: Generate Report
    generate_report(summary, product_summary, OUTPUT_FILE)
    print("Report generated successfully")

    # Output summary
    print("\nSummary:")
    for key, value in summary.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    run_pipeline()

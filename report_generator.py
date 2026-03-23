import pandas as pd

def generate_report(summary, product_summary, output_path):
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        
        # Summary Sheet
        summary_df = pd.DataFrame([summary])
        summary_df.to_excel(writer, sheet_name='Summary', index=False)

        # Product-wise Report
        product_summary.to_excel(writer, sheet_name='Product Report', index=False)

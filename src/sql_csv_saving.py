import os
import pandas as pd

def export_table_to_csv(cursor, table_name, folder_path):
    """
    Export all data from an Oracle table to a CSV file in the given folder.

    Args:
        cursor: Oracle DB cursor object.
        table_name (str): Name of the table to export.
        folder_path (str): Directory where CSV will be saved.
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  # Create the folder if it doesn't exist

    csv_filename = os.path.join(folder_path, f"{table_name}_dump.csv")
    cursor.execute(f"SELECT * FROM {table_name}")
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(cursor.fetchall(), columns=columns)
    df.to_csv(csv_filename, index=False)
    print(f"Exported {table_name} to {csv_filename} ({len(df)} rows)")


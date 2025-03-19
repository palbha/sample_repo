import os
import pandas as pd
from datetime import datetime

# Define the CSV file name
CSV_FILE = "runs.csv"

def log_run():
    """Logs the current datetime to a CSV file."""
    # Create a DataFrame with the current run datetime
    df_new = pd.DataFrame([[datetime.now().strftime("%Y-%m-%d %H:%M:%S")]], columns=["run_datetime"])

    if os.path.exists(CSV_FILE):
        # Append to existing CSV
        df_existing = pd.read_csv(CSV_FILE)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        # Create a new CSV file
        df_combined = df_new

    # Save the updated CSV file
    df_combined.to_csv(CSV_FILE, index=False)
    print(f"Logged run at {df_new.iloc[0, 0]}")

if __name__ == "__main__":
    log_run()

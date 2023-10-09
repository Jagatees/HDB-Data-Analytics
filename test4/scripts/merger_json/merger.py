import os
import pandas as pd

def meger_csv(first_file, second_file, output_file):


    if os.path.exists(first_file) and os.path.exists(second_file):
        if not os.path.exists("centralized/merger"):
            os.makedirs("centralized/merger")

        # Specify the paths to the two CSV files
        csv_file1 = first_file
        csv_file2 = second_file

        # Read the CSV files into DataFrames
        df1 = pd.read_csv(csv_file1)
        df2 = pd.read_csv(csv_file2)

        # Merge the DataFrames based on a common column (e.g., 'ID')
        merged_df = pd.concat([df1, df2], ignore_index=True)
        # Save the merged DataFrame to a new CSV file
        merged_df.to_csv(output_file, index=False)  # Change the output filename as needed

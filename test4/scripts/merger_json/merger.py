import os
import pandas as pd

def meger_csv(first_file, second_file, output_file):


    if os.path.exists(first_file) and os.path.exists(second_file):
        if not os.path.exists("centralized/merger"):
            os.makedirs("centralized/merger")

            df1 = pd.read_csv(first_file)
            df2 = pd.read_csv(second_file)

            merged_df = pd.concat([df1, df2], ignore_index=True)
            merged_df.drop_duplicates(subset='Full Address', keep='first', inplace=True)

            max_rows = 4000
            merged_df = merged_df.head(max_rows)

            merged_df.to_csv(output_file, index=False)

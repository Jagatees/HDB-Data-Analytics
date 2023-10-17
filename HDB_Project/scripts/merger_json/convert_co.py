import pandas as pd
import json

def convert_csv(file_path, output_path):
    df = pd.read_json(file_path)

    df.to_csv(output_path, index=False)

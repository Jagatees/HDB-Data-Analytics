import pandas as pd


def clean_data(csv_file_location, clean_csv_file_location):
    # Read the CSV file
    df = pd.read_csv(csv_file_location)

    # Remove columns from csv file
    df = df.drop(['Lease','Num_Bed','Num_Toilet','Type','Title'], axis=1)

    df.rename(columns={"Room_Type": "Location_Type","Location": "Full_Address"}, inplace=True)

    df["Blk_No"] = df["Full_Address"].str.split().str[1].str.strip()

    df["Address"] = df["Full_Address"].str.split().str[2:].str.join(" ")

    df = df.reindex(columns=['Location_Name','Location_Type', 'Blk_No', 'Address', 'Postal_Code', 'Full_Address', 'Price', 'Links'])

    df['Address'] = df['Address'].replace('Tamp', 'Tampines').replace('Yishun R', 'Yisun Road')

    # Write the cleaned CSV file
    df.to_csv(clean_csv_file_location, index=False)
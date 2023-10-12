import pandas as pd

def clean_co(file_path, output_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    df = df.drop(['Model','Built'], axis=1)

    # Drop rows with empty values
    df.dropna(inplace=True)

    # Optionally, reset the index of the DataFrame
    df.reset_index(drop=True, inplace=True)

    df.rename(columns={"Bed": "Num_Bed", "Toilet": "Num_Toilet", "Size": "floor_area_sqm", "Remaing": "Lease_Used", "Title": "Full Address", "Room": "Location_Type"}, inplace=True)

    def calculate_remain_lease(value):
        leftover = 99 - int(value)
        return leftover
    df['remaining_lease'] = df['Lease_Used'].apply(calculate_remain_lease)

    def add_hdb(value):
        if 'HDB' in str(value):
            return value
        #elif 'None' in str(value):
        else:
            new_value = "HDB" + " " + str(value)
            return new_value
    df['Location_Type'] = df['Location_Type'].apply(add_hdb)

    df = df[~df.apply(lambda row: row.astype(str).str.contains('HDB nan').any(), axis=1)]

    df["Blk_No"] = df["Full Address"].str.split().str[1].str.strip()

    df["Address"] = df["Full Address"].str.split().str[2:].str.join(" ")

    df = df.reindex(columns=['Location_Name','Location_Type', 'Blk_No', 'Address', 'Postal_Code', 'Full Address', 'Long', 'Lat', 'floor_area_sqm', 'remaining_lease', 'Price', 'Link', 'Lease_Used', 'Num_Bed', 'Num_Toilet'])

    df["Location_Name"] = df['Address']

    def remove_avenue(value):
        if 'Avenue' in value:
            return value.split('Avenue')[0].strip()
        elif 'Drive' in value:
            return value.split('Drive')[0].strip()
        elif 'Street' in value:
            return value.split('Street')[0].strip()
        elif 'Plains' in value:
            return value.split('Plain')[0].strip()
        elif 'Road' in value:
            return value.split('Road')[0].strip()
        else:
            return value
    df['Location_Name'] = df['Location_Name'].apply(remove_avenue)

    df["Location_Name"] = df["Location_Name"].str.split("@").str[0].str.strip()

    df = df[~df['Full Address'].str.endswith(' I')]
    df = df[~df['Full Address'].str.endswith(' 1')]
    df = df[~df['Full Address'].str.contains('23 Jalan Memb')]

    pattern = r'[@#&$%+\-/*]'

    spec_remove = df['Address'].str.contains(pattern)
    df = df[~spec_remove]

    df.to_csv(output_path, index=False)


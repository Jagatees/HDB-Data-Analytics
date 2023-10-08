import pandas as pd

def clean_co(file_path, output_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    df = df.drop(['Model','Built'], axis=1)

    df.rename(columns={"Bed": "Num_Bed", "Toilet": "Num_Toilet", "Size": "Sqft", "Remaing": "Lease_Used", "Title": "Full Address", "Room": "Room_Type"}, inplace=True)

    df["Blk_No"] = df["Full Address"].str.split().str[1].str.strip()

    df["Address"] = df["Full Address"].str.split().str[2:].str.join(" ")

    df = df.reindex(columns=['Location_Name','Room_Type', 'Blk_No', 'Address', 'Postal_Code', 'Full Address', 'Price', 'Link', 'Lease', 'Lease_Used', 'Sqft', 'Num_Bed', 'Num_Toilet'])

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

    df.to_csv(output_path, index=False)

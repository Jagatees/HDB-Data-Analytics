import pandas as pd

def clean_co(file_path, output_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    df = df.drop(['Type','Title'], axis=1)  

    df.rename(columns={"YearLeft": "Lease_Used"}, inplace=True)

    df = df.reindex(columns=['Location_Name','Room_Type', 'Blk_No', 'Address', 'Postal_Code', 'Full Address', 'Price', 'Link', 'Lease', 'Lease_Used', 'Sqft', 'Num_Bed', 'Num_Toilet'])

    def replace_r_with_road(value):
        words = value.split()
        for i in range(len(words)):
            if words[i] == 'R':
                words[i] = 'Road'
        return ' '.join(words)
    df['Full Address'] = df['Full Address'].apply(replace_r_with_road)

    def replace_l_with_link(value):
        words = value.split()
        for i in range(len(words)):
            if words[i] == 'L':
                words[i] = 'Link'
        return ' '.join(words)
    df['Full Address'] = df['Full Address'].apply(replace_l_with_link)

    def replace_pl_with_plains(value):
        words = value.split()
        for i in range(len(words)):
            if words[i] == 'Pla':
                words[i] = 'Plains'
        return ' '.join(words)
    df['Full Address'] = df['Full Address'].apply(replace_pl_with_plains)

    df["Blk_No"] = df["Full Address"].str.split().str[0].str.strip()

    df["Address"] = df["Full Address"].str.split().str[1:].str.join(" ")

    df['Address'] = df['Address'].replace('Tamp', 'Tampines').replace('Marsil', 'Marsiling').replace('Stirl', 'Stirling').replace('Yuan Ch', 'Yuan Ching').replace('Jalan Kl', 'Jalan Klinik').replace('Well', 'Wellington').replace('Tangl', 'Tanglin Road').replace('Tah Ch', 'Tah Ching Road')

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

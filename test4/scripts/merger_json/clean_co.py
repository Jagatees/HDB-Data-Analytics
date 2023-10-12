import pandas as pd

def clean_co(file_path, output_path):
    df = pd.read_csv(file_path)

    df = df.drop(['Type','Title'], axis=1)

    # Drop rows with empty values
    df.dropna(inplace=True)

    # Optionally, reset the index of the DataFrame
    df.reset_index(drop=True, inplace=True)

    # Rename column names
    df.rename(columns={"YearLeft": "Lease_Used", "Room_Type": "Location_Type", "Sqft": "floor_area_sqm"}, inplace=True)

    df = df.reindex(columns=['Location_Name','Location_Type', 'Blk_No', 'Address', 'Postal_Code', 'Full Address', 'Long', 'Lat', 'floor_area_sqm', 'remaining_lease', 'Price', 'Link', 'Lease_Used', 'Num_Bed', 'Num_Toilet'])

    def calculate_remain_lease(value):
        leftover = 99 - int(value)
        return leftover
    df['remaining_lease'] = df['Lease_Used'].apply(calculate_remain_lease)

    def calculate_sqm(value):
        value = value.replace(',', '')
        convert_sqm = float(value) / 10.7639
        return int(convert_sqm)
    df['floor_area_sqm'] = df['floor_area_sqm'].apply(calculate_sqm)

    def putinfront_hdb(value):
        if 'Exec HDB' in value:
            rename_value = 'HDB Executive'
            return rename_value
        else:
            words = value.split()
            new_value = " ".join((words[2], words[0], words[1]))
            return new_value
    df['Location_Type'] = df['Location_Type'].apply(putinfront_hdb)

    def change_bed_to_room(value):
        if 'HDB 1 Bed' in value:
            changed2_word = 'HDB 2 Room'
            return changed2_word
        elif 'HDB 2 Bed' in value:
            changed3_word = 'HDB 3 Room'
            return changed3_word
        elif 'HDB 3 Bed' in value:
            changed4_word = 'HDB 4 Room'
            return changed4_word
        elif 'HDB 4 Bed' in value:
            changed5_word = "HDB 5 Room"
            return changed5_word
        else:
            return value
    df['Location_Type'] = df['Location_Type'].apply(change_bed_to_room)

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

    df = df[~df['Full Address'].str.endswith(' I')]
    df = df[~df['Full Address'].str.endswith(' 1')]

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
    df = df[~df['Full Address'].str.contains('23 Jalan Memb')]

    pattern = r'[@#&$%+\-/*]'

    spec_remove = df['Address'].str.contains(pattern)
    df = df[~spec_remove]

    df.to_csv(output_path, index=False)



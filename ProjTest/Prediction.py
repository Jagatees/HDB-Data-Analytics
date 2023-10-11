from statistics import mean
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import math
from sklearn.metrics import r2_score
import KerwinFunction

def Prediction(Actual2023DF, PredictionDF, PredictionYear):
    flat_types_to_predict = ["HDB 2 ROOM", "HDB 3 ROOM", "HDB 4 ROOM", "HDB 5 ROOM", "HDB EXECUTIVE"]
    prediction_results = []
    
    ColName = "PredictedYear" + str(PredictionYear)

        # Loop through towns
    for town in ["ANG MO KIO", "BEDOK", "BISHAN", "BUKIT BATOK", "BUKIT MERAH", "BUKIT PANJANG", "BUKIT TIMAH"
                , "CENTRAL AREA", "CHOA CHU KANG", "CLEMENTI", "GEYLANG", "HOUGANG", "JURONG EAST", "JURONG WEST"
                , "KALLANG/WHAMPOA", "MARINE PARADE", "PASIR RIS", "PUNGGOL", "QUEENSTOWN", "SEMBAWANG", "SENGKANG"
                , "SERANGOON", "TAMPINES", "TOA PAYOH", "WOODLANDS", "YISHUN"]:
        for flat_type in flat_types_to_predict:

            # Filter data for the specified town and flat type
            filtered_data = PredictionDF[(PredictionDF['Town'] == town) & (PredictionDF['Flat_Type'] == flat_type)]

            if not filtered_data.empty:
                # Separate the features (X) and target (y)
                X = filtered_data[['Year']]
                y = filtered_data['Price']

                # Create a linear regression model
                model = LinearRegression()

                # Fit the model to the data
                model.fit(X, y)

                # Predict price
                predicted_price = model.predict([[PredictionYear]])[0]


                # Append the prediction results to the list
                prediction_results.append({"Year": PredictionYear,"Town": town,"Flat_Type": flat_type, ColName: predicted_price})
            else:
                # If data is not available, set the price to 0
                prediction_results.append({"Year": PredictionYear,"Town": town,"Flat_Type": flat_type, ColName: 0})

    # Create a DataFrame from the prediction results
    prediction_df = pd.DataFrame(prediction_results)

    print(prediction_df)

    merged_Predictiondf = Actual2023DF.merge(prediction_df[['Year', 'Town', 'Flat_Type', ColName]], on=['Town', 'Flat_Type'], how='left')

    # Loop through the PredictedPrice column and replace empty values with 0
    for index, row in merged_Predictiondf.iterrows():
        if pd.isna(row[ColName]):
            merged_Predictiondf.at[index, ColName] = 0

    return merged_Predictiondf

csv_file = 'ProjTest\\Excel Data\\HistoryResaleData.csv'

HistoryResaleDataDF = pd.read_csv(csv_file, header=None)

#Take only selected col
HistoryResaleDataDF = HistoryResaleDataDF[[0, 1, 2, 10]]
#Change col name
HistoryResaleDataDF.columns = ['Year', 'Town', 'Flat_Type' ,'Price']
#Drop first row
HistoryResaleDataDF = HistoryResaleDataDF.drop(0)

# Convert the "Price" column to numeric
HistoryResaleDataDF['Price'] = pd.to_numeric(HistoryResaleDataDF['Price'])
HistoryResaleDataDF['Year'] = pd.to_numeric(HistoryResaleDataDF['Year'])

#get all the unique values and find the average price of it.
UniqueGroupValues = HistoryResaleDataDF.groupby(['Year', 'Town', 'Flat_Type'])['Price'].mean().reset_index()
UniqueGroupValues_sorted = UniqueGroupValues.sort_values(by=['Year', 'Town'])

print('Filter Done')
#Save dataframe into new csv file
UniqueGroupValues_sorted.to_csv('ProjTest\Excel Data\Cleaned_UnPredicted_HistoryData.csv', index=False)

Actual2023DF = UniqueGroupValues_sorted[UniqueGroupValues_sorted['Year'] == 2023]

Predict2023_DF = UniqueGroupValues_sorted.copy()

NewPredictionDF = Prediction(Actual2023DF, Predict2023_DF, 2023)

NewPredictionDF.rename(columns={'Year_x': 'Year'}, inplace=True)

FinalPredictDF = Prediction(NewPredictionDF, NewPredictionDF, 2024)

FinalPredictDF["Accuracy_Percentage"] = FinalPredictDF['PredictedYear2023'] / FinalPredictDF["Price"] * 100

Accuracy = FinalPredictDF["Accuracy_Percentage"].mean()
Accuracy_percentage = math.floor(Accuracy)
print(str(Accuracy_percentage) + "%")

FinalPredictDF.to_csv('ProjTest\Excel Data\Cleaned_HistoryData.csv', index=False)

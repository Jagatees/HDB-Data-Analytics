To Integrate

1) Move all the relevant excel files over
    a) DummyUserAddress.CSV
    b) fairprice.CSV
    c) FilteredMillionDollarHse.CSV
    d) FilteredUserHse.CSV
    e) HospitalClinic.CSV
    f) Malls.CSV
    g) MillionDollarHse.CSV
    h) MRTData.CSV
    i) Parks.CSV
    j) primaryschool.CSV
    k) secondaryschool.CSV
    l) tertiaryschool.CSV
    m) universities.CSV

Copy the code from ToIntegrate.py over 
Copy the function code KerwinFunction.py over

FLOW
1) Get all the data from the CSV files
2) Convert the scraped data addresses into coordinates
3) Remove all the duplicate history data & scraped data
4) Retrieve the Longitude and latitude from each CSV and store into a list
5) Convert the stored list from string into float
6) Calculate the amenties within 1km radius of the history data & scraped data
7) Filter all the history data & scrapped data for those within 1km radius of the addresses
8) Convert the distance into meters
9) Using the point system generate a point for each addresses per amenties
10) Group the addresses and all amenties together and merge into one dataframe
11) Replace those empty values with 0 for easy calculations
12) Calculate the total point for each addresses
13) Calculate the average point for the history data
14) Compare each scraped data addresses points with the average point 
    a) if more than average store into CSV
    b) if less than average drop the data
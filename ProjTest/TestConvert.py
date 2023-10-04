import KerwinFunction

UserHseFilePath = 'ProjTest\\Excel Data\\DummyUserAddress.csv'

print("Start")

UserHseDT = KerwinFunction.GetUserDatafromcsv(UserHseFilePath)
UserHseDF = UserHseDT.drop_duplicates()

UserAreaName = UserHseDF['Location_Name'].tolist()
UserLong = UserHseDF['Long'].tolist()
UserLat = UserHseDF['Lat'].tolist()
UserLink = UserHseDF['Link'].tolist()

print(UserAreaName)
print(UserLong)
print(UserLat)
print(UserLink)

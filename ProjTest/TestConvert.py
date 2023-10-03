import KerwinFunction

UserHseFilePath = 'ProjTest\\Excel Data\\DummyUserAddress.csv'

print("Start")
#Read the CSV File
UserAddressArray = KerwinFunction.ReadCSVFile(UserHseFilePath)

print("Converting")
#Convert User Address into coordinates
KerwinFunction.GetLongLatFromAddress(UserAddressArray, UserHseFilePath)
print("done")
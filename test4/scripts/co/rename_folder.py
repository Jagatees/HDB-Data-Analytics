import glob
import os

list_in_dir = []

# rename all HTML page to simple name index.html
def renameFiles(data_dir_path):
    for count, filename in enumerate(os.listdir(data_dir_path)):
        src = os.path.join(data_dir_path, filename)
        dst = os.path.join(data_dir_path, f'{str(count)}.html')
        os.rename(src, dst)


# Return list of item in folder
def get_item_in_dic(location):
    txtfiles = []
    arr = os.listdir(location)
    for file in arr:
        print(file)
        txtfiles.append(file)
    return txtfiles




# get all name inside the directory of the folder and store into array

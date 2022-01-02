import os
import datetime
import shutil

path = input("Give A Path:- ")
days = int(
    input("No.of Day's Limit - "))

exist = os.path.exists(path)

if(exist == False):
    print("Please Provide Valid Path")
    path = input("Give A Path To Clear The Files And Folders:- ")

if(os.path.isfile(path)):
    print("Please Provide Path Of A Directory")
    path = input("Give A Path To a Folders:- ")


for root, dirs, files in os.walk(path, topdown=False):
    for file in files:
        full_path = os.path.join(root, file)
        presentTime = datetime.datetime.now()
        file_cre_time = datetime.datetime.fromtimestamp(
            os.path.getctime(full_path))
        no_of_days = (presentTime - file_cre_time).days
        if(no_of_days >= days):
            os.remove(full_path)
            print("Congratulations!! Your PC Is Now Clean Without Any Unwanted Files")
    for i in dirs:
        fol_path = os.path.join(root, i)
        if len(os.listdir(fol_path)) == 0:
            shutil.rmtree(fol_path)
            print("Congratulations!! Your PC Is Now Clean Without Any Unwanted Folders")

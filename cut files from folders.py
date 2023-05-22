import shutil
import os

print("\nThis application moves files from source folder and his subfolders to destination folder. \n")
#I know there is many other windows build-in ways to do it but i wanted to make it using python :D"
while(True):
    foldersrc = input("Source folder (path): ")
    if os.path.exists(foldersrc) == False:
        print("Source folder does not exist.\n")
        continue
    folderdst = input("Destination folder (path): ")
    if os.path.exists(folderdst) == False:
        newFolder = input("""Destination folder does not exist.
Do you want to create it? (yes/no): \n""").upper()
        if newFolder == "YES":
            os.makedirs(folderdst)
        elif newFolder == "NO":
            continue
        else:
            print("whaaat? o_O")
            continue
    os.chdir(foldersrc)
    files = os.listdir(foldersrc)
    if os.path.exists(foldersrc) and os.path.exists(folderdst) == True:
        try:
            for f in files :
                    if os.path.isfile(f):
                        shutil.move(f , folderdst)
                        print(f"""Transfering file: {f}
from {os.getcwd()} to {folderdst}. \n""")
                    
                    elif os.path.isdir(f):
                        os.chdir(f)
                        sub = os.listdir()
                        for f in sub:
                            shutil.move(f , folderdst)
                            print(f"""Transfering file: {f}
from {os.getcwd()} to {folderdst}. \n""")
                        os.chdir(foldersrc)
                        continue
                    
        except:
            shutil.Error
            print(f"Error: {f} already exists.")


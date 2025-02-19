import os
import shutil


file_type = {
    ".txt": "Text Files",
    ".csv": "CSV Files",
    ".bin": "Binary Files",
    ".jpeg": "Image Files",
    ".jpg": "Image Files"
}


path = "/Users/alfiea/Desktop/Alfie Coding/Projects/Python/Other/Folder Organizer/Generated Files" 
destination = "/Users/alfiea/Desktop/Alfie Coding/Projects/Python/Other/Folder Organizer/Organized Files" 

# list all files in the "Generated Files" directory
file_list = os.listdir(path)


for i in file_list:
    for key in file_type.keys():
        # if the filetype end with a known filetype, then put it in its according directory 
        if i.endswith(key):
            shutil.move(f"{path}/{i}", f"{destination}/{file_type[key]}")


left_over_file = os.listdir(path) # all left over files
            
# move all left over files into "Other" directory        
for i in left_over_file:
    shutil.move(f"{path}/{i}", f"{destination}/Other")


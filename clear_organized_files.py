import os


extensions = ["Text Files/", "CSV Files/", "Binary Files/", "Image Files/", "Other/"]

path = "/Users/alfiea/Desktop/Alfie Coding/Projects/Python/Other/Folder Organizer/Organized Files/"

for i in extensions:
    src = os.path.join(path, i)
    file = os.listdir(src)
    for j in file:
        os.remove(src + j)
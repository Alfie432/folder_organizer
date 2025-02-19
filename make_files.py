import os
from PIL import Image

# Create a folder for the files
folder = "Generated Files"
os.makedirs(folder, exist_ok=True)

def create_txt_files():
    for i in range(1, 6):
        with open(os.path.join(folder, f"file_{i}.txt"), "w") as f:
            f.write(f"This is text file {i}\n")

def create_csv_files():
    for i in range(1, 6):
        with open(os.path.join(folder, f"file_{i}.csv"), "w") as f:
            f.write("Name, Age, City\n")
            f.write(f"User{i}, {20 + i}, City{i}\n")

def create_bin_files():
    for i in range(1, 6):
        with open(os.path.join(folder, f"file_{i}.bin"), "wb") as f:
            f.write(os.urandom(10))  # Writes 10 random bytes

def create_jpeg_jpg__file():
    for i in range(1, 6):
        image = Image.new(mode = "RGB", size = (200, 200), color = (153, 153, 255))
        image.save(os.path.join(folder, f"file_{i}.jpg"))
        image.save(os.path.join(folder, f"file_{i}.jpeg"))
        image.save(os.path.join(folder, f"file_{i}.png"))


if __name__ == "__main__":
    create_txt_files()
    create_csv_files()
    create_bin_files()
    create_jpeg_jpg__file()
    
# Remove .exe files from downloads folder to free up space
import os

for file in os.scandir(r"C:\Users\Sean\Downloads"):
    if file.name.endswith(".exe"):
        os.unlink(file.path)

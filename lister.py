# List contents of desktop
import os

spath = r"C:\Users\Sean\Desktop"

# Print contents of spath
print(os.listdir(spath))

# Walk path and determine folders, files, root

for roots, dirs, files in os.walk(spath):
    for dir in dirs:
        print("Dir = %s" % dir)
    for file in files:
        print("File = %s" % file)

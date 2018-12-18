from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
# show an "Open" dialog box and return the path to the selected file
filename = askopenfilename()
print(filename)
with open(filename, "r+", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)
    swap = True
    while swap:
        swap = False
        for i in range(len(lines)-1):
            if lines[i].replace("\t", "").startswith("\\acro") and lines[i+1].replace("\t", "").startswith("\\acro") and lines[i].lower() > lines[i+1].lower():
                lines[i], lines[i+1] = lines[i+1], lines[i]
                swap = True
        print(lines)
    f.seek(0)

    f.writelines(lines)

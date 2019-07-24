
import os

fPath = 'C:\\AS\\'

dirs = os.listdir(fPath)

for file in dirs:
    abPath = os.path.join(fPath, file)
    mTime = os.path.getmtime(abPath)
    if file.endswith(".txt"):
        print(mTime, abPath)

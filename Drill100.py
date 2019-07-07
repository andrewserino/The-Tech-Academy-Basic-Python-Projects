

import os

fPath = 'C:\\AS\\'

dirs = os.listdir(fPath)

for file in dirs:
    abPath = os.path.join(fPath, file)
    print (abPath)

    mTime = os.path.getmtime(abPath)
    print (mTime)

txt = ".jpg"

x = txt.endswith(".jpg")

print(x)


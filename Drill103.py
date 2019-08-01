
import sqlite3

conn = sqlite3.connect('drill103.db')

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_filenames ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_datatype TEXT \
        )")
    conn.commit()

with conn:
    cur = conn.cursor()
    for file in fileList:
        if file.endswith('.txt'):
            print(file)

            cur.execute('INSERT INTO tbl_filenames(col_datatype) VALUES(?)',(file,))
            
    conn.commit()
conn.close()





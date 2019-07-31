
import sqlite3

conn = sqlite3.connect('drill103.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_filenames ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_datatype TEXT \
        )")
    conn.commit()

with conn:
    cur.execute("INSERT INTO tbl_filenames(col_datatype) VALUES (?)", \
                ('information.docx',))
    cur.execute("INSERT INTO tbl_filenames(col_datatype) VALUES (?)", \
                ('Hello.txt',))
    cur.execute("INSERT INTO tbl_filenames(col_datatype) VALUES (?)", \
                ('myImage.png',))
    cur.execute("INSERT INTO tbl_filenames(col_datatype) VALUES (?)", \
                ('myMovie.mpg',))
    cur.execute("INSERT INTO tbl_filenames(col_datatype) VALUES (?)", \
                ('World.txt',))
    cur.execute("INSERT INTO tbl_filenames(col_datatype) VALUES (?)", \
                ('data.pdf',))
    cur.execute("INSERT INTO tbl_filenames(col_datatype) VALUES (?)", \
                ('myPhoto.jpg',))
    conn.commit()
conn.close()


fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

result = fileList.endswith('.txt')
for result in fileList:
    if result == ".txt":
        break
    print(result)


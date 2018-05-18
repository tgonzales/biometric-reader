import sqlite3

def createDatabase():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    rows = [
	('1001','512245'),
	('1002','512246'),
        ('1003','512247')
    ]
    try:
        c.execute('''CREATE TABLE users (pId, bir)''')
        c.executemany('INSERT INTO users VALUES (?,?)', rows)
        conn.commit()
    except:
        pass
    conn.close()

def removeDatabase():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''DROP TABLE users''')
    conn.commit()
    conn.close()

def fetch():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    tmp_list = c.fetchall()

    while True:
        for template in tmp_list:
            print(template[1])
        break

if __name__ == '__main__':
    try:
        removeDatabase()
    except:
        pass
    createDatabase()
    fetch()

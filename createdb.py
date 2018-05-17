import sqlite3

def createDatabase():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE users (pId, bir)''')
        c.execute("INSERT INTO users VALUES ('1001','512245')")
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

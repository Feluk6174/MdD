import sqlite3


while True:
    conn = sqlite3.connect("usuaris.db")

    c = conn.cursor()
    sql = input("   >> ")
    if sql == "e" or sql == "exit":
        break
    temp = c.execute(sql)

    res = temp.fetchall()

    print(res)

    conn.commit

conn.close()
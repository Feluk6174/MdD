import sqlite3

path = ""

conn = sqlite3.connect(path+"usuaris.db")


c = conn.cursor()

def create_usuaris():
    conn = sqlite3.connect(path+"usuaris.db")

    c = conn.cursor()

    c.execute("""CREATE TABLE usuaris (
    id integer,
    usuari text,
    cantitat integer
    )
    

    """)

    conn.commit()
    conn.close()

def create_ofertes():
    conn = sqlite3.connect(path+"usuaris.db")

    c = conn.cursor()

    c.execute("""CREATE TABLE ofertes (
    id text,
    titol text,
    descripcio text,
    seller_id integer,
    seller_usuari text,
    preu integer
    )
    

    """)

    conn.commit()
    conn.close()

def add_user(id, name, cantitat=25):
    conn = sqlite3.connect(path+"usuaris.db")

    c = conn.cursor()
    params = (id, name, cantitat)
    c.execute("INSERT INTO usuaris VALUES (?, ?, ?)", params)
    conn.commit(), 
    conn.close()

def search_user(id):
    conn = sqlite3.connect(path+"usuaris.db")

    c = conn.cursor()
    c.execute("SELECT * FROM usuaris WHERE id == ")
    conn.commit()
    conn.close()

def check_balance(id):
    conn = sqlite3.connect(path+"usuaris.db")

    c = conn.cursor()
    params = (id)
    sql = "SELECT * FROM usuaris WHERE id == " + str(id)
    temp = c.execute(sql)
    res = temp.fetchall()
    conn.commit()
    conn.close()
    return res

def add_oferta(id, titol, descripcio, seller_id, seller_usuari, preu):
    conn = sqlite3.connect(path+"usuaris.db")

    c = conn.cursor()
    params = (id, titol, descripcio, seller_id, seller_usuari, preu)
    c.execute("INSERT INTO ofertes VALUES (?, ?, ?, ?, ?, ?)", params)
    conn.commit(), 
    conn.close()

def check_ofertes():
    conn = sqlite3.connect(path+"usuaris.db")

    c = conn.cursor()
    params = (id)
    sql = "SELECT * FROM ofertes"
    temp = c.execute(sql)
    res = temp.fetchall()
    conn.commit()
    conn.close()
    return res

def search_oferta(id):
    conn = sqlite3.connect(path+"usuaris.db")

    c = conn.cursor()
    sql = "SELECT * FROM ofertes WHERE id == '"+str(id)+"'"
    temp = c.execute(sql)
    res = temp.fetchall()
    conn.commit()
    conn.close()
    return res

def modificar_cartera(id, cantitat):
    conn = sqlite3.connect(path+"usuaris.db")

    c = conn.cursor()

    original = check_balance(id)

    sql = f"UPDATE usuaris SET cantitat = {original[0][2]+cantitat} WHERE id == {original[0][0]}"
    temp = c.execute(sql)
    res = temp.fetchall()

    conn.commit()
    conn.close()
    return res


#create_usuaris()
#create_ofertes()

conn.commit()

conn.close()
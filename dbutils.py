import sqlite3

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        return e
    return None

def insert_stock(conn, stock):
    sql = ''' INSERT INTO stocks (date,trans,symbol,qty,price)
                  VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, stock)
    conn.commit
    
    return cur.lastrowid

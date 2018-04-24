import sqlite3

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None


def main():
    database = "C:\\Users\\paul.smith\\Documents\\Python Projects\\db\\notification.db"
 
    conn = create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM stocks")
        conn.commit
 
 
if __name__ == '__main__':
    main()

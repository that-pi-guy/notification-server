import dbutils

def main():
    database = "C:\\Users\\paul.smith\\Documents\\Python Projects\\db\\notification.db"
 
    conn = dbutils.create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM stocks")
        rows = cur.fetchall()
 
        for row in rows:
            print(row)
 
 
if __name__ == '__main__':
    main()



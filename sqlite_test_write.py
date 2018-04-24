import dbutils

def main():
    database = "C:\\Users\\paul.smith\\Documents\\Python Projects\\db\\notifications.db"
    conn = dbutils.create_connection(database)
    with conn:
        purchases = ('2018-04-24', 'BUY', 'Apple', 1111, 66.66)
                    # ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
                    # ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
                    # ('2006-01-05','BUY','RHAT',100,35.14),
                    #]
        dbutils.insert_stock(conn, purchases)
 
if __name__ == '__main__':
    main()


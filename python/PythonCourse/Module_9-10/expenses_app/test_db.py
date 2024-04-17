import sqlite3
import datetime

with sqlite3.connect('database.db') as db: # db, db3, sqlite, sqlite3
    cursor = db.cursor() # бегать и вносить изменения
    # query = """ CREATE TABLE IF NOT EXISTS expenses(id INTEGER, name TEXT) """
    query1 = """ INSERT INTO expenses (id, name) VALUES(1, 'Коммуналка') """
    query2 = """ INSERT INTO expenses (id, name) VALUES(2, 'Бензин') """
    query3 = """ INSERT INTO expenses (id, name) VALUES(3, 'Интернет') """
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    db.commit()
    
def get_timestamp(y,m,d):
    return datetime.datetime.timestamp(datetime.datetime(y,m,d))

def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()

# insert_payments = [
#     (1, 120, get_timestamp(2020, 9, 1), 1),
#     (2, 12, get_timestamp(2020, 9, 1), 3),
#     (3, 20, get_timestamp(2020, 9, 1), 2),
#     (4, 20, get_timestamp(2020, 9, 2), 2),
#     (5, 20, get_timestamp(2020, 9, 3), 2),
#     (6, 20, get_timestamp(2020, 9, 4), 2),
#     (7, 20, get_timestamp(2020, 9, 5), 2)
# ]


with sqlite3.connect('database.db') as db: # db, db3, sqlite, sqlite3
    cursor = db.cursor() # бегать и вносить изменения
    # query = """ CREATE TABLE IF NOT EXISTS payments(
    #     id INTEGER, 
    #     amount REAL,
    #     payment_date INTEGER,
    #     expense_id INTEGER
    
    # ) """
    # query = """ INSERT INTO payments(id, amount, payment_date, expense_id)
    #                         VALUES(?,?,?,?); """
    # cursor.executemany(query, insert_payments)
    # db.commit()
    # print(cursor.rowcount, "Строк добавлено")
    
    # query = """ SELECT * FROM payments """
    query = """ SELECT amount, payment_date, name FROM payments 
                        JOIN expenses ON expenses.id = payments.expense_id
                        WHERE expense_id = 2 """
    
    cursor.execute(query)
    sum = 0
    for res in cursor:
        sum += res[0]
        print(res[0], get_date(res[1]))
    print('TOTAL ', sum)
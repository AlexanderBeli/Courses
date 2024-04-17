import datetime
import sqlite3


def get_statistic_data():
    all_data = []
    with sqlite3.connect('database.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        query = """ SELECT * FROM payments JOIN expenses
                    ON expenses.id = payments.expense_id """
        cursor.execute(query)
        all_data = cursor
    return all_data

def get_date(tmstp):
    return datetime.datetime.fromtimestamp(tmstp).date()

def get_most_exp_month():
    data = get_statistic_data()
    month_list = ("0", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", 
                  "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")
    days = {}
    for payment in data:
        # print(get_date(payment['payment_date']).month, payment['amount'])
        if get_date(payment['payment_date']).month in days:
            days[get_date(payment['payment_date']).month] += payment['amount']
        else:
            days[get_date(payment['payment_date']).month] = payment['amount']
    print(days)
    return month_list[max(days,key=days.get)]

if __name__ == '__main__':
    get_most_exp_month()
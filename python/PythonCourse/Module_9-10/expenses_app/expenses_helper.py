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


def get_most_common_item():
    data = get_statistic_data()
    quantity = {}
    for payments in data:
        if payments['expense_id'] in quantity:
            quantity[payments['expense_id']]['qty'] += 1
        else: 
            quantity[payments['expense_id']] = {'qty':1, 'name':payments['name']}
    return max(quantity.values(), key=lambda x: x['qty'])['name']


def get_most_exp_item():
    data = get_statistic_data()
    return max(list(data), key=lambda x:x['amount'])['name']

def get_timestamp(y,m,d):
    return int(datetime.datetime.timestamp(datetime.datetime(y,m,d)))

def get_date(tmstp):
    return datetime.datetime.fromtimestamp(tmstp).date()

def get_most_exp_day():
    data = get_statistic_data()
    week_days = ("Понедельник", "Вторник", "Среда", 
                 "Четверг", "Пятница", "Суббота", "Воскресенье")
    days = {}
    for payment in data:
        if get_date(payment['payment_date']).weekday() in days:
            days[get_date(payment['payment_date']).weekday()] += payment['amount']
        else:
            days[get_date(payment['payment_date']).weekday()] += payment['amount']
    return week_days[max(days,key=days.get)]

def get_most_exp_month():
    data = get_statistic_data()
    month_list = ("0", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", 
                  "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")
    days = {}
    for payment in data:
        if get_date(payment['payment_date']).month in days:
            days[get_date(payment['payment_date']).month] += payment['amount']
        else:
            days[get_date(payment['payment_date']).month] += payment['amount']
    # print(days)
    return month_list[max(days,key=days.get)]

def get_table_data():
    data = get_statistic_data()
    return [(i['id'], i['name'], i['amount'], '{:%d-%m-%Y}'.format(get_date(i['payment_date']))) for i in data]
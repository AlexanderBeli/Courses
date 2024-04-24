import datetime
import sqlite3


def get_statistic_data():
    all_data = []
    with sqlite3.connect('database.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        query = """ SELECT * FROM payments JOIN expenses
                    ON expenses.id = payments.expense_id; """
        cursor.execute(query)
        all_data = cursor
    return all_data

def get_date(tmstp):
    return datetime.datetime.fromtimestamp(tmstp).date()

# def get_most_exp_month():
#     data = get_statistic_data()
#     month_list = ("0", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", 
#                   "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")
#     days = {}
#     for payment in data:
#         # print(get_date(payment['payment_date']).month, payment['amount'])
#         if get_date(payment['payment_date']).month in days:
#             days[get_date(payment['payment_date']).month] += payment['amount']
#         else:
#             days[get_date(payment['payment_date']).month] = payment['amount']
#     print(days)
#     return month_list[max(days,key=days.get)]

# def get_lang_schema(lang):
#     result = {}
#     with sqlite3.connect('database.db') as db:
#         # db.row_factory = sqlite3.Row
#         cursor = db.cursor()
#         query = """ SELECT ls_name, ls_{} FROM lang_schema; """.format(lang)
#         cursor.execute(query)
#         result = dict(cursor)
#     return result

def get_most_exp_day(lang):
    data = get_statistic_data()
    week_days = {'ru':("Понедельник", "Вторник", "Среда", 
                 "Четверг", "Пятница", "Суббота", "Воскресенье"),
                 'en':("Monday", "Tuesday", "Wednesday", 
                 "Thursday", "Friday", "Saturday", "Sunday")
                }
    days = {}
    for payment in data:
        if get_date(payment['payment_date']).weekday() in days:
            days[get_date(payment['payment_date']).weekday()] += payment['amount']
        else:
            days[get_date(payment['payment_date']).weekday()] = payment['amount']
    return week_days[lang][max(days,key=days.get)]

if __name__ == '__main__':
    # get_most_exp_month()
    lang = 'ru'
    # f = get_lang_schema(lang)
    f = get_most_exp_day(lang)
    print(f)
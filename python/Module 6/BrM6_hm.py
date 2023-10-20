'''
Напишите функцию get_thread(thread_name), которая принимает один аргумент - название потока.
Функция должна ждать одну секунду, затем выводить в стандартный вывод (print) название потока.
def get_thread(thread_name):
  pass
Ожидание в 1 секунду реализуйте с помощью библиотеки time.
Запустите 5 потоков с с данной функцией и разными именами в качестве аргументов.
'''
import time
from threading import Thread
from datetime import datetime

def get_thread(thread_name):
  time.sleep(1)
  print(f"The name of the thread is {thread_name}.")

threads = [Thread(target = get_thread, args = (thread_name + 1, )) for thread_name in range(5)]
t1 = datetime.now()
for t in threads:
	t.start()
for t in threads:
	t.join()
print('time1 ', (datetime.now() - t1).microseconds)

#Сравните время работы параллельного и последовательного запуска с помощью библиотеки time.

t2 = datetime.now()
for i in range(5):
	get_thread(i + 1)
print('time2 ', (datetime.now() - t2).microseconds)

print("Hello world!")
a = float(155555)
print(a)
b = int(2.3)
print(b)
c = round(4.8)
print(c)
d = bool(3 < 2)
print(d)
e = type(a)
f = type(b)
g = type(c)
h = type(d)
print(e)
print(f)
print(g)
print(h)
i = None
j = type(i)
print(j)
a = 100
a += 1
print(a)
# вводи в градусах цельсия, рассчитываем и выводим в форингейтах
degree = float(
    input("Введите сюда цифру по цельсию, а мы выведем вам ее по фаренгейту ")
)  # для дробных чисел
# degree2 = int(degree) #если целые числа
fareng = (degree * 9 / 5) + 32
print(fareng)
# пользователи вводят два числа, нужно найти большее из них
print("Сравним два числа")
user1 = int(input("Введите первое число здесь "))
user2 = int(input("Введите второе число здесь "))
a = (user1 > user2) * user1 + (user2 >= user1) * user2
print("Наибольшее число: ", a)
# if (user1<user2)
# {print(user1, ' больше')}
# if (user2>user1)
# print(user2, ' больше')

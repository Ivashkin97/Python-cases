#1

"""
lst = [-2, -4, -6, 4, 5, 4, 0]
print(sorted(lst)) #сортировка списка
print(min(lst)) #минимальный элемент списка
print(max(lst)) #максимальный элемент списка
print(len(lst)) #длина списка
print(lst[0]) #самый первый элемент списка
print(lst[6])
last = len(lst) - 1 #номер последнего элемента
print(lst[last]) #последний элемент
lst.append(100) #добавление элемента в конец списка
lst.insert(3, 1000) #добавление элемента на 3-ю позицию
lst.pop() #удаление последнего элемента
lst.pop(2) #удаление элемента с индексом 2
del lst[2] #удаление элемента с индексом 2
print(lst.count(4)) #подсчет кол-ва элементов
a = ["A"]*100 #создание списка с повторяющимися элементами
"""

#2

"""
for i in range(1,16):
    print(i)

for i in range(1,16,2):
    print(i)

for i in range(16,1,-1):
    print(i)

for i in range(15,0,-1):
    print(i)
"""

#3

"""
s = input("Введите строку: ")
n = int(input("Введите натуральное число: "))
for i in range(n):
    print(s)
"""

"""
lst = ["яблоки", "бананы", "груши", \
       "черешня", "виноград"]

n = len(lst) #кол-во элементов
for i in range(n):
    print(lst[i])
"""

"""
lst = ["яблоки", "бананы", "груши", \
       "черешня", "виноград"]
for b in lst:
    print(b)
"""

#4

"""
n = int(input("Введите кол-во: "))
a = []
for i in range(n):
    b = input("Введите наименование: ")
    a.append(b)
for d in a:
    print(d)
"""

#5

"""
n = int(input("Введите кол-во: "))
names = []
price = []
for i in range(n):
    a = input("Введите наименование: ")
    names.append(a)
    b = int(input("Введите цену: "))
    price.append(b)
for i in range(n):
    print(names[i], price[i], 'руб.')
"""


n = int(input("Введите кол-во: "))
names = []
price = []
s = 0
for i in range(n):
    a = input("Введите наименование: ")
    names.append(a)
    b = int(input("Введите цену: "))
    s = s + b
    price.append(b)
for i in range(n):
    print(names[i], price[i], 'руб.')
print("на все покупки мы потратили", s, "руб.")


#6

"""
n = int(input("Введите кол-во: "))
names = []
for i in range(n):
    a = input("Введите наименование: ")
    names.append(a)
print(names)
"""

"""
n = int(input("Введите кол-во: "))
names = []
for i in range(n):
    a = input("Введите наименование: ")
    names.append(a)
print(names)

b = names.pop(0)
names.append(b)
print(names)
"""

#7


n = int(input("Введите количество строк: "))
names = []
for i in range(n):
    s = input("Введите строку: ")
    names.append(s)
stroka = input("Поисковая строка: ")
for b in names:
    if stroka in b:
        print(b)


input()
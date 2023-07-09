#1

"""
for i in range(2,16,2):
    print(i)
"""

"""
for i in range(1,15,2):
    print(i)
"""

"""for i in range(1,27,2):
    print(i)
"""

#2

"""
lst = ['паучьи лапки', 'жабий палец', 'глаз тритона', 'крыло летучей мыши', 'хвост змеи']
lst2 = lst
for i, lst in enumerate(lst):
    print(i + 1, lst)

print()

lst2.insert(len(lst), lst2.pop(0))
for i, lst2 in enumerate(lst2):
    print(i + 1, lst2)
"""

#3

n = int(input("Введите количество строк: "))
names = []
count = 0
for i in range(n):
    s = input("Введите строку: ")
    names.append(s)
stroka = input("Поисковая строка: ")
for b in names:
    if stroka in b:
        count = count + 1
        print(b)
print("Строка",stroka,"встретилась",count,"раза")
input()
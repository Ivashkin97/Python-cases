#1

"""A = int(input("Введите первое число: "))
B = int(input("Введите второе число: "))

if A !=B:
    if A>B:
        B = A
    elif B>A:
        A = B
elif A == B:
    A = 0
    B = 0
print("A = ",A)
print("B = ",B)"""

#2

"""
A = int(input("Введите первое число: "))
B = int(input("Введите второе число: "))
C = int(input("Введите третье число: "))

p = 0
n = 0
z = 0

if A == 0:
    z = z + 1
else:
    if A % 2 != 0:
        n = n + 1
    else:
        p = p + 1

if B == 0:
    z = z + 1
else:
    if B % 2 != 0:
        n = n + 1
    else:
        p = p + 1

if C == 0:
    z = z + 1
else:
    if C % 2 != 0:
        n = n + 1
    else:
        p = p + 1

print(p, n, z)"""

#3

"""A = int(input("Введите первое число: "))
B = int(input("Введите второе число: "))
C = int(input("Введите третье число: "))

B = A < B < C
print(B)"""

#4 (некорректное задание)

#5

a = int(input("Проверьте, явл. ли год високосным: "))

if a%4 == 0 and a%100!=0 or a%400==0:
    print("YES")
else:
    print("NO")


input()



# Пользователь на вход присылает 2 числа A и B.
# Оба числа - натуральные. A всегда меньше B (A < B).

# Написать функцию, которая считает сумму всех НАТУРАЛЬНЫХ
# чисел между A и B, включая A и B.

def nat_sum(A, B):
    summ = 0
    while A <= B:
        if A % 2 == 0:
            summ += A
        A +=1
    return summ


a = int(input())
b = int(input())

#7 ..... 10 ---> 7 + 8 + 9 + 10 == 34

print(nat_sum(a,b))

#1........A == 1 + 2 + 3 ... + A

    

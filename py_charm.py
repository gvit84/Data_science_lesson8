#Функція, яка приймає ціле число та повертає суму всіх його цифр
def sum_int(a):
    um_a = 0
    a = str(a)
    for i in a:
        sum_a += int(i)
    return sum_a

print(sum_int(103))


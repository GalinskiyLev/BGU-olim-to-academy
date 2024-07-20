num = input('Пожалуйста введите число: ')
sum_of_digits = int(num)

while sum_of_digits > 9:
    sum_of_digits = 0
    for i in num:
        sum_of_digits += int(i)
    num = str(sum_of_digits)
print(num)
n = input('Введите целое положительное число\n')
while True:
    if not n.isdigit():
        n = input('Введите целое положительное число\n')
    elif int(n) < 0:
        n = input('Введите целое положительное число\n')
    else:
        n = int(n)
        break
symbol_counter = 1
space_counter = n - 1
for i in range(n):
    print(' '*space_counter+'*'*symbol_counter)
    symbol_counter += 2
    space_counter -= 1
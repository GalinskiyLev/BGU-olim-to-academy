list_with_transkriptions = [
    ['один', "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"],
    ['десять', 'одиннадцать', "двенадцать", "тринадцать", "четрынадцать", "пятнадцать", "шестнадцать", "семнадцать",
     "восемнадцать", "девятнадцать"],
    ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семдесят", "восемдесят", "девяносто"],
    ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
]

n = input('Введите целое число от 1 до 999\n')
while True:
    if not n.isdigit():
        n = input('Введите целое число от 1 до 999\n')
    elif not (1 <= int(n) <= 999):
        n = input('Введите целое число от 1 до 999\n')
    else:
        break

if len(n) == 1:
    res = list_with_transkriptions[0][int(n)-1]
    print(res)
elif len(n) == 2:
    if n[0] == '1':
        print(list_with_transkriptions[1][int(n[1])])
    else:
        if n[1] == '0':
            print(list_with_transkriptions[2][int(n[0]) - 2])
        else:
            print(list_with_transkriptions[2][int(n[0])-2], list_with_transkriptions[0][int(n[1])-1])
else:
    if n[1] == n[2] == '0':
        print(list_with_transkriptions[3][int(n[0]) - 1])
    else:
        if n[1] == '1':
            print(list_with_transkriptions[3][int(n[0]) - 1], list_with_transkriptions[1][int(n[2])])
        elif n[1] == '0':
            print(list_with_transkriptions[3][int(n[0]) - 1], list_with_transkriptions[0][int(n[2])-1])
        else:
            if n[2] == '0':
                print(list_with_transkriptions[3][int(n[0]) - 1], list_with_transkriptions[2][int(n[1]) - 2])
            else:
                print(list_with_transkriptions[3][int(n[0]) - 1], list_with_transkriptions[2][int(n[1]) - 2], list_with_transkriptions[0][int(n[2]) - 1])
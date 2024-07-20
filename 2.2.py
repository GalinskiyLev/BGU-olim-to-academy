try:
    with open('input.txt', 'r') as f:
        string_list = f.readlines()
        print(string_list)
    with open('output.txt', 'w') as output:
        symbols = input('ведите символы для удаления: ') + ';' + '\n'
        for i in range(len(string_list)):
            result = string_list[i].rstrip(symbols)[::-1]
            print(result, file=output)

except FileNotFoundError:
    print('The file was not found')

subject = input().strip()
names = []
try:
    with open('input.txt', 'r') as input_file:
        for i in input_file:
            line = i.strip().split(' : ')
            name, subjects = line[0], line[1].strip(',\n ').split(', ')
            if subject in subjects:
                names.append(name)
        print(names)

except FileNotFoundError:
    print('The file doesn\'t exist. Sorry:(')
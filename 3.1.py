cities_list = []
min_population = int(input('Введите минимальное число населения города: '))
try:
    with open('cities.txt', 'r') as cities_file:
        for city in cities_file:
            current_city = city.strip().split(':')
            if int(current_city[1]) > min_population:
                cities_list.append(current_city)

except FileNotFoundError:
    print('The file doesn\'t exist. Sorry:(')

cities_list.sort(key=lambda x:x[0])
with open('filtered_cities.txt', 'w') as filtered_cities_file:
    for filtered_city in cities_list:
        print(':'.join(filtered_city), file=filtered_cities_file)

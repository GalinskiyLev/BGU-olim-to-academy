list_with_grades = []
sum_grade = 0
try:
    with open('input.txt', 'r') as f:
        for line in f:
            name, grade = line.split(',')
            grade = int(grade)
            list_with_grades.append([name.strip(), grade])
            sum_grade += grade
        average_value = sum_grade / len(list_with_grades)
    with open('output.txt', 'w') as output:
        for i in list_with_grades:
            if i[1] > average_value:
                print(i[0], file=output)
except FileNotFoundError:
    print('This file does not exist.')
lines = []
try:
    with open('input1.txt', 'r') as f1:
        with open('input2.txt', 'r') as f2:
            with open('output.txt', 'w') as output:
                for line_from_f1 in f1:
                    line_from_f2 = f2.readline().strip()
                    print(*sorted(line_from_f1.strip() + line_from_f2), sep='', file=output)
except FileNotFoundError:
    print('The file was not found')

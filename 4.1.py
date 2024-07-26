result_list = []
closing_brackets = {
    ')': '(',
    '}': '{',
    '>': '<',
    ']': '['
}
with open('input.txt', 'r') as input_file:
    for line in input_file:
        dict_with_brackets = {}
        a = '({<['
        for i in a:
            dict_with_brackets[i] = 0
        result = True
        for symbol in line:
            if symbol in closing_brackets:
                dict_with_brackets[closing_brackets[symbol]] -= 1
                if dict_with_brackets[closing_brackets[symbol]] < 0:
                    result = False
                    break
            if symbol in dict_with_brackets:
                dict_with_brackets[symbol] += 1
        if result:
            for k, v in dict_with_brackets.items():
                if v != 0:
                    result = False
        result_list.append(result)
with open('output.txt', 'w') as output_file:
    print(*result_list, sep='\n', end='', file=output_file)



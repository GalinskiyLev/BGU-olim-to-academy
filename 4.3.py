count = [1, 1]


def steps(n):
    if n < len(count):
        return count[n]
    if n == len(count):
        count.append(steps(n-1) + steps(n-2))
    return steps(n-1) + steps(n-2)


print(steps(5))
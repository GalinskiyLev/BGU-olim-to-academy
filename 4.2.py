def algortmus_Evklidus(x, y):
    if x == 0 and y == 0:
        return False
    if x == 0 or y == 0:
        return x + y
    if x > y:
        return algortmus_Evklidus(x % y, y)
    return algortmus_Evklidus(x, y % x)


while True:
    print(algortmus_Evklidus(int(input()), int(input())))
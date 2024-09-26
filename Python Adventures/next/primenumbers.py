for x in range(2, 10):
    for y in range(2, x):
        if x % y == 0:
            print(x, " = ", y, "*", x // y)
            break
    else:
        print(x, "is Prime number! ")
